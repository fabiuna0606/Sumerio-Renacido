# -*- coding: utf-8 -*-
"""Pruebas de las reglas del repositorio fijadas en CLAUDE.md.

Automatizan lo que hasta ahora solo estaba escrito:

* regla 1 — la cadena de fuente sin verificar se escribe exactamente así;
* regla 4 — el código solo usa la biblioteca estándar de Python 3.11;
* regla 5 — todo el texto va en UTF-8, en NFC y con fin de línea LF;
* TEC-004 — el workflow de integración continua ejecuta de verdad el
  validador y las pruebas con Python 3.11.

Añade además una comprobación de coherencia: toda ficha citada en la
documentación debe existir en decisiones/.

Se ejecutan con:
    python3 -m unittest discover -s tests -v
"""

from __future__ import annotations

import ast
import json
import os
import re
import sys
import unicodedata
import unittest
from pathlib import Path

from repository_files import PROJECT_ROOT, repository_files, text_files

UNVERIFIED_SOURCE = "FUENTE POR VERIFICAR"

CARD_ID = re.compile(r"\b(?:FON|ORT|GRA|LEX|TEC)-[0-9]{3}\b")

DECISIONS_DIR = PROJECT_ROOT / "decisiones"

# Documentación donde una referencia a una ficha debe apuntar a una ficha real.
# PLANTILLA.md queda fuera: usa el identificador de ejemplo XXX-000.
DOCUMENTATION_FILES = (
    "CLAUDE.md",
    "README.md",
    "CHANGELOG.md",
    "decisiones/PENDIENTES.md",
    "lexico/README.md",
)

# .editorconfig permite espacios finales en los TSV del glosario, porque un
# campo vacío al final de una línea es un dato, no un descuido.
TRAILING_WHITESPACE_EXEMPT_SUFFIXES = frozenset({".tsv"})

WORKFLOW_PATH = ".github/workflows/ci.yml"

HOOK_PATH = ".claude/hooks/session-start.sh"

SETTINGS_PATH = ".claude/settings.json"

PROJECT_CODE_DIRECTORIES = ("scripts", "tests")

VALIDATOR_COMMAND = "python3 scripts/validate_decisions.py"
TESTS_COMMAND = "python3 -m unittest discover -s tests"


def project_code_paths() -> list[Path]:
    """Archivos .py del proyecto, en scripts/ y en tests/."""
    paths: list[Path] = []
    for directory in PROJECT_CODE_DIRECTORIES:
        paths += sorted((PROJECT_ROOT / directory).glob("*.py"))
    return paths


def local_module_names() -> set[str]:
    """Módulos del propio proyecto, importables sin ser dependencias."""
    return {path.stem for path in project_code_paths()}


def imported_root_modules(tree: ast.Module) -> set[str]:
    """Nombres de módulo raíz que importa un árbol sintáctico."""
    roots: set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                roots.add(alias.name.split(".")[0])
        elif isinstance(node, ast.ImportFrom):
            if node.level == 0 and node.module:
                roots.add(node.module.split(".")[0])
    return roots


class TestEncodingRules(unittest.TestCase):
    """Regla 5 de CLAUDE.md: UTF-8, NFC y fin de línea LF, en todo el texto."""

    def test_every_file_is_valid_utf8(self) -> None:
        offenders = [
            relative
            for path, relative in repository_files()
            if relative not in {item[1] for item in text_files()}
        ]
        self.assertEqual(offenders, [],
                         msg=f"archivos que no son UTF-8 válido: {offenders}")

    def test_every_file_is_nfc(self) -> None:
        offenders = [
            relative
            for _, relative, text in text_files()
            if not unicodedata.is_normalized("NFC", text)
        ]
        self.assertEqual(offenders, [],
                         msg=f"archivos sin normalizar en NFC: {offenders}")

    def test_no_file_uses_carriage_returns(self) -> None:
        offenders = [
            relative for _, relative, text in text_files() if "\r" in text
        ]
        self.assertEqual(
            offenders, [],
            msg=f"archivos con fin de línea distinto de LF: {offenders}")

    def test_every_non_empty_file_ends_with_a_newline(self) -> None:
        offenders = [
            relative
            for _, relative, text in text_files()
            if text and not text.endswith("\n")
        ]
        self.assertEqual(offenders, [],
                         msg=f"archivos sin salto de línea final: {offenders}")

    def test_no_line_has_trailing_whitespace(self) -> None:
        offenders = []
        for path, relative, text in text_files():
            if path.suffix in TRAILING_WHITESPACE_EXEMPT_SUFFIXES:
                continue
            for number, line in enumerate(text.split("\n"), start=1):
                if line != line.rstrip():
                    offenders.append(f"{relative}:{number}")
        self.assertEqual(offenders, [],
                         msg=f"líneas con espacios finales: {offenders}")


