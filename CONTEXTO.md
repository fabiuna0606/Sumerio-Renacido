# CONTEXTO.md · memoria de trabajo del proyecto

> **Para qué existe.** Las conversaciones de trabajo son largas y su contexto se comprime. Este archivo permite que cualquier sesión o persona continúe el proyecto **sin preguntarle nada a Fabián** sobre qué se está haciendo ni qué se decidió.
>
> **Mantenimiento:** se actualiza con cada mensaje de Fabián durante las sesiones de trabajo. Pidió el archivo el 19-10-2026.
>
> **Alcance:** solo el proyecto. El repositorio es público, así que los datos personales de Fabián no se guardan aquí.
>
> **Sobre las citas:** las páginas citadas aquí las cotejó Claude, como secretaría técnica, en las propias obras (`CLAUDE.md` §4). Cada ficha indica quién las cotejó y cómo.
>
> Última actualización: **2026-11-09, 01:00 (UTC−6)**.

---

## 1. Fuente de verdad

**Decisión de Fabián (19-10-2026):** las decisiones se toman en la conversación de trabajo con él y en la Carta Fundacional (Claude Docs, privada). **El repositorio es su reflejo, nunca al revés.** Claude lo actualiza en cada mensaje, sin pedir permiso para leerlo.

Estado actual: **v0.4.2-borrador**, en la rama `main`. La v0.4.0 fue la primera con decisiones adoptadas.
- 27 fichas: 21 adoptadas, 1 verificada (FON-002) y 5 reemplazadas.
- Los PR entran a `main` cuando la integración continua está en verde; los fusiona la secretaría técnica (TEC-003).
- Todas las pruebas pasan, también en la integración continua de GitHub.
- Sobre las fichas de fonología, Fabián delegó: «hazlo como hemos venido trabajando y resuelve tú». Se adoptaron las que tienen doble fuente B coincidente (Jagersma 2010 y Zólyomi 2017).

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

## 3. Decisiones aprobadas (cada una tiene su ficha en `decisiones/`)

- **Capa 0**: nueve principios, aprobados el 18-10-2026 (edición 0.1).
- **Obra de referencia principal**: Jagersma (2010), *A Descriptive Grammar of Sumerian*.
- **Período estándar** (FUN-001): neosumerio de **Ur III** (siglo XXI a. e. c.).
- **Acadio** (ACA-001): período estándar **paleobabilónico**.
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

## 5. NOM-001: nombre personal (adoptada)

Fabián quiere un nombre que deje implícita la restauración del conocimiento perdido a través de la mirada hacia el cielo, sin nombres divinos (LEX-002).

**𒅆𒈬𒅔𒅆𒅅 *Igi-ĝu₁₀-in-ši-ĝál* · *Šiṭir-šamê-akaššar***
«Mis ojos están puestos en Él · Restauro la escritura del cielo»

| Pieza | Procedencia | Referencia |
|---|---|---|
| *igi-ĝu₁₀-in-ši-ĝál* | `[ATESTIGUADO]`: nombre de persona, Lagash, siglo XXI a. e. c. | Jagersma 2010, p. 536, ej. 88b (TCTI 1:L.618 4:10) |
| *igi-ĝu₁₀-an-šè-ĝál* | `[ATESTIGUADO]`, siglo XXIV a. e. c. Solo como nota histórica | Jagersma 2010, pp. 21, 535–536, ej. 88a |
| *šiṭir šamê*, «escritura del cielo» (las estrellas) | Frase acadia atestiguada en inscripciones neoasirias y neobabilónicas | Rochberg 2004, p. 1 |
| *akaššar*, «reparo, restauro» | *kašāru* A, paleobabilónico *ikšur — ikaššar*. Los objetos atestiguados son muros, edificios y ruinas | CAD K, pp. 284–285 |
| Nombre completo | `[DERIVADO]`: construido con reglas nativas, no atestiguado como nombre | — |

**Una trampa evitada:** en la forma arcaica, *an-šè* **no** significa «hacia el cielo». Son prefijos verbales que significan «hacia-él».

