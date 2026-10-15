# -*- coding: utf-8 -*-
"""Recorrido de los archivos del repositorio, compartido por las pruebas.

No es un módulo de pruebas: `unittest discover` solo recoge los archivos
`test*.py`, así que este se importa pero no se ejecuta como suite.
"""

from __future__ import annotations

from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Carpetas que no forman parte del texto del repositorio.
IGNORED_DIRECTORIES = frozenset({".git", "__pycache__"})

# Sufijos que no son texto y quedan fuera de las comprobaciones de formato.
BINARY_SUFFIXES = frozenset({".pyc", ".pyo"})


def repository_files() -> list[tuple[Path, str]]:
    """Archivos del repositorio, como (ruta, ruta relativa en formato POSIX)."""
    files: list[tuple[Path, str]] = []
    for path in sorted(PROJECT_ROOT.rglob("*")):
        if not path.is_file():
            continue
        relative = path.relative_to(PROJECT_ROOT)
        if IGNORED_DIRECTORIES.intersection(relative.parts):
            continue
        if path.suffix in BINARY_SUFFIXES:
            continue
        files.append((path, relative.as_posix()))
    return files


def text_files() -> list[tuple[Path, str, str]]:
    """Archivos legibles como UTF-8, como (ruta, ruta relativa, texto)."""
    decoded: list[tuple[Path, str, str]] = []
    for path, relative in repository_files():
        try:
            decoded.append((path, relative, path.read_bytes().decode("utf-8")))
        except UnicodeDecodeError:
            continue
    return decoded
