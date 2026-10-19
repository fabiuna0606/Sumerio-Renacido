# sumerio renacido (eme-ĝir gibil)

Proyecto para revivir el **sumerio** como lengua hablada mediante un estándar
**documentado y auditable**, regido por la **Carta Fundacional de eme-ĝir
gibil**. Sus principios inamovibles incluyen la **fidelidad fonética** al
período base (Gudea y Ur III, c. 2150–2000 a.C.) y la **pureza léxica**: el
costo de aprendizaje nunca justifica alterar un rasgo atestiguado.

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

Las decisiones las toma **Fabián**, fundador y dueño del proyecto. El
asistente actúa como secretaría técnica: investiga, coteja fuentes y mantiene
las herramientas que **registran y verifican** las decisiones. La memoria de
trabajo del proyecto está en `CONTEXTO.md`.

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
bitácora), `CHANGELOG.md` (versiones del estándar) y `.editorconfig`.

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
  nativo atestiguado (LEX-001 de la Carta).

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
