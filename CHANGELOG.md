# Registro de cambios del estándar

Este archivo registra las versiones del **estándar** del sumerio renacido, no
las de las herramientas del repositorio.

## Regla de versiones

El número de versión tiene la forma `mayor.menor.parche`:

- **Mayor** — cambios que **invalidan textos ya escritos** en el estándar.
- **Menor** — **añadidos** que no invalidan lo ya escrito.
- **Parche** — **correcciones**.

## v0.3.0-borrador (19-10-2026)

Primera versión con decisiones adoptadas.

- **Fonología.** FON-001, FON-004, FON-005, FON-006, FON-008 y FON-011 a
  FON-014 pasan a `adoptada`, con doble fuente de rango B (Jagersma 2010 y
  Zólyomi 2017). FON-002 queda `verificada` por falta de consenso.
- **Fichas nuevas, adoptadas, que reflejan decisiones ya tomadas por
  Fabián:**
  - FUN-001: período base.
  - FUN-002: obra de referencia principal.
  - ESC-002: forma visual de los signos.
  - LEX-001: préstamos acadios antiguos.
  - LEX-002: vocabulario religioso.
  - NOM-001: nombre del fundador.
  - ACA-001: período del acadio.
- **Técnica.** TEC-001 y TEC-002 adoptadas.
- **Validador.** Nueva área `fundamentos`.
- **Sincronización.** `CLAUDE.md` fija que el repositorio refleja la
  conversación de trabajo y la Carta, nunca al revés.

## v0.2.0-borrador (19-10-2026)

El repositorio se alinea con la Carta Fundacional, por decisión de Fabián.

- **Método.** El nuevo tipo de ficha `evidencia` se decide por las fuentes,
  sin puntaje. La regla `E − C + FL` queda como histórica, porque permitía
  excluir rasgos atestiguados por su costo de aprendizaje, contra la
  fidelidad fonética de la capa 0. `CLAUDE.md` recoge los principios de la
  capa 0 y las jerarquías de evidencia y de fuentes de la Carta.
- **Fichas nuevas.**
  - ESC-001 (adoptada): ĝ.
  - FON-011: b/d/g sordas sin aspirar, sin excepción por nivel.
  - FON-012: ř ya no es fonema.
  - FON-013: 8 vocales.
  - FON-014: acento final.
- **Fichas reemplazadas.** ORT-001, FON-003, FON-007, FON-009 y FON-010
  quedan en estado `reemplazada`; nada se borra.
- **Fichas convertidas.** FON-001, FON-002, FON-004, FON-005, FON-006 y
  FON-008 pasan a fichas de evidencia, con páginas de Jagersma (2010)
  cotejadas. Sus decisiones no cambian.
- **Validador.** Admite el tipo `evidencia`. Exige una fuente real en las
  fichas de evidencia y en las verificadas o adoptadas. 47 pruebas.
- **Etiquetas.** Nueva etiqueta de procedencia `[ANTIGUO-PRÉSTAMO]`
  (LEX-001 de la Carta).
- **Memoria de trabajo.** Nuevo `CONTEXTO.md`.

Es un cambio de versión **menor**: ninguna ficha estaba adoptada, así que no
se invalida ningún texto escrito en el estándar.

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
