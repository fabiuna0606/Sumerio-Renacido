# -*- coding: utf-8 -*-
"""Pruebas del validador de fichas de decisión.

Se ejecutan con:
    python3 -m unittest discover -s tests -v
"""

from __future__ import annotations

import contextlib
import io
import sys
import tempfile
import unicodedata
import unittest
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT / "scripts"))

import validate_decisions as validator  # noqa: E402

DECISIONS_DIR = PROJECT_ROOT / "decisiones"

EXPECTED_CARD_COUNT = 15

EPSD2_SOURCE = (
    "ePSD2, versión 2.7.2 (compilada el 2024-08-31), consultado el 2026-09-27"
)

# Fichas reales cuyas fuentes ya no son "FUENTE POR VERIFICAR". Las que no
# aparecen aquí siguen sin ninguna fuente comprobada.
REAL_CARD_SOURCES = {"ORT-001": [EPSD2_SOURCE]}

# Letra descartada por ORT-001 (g con circunflejo, U+011D). Se escribe con
# escapes para que este archivo de pruebas no la contenga.
DISCARDED_LETTER = "\u011d"
DISCARDED_LETTER_DECOMPOSED = "g\u0302"

# Única ruta del repositorio que puede mencionarla: la ficha que describe la
# opción descartada.
DISCARDED_LETTER_EXEMPT_FILES = frozenset({"decisiones/ORT-001.md"})

# Directorios que no forman parte del texto del repositorio.
IGNORED_DIRECTORIES = frozenset({".git", "__pycache__"})

VALID_CARD = {
    "id": "TEC-900",
    "titulo": "Ficha de prueba",
    "area": "tecnica",
    "tipo": "puntuada",
    "pregunta": "¿Es válida esta ficha de prueba?",
    "opciones": ["Sí", "No"],
    "decision": "Incluir.",
    "estado": "propuesta",
    "verificacion": "PENDIENTE: ficha sintética usada solo en las pruebas",
    "fuentes": ["FUENTE POR VERIFICAR"],
    "se_revisa_si": "Cambia el formato de las fichas.",
    "reemplazada_por": "",
    "E": 2,
    "C": 1,
    "FL": 1,
    "puntaje": 2,
    "incluye": True,
}

CONVENTION_CARD = {
    "id": "TEC-901",
    "titulo": "Ficha de convención de prueba",
    "area": "tecnica",
    "tipo": "convencion",
    "pregunta": "¿Es válida esta ficha de convención de prueba?",
    "opciones": ["Convención A", "Convención B"],
    "decision": "Convención A.",
    "estado": "propuesta",
    "verificacion": "PENDIENTE: ficha sintética usada solo en las pruebas",
    "fuentes": ["FUENTE POR VERIFICAR"],
    "se_revisa_si": "Cambia el formato de las fichas.",
    "reemplazada_por": "",
}


def render_toml_value(value) -> str:
    """Serializa a TOML los tipos que usan las fichas."""
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, int):
        return str(value)
    if isinstance(value, list):
        inner = ", ".join(render_toml_value(item) for item in value)
        return f"[{inner}]"
    escaped = str(value).replace("\\", "\\\\").replace('"', '\\"')
    return f'"{escaped}"'


def render_card(metadata: dict, body: str = "\nTexto de la ficha.\n") -> str:
    """Construye el texto completo de una ficha a partir de sus metadatos."""
    lines = ["+++"]
    for key, value in metadata.items():
        lines.append(f"{key} = {render_toml_value(value)}")
    lines.append("+++")
    return "\n".join(lines) + body


class CardDirectoryMixin:
    """Escribe fichas sintéticas en un directorio temporal."""

    def setUp(self) -> None:
        self._temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self._temporary.cleanup)
        self.directory = Path(self._temporary.name)

    def write_card(self, metadata: dict, filename: str | None = None,
                   body: str = "\nTexto de la ficha.\n") -> Path:
        name = filename if filename is not None else f"{metadata['id']}.md"
        path = self.directory / name
        path.write_text(render_card(metadata, body), encoding="utf-8",
                        newline="\n")
        return path

    def write_raw(self, filename: str, text: str) -> Path:
        path = self.directory / filename
        path.write_text(text, encoding="utf-8", newline="\n")
        return path

    def errors_for(self, filename: str) -> list[str]:
        return validator.validate_directory(self.directory).get(filename, [])

    def assertErrorMentions(self, filename: str, fragment: str) -> None:
        errors = self.errors_for(filename)
        self.assertTrue(
            errors,
            msg=f"se esperaba al menos un error en {filename} y no hubo ninguno",
        )
        joined = "\n".join(errors)
        self.assertIn(fragment, joined)