**Estado**: adoptada. Fabián confirmó Ur III para la parte sumeria y paleobabilónico para la acadia el 19-10-2026.

## 6. Pendientes

- **FON-002 (no hay /o/).** Sin consenso. La fuente C encontrada (Smith, JCS 59, 2007) defiende siete vocales, pero es anterior a Jagersma (2010), así que rige FUN-002. Fabián decidió dejarla `verificada`; para cerrarla hace falta una publicación posterior a 2010.
- **Forma de cita de *gibil* en el ePSD2**: el glosario del ePSD2 no se pudo abrir desde el entorno de trabajo.
- **Ficha «computadora»**: verificar *ĝiš-ḫur* y *-zu* en el ePSD2.
- **LEX-003**: vocabulario para «Dios único».
- **Ficha para «y»**: *ù* es un préstamo acadio; cotejar en Jagersma la coordinación nativa.

## 7. Bitácora

- **27-09-2026**: andamiaje del repositorio (v0.1.0-borrador). El mismo día, en la sesión 2 sobre `main`: licencias, ORT-001 con ŋ (v0.2.0) e integración continua (v0.2.1, ampliada el 13 y el 15-10).
- **17 y 18-10-2026**: Carta Fundacional, capas 0 a 6, decisiones de la §3 y Clase 1 de sumerio.
- **19-10-2026**:
  - Investigación del nombre. Se verificó *ki-bé gi₄*, «restaurar» (Jagersma pp. 417, 442, 652).
  - Se propone NOM-001.
  - Se verificó *kašāru* en el CAD K.
  - Fabián propone este archivo de contexto y da permiso para usar el repositorio.
  - Fabián decide que se resuelvan las contradicciones según la Carta. Resultado:
    - Versión v0.3.0-borrador (publicada entonces como v0.2.0).
    - 18 fichas, todas válidas.
    - 47 pruebas, todas pasan.
  - Fabián delega la adopción y fija que el repositorio es reflejo de la conversación. Resultado:
    - Se coteja Zólyomi (2017) como segunda fuente.
    - Se adoptan las fichas con doble fuente.
    - Se migran FUN-001, FUN-002, ESC-002, LEX-001, LEX-002, NOM-001 y ACA-001.
    - Versión v0.4.0-borrador (publicada entonces como v0.3.0).
  - Fabián pregunta qué falta para empezar las clases. Respuesta: las bases del sumerio permiten empezar ya; los pendientes son de capas altas y no bloquean.
  - Se crea una memoria maestra privada en Claude Docs, con el contexto completo, incluido el personal, que no va en este repositorio público.
- **19 a 21-10-2026**: empiezan las clases de sumerio con oraciones y signos atestiguados en Jagersma. El seguimiento personal de las clases queda en la memoria privada, no aquí.
- **08-11-2026**: fusión de las dos líneas de trabajo (v0.4.1-borrador), por pedido de Fabián.
  - `main` y `claude/contexto-proyecto` habían avanzado por separado desde el 27-09. Prevalece la Carta: rige ĝ (ESC-001) y el nombre eme-ĝir gibil. Se conservan las licencias, la integración continua, TEC-003 y TEC-004.
  - Las versiones se renumeran en orden cronológico (`CHANGELOG.md`).
  - `README.md`: sección «Autoría y papel de la IA».
  - `main` pasa a ser la rama por defecto, como dice la TEC-003.
  - Se corrigen en este archivo el número de fichas adoptadas (19) y la fecha del andamiaje (27-09).
- **09-11-2026**: Fabián decide los pendientes, eligiendo las opciones recomendadas (v0.4.2-borrador).
  - TEC-003 y TEC-004 adoptadas: la secretaría técnica fusiona los PR con la CI en verde.
  - Se descarta el tipo de ficha `seleccion`.
  - FON-002 sigue `verificada`. Se encontró la fuente C: Smith (2007), con siete vocales.
  - Páginas de Zólyomi recomprobadas contra la edición impresa: las diez citas coinciden.
  - Licencias aceptadas sin asesoría legal.
  - Referencias completas: Foxvog, Oracc y ETCSL.
  - Se borran las ramas antiguas ya contenidas en `main`.
