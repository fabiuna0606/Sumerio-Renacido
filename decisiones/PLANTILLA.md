+++
# --- Plantilla de ficha de decisión -------------------------------------
# Copia este archivo como decisiones/<ID>.md, donde <ID> es exactamente el
# valor del campo "id" (por ejemplo: FON-011.md, GRA-003.md, TEC-005.md).
# El validador ignora PLANTILLA.md y PENDIENTES.md.
#
# Este bloque, delimitado por dos líneas con exactamente "+++", contiene los
# metadatos en TOML. Debajo del bloque va el texto de la ficha en Markdown.
#
# CAMPOS OBLIGATORIOS EN TODAS LAS FICHAS
# -----------------------------------------------------------------------

# Identificador. Debe coincidir con el nombre del archivo, sin la extensión,
# y ser único en todo el directorio.
id = "XXX-000"

# Título breve del asunto que resuelve la ficha.
titulo = ""

# Área. Solo uno de: "fonologia", "ortografia", "gramatica", "lexico", "tecnica".
area = ""

# Tipo de ficha. Solo uno de: "evidencia", "convencion", "puntuada".
#   "evidencia"  → el rasgo se decide por las fuentes (CLAUDE.md §3).
#                  Exige al menos una fuente real. NO se puntúa.
#   "convencion" → ninguna evidencia decide entre las opciones; se adopta
#                  una convención declarada como tal. NO se puntúa.
#   "puntuada"   → HISTÓRICO (E − C + FL, en desuso desde el 19-10-2026).
#                  No lo uses en fichas nuevas.
# En "evidencia" y "convencion" no incluyas los campos de puntaje: el
# validador los rechaza.
tipo = ""

# La pregunta que la ficha responde, formulada de modo que admita respuesta.
pregunta = ""

# Lista de las opciones consideradas, una cadena por opción.
opciones = []

# La decisión tomada. La toma Fabián; se copia tal cual, sin matices propios.
decision = ""

# Estado. Solo uno de: "propuesta", "verificada", "adoptada", "rechazada",
# "reemplazada". Solo Fabián cambia el estado.
estado = "propuesta"

# Qué falta comprobar, o cómo se comprobó. Si está pendiente, dilo aquí.
verificacion = ""

# Lista de fuentes. Si ninguna está verificada: ["FUENTE POR VERIFICAR"].
# Nunca inventes referencias, páginas ni citas textuales.
fuentes = ["FUENTE POR VERIFICAR"]

# Condición explícita que obligaría a revisar esta decisión.
se_revisa_si = ""

# Vacío ("") salvo si estado = "reemplazada"; en ese caso, el id de la ficha
# que sustituye a esta, que debe existir en decisiones/.
reemplazada_por = ""

# CAMPOS SOLO EN FICHAS PUNTUADAS (tipo = "puntuada", HISTÓRICO)
# -----------------------------------------------------------------------
# Elimina las cinco líneas siguientes en toda ficha nueva.

# E — evidencia, de 0 a 3:
#   0 ninguna | 1 propuesta de un solo investigador
#   2 mayoritaria pero discutida | 3 consenso o atestiguación directa
E = 0

# C — costo de aprendizaje para un hispanohablante, de 0 a 3:
#   0 existe en español | 1 existe en inglés, árabe o chino
#   2 nuevo pero regular | 3 nuevo y difícil
C = 0

# FL — carga funcional, 0 o 1:
#   1 si distingue muchas palabras o es central en la gramática | 0 si no
FL = 0

# puntaje = E − C + FL. El validador comprueba la aritmética.
puntaje = 0

# incluye = (puntaje > 0). Un puntaje de 0 excluye.
incluye = false
+++

# XXX-000 — Título de la ficha

## Pregunta

Repite aquí la pregunta y explica por qué se plantea, sin introducir datos
sobre el sumerio que no estén verificados.

## Opciones consideradas

1. Primera opción.
2. Segunda opción.

## Decisión

La decisión, copiada tal como la entregó Fabián.

## Puntuación

Solo en fichas puntuadas: `E − C + FL = puntaje`, y la conclusión
(incluir o excluir). No añadas justificaciones propias de los valores.

## Verificación

Qué falta comprobar y en qué referencia. Mientras no esté comprobado:
`FUENTE POR VERIFICAR`.

## Se revisa si

La condición que obligaría a reabrir la ficha.
