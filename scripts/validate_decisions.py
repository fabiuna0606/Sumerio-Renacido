#!/usr/bin/env python3
"""Validador de las fichas de decisión de decisiones/.

Comprueba, para cada ficha (todo archivo .md del directorio excepto
PLANTILLA.md y PENDIENTES.md):

* que el bloque de metadatos TOML es válido;
* que están todos los campos obligatorios y ninguno desconocido;
* que los valores están dentro de los permitidos;
* que el id es único y coincide con el nombre del archivo;
* en fichas puntuadas: E y C entre 0 y 3, FL igual a 0 o 1,
  puntaje = E - C + FL e incluye = (puntaje > 0);
* en fichas de convención y de evidencia: que no haya campos de puntaje;
* en fichas de evidencia, y en toda ficha verificada o adoptada: que haya
  al menos una fuente real (distinta de "FUENTE POR VERIFICAR");
* que reemplazada_por apunte a un id existente si estado = "reemplazada",
  y esté vacío en cualquier otro caso;
* que todo el texto del archivo esté en NFC.

Solo biblioteca estándar de Python 3.11 o superior (tomllib).

Uso:
    python3 scripts/validate_decisions.py [directorio]
"""

from __future__ import annotations

import sys
import tomllib
import unicodedata
from pathlib import Path

if sys.version_info < (3, 11):  # pragma: no cover - depende del intérprete
    raise SystemExit(
        "Se requiere Python 3.11 o superior (tomllib). Versión encontrada: "
        f"{sys.version.split()[0]}"
    )

DECISIONS_DIR = Path(__file__).resolve().parent.parent / "decisiones"

SKIPPED_FILENAMES = frozenset({"PLANTILLA.md", "PENDIENTES.md"})

FENCE = "+++"

REQUIRED_FIELDS = (
    "id",
    "titulo",
    "area",
    "tipo",
    "pregunta",
    "opciones",
    "decision",
    "estado",
    "verificacion",
    "fuentes",
    "se_revisa_si",
    "reemplazada_por",
)

SCORE_FIELDS = ("E", "C", "FL", "puntaje", "incluye")

ALLOWED_AREAS = (
    "fundamentos",
    "fonologia",
    "ortografia",
    "gramatica",
    "lexico",
    "tecnica",
)
ALLOWED_TYPES = ("evidencia", "convencion", "puntuada")
ALLOWED_STATES = (
    "propuesta",
    "verificada",
    "adoptada",
    "rechazada",
    "reemplazada",
)

TEXT_FIELDS = (
    "id",
    "titulo",
    "area",
    "tipo",
    "pregunta",
    "decision",
    "estado",
    "verificacion",
    "se_revisa_si",
)
LIST_FIELDS = ("opciones", "fuentes")

REPLACED_STATE = "reemplazada"
SCORED_TYPE = "puntuada"
CONVENTION_TYPE = "convencion"
EVIDENCE_TYPE = "evidencia"
UNSCORED_TYPES = (CONVENTION_TYPE, EVIDENCE_TYPE)
SOURCED_STATES = ("verificada", "adoptada")

UNVERIFIED_SOURCE = "FUENTE POR VERIFICAR"


class CardError(Exception):
    """Un error que impide incluso leer los metadatos de la ficha."""


def split_front_matter(text: str) -> tuple[str, str]:
    """Separa el bloque TOML del texto de la ficha.

    Los delimitadores son las dos primeras líneas cuyo contenido es
    exactamente "+++"; la primera debe ser la primera línea del archivo. Se
    comparan líneas completas y no subcadenas, porque el texto de una ficha
    puede mencionar "+++" sin delimitar nada.
    """
    lines = text.split("\n")
    if not lines or lines[0].strip() != FENCE:
        raise CardError(
            'la ficha no empieza por una línea con exactamente "+++"'
        )
    for index in range(1, len(lines)):
        if lines[index].strip() == FENCE:
            return "\n".join(lines[1:index]), "\n".join(lines[index + 1:])
    raise CardError(
        'falta la línea de cierre con exactamente "+++" del bloque de metadatos'
    )


def load_card(path: Path) -> tuple[dict, str]:
    """Devuelve (metadatos, texto) de una ficha, o lanza CardError."""
    raw = path.read_bytes()
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError as error:
        raise CardError(f"el archivo no está en UTF-8 válido: {error}") from error
    front_matter, body = split_front_matter(text)
    try:
        metadata = tomllib.loads(front_matter)
    except tomllib.TOMLDecodeError as error:
        raise CardError(f"el bloque TOML no es válido: {error}") from error
    if not isinstance(metadata, dict):  # pragma: no cover - tomllib siempre da dict
        raise CardError("el bloque TOML no define una tabla de metadatos")
    return metadata, body


