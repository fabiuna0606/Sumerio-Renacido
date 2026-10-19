# CLAUDE.md — instrucciones permanentes del proyecto

Este archivo gobierna todas las sesiones de trabajo en el repositorio
**sumerio renacido** (eme-ĝir gibil). Léelo completo antes de modificar nada,
y lee también `CONTEXTO.md`, la memoria de trabajo del proyecto.

El proyecto busca revivir el sumerio como lengua hablada mediante un estándar
documentado y auditable. Lo rige la **Carta Fundacional de eme-ĝir gibil**
(Claude Docs, privada), cuyos principios de la capa 0 están resumidos abajo.
Cuando este repositorio y la Carta discrepen, **prevalece lo verificado en la
Carta**; la discrepancia se registra en `decisiones/PENDIENTES.md` y se
resuelve con una ficha. Así lo decidió Fabián el 19-10-2026.

**Reparto de responsabilidades:** Fabián, fundador y dueño del proyecto, toma
todas las decisiones. El asistente actúa como **secretaría técnica**: investiga,
redacta fichas, coteja fuentes y mantiene la infraestructura que las registra y
las verifica.

## 0. Principios inamovibles (capa 0 de la Carta, aprobada el 18-10-2026)

1. **Identidad.** Es sumerio. Ninguna regla nueva contradice una regla atestiguada.
2. **Base.** Sumerio del sur de Mesopotamia en la época de Gudea de Lagash y
   Ur III (c. 2150–2000 a.C.); dialecto de referencia: el neosumerio estándar.
3. **Escritura.** El cuneiforme es la escritura principal; las demás formas
   escritas lo transcriben.
4. **Pureza.** No se crean préstamos ni calcos de otras lenguas.
5. **Fidelidad fonética.** Se pronuncia según la reconstrucción mejor
   respaldada para el período base, nunca adaptada a otra lengua.
6. **Transparencia.** Cada palabra, regla y sonido lleva su etiqueta de
   procedencia. Lo creado nunca se presenta como antiguo.
7. **Continuidad.** Quien habla eme-ĝir gibil debe poder leer a Gudea. Nada se
   borra: lo que sale del uso activo pasa al registro de lectura.
8. **Crecimiento por adición.** Las capas superiores se corrigen; esta no.
9. **Evidencia sobre autoridad.** Ninguna decisión se sostiene en la palabra de
   nadie, ni del fundador ni de la IA, sin una fuente citada.

## 1. Reglas que no se pueden romper

1. **No inventes** referencias, números de página, citas textuales ni datos
   sobre el sumerio. Donde falte una fuente verificada, escribe exactamente:
   `FUENTE POR VERIFICAR`.
2. **No tomes decisiones filológicas** ni corrijas por tu cuenta las que ya
   están registradas. Si detectas una inconsistencia, anótala en
   `decisiones/PENDIENTES.md` y no la resuelvas hasta que Fabián decida.
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
8. **Nada se borra.** Una ficha superada se marca `reemplazada`, con el id de
   la que la sustituye; nunca se elimina.

## 2. Tipos de ficha y regla de decisión

| Tipo | Cuándo | Cómo se decide |
|------|--------|----------------|
| `evidencia` | Fonología, gramática y todo rasgo que las fuentes permiten decidir | Por la jerarquía de la §3. Exige al menos una fuente real. **No se puntúa.** |
| `convencion` | Ninguna evidencia decide entre las opciones (por ejemplo, dos letras para el mismo sonido) | Se adopta una convención y se marca como tal, nunca como evidencia. No se puntúa. |
| `puntuada` | **Histórico.** Fichas del borrador v0.1.0 | Ya no se usa: solo puede quedar en fichas `reemplazadas`. |

**El costo de aprendizaje nunca excluye un rasgo atestiguado** (principio 5,
fidelidad fonética). La antigua regla `Puntaje = E − C + FL` lo permitía; por
eso quedó en desuso el 19-10-2026.

