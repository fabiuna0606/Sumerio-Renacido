# CLAUDE.md — instrucciones permanentes del proyecto

Este archivo gobierna todas las sesiones de trabajo en el repositorio
**sumerio renacido** (emegir gibil). Léelo completo antes de modificar nada.

El proyecto busca revivir el sumerio como lengua hablada mediante un estándar
documentado y auditable, con un perfil **equilibrado** entre fidelidad
histórica y facilidad de aprendizaje.

**Reparto de responsabilidades:** Fabián, dueño del proyecto, toma todas las
decisiones filológicas. El asistente construye y mantiene la infraestructura
que las registra y las verifica.

## 1. Reglas que no se pueden romper

1. **No inventes** referencias, números de página, citas textuales ni datos
   sobre el sumerio. Donde falte una fuente verificada, escribe exactamente:
   `FUENTE POR VERIFICAR`.
2. **No tomes decisiones filológicas** ni corrijas las que ya están
   registradas. Si detectas una inconsistencia, anótala en
   `decisiones/PENDIENTES.md` y no la resuelvas.
3. **Copia las decisiones tal como las entrega Fabián**, sin matices ni
   justificaciones propias.
4. Usa **solo la biblioteca estándar de Python 3.11 o superior**: `tomllib`
   para leer TOML y `unittest` para las pruebas. No instales paquetes. Si la
   versión de Python es menor, detente y repórtalo.
5. Todo el texto va en **UTF-8**, con **normalización Unicode NFC** y fin de
   línea **LF**.
6. **Documentación en español**; nombres de archivos de código, funciones y
   variables **en inglés**.
7. **Commits pequeños y descriptivos**, uno por unidad lógica.

## 2. Regla de decisión

```
Puntaje = E − C + FL
```

Un rasgo **se incluye si y solo si Puntaje > 0**; un puntaje de **0 excluye**.

Las escalas son **ordinales**: el puntaje es una **regla de decisión
explícita, no una medida exacta**.

### Tipos de ficha

- **`puntuada`** — decisión **binaria** sobre incluir o no un rasgo. **Siempre
  se puntúa**, aunque `E < 2`: un `E` bajo lleva a **excluir** por la propia
  fórmula, y no convierte la ficha en otro tipo.
- **`convencion`** — **elección entre formas alternativas** (por ejemplo, la
  posición del acento o la letra que se usa) cuando **ninguna alcanza
  `E ≥ 2`**. Se adopta la convención académica y **no se puntúa**.

### E — evidencia

| Valor | Significado |
|-------|-------------|
| 0 | ninguna |
| 1 | propuesta de un solo investigador |
| 2 | mayoritaria pero discutida |
| 3 | consenso o atestiguación directa |

### C — costo de aprendizaje para un hispanohablante

| Valor | Significado |
|-------|-------------|
| 0 | existe en español |
| 1 | existe en inglés, árabe o chino |
| 2 | nuevo pero regular |
| 3 | nuevo y difícil |

### FL — carga funcional

| Valor | Significado |
|-------|-------------|
| 1 | distingue muchas palabras o es central en la gramática |
| 0 | no |

## 3. Jerarquía de evidencia

Se usa **el primer nivel que ofrezca solución**:

1. Sumerio del tercer milenio.
2. Sumerio literario paleobabilónico.
3. Analogía con reglas productivas del sumerio.
4. Calco del acadio.
5. Invención declarada.

## 4. Referencias del proyecto

- **Jagersma, A Descriptive Grammar of Sumerian (2010)** — gramática
  normativa del proyecto.
- Zólyomi, *An Introduction to the Grammar of Sumerian* (2017).
- Foxvog, *Introduction to Sumerian Grammar*. Año y edición: FUENTE POR
  VERIFICAR.
- ePSD2, versión 2.7.2 (compilada el 2024-08-31), consultado el 2026-09-27.
- Oracc. Versión y fecha de consulta: FUENTE POR VERIFICAR.
- ETCSL. Versión y fecha de consulta: FUENTE POR VERIFICAR.

Las referencias digitales se citan con su versión y su fecha de consulta
cuando se conocen; mientras no se conozcan, se escribe `FUENTE POR VERIFICAR`
en su lugar.

No cites páginas, secciones ni pasajes concretos de estas obras sin que
Fabián los haya verificado; mientras no lo estén, usa `FUENTE POR VERIFICAR`.

## 5. Gramática productiva frente a gramática receptiva

- **Gramática productiva:** lo que se usa al hablar y escribir en el estándar.
- **Gramática receptiva:** lo que solo se reconoce al leer textos antiguos.

Toda regla del estándar debe indicar a cuál de las dos pertenece.

## 6. Ciclo de vida de una ficha

```
propuesta → verificada (Fabián comprobó las fuentes) → adoptada
```

Una ficha también puede quedar **rechazada** o **reemplazada** (indicando por
cuál, en el campo `reemplazada_por`).

**Solo Fabián cambia el estado de una ficha.**

## 7. Pruebas

Toda afirmación de que algo funciona debe acompañarse de **pruebas que pasen
en `tests/`**. Ejecuta:

```
python3 -m unittest discover -s tests -v
```

## 8. Cierre de sesión

Al cerrar cada sesión, informa:

1. Archivos cambiados.
2. Salida de las pruebas.
3. Inconsistencias detectadas.
4. Preguntas pendientes.
