# CONTEXTO.md · memoria de trabajo del proyecto

> **Para qué existe.** Las conversaciones de trabajo son largas y su contexto se comprime. Este archivo permite que cualquier sesión o persona continúe el proyecto **sin preguntarle nada a Fabián** sobre qué se está haciendo ni qué se decidió.
>
> **Mantenimiento:** se actualiza con cada mensaje de Fabián durante las sesiones de trabajo. Pidió el archivo el 19-10-2026.
>
> **Alcance:** solo el proyecto. El repositorio es público, así que los datos personales de Fabián no se guardan aquí.
>
> **Sobre las citas:** las páginas citadas aquí las cotejó Claude contra los PDF de las obras. Conforme a `CLAUDE.md` §4, para el estándar siguen contando como `FUENTE POR VERIFICAR` hasta que Fabián las compruebe.
>
> Última actualización: **2026-10-19, 17:40 (UTC−6)**.

---

## 1. Dos fuentes de decisiones que hay que reconciliar

1. **Este repositorio** (creado el 16-10-2026): fichas FON-001 a FON-010, ORT-001, TEC-001 y TEC-002, todas en estado `propuesta`. Regla de decisión `E − C + FL`.
2. **La Carta Fundacional de *eme-ĝir gibil*** (Claude Docs, privada, creada del 17 al 19-10-2026): arquitectura en capas 0 a 6, con decisiones que Fabián **aprobó** en conversación. Algunas contradicen fichas de este repositorio.

Las contradicciones están en `decisiones/PENDIENTES.md`, sin resolver: decide Fabián.

## 2. Reglas de trabajo que pidió Fabián

1. **Rigor máximo**: nada se afirma sin fuente. Jerarquía de fuentes de la Carta:
   - A: textos primarios.
   - B: gramáticas.
   - C: artículos revisados por pares.
   - D: ePSD2 y Oracc.
   - E: Wikipedia, IA y aficionados, con **peso nulo** como evidencia.
   Hay consenso cuando coinciden dos fuentes B o C.
2. **Ser herramienta, no traba**: corregir los errores manteniendo su idea, con honestidad sobre lo que no está atestiguado.
3. **Fonética para no especialistas**: explicar desde el español y con sonidos de lenguas vivas; los símbolos académicos van al final.
4. **Pureza léxica total**, sin préstamos. Neologismos solo con reglas nativas, al estilo de la RAE y de Islandia. Cuneiforme puro. Fonética fiel, no españolizada.
5. **Bases irrompibles, en efecto dominó**: no construir sobre nada sin verificar, y que ninguna recomendación rompa una regla ya aprobada.
6. **Orden**: primero el sumerio y después el acadio, con el mismo método.

## 3. Decisiones aprobadas por Fabián en la Carta (19-10-2026)

- **Capa 0**: nueve principios, aprobados el 18-10-2026 (edición 0.1).
- **Obra de referencia principal**: Jagersma (2010), *A Descriptive Grammar of Sumerian*.
- **Período estándar**: neosumerio de **Ur III** (siglo XXI a.C.).
- **ESC-001**: la nasal velar se escribe **ĝ**, aunque ePSD2 y Oracc usan ŋ.
- **ESC-002**: fuente **Noto Sans Cuneiform**, con glifos de estilo Ur III, que coinciden con los glifos de referencia de Unicode.
- **FON v1** (Jagersma, cap. 3):
  - *b d g* = [p t k] sin aspiración; *p t k* = [pʰ tʰ kʰ].
  - *z* = [ts].
  - *ř* → [ɾ].
  - Sin /h ʔ j/.
  - Ocho vocales: a e i u, breves y largas. No existe /o/.
  - Acento en la última sílaba.
- **LEX-001, opción C**: un préstamo acadio antiguo se reemplaza **solo** si existe un equivalente sumerio nativo atestiguado; si no, se marca [ANTIGUO-PRÉSTAMO].
- **LEX-002**: el vocabulario divino queda **solo para lectura**. Norma neutral, más una variante [TRADICIONAL] opcional.

## 4. Errores registrados, para no repetirlos

- **ERR-001**: se dieron *b d g* como sonoras (dato de Wikipedia). Se corrigió con Zólyomi (2017) y Jagersma (2010).
- **ERR-002**: *dub-šid* no significa «computadora». Por su tipo de compuesto significa «quien cuenta tablillas».
- **ERR-003**: se dio ř = [tsʰ] como dato firme. En el neosumerio estándar, ř pasa a r.
- **19-10-2026**: se recomendó una forma sumeria arcaica, del siglo XXIV, aunque el estándar es Ur III. Se corrigió.

## 5. Ficha en preparación: NOM-001 (nombre personal)

Fabián quiere un nombre que deje implícita la restauración del conocimiento perdido a través de la mirada hacia el cielo, sin nombres divinos (LEX-002).

**𒅆𒈬𒅔𒅆𒅅 *Igi-ĝu₁₀-in-ši-ĝál* · *Šiṭir-šamê-akaššar***
«Mis ojos están puestos en Él · Restauro la escritura del cielo»

| Pieza | Procedencia | Referencia |
|---|---|---|
| *igi-ĝu₁₀-in-ši-ĝál* | `[ATESTIGUADO]`: nombre de persona, Lagash, siglo XXI a.C. | Jagersma 2010, p. 536, ej. 88b (TCTI 1:L.618 4:10) |
| *igi-ĝu₁₀-an-šè-ĝál* | `[ATESTIGUADO]`, siglo XXIV a.C. Solo como nota histórica | Jagersma 2010, pp. 21, 535–536, ej. 88a |
| *šiṭir šamê*, «escritura del cielo» (las estrellas) | Frase acadia atestiguada en inscripciones neoasirias y neobabilónicas | Rochberg 2004, p. 1 |
| *akaššar*, «reparo, restauro» | *kašāru* A, paleobabilónico *ikšur — ikaššar*. Los objetos atestiguados son muros, edificios y ruinas | CAD K, pp. 284–285 |
| Nombre completo | `[DERIVADO]`: construido con reglas nativas, no atestiguado como nombre | — |

**Una trampa evitada:** en la forma arcaica, *an-šè* **no** significa «hacia el cielo». Son prefijos verbales que significan «hacia-él».

**Estado**: propuesta. Faltan dos confirmaciones de Fabián: Ur III para la parte sumeria y paleobabilónico para la acadia (ficha ACA-001).

## 6. Pendientes

- **Reconciliar las fichas de este repositorio con la Carta.** Ver `decisiones/PENDIENTES.md`.
- **Ficha «computadora»**: verificar *ĝiš-ḫur* y *-zu*.
- **LEX-003**: vocabulario para «Dios único».
- **Ficha para «y»**: *ù* es un préstamo acadio.
- **ACA-001**: período estándar del acadio. Se recomienda el paleobabilónico.
- **Clase 1 de sumerio (ergativo)**: falta el ejercicio de ordenar piezas y la pregunta «¿quién lleva la -e?».

## 7. Bitácora

- **16-10-2026**: andamiaje del repositorio (v0.1.0-borrador).
- **17 y 18-10-2026**: Carta Fundacional, capas 0 a 6, decisiones de la §3 y Clase 1 de sumerio.
- **19-10-2026**:
  - Investigación del nombre. Se verificó *ki-bé gi₄*, «restaurar» (Jagersma pp. 417, 442, 652).
  - Se propone NOM-001.
  - Se verificó *kašāru* en el CAD K.
  - Fabián propone este archivo de contexto y da permiso para usar el repositorio.