class TestRealCards(unittest.TestCase):
    """Las fichas reales del repositorio deben ser válidas."""

    def test_all_real_cards_are_valid(self) -> None:
        report = validator.validate_directory(DECISIONS_DIR)
        self.assertEqual(report, {}, msg=validator.format_report(report, 0))

    def test_expected_number_of_cards(self) -> None:
        self.assertEqual(len(validator.card_paths(DECISIONS_DIR)),
                         EXPECTED_CARD_COUNT)

    def test_template_and_pending_are_skipped(self) -> None:
        names = {path.name for path in validator.card_paths(DECISIONS_DIR)}
        self.assertNotIn("PLANTILLA.md", names)
        self.assertNotIn("PENDIENTES.md", names)

    def test_real_cards_are_nfc(self) -> None:
        for path in validator.card_paths(DECISIONS_DIR):
            with self.subTest(ficha=path.name):
                text = path.read_text(encoding="utf-8")
                self.assertTrue(unicodedata.is_normalized("NFC", text))

    def test_real_cards_are_proposals(self) -> None:
        for path in validator.card_paths(DECISIONS_DIR):
            with self.subTest(ficha=path.name):
                metadata, _ = validator.load_card(path)
                self.assertEqual(metadata["estado"], "propuesta")

    def test_real_cards_declare_the_expected_sources(self) -> None:
        for path in validator.card_paths(DECISIONS_DIR):
            with self.subTest(ficha=path.name):
                metadata, _ = validator.load_card(path)
                expected = REAL_CARD_SOURCES.get(
                    path.stem, [validator.UNVERIFIED_SOURCE]
                )
                self.assertEqual(metadata["fuentes"], expected)


class TestValidCards(CardDirectoryMixin, unittest.TestCase):
    """Fichas sintéticas correctas: el validador no debe protestar."""

    def test_scored_card_passes(self) -> None:
        self.write_card(VALID_CARD)
        self.assertEqual(validator.validate_directory(self.directory), {})

    def test_convention_card_passes(self) -> None:
        self.write_card(CONVENTION_CARD)
        self.assertEqual(validator.validate_directory(self.directory), {})

    def test_zero_score_excludes(self) -> None:
        card = dict(VALID_CARD, E=1, C=1, FL=0, puntaje=0, incluye=False)
        self.write_card(card)
        self.assertEqual(validator.validate_directory(self.directory), {})

    def test_replaced_card_pointing_to_existing_id_passes(self) -> None:
        self.write_card(VALID_CARD)
        replaced = dict(CONVENTION_CARD, estado="reemplazada",
                        reemplazada_por=VALID_CARD["id"])
        self.write_card(replaced)
        self.assertEqual(validator.validate_directory(self.directory), {})

    def test_empty_directory_passes(self) -> None:
        self.assertEqual(validator.validate_directory(self.directory), {})