def card_paths(directory: Path) -> list[Path]:
    """Fichas del directorio, en orden, sin la plantilla ni los pendientes."""
    return sorted(
        path
        for path in directory.glob("*.md")
        if path.name not in SKIPPED_FILENAMES
    )


def check_encoding(path: Path) -> list[str]:
    """Comprueba que todo el texto del archivo esté en NFC."""
    errors: list[str] = []
    raw = path.read_bytes()
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError as error:
        return [f"el archivo no está en UTF-8 válido: {error}"]
    if not unicodedata.is_normalized("NFC", text):
        offenders = sorted(
            {
                character
                for character in text
                if not unicodedata.is_normalized("NFC", character)
            }
        )
        detail = ", ".join(repr(character) for character in offenders[:5])
        errors.append(f"el texto no está en NFC (caracteres sin normalizar: {detail})")
    return errors


def check_required_fields(metadata: dict) -> list[str]:
    """Campos obligatorios presentes, con el tipo correcto, y sin extraños."""
    errors: list[str] = []
    for field in REQUIRED_FIELDS:
        if field not in metadata:
            errors.append(f"falta el campo obligatorio: {field}")

    for field in TEXT_FIELDS:
        value = metadata.get(field)
        if field in metadata and not isinstance(value, str):
            errors.append(f"el campo {field} debe ser una cadena de texto")
        elif isinstance(value, str) and not value.strip():
            errors.append(f"el campo {field} no puede estar vacío")

    if "reemplazada_por" in metadata and not isinstance(
        metadata["reemplazada_por"], str
    ):
        errors.append("el campo reemplazada_por debe ser una cadena de texto")

    for field in LIST_FIELDS:
        if field not in metadata:
            continue
        value = metadata[field]
        if not isinstance(value, list) or not all(
            isinstance(item, str) for item in value
        ):
            errors.append(f"el campo {field} debe ser una lista de cadenas")
        elif not value:
            errors.append(f"el campo {field} no puede ser una lista vacía")

    known_fields = set(REQUIRED_FIELDS) | set(SCORE_FIELDS)
    for field in sorted(set(metadata) - known_fields):
        errors.append(f"campo desconocido: {field}")
    return errors


def check_allowed_values(metadata: dict) -> list[str]:
    """Valores dentro de las listas permitidas de area, tipo y estado."""
    errors: list[str] = []
    checks = (
        ("area", ALLOWED_AREAS),
        ("tipo", ALLOWED_TYPES),
        ("estado", ALLOWED_STATES),
    )
    for field, allowed in checks:
        value = metadata.get(field)
        if isinstance(value, str) and value not in allowed:
            errors.append(
                f"el campo {field} tiene el valor no permitido {value!r}; "
                f"valores permitidos: {', '.join(allowed)}"
            )
    return errors


def check_identifier(metadata: dict, path: Path) -> list[str]:
    """El id debe coincidir con el nombre del archivo."""
    card_id = metadata.get("id")
    if not isinstance(card_id, str):
        return []
    if card_id != path.stem:
        return [
            f"el id {card_id!r} no coincide con el nombre del archivo "
            f"{path.name!r} (se esperaba {path.stem!r})"
        ]
    return []


def check_scores(metadata: dict) -> list[str]:
    """Campos de puntaje según el tipo de ficha."""
    errors: list[str] = []
    card_type = metadata.get("tipo")

    if card_type in UNSCORED_TYPES:
        label = "convención" if card_type == CONVENTION_TYPE else "evidencia"
        for field in SCORE_FIELDS:
            if field in metadata:
                errors.append(
                    f"una ficha de {label} no puede llevar el campo de "
                    f"puntaje {field}"
                )
        return errors

    if card_type != SCORED_TYPE:
        return errors

    for field in SCORE_FIELDS:
        if field not in metadata:
            errors.append(f"falta el campo de puntaje obligatorio: {field}")

    ranges = (("E", 0, 3), ("C", 0, 3), ("FL", 0, 1))
    for field, low, high in ranges:
        if field not in metadata:
            continue
        value = metadata[field]
        if isinstance(value, bool) or not isinstance(value, int):
            errors.append(f"el campo {field} debe ser un número entero")
        elif not low <= value <= high:
            errors.append(
                f"el campo {field} vale {value}; debe estar entre {low} y {high}"
            )

    score = metadata.get("puntaje")
    if isinstance(score, bool) or not isinstance(score, int):
        if "puntaje" in metadata:
            errors.append("el campo puntaje debe ser un número entero")
    included = metadata.get("incluye")
    if "incluye" in metadata and not isinstance(included, bool):
        errors.append("el campo incluye debe ser un booleano (true o false)")

    if errors:
        return errors

    expected_score = metadata["E"] - metadata["C"] + metadata["FL"]
    if score != expected_score:
        errors.append(
            f"puntaje incoherente: {score} declarado, pero "
            f"E − C + FL = {metadata['E']} − {metadata['C']} + "
            f"{metadata['FL']} = {expected_score}"
        )
    expected_inclusion = expected_score > 0
    if included is not expected_inclusion:
        errors.append(
            f"incluye incoherente: {str(included).lower()} declarado, pero "
            f"puntaje = {expected_score} exige "
            f"{str(expected_inclusion).lower()} (se incluye si y solo si "
            f"puntaje > 0)"
        )
    return errors