class TestDependencyRule(unittest.TestCase):
    """Regla 4 de CLAUDE.md: solo la biblioteca estándar."""

    def test_project_code_imports_only_the_standard_library(self) -> None:
        allowed = set(sys.stdlib_module_names) | local_module_names()
        offenders = []
        for path in project_code_paths():
            tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
            for module in sorted(imported_root_modules(tree) - allowed):
                offenders.append(f"{path.name}: {module}")
        self.assertEqual(
            offenders, [],
            msg=f"importaciones ajenas a la biblioteca estándar: {offenders}")

    def test_the_project_runs_on_python_3_11_or_later(self) -> None:
        self.assertGreaterEqual(sys.version_info[:2], (3, 11))


class TestSourceLiteral(unittest.TestCase):
    """Regla 1 de CLAUDE.md: la cadena se escribe exactamente así."""

    def test_unverified_source_is_always_written_in_the_exact_form(self) -> None:
        pattern = re.compile(UNVERIFIED_SOURCE, re.IGNORECASE)
        offenders = []
        for _, relative, text in text_files():
            for match in pattern.finditer(text):
                if match.group(0) != UNVERIFIED_SOURCE:
                    offenders.append(f"{relative}: {match.group(0)!r}")
        self.assertEqual(
            offenders, [],
            msg=f"variantes de {UNVERIFIED_SOURCE!r}: {offenders}")


class TestCardReferences(unittest.TestCase):
    """Toda ficha citada en la documentación debe existir."""

    def existing_card_ids(self) -> set[str]:
        return {
            path.stem
            for path in DECISIONS_DIR.glob("*.md")
            if CARD_ID.fullmatch(path.stem)
        }

    def test_documentation_only_references_existing_cards(self) -> None:
        existing = self.existing_card_ids()
        offenders = []
        for name in DOCUMENTATION_FILES:
            path = PROJECT_ROOT / name
            if not path.is_file():
                offenders.append(f"{name}: el archivo no existe")
                continue
            text = path.read_text(encoding="utf-8")
            for card_id in sorted(set(CARD_ID.findall(text)) - existing):
                offenders.append(f"{name}: {card_id}")
        self.assertEqual(
            offenders, [],
            msg=f"referencias a fichas que no existen: {offenders}")


class TestContinuousIntegration(unittest.TestCase):
    """TEC-004: el workflow ejecuta de verdad las comprobaciones del proyecto.

    Se comprueba sobre el texto del archivo, porque leer YAML exigiría una
    dependencia externa y la regla 4 no lo permite.
    """

    def setUp(self) -> None:
        path = PROJECT_ROOT / WORKFLOW_PATH
        self.assertTrue(path.is_file(),
                        msg=f"falta el workflow {WORKFLOW_PATH}")
        self.workflow = path.read_text(encoding="utf-8")

    def test_workflow_runs_the_validator(self) -> None:
        self.assertIn(VALIDATOR_COMMAND, self.workflow)

    def test_workflow_runs_the_tests(self) -> None:
        self.assertIn(TESTS_COMMAND, self.workflow)

    def test_workflow_uses_python_3_11(self) -> None:
        self.assertIn("python-version: '3.11'", self.workflow)

    def test_workflow_triggers_on_push_pull_request_and_schedule(self) -> None:
        for trigger in ("push:", "pull_request:", "schedule:"):
            with self.subTest(disparador=trigger):
                self.assertIn(trigger, self.workflow)


class TestSessionStartHook(unittest.TestCase):
    """El hook de arranque deja el repositorio comprobado en cada sesión."""

    def test_hook_exists_and_is_executable(self) -> None:
        path = PROJECT_ROOT / HOOK_PATH
        self.assertTrue(path.is_file(), msg=f"falta el hook {HOOK_PATH}")
        self.assertTrue(
            os.access(path, os.X_OK),
            msg=f"el hook {HOOK_PATH} no tiene permiso de ejecución",
        )

    def test_hook_runs_the_project_checks(self) -> None:
        hook = (PROJECT_ROOT / HOOK_PATH).read_text(encoding="utf-8")
        for command in (VALIDATOR_COMMAND, TESTS_COMMAND):
            with self.subTest(comando=command):
                self.assertIn(command, hook)

    def test_settings_register_the_hook(self) -> None:
        path = PROJECT_ROOT / SETTINGS_PATH
        self.assertTrue(path.is_file(), msg=f"falta {SETTINGS_PATH}")
        settings = json.loads(path.read_text(encoding="utf-8"))
        commands = [
            entry.get("command", "")
            for group in settings.get("hooks", {}).get("SessionStart", [])
            for entry in group.get("hooks", [])
        ]
        self.assertTrue(
            any(HOOK_PATH in command for command in commands),
            msg=f"{SETTINGS_PATH} no registra {HOOK_PATH}: {commands}",
        )


if __name__ == "__main__":
    unittest.main()
