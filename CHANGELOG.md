# Registro de cambios del estándar

Este archivo registra las versiones del **estándar** del sumerio renacido, no
las de las herramientas del repositorio.

## Regla de versiones

El número de versión tiene la forma `mayor.menor.parche`:

- **Mayor** — cambios que **invalidan textos ya escritos** en el estándar.
- **Menor** — **añadidos** que no invalidan lo ya escrito.
- **Parche** — **correcciones**.

**Nota sobre la numeración.** Entre el 27-09-2026 y el 08-11-2026 hubo dos
líneas de trabajo en paralelo: la rama `main` y la rama
`claude/contexto-proyecto`, que alineó el repositorio con la Carta
Fundacional. Las dos usaron el número v0.2.0. Al fusionarlas, las versiones
quedaron en orden cronológico: las de la Carta, antes publicadas como v0.2.0
y v0.3.0, son ahora **v0.3.0** y **v0.4.0**.

## v0.4.2-borrador (09-11-2026)

Decisiones de Fabián sobre los pendientes. No cambia ninguna decisión de la
lengua.

- **TEC-003** (adoptada): la secretaría técnica fusiona los PR a `main` solo
  si la integración continua está en verde. **TEC-004** (adoptada): ningún PR
  se fusiona con la CI en rojo.
- Se descarta el tipo de ficha `seleccion`, pensado para la regla de puntaje
  en desuso.
- **FON-002** sigue `verificada`. Fuente C encontrada: Smith, *JCS* 59 (2007),
  que defiende siete vocales; como es anterior a Jagersma (2010), rige FUN-002.
- Páginas de Zólyomi (2017) recomprobadas contra la edición impresa.
- Licencias aceptadas sin asesoría legal.
- Referencias de `CLAUDE.md` §4 completas para Zólyomi, Foxvog, Oracc y el
  ETCSL.

## v0.4.1-borrador (08-11-2026)

Fusión de las dos líneas de trabajo en `main`. No cambia ninguna decisión del
estándar.

- **ĝ o ŋ.** Rige ESC-001 (adoptada el 19-10-2026): **ĝ**. Se deshace la
  sustitución por ŋ que la rama `main` había aplicado el 27-09-2026 por
  ORT-001, ya reemplazada. El nombre del proyecto vuelve a ser **eme-ĝir
  gibil**. Se aplicó la decisión de Fabián del 19-10-2026: donde el
  repositorio y la Carta discrepan, prevalece la Carta.
- **De `main` se conservan:** las licencias (MIT para el código y CC BY-SA
  4.0 para el contenido), la integración continua, el hook de arranque de
  sesión, las comprobaciones automáticas de `tests/test_repository_rules.py`,
  las fichas TEC-003 y TEC-004 (en estado `propuesta`) y la versión del ePSD2
  en las referencias.
- **`README.md`**: nueva sección «Autoría y papel de la IA» y línea de estado.
- **`CONTEXTO.md`**: se corrigen el número de fichas adoptadas (19, no 17) y
  la fecha del andamiaje (27-09-2026); salen las notas personales de las
  clases, que no corresponden a un repositorio público.
- Las fechas históricas se escriben con «a. e. c.».
- Las pruebas esperan ahora 27 fichas.

## v0.4.0-borrador (19-10-2026)

Primera versión con decisiones adoptadas. Publicada originalmente como
v0.3.0-borrador.

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

## v0.3.0-borrador (19-10-2026)

El repositorio se alinea con la Carta Fundacional, por decisión de Fabián.
Publicada originalmente como v0.2.0-borrador.

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

## v0.2.1-borrador (27-09-2026; ampliada el 13 y el 15-10-2026)

Infraestructura del repositorio. No cambia nada del estándar ni del contenido
de ninguna ficha ya existente.

- **Integración continua:** `.github/workflows/ci.yml` ejecuta el validador de
  fichas y las pruebas con Python 3.11, sin dependencias externas, en cada
  push y en cada pull request. El workflow falla si falla cualquiera de los
  dos.
- **Fichas técnicas nuevas**, ambas de convención y en estado `propuesta`:
  **TEC-003** (estrategia de ramas: `main` es la rama estable y por defecto;
  cada sesión trabaja en su propia rama y entra a `main` solo mediante un PR
  que Fabián fusiona) y **TEC-004** (integración continua: ningún PR se
  fusiona con la CI en rojo).
- `CLAUDE.md` recoge las dos reglas en la sección 8, «Ramas e integración
  continua»; el cierre de sesión pasa a ser la sección 9.
- `README.md` completa la lista de archivos de la raíz: añade `LICENSE`,
  `LICENSE-CONTENT` y la carpeta `.github/workflows/`.

### Comprobaciones automáticas

Las reglas de `CLAUDE.md` que hasta ahora solo estaban escritas pasan a
comprobarse solas, en `tests/test_repository_rules.py`:

- **Regla 1** — la cadena `FUENTE POR VERIFICAR` se escribe exactamente así,
  sin variantes de mayúsculas, en todo el repositorio.
- **Regla 4** — el código de `scripts/` y `tests/` solo importa la biblioteca
  estándar, comprobado sobre el árbol sintáctico de cada archivo.
- **Regla 5** — todos los archivos del repositorio van en UTF-8, en NFC, con
  fin de línea LF, con salto de línea final y sin espacios al final de las
  líneas.
- **TEC-004** — el workflow ejecuta de verdad el validador y las pruebas con
  Python 3.11, y se dispara en push, en pull request y por calendario.
- Coherencia: toda ficha citada en la documentación existe en `decisiones/`.

Y la propia automatización se amplía:

- `.github/workflows/ci.yml` añade dos disparadores, `schedule` (los lunes) y
  `workflow_dispatch`, y un job nuevo que hace cumplir la **TEC-003**: un pull
  request que no apunte a `main` falla.
- `.claude/hooks/session-start.sh`, registrado en `.claude/settings.json`,
  comprueba al arrancar cada sesión que el intérprete cumple la regla 4 y que
  el validador y las pruebas pasan. Informa sin bloquear la sesión.
- `tests/repository_files.py` reúne el recorrido de los archivos del
  repositorio, que antes estaba duplicado en las pruebas.

## v0.2.0-borrador (27-09-2026)

Resolución de los pendientes de la sesión 1. Ninguna ficha cambia de estado:
todas siguen en `propuesta`.

- Aclarados los **tipos de ficha** en `CLAUDE.md`, `decisiones/PLANTILLA.md` y
  `README.md`: `puntuada` es una decisión binaria sobre incluir o no un rasgo
  y siempre se puntúa, aunque `E < 2`; `convencion` es la elección entre
  formas alternativas cuando ninguna alcanza `E ≥ 2`. FON-002, FON-007,
  FON-008 y FON-009 siguen siendo puntuadas y no cambian. *(Superado en
  v0.3.0 por el tipo `evidencia`.)*
- Las cuatro fichas de convención (FON-010, ORT-001, TEC-001 y TEC-002) llevan
  `verificacion = "PENDIENTE: comprobar la convención en las fuentes"`.
- **ORT-001** decide usar `ŋ`, como el ePSD2, con el ePSD2 2.7.2 como fuente,
  y el nombre del proyecto pasa a ser «emegir gibil». *(Superado en v0.3.0:
  ESC-001 adopta ĝ y ORT-001 queda reemplazada.)*
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

## v0.1.0-borrador (27-09-2026)

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