def check_sources(metadata: dict) -> list[str]:
    """Fuentes reales donde la ficha las exige.

    Una ficha de evidencia se decide por las fuentes, así que necesita al
    menos una. Una ficha verificada o adoptada también: lo que está por
    cotejar nunca se presenta como firme.
    """
    sources = metadata.get("fuentes")
    if not isinstance(sources, list) or not all(
        isinstance(item, str) for item in sources
    ):
        return []
    has_real_source = any(
        item.strip() and item.strip() != UNVERIFIED_SOURCE for item in sources
    )
    if has_real_source:
        return []
    errors: list[str] = []
    if metadata.get("tipo") == EVIDENCE_TYPE:
        errors.append(
            "una ficha de evidencia necesita al menos una fuente real "
            f"(distinta de {UNVERIFIED_SOURCE!r})"
        )
    state = metadata.get("estado")
    if state in SOURCED_STATES:
        errors.append(
            f"una ficha en estado {state!r} necesita al menos una fuente real "
            f"(distinta de {UNVERIFIED_SOURCE!r})"
        )
    return errors


def check_replacement(metadata: dict, known_ids: set[str]) -> list[str]:
    """reemplazada_por solo se usa, y es obligatorio, si estado = reemplazada."""
    errors: list[str] = []
    state = metadata.get("estado")
    replacement = metadata.get("reemplazada_por")
    if not isinstance(replacement, str):
        return errors

    if state == REPLACED_STATE:
        if not replacement.strip():
            errors.append(
                "estado es \"reemplazada\", así que reemplazada_por no puede "
                "estar vacío"
            )
        elif replacement not in known_ids:
            errors.append(
                f"reemplazada_por apunta a {replacement!r}, que no es el id de "
                "ninguna ficha existente"
            )
        elif replacement == metadata.get("id"):
            errors.append("reemplazada_por no puede apuntar a la propia ficha")
    elif replacement.strip():
        errors.append(
            f"reemplazada_por vale {replacement!r}, pero solo puede llevar "
            f'valor si estado es "reemplazada" (estado actual: {state!r})'
        )
    return errors


def validate_directory(directory: Path) -> dict[str, list[str]]:
    """Valida todas las fichas del directorio.

    Devuelve un diccionario {nombre de archivo: lista de errores}, con una
    entrada por cada ficha que tenga al menos un error.
    """
    directory = Path(directory)
    if not directory.is_dir():
        return {str(directory): ["el directorio de fichas no existe"]}

    paths = card_paths(directory)
    report: dict[str, list[str]] = {}
    loaded: list[tuple[Path, dict, str]] = []

    for path in paths:
        try:
            metadata, body = load_card(path)
        except CardError as error:
            report[path.name] = [str(error)]
            continue
        loaded.append((path, metadata, body))

    known_ids = {
        metadata["id"]
        for _, metadata, _ in loaded
        if isinstance(metadata.get("id"), str)
    }

    seen_ids: dict[str, str] = {}
    for path, metadata, _ in loaded:
        errors: list[str] = []
        errors += check_encoding(path)
        errors += check_required_fields(metadata)
        errors += check_allowed_values(metadata)
        errors += check_identifier(metadata, path)
        errors += check_scores(metadata)
        errors += check_sources(metadata)
        errors += check_replacement(metadata, known_ids)

        card_id = metadata.get("id")
        if isinstance(card_id, str):
            if card_id in seen_ids:
                errors.append(
                    f"el id {card_id!r} ya lo usa la ficha {seen_ids[card_id]}"
                )
            else:
                seen_ids[card_id] = path.name

        if errors:
            report.setdefault(path.name, []).extend(errors)

    return report


def format_report(report: dict[str, list[str]], card_count: int) -> str:
    """Convierte el informe de errores en texto legible."""
    if not report:
        return f"{card_count} fichas revisadas: todas válidas."
    lines = [f"{card_count} fichas revisadas, {len(report)} con errores:", ""]
    for name in sorted(report):
        lines.append(f"{name}:")
        for error in report[name]:
            lines.append(f"  - {error}")
        lines.append("")
    return "\n".join(lines).rstrip()


def main(argv: list[str]) -> int:
    directory = Path(argv[1]) if len(argv) > 1 else DECISIONS_DIR
    report = validate_directory(directory)
    count = len(card_paths(directory)) if directory.is_dir() else 0
    print(format_report(report, count))
    return 1 if report else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