class TestInvalidCards(CardDirectoryMixin, unittest.TestCase):
    """Cada prueba escribe una ficha inválida y exige que se detecte."""

    def test_broken_toml_is_detected(self) -> None:
        self.write_raw("TEC-902.md", '+++\nid = "TEC-902\n+++\n\nTexto.\n')
        self.assertErrorMentions("TEC-902.md", "TOML no es válido")

    def test_missing_opening_fence_is_detected(self) -> None:
        self.write_raw("TEC-903.md", 'id = "TEC-903"\n\nTexto.\n')
        self.assertErrorMentions("TEC-903.md", "no empieza por una línea")

    def test_missing_closing_fence_is_detected(self) -> None:
        self.write_raw("TEC-904.md", '+++\nid = "TEC-904"\n\nTexto.\n')
        self.assertErrorMentions("TEC-904.md", "falta la línea de cierre")

    def test_missing_required_field_is_detected(self) -> None:
        card = {key: value for key, value in VALID_CARD.items()
                if key != "se_revisa_si"}
        self.write_card(card)
        self.assertErrorMentions("TEC-900.md",
                                 "falta el campo obligatorio: se_revisa_si")

    def test_empty_required_field_is_detected(self) -> None:
        self.write_card(dict(VALID_CARD, titulo=""))
        self.assertErrorMentions("TEC-900.md",
                                 "el campo titulo no puede estar vacío")

    def test_empty_sources_list_is_detected(self) -> None:
        self.write_card(dict(VALID_CARD, fuentes=[]))
        self.assertErrorMentions("TEC-900.md",
                                 "el campo fuentes no puede ser una lista vacía")

    def test_unknown_field_is_detected(self) -> None:
        self.write_card(dict(VALID_CARD, comentario="campo no previsto"))
        self.assertErrorMentions("TEC-900.md", "campo desconocido: comentario")

    def test_disallowed_area_is_detected(self) -> None:
        self.write_card(dict(VALID_CARD, area="sintaxis"))
        self.assertErrorMentions("TEC-900.md", "el campo area tiene el valor")

    def test_disallowed_type_is_detected(self) -> None:
        self.write_card(dict(VALID_CARD, tipo="mixta"))
        self.assertErrorMentions("TEC-900.md", "el campo tipo tiene el valor")

    def test_disallowed_state_is_detected(self) -> None:
        self.write_card(dict(VALID_CARD, estado="pendiente"))
        self.assertErrorMentions("TEC-900.md", "el campo estado tiene el valor")

    def test_identifier_not_matching_filename_is_detected(self) -> None:
        self.write_card(VALID_CARD, filename="TEC-999.md")
        self.assertErrorMentions("TEC-999.md", "no coincide con el nombre")

    def test_duplicate_identifier_is_detected(self) -> None:
        self.write_card(VALID_CARD)
        duplicate = self.directory / "TEC-900-copia.md"
        duplicate.write_text(render_card(VALID_CARD), encoding="utf-8",
                             newline="\n")
        report = validator.validate_directory(self.directory)
        joined = "\n".join(sum(report.values(), []))
        self.assertIn("ya lo usa la ficha", joined)

    def test_evidence_out_of_range_is_detected(self) -> None:
        self.write_card(dict(VALID_CARD, E=4, puntaje=4, incluye=True))
        self.assertErrorMentions("TEC-900.md", "el campo E vale 4")

    def test_cost_out_of_range_is_detected(self) -> None:
        self.write_card(dict(VALID_CARD, C=-1, puntaje=4, incluye=True))
        self.assertErrorMentions("TEC-900.md", "el campo C vale -1")

    def test_functional_load_out_of_range_is_detected(self) -> None:
        self.write_card(dict(VALID_CARD, FL=2, puntaje=3, incluye=True))
        self.assertErrorMentions("TEC-900.md", "el campo FL vale 2")

    def test_wrong_score_arithmetic_is_detected(self) -> None:
        self.write_card(dict(VALID_CARD, puntaje=3))
        self.assertErrorMentions("TEC-900.md", "puntaje incoherente")

    def test_wrong_inclusion_flag_is_detected(self) -> None:
        self.write_card(dict(VALID_CARD, incluye=False))
        self.assertErrorMentions("TEC-900.md", "incluye incoherente")

    def test_zero_score_marked_as_included_is_detected(self) -> None:
        self.write_card(dict(VALID_CARD, E=1, C=1, FL=0, puntaje=0,
                             incluye=True))
        self.assertErrorMentions("TEC-900.md", "incluye incoherente")

    def test_missing_score_field_in_scored_card_is_detected(self) -> None:
        card = {key: value for key, value in VALID_CARD.items() if key != "FL"}
        self.write_card(card)
        self.assertErrorMentions("TEC-900.md",
                                 "falta el campo de puntaje obligatorio: FL")

    def test_score_fields_in_convention_card_are_detected(self) -> None:
        self.write_card(dict(CONVENTION_CARD, E=2, C=0, FL=1, puntaje=3,
                             incluye=True))
        self.assertErrorMentions(
            "TEC-901.md",
            "una ficha de convención no puede llevar el campo de puntaje",
        )

    def test_replacement_pointing_to_unknown_id_is_detected(self) -> None:
        self.write_card(dict(VALID_CARD, estado="reemplazada",
                             reemplazada_por="TEC-950"))
        self.assertErrorMentions("TEC-900.md", "no es el id de ninguna ficha")

    def test_replaced_state_without_replacement_is_detected(self) -> None:
        self.write_card(dict(VALID_CARD, estado="reemplazada"))
        self.assertErrorMentions("TEC-900.md",
                                 "reemplazada_por no puede estar vacío")

    def test_replacement_in_non_replaced_card_is_detected(self) -> None:
        self.write_card(dict(VALID_CARD, reemplazada_por="TEC-901"))
        self.assertErrorMentions("TEC-900.md", "solo puede llevar valor")

    def test_self_replacement_is_detected(self) -> None:
        self.write_card(dict(VALID_CARD, estado="reemplazada",
                             reemplazada_por=VALID_CARD["id"]))
        self.assertErrorMentions("TEC-900.md", "a la propia ficha")

    def test_text_not_in_nfc_is_detected(self) -> None:
        decomposed = unicodedata.normalize("NFD", "š")
        self.assertNotEqual(decomposed, "š")
        self.write_card(VALID_CARD, body=f"\nLa letra {decomposed} sin componer.\n")
        self.assertErrorMentions("TEC-900.md", "no está en NFC")

    def test_wrong_field_type_is_detected(self) -> None:
        self.write_card(dict(VALID_CARD, opciones="Sí o no"))
        self.assertErrorMentions("TEC-900.md",
                                 "el campo opciones debe ser una lista")

    def test_invalid_card_next_to_valid_one_is_isolated(self) -> None:
        """Una ficha inválida no debe invalidar a las demás."""
        self.write_card(VALID_CARD)
        self.write_card(dict(CONVENTION_CARD, area="sintaxis"))
        report = validator.validate_directory(self.directory)
        self.assertEqual(sorted(report), ["TEC-901.md"])


