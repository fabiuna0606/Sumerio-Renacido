# Léxico del sumerio renacido — esquema

Esta carpeta contendrá el **glosario** del estándar. **Todavía no hay
entradas**: por ahora solo queda fijado el esquema que tendrá el archivo.

## Formato del archivo

- Un único archivo **TSV** (valores separados por tabuladores) en **UTF-8**,
  con normalización **NFC** y fin de línea **LF**.
- Se elige TSV, y no CSV, porque ningún campo del glosario contiene
  tabuladores, mientras que las comas aparecen con frecuencia en los
  significados y en las notas.
- La primera línea es la de encabezados, con los nombres de columna exactos
  que se indican más abajo y en ese mismo orden.
- Un campo vacío se deja vacío; no se escriben marcadores como `NULL` o `-`.

## Columnas

| Columna | Obligatoria | Contenido |
|---------|-------------|-----------|
| `id` | sí | Identificador único y estable de la entrada. |
| `lema_romanizado` | sí | Forma del lema en la romanización práctica del estándar. |
| `lema_epsd2` | sí | Forma del lema tal como aparece en el ePSD2, para poder cotejar. |
| `significado_es` | sí | Significado en español. |
| `categoria` | sí | Categoría gramatical de la entrada. |
| `procedencia` | sí | `ATESTIGUADO`, `DERIVADO` o `NUEVO`. |
| `fuente` | sí | Fuente de la entrada; `FUENTE POR VERIFICAR` mientras no esté comprobada. |
| `regla` | condicional | **Obligatoria si `procedencia` es `DERIVADO` o `NUEVO`**: la regla de formación aplicada. Vacía si es `ATESTIGUADO`. |
| `nivel` | sí | `nucleo` o `extendido`. |
| `estado` | sí | Estado de la entrada, con el mismo ciclo de vida que las fichas de decisión. |
| `notas` | no | Observaciones, dudas y remisiones a fichas de `decisiones/`. |

### Procedencia

Las tres etiquetas tienen el significado que fija el `README.md` de la raíz:
`ATESTIGUADO` para lo que aparece en el corpus, `DERIVADO` para lo obtenido
aplicando una regla productiva del sumerio a material atestiguado, y `NUEVO`
para las invenciones declaradas del proyecto. `DERIVADO` y `NUEVO` no se
admiten sin `regla`.

### Nivel

- `nucleo` — vocabulario básico del estándar, el que se aprende primero.
- `extendido` — el resto del glosario.

## Pendiente

- Decidir el nombre del archivo del glosario.
- Decidir la lista cerrada de valores admitidos en `categoria`.
- Escribir el validador del glosario, análogo a `scripts/validate_decisions.py`.
- ORT-001 afecta a `lema_romanizado`: mientras esa ficha no esté verificada,
  no hay forma fijada de escribir la letra en cuestión.
