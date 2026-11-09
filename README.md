# sumerio renacido (eme-ĝir gibil)

Proyecto para revivir el **sumerio** como lengua hablada mediante un estándar
**documentado y auditable**, regido por la **Carta Fundacional de eme-ĝir
gibil**. Sus principios inamovibles incluyen la **fidelidad fonética** al
período base (Gudea y Ur III, c. 2150–2000 a. e. c.) y la **pureza léxica**:
el costo de aprendizaje nunca justifica alterar un rasgo atestiguado. Cuando
el sumerio esté consolidado, el mismo método se aplicará al **acadio**.

**Estado:** v0.4.1-borrador. 27 fichas de decisión: 21 adoptadas, 1
verificada, 0 propuestas y 5 reemplazadas.

## Propósito

El sumerio se conoce por sus textos, no por hablantes vivos. Cualquier intento
de hablarlo obliga a tomar decisiones donde la evidencia es incompleta. Este
repositorio no oculta esas decisiones: las **registra una por una**, con la
evidencia que las respalda, su estado de verificación y las condiciones que
obligarían a revisarlas.

Dos consecuencias prácticas:

- Nada del estándar es anónimo: cada rasgo del sumerio renacido nace de una
  ficha de decisión que se puede leer, discutir y refutar.
- La distancia entre lo atestiguado y lo reconstruido queda siempre visible
  mediante las etiquetas de procedencia.

## Autoría y papel de la IA

**Sumerio Renacido es un proyecto de Fabián**, su fundador y dueño.

- **Fabián eligió las fuentes** en las que se basa el estándar. La obra de
  referencia principal es la tesis doctoral de Bram Jagersma, *A Descriptive
  Grammar of Sumerian* (Universidad de Leiden, 2010), fijada en la ficha
  FUN-002. Para el acadio se usa el *Chicago Assyrian Dictionary*.
- **Fabián fijó las condiciones del proyecto**: el período de Ur III como
  base, el cuneiforme como escritura principal, la pureza léxica, la
  pronunciación fiel sin adaptarla al español, y que la investigación
  académica con consenso pese siempre más que Wikipedia o cualquier fuente sin
  fundamento. Sobre esas condiciones aprobó los principios de la Carta
  Fundacional.
- **Solo Fabián decide** que una ficha pase a adoptada, rechazada o
  reemplazada.

El proyecto se trabaja con **Claude**, una IA de Anthropic, que aparece en el
historial como coautora de los commits. Su papel es de **secretaría técnica**:
propone, redacta las fichas, coteja cada afirmación con las fuentes elegidas y
mantiene el validador, las pruebas y la integración continua. **Las reglas del
estándar no salen de la IA**, sino de las fuentes académicas, y la propia
jerarquía de fuentes del proyecto le da a la IA peso nulo como evidencia
(`CLAUDE.md` §3). La memoria de trabajo del proyecto está en `CONTEXTO.md`.

## Estructura de carpetas

| Carpeta | Contenido |
|---------|-----------|
| `decisiones/` | Fichas de decisión, una por archivo `<ID>.md`. Incluye `PLANTILLA.md` (formato comentado) y `PENDIENTES.md` (preguntas abiertas e inconsistencias detectadas). |
| `lexico/` | Glosario del estándar. Por ahora solo el esquema previsto en `lexico/README.md`. |
| `corpus/` | Textos del proyecto (vacía por el momento). |
| `scripts/` | Herramientas en Python, biblioteca estándar únicamente. |
| `tests/` | Pruebas con `unittest`. |

Archivos en la raíz: `CLAUDE.md` (instrucciones permanentes para las sesiones
de trabajo), `CONTEXTO.md` (memoria de trabajo: estado, decisiones y
bitácora), `CHANGELOG.md` (versiones del estándar), `LICENSE` (licencia del
código), `LICENSE-CONTENT` (licencia del contenido) y `.editorconfig`. En
`.github/workflows/` está la integración continua, y en `.claude/` el hook que
comprueba el repositorio al empezar cada sesión de trabajo.

## Etiquetas de procedencia

Toda forma del estándar lleva una etiqueta que declara de dónde viene:

- **`[ATESTIGUADO]`** — la forma aparece en el corpus sumerio. Es un dato, no
  una reconstrucción.
- **`[DERIVADO]`** — la forma no está atestiguada como tal, pero se obtiene
  aplicando una regla productiva del propio sumerio a material atestiguado.
  Exige indicar la regla empleada.
- **`[NUEVO]`** — la forma es una invención declarada del proyecto, necesaria
  para hablar de lo que el corpus no cubre. Exige indicar la regla de
  formación empleada.
- **`[ANTIGUO-PRÉSTAMO]`** — préstamo acadio antiguo, ya presente en el
  sumerio atestiguado, que se conserva porque no existe un equivalente sumerio
  nativo atestiguado (LEX-001).

Estas etiquetas describen **el origen** de una forma, no su calidad ni su
grado de aceptación: el estado de una decisión se indica aparte, en el campo
`estado` de su ficha.

## Ciclo de vida de las fichas

```
propuesta → verificada → adoptada
```

- **`propuesta`** — registrada; sus fuentes pueden estar por cotejar.
- **`verificada`** — sus fuentes están cotejadas en la obra misma, por Fabián
  o por la secretaría técnica, y la ficha dice por quién.
- **`adoptada`** — Fabián la aprobó: forma parte del estándar.

Una ficha puede terminar también como **`rechazada`**, o como
**`reemplazada`**, indicando en `reemplazada_por` la ficha que la sustituye.
Nada se borra.

**Solo Fabián decide** que una ficha pase a adoptada, rechazada o reemplazada.

## Tipos de ficha

- **`evidencia`** — el rasgo se decide por las fuentes, con la jerarquía de
  `CLAUDE.md` §3. Exige al menos una fuente real. No se puntúa.
- **`convencion`** — ninguna evidencia decide entre las opciones; se adopta
  una convención declarada como tal.
- **`puntuada`** — histórico: la regla `E − C + FL` del borrador v0.1.0
  quedó en desuso el 19-10-2026, porque permitía excluir rasgos atestiguados
  por su costo de aprendizaje. Solo se conserva en fichas reemplazadas.

## Cómo ejecutar las pruebas

Requiere **Python 3.11 o superior** y ninguna dependencia externa.

```sh
python3 -m unittest discover -s tests -v
```

Para validar las fichas directamente y ver los errores por ficha:

```sh
python3 scripts/validate_decisions.py
```

El validador termina con código de salida `0` si todas las fichas de
`decisiones/` son válidas y `1` si encuentra algún error. Acepta como
argumento opcional un directorio distinto de `decisiones/`.

## Licencias y atribución

- **Código** (`scripts/`, `tests/`) — licencia MIT, en `LICENSE`, con titular
  Fabián y año 2026.
- **Contenido** (estándar, fichas de `decisiones/`, léxico y documentación) —
  CC BY-SA 4.0, en `LICENSE-CONTENT`:
  <https://creativecommons.org/licenses/by-sa/4.0/>.

Materiales de terceros incorporados al proyecto:

- Los datos de **Oracc** y del **ePSD2** están bajo **CC BY-SA 3.0**: exigen
  **atribución** y **compartir igual**.
- El material derivado del **ETCSL** está bajo **CC BY-NC-SA 3.0**: debe
  **marcarse en su procedencia** y **no puede usarse en materiales de pago**.

Las licencias se eligieron **sin asesoría legal**; queda anotado en
`decisiones/PENDIENTES.md`.
