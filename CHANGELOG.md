# Registro de cambios del estándar

Este archivo registra las versiones del **estándar** del sumerio renacido, no
las de las herramientas del repositorio.

## Regla de versiones

El número de versión tiene la forma `mayor.menor.parche`:

- **Mayor** — cambios que **invalidan textos ya escritos** en el estándar.
- **Menor** — **añadidos** que no invalidan lo ya escrito.
- **Parche** — **correcciones**.

## v0.2.0-borrador

Resolución de los pendientes de la sesión 1. Ninguna ficha cambia de estado:
todas siguen en `propuesta`.

- Aclarados los **tipos de ficha** en `CLAUDE.md`, `decisiones/PLANTILLA.md` y
  `README.md`: `puntuada` es una decisión binaria sobre incluir o no un rasgo
  y siempre se puntúa, aunque `E < 2`; `convencion` es la elección entre
  formas alternativas cuando ninguna alcanza `E ≥ 2`. FON-002, FON-007,
  FON-008 y FON-009 siguen siendo puntuadas y no cambian.
- Las cuatro fichas de convención (FON-010, ORT-001, TEC-001 y TEC-002) llevan
  `verificacion = "PENDIENTE: comprobar la convención en las fuentes"`.
- **ORT-001** decide usar `ŋ`, como el ePSD2, con el ePSD2 2.7.2 como fuente.
  La letra descartada se reemplazó por `ŋ` en la documentación, en la ficha
  FON-004 y en el nombre del proyecto, que pasa a ser **emegir gibil**; solo
  ORT-001 la conserva, al describir la opción descartada. Una prueba nueva
  falla si reaparece en cualquier otro archivo.
- **Licencias:** `LICENSE` (MIT, titular Fabián, 2026) para el código de
  `scripts/` y `tests/`; `LICENSE-CONTENT` (CC BY-SA 4.0) para el estándar,
  las fichas, el léxico y la documentación. El `README.md` añade la sección
  «Licencias y atribución» con las condiciones de Oracc, del ePSD2 y del
  ETCSL.
- **Referencias** de `CLAUDE.md` con versión y fecha de consulta cuando se
  conocen (ePSD2 2.7.2, consultado el 2026-09-27); en Foxvog, Oracc y ETCSL
  queda `FUENTE POR VERIFICAR`.
- `decisiones/PENDIENTES.md` marca como resueltas las cuatro inconsistencias y
  las preguntas de licencias y de ORT-001; deja abierta la de Foxvog, y anota
  el tipo `seleccion` como diseño futuro, la forma de cita de «gibil» en el
  ePSD2 y que las licencias se eligieron sin asesoría legal.

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
