# Registro de cambios del estándar

Este archivo registra las versiones del **estándar** del sumerio renacido, no
las de las herramientas del repositorio.

## Regla de versiones

El número de versión tiene la forma `mayor.menor.parche`:

- **Mayor** — cambios que **invalidan textos ya escritos** en el estándar.
- **Menor** — **añadidos** que no invalidan lo ya escrito.
- **Parche** — **correcciones**.

## v0.1.0-borrador

Primera versión del andamiaje del proyecto.

- Estructura de carpetas: `decisiones/`, `lexico/`, `corpus/`, `scripts/` y
  `tests/`.
- `CLAUDE.md` con las instrucciones permanentes: reglas irrompibles, regla de
  decisión `Puntaje = E − C + FL`, jerarquía de evidencia, referencias del
  proyecto y ciclo de vida de las fichas.
- `README.md` con el propósito, las etiquetas de procedencia y las
  instrucciones de uso.
- Formato de las fichas de decisión y `decisiones/PLANTILLA.md`.
- Trece fichas iniciales, todas en estado `propuesta`: FON-001 a FON-010,
  ORT-001, TEC-001 y TEC-002.
- Esquema del glosario en `lexico/README.md`, todavía sin entradas.
- Validador de fichas `scripts/validate_decisions.py` con sus pruebas en
  `tests/test_decisions.py`.
- `decisiones/PENDIENTES.md` con las preguntas abiertas.

Ninguna decisión está verificada ni adoptada: **el estándar aún no fija nada**.