class TestDiscardedLetter(unittest.TestCase):
    """ORT-001 decide la letra de la romanización práctica.

    La letra descartada no puede aparecer en ningún archivo del repositorio,
    salvo en la propia ficha ORT-001, que la menciona al describir la opción
    descartada.
    """

    def repository_files(self) -> list[tuple[Path, str]]:
        """Archivos del repositorio, con su ruta relativa en formato POSIX."""
        files = []
        for path in sorted(PROJECT_ROOT.rglob("*")):
            if not path.is_file():
                continue
            relative = path.relative_to(PROJECT_ROOT)
            if IGNORED_DIRECTORIES.intersection(relative.parts):
                continue
            files.append((path, relative.as_posix()))
        return files

    def test_exempt_file_exists(self) -> None:
        for name in sorted(DISCARDED_LETTER_EXEMPT_FILES):
            with self.subTest(archivo=name):
                self.assertTrue(
                    (PROJECT_ROOT / name).is_file(),
                    msg=f"la excepción {name} ya no existe en el repositorio",
                )

    def test_discarded_letter_only_in_the_exempt_file(self) -> None:
        offenders = []
        for path, relative in self.repository_files():
            if relative in DISCARDED_LETTER_EXEMPT_FILES:
                continue
            try:
                text = path.read_text(encoding="utf-8")
            except (UnicodeDecodeError, OSError):
                continue
            if DISCARDED_LETTER in text or DISCARDED_LETTER_DECOMPOSED in text:
                offenders.append(relative)
        self.assertEqual(
            offenders,
            [],
            msg=(
                "la letra descartada por ORT-001 aparece en archivos que "
                f"deben usar la letra adoptada: {', '.join(offenders)}"
            ),
        )


class TestReportAndExitCode(CardDirectoryMixin, unittest.TestCase):
    """El informe y el código de salida del validador."""

    def test_report_of_valid_directory(self) -> None:
        self.assertIn("todas válidas", validator.format_report({}, 13))

    def test_report_lists_each_error(self) -> None:
        report = {"TEC-900.md": ["primer error", "segundo error"]}
        text = validator.format_report(report, 1)
        self.assertIn("1 con errores", text)
        self.assertIn("primer error", text)
        self.assertIn("segundo error", text)

    def run_validator(self, directory: Path) -> tuple[int, str]:
        """Ejecuta el validador capturando su salida, y devuelve (código, texto)."""
        buffer = io.StringIO()
        with contextlib.redirect_stdout(buffer):
            code = validator.main(["validate_decisions.py", str(directory)])
        return code, buffer.getvalue()

    def test_exit_code_is_zero_for_real_cards(self) -> None:
        code, output = self.run_validator(DECISIONS_DIR)
        self.assertEqual(code, 0)
        self.assertIn("todas válidas", output)

    def test_exit_code_is_one_for_invalid_card(self) -> None:
        self.write_card(dict(VALID_CARD, estado="pendiente"))
        code, output = self.run_validator(self.directory)
        self.assertEqual(code, 1)
        self.assertIn("TEC-900.md", output)

    def test_missing_directory_is_reported(self) -> None:
        missing = self.directory / "no-existe"
        report = validator.validate_directory(missing)
        self.assertIn(str(missing), report)


if __name__ == "__main__":
    unittest.main()