Para **neologismos** (capa 5 de la Carta) se seguirá el procedimiento de nueve
pasos de la Carta, con su puntuación Q, cuando se registren las primeras
fichas de léxico.

## 3. Jerarquía de evidencia y de fuentes

**Para decisiones de la lengua** se usa el primer nivel que dé solución:

1. Atestiguado en el sumerio del tercer milenio.
2. Atestiguado en el sumerio paleobabilónico.
3. Analogía con reglas productivas del sumerio.
4. Creación con material y reglas nativas, declarada como tal.

No existe un nivel de «calco del acadio»: lo prohíbe el principio 4 (pureza).

**Para afirmaciones académicas:**

| Rango | Tipo | Ejemplos | Peso |
|-------|------|----------|------|
| A | Fuente primaria: los textos | Ediciones en ETCSL, Oracc, CDLI | Máximo |
| B | Gramáticas y monografías | Jagersma 2010; Zólyomi 2017; Attinger 1993; Edzard 2003 | Alto |
| C | Artículos con revisión por pares | JCS, ZA, Orientalia | Alto |
| D | Diccionarios académicos | ePSD2 | Alto para significados |
| E | Enciclopedias, Wikipedia, blogs, IA | — | **Nulo** como evidencia; solo sirven para localizar fuentes A–D |

**Consenso:** al menos dos fuentes independientes de rango B o C coinciden y
ninguna más reciente las contradice. En las capas 0 a 3, una ficha solo se da
por firme con doble fuente B o C; para una palabra basta su entrada del ePSD2.

## 4. Referencias del proyecto

- **Jagersma, *A Descriptive Grammar of Sumerian* (2010)** — obra de
  referencia principal, aprobada por Fabián el 18-10-2026. Si otra fuente la
  contradice, prevalece Jagersma, salvo que una publicación posterior con
  revisión por pares aporte evidencia nueva.
- Zólyomi, *An Introduction to the Grammar of Sumerian* (2017), para la
  enseñanza.
- Attinger (1993) y Edzard (2003), para contrastar.
- Foxvog, *Introduction to Sumerian Grammar*.
- ePSD2, Oracc, ETCSL, CDLI, BDTNS, DCCLT.

Una página o un pasaje concreto solo se cita si se **cotejó** en la obra misma,
y la ficha dice quién lo cotejó. Mientras no esté cotejado, se escribe
`FUENTE POR VERIFICAR`.

## 5. Gramática productiva frente a gramática receptiva

- **Gramática productiva:** lo que se usa al hablar y escribir en el estándar.
- **Gramática receptiva:** lo que solo se reconoce al leer textos antiguos.

Toda regla del estándar debe indicar a cuál de las dos pertenece.

## 6. Ciclo de vida de una ficha

```
propuesta → verificada → adoptada
```

- **propuesta** — registrada; sus fuentes pueden estar por cotejar.
- **verificada** — sus fuentes están cotejadas, por Fabián o por la secretaría
  técnica, y la ficha dice por quién.
- **adoptada** — Fabián la aprobó: forma parte del estándar.

Una ficha también puede quedar **rechazada** o **reemplazada** (indicando por
cuál, en el campo `reemplazada_por`). **Solo Fabián decide** que una ficha
pase a adoptada, rechazada o reemplazada. Una ficha verificada o adoptada
necesita al menos una fuente real; el validador lo comprueba.

## 7. Pruebas

Toda afirmación de que algo funciona debe acompañarse de **pruebas que pasen
en `tests/`**. Ejecuta:

```
python3 -m unittest discover -s tests -v
```

## 8. Cierre de sesión

Al cerrar cada sesión:

1. Actualiza `CONTEXTO.md` (bitácora y pendientes).
2. Informa los archivos cambiados.
3. Informa la salida de las pruebas.
4. Informa las inconsistencias detectadas.
5. Informa las preguntas pendientes.
