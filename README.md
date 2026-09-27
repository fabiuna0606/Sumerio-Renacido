# sumerio renacido (eme-ĝir gibil)

Proyecto para revivir el **sumerio** como lengua hablada mediante un estándar
**documentado y auditable**, con un perfil **equilibrado** entre fidelidad
histórica y facilidad de aprendizaje.

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

Las decisiones filológicas las toma **Fabián**, dueño del proyecto. El
repositorio y sus herramientas solo las **registran y verifican**.

## Estructura de carpetas

| Carpeta | Contenido |
|---------|-----------|
| `decisiones/` | Fichas de decisión, una por archivo `<ID>.md`. Incluye `PLANTILLA.md` (formato comentado) y `PENDIENTES.md` (preguntas abiertas e inconsistencias detectadas). |
| `lexico/` | Glosario del estándar. Por ahora solo el esquema previsto en `lexico/README.md`. |
| `corpus/` | Textos del proyecto (vacía por el momento). |
| `scripts/` | Herramientas en Python, biblioteca estándar únicamente. |
| `tests/` | Pruebas con `unittest`. |

Archivos en la raíz: `CLAUDE.md` (instrucciones permanentes para las sesiones
de trabajo), `CHANGELOG.md` (versiones del estándar) y `.editorconfig`.

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

Estas etiquetas describen **el origen** de una forma, no su calidad ni su
grado de aceptación: el estado de una decisión se indica aparte, en el campo
`estado` de su ficha.

## Ciclo de vida de las fichas

```
propuesta → verificada → adoptada
```

- **`propuesta`** — registrada, con puntajes o convención provisionales.
- **`verificada`** — Fabián comprobó las fuentes.
- **`adoptada`** — forma parte del estándar.

Una ficha puede terminar también como **`rechazada`**, o como
**`reemplazada`**, indicando en `reemplazada_por` la ficha que la sustituye.

**Solo Fabián cambia el estado de una ficha.**

## Regla de decisión

Las fichas de tipo `puntuada` aplican:

```
Puntaje = E − C + FL
```

donde `E` es la evidencia (0–3), `C` el costo de aprendizaje para un
hispanohablante (0–3) y `FL` la carga funcional (0 o 1). Un rasgo se incluye
**si y solo si Puntaje > 0**; un puntaje de 0 excluye. Cuando ninguna opción
alcanza `E ≥ 2`, la ficha es de tipo `convencion`: se adopta la convención
académica y no se puntúa. Las escalas son **ordinales**: el puntaje es una
regla de decisión explícita, no una medida exacta. El detalle de las escalas
está en `CLAUDE.md`.

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
