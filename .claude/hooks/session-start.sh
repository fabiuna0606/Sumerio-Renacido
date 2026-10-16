#!/bin/bash
# Hook de arranque de sesión del proyecto "sumerio renacido".
#
# El proyecto no tiene dependencias que instalar: la regla 4 de CLAUDE.md
# admite solo la biblioteca estándar de Python 3.11 o superior. Así que este
# hook no instala nada; comprueba el intérprete y deja el estado del
# repositorio verificado antes de que empiece la sesión.
#
# Es idempotente y no pide nada por entrada. Termina siempre con código 0:
# informa de los fallos por su salida, sin impedir que la sesión arranque.
set -uo pipefail

cd "${CLAUDE_PROJECT_DIR:-$(dirname "$0")/../..}" || exit 0

echo "== sumerio renacido: comprobación de arranque =="

if ! command -v python3 >/dev/null 2>&1; then
  echo "DETENTE: no hay python3 en el entorno. La regla 4 de CLAUDE.md exige"
  echo "Python 3.11 o superior."
  exit 0
fi

version="$(python3 --version 2>&1)"
if ! python3 -c 'import sys; raise SystemExit(0 if sys.version_info >= (3, 11) else 1)'; then
  echo "DETENTE: $version es anterior a Python 3.11, que es lo que exige la"
  echo "regla 4 de CLAUDE.md (tomllib). Repórtalo antes de tocar nada."
  exit 0
fi
echo "$version"

status=0

echo "-- validador de fichas"
if ! python3 scripts/validate_decisions.py; then
  echo "El validador de fichas falla."
  status=1
fi

echo "-- pruebas"
if ! python3 -m unittest discover -s tests 2>&1 | tail -3; then
  echo "Las pruebas fallan."
  status=1
fi

if [ "$status" -ne 0 ]; then
  echo "AVISO: el repositorio no está en verde. Arréglalo antes de dar por"
  echo "bueno cualquier cambio (regla 7 de CLAUDE.md)."
else
  echo "Repositorio en verde."
fi

exit 0
