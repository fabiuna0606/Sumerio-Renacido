# Pendientes del proyecto

Preguntas abiertas e inconsistencias detectadas. **Aquí no se resuelve nada**:
las decisiones las toma Fabián. Este archivo solo las registra para que no se
pierdan. Lo resuelto no se borra: pasa a la sección final, con la fecha y la
ficha que lo resolvió.

## Preguntas abiertas

1. **FON-002 (no hay /o/).** Jagersma lo sostiene. Zólyomi (2017: 32) recoge
   propuestas de seis vocales y cita a Keetman (2005) con siete o nueve. La
   fuente C buscada el 09-11-2026 es Smith, «[-ATR] Harmony and the Vowel
   Inventory of Sumerian», *Journal of Cuneiform Studies* 59 (2007): 19–38,
   que defiende siete vocales, entre ellas /o/. Contradice a Jagersma, pero es
   anterior a él, así que rige Jagersma (FUN-002 y `CLAUDE.md` §4). No hay
   consenso de dos fuentes: por decisión de Fabián del 09-11-2026, la ficha
   sigue `verificada` y no se adopta. Para cerrarla haría falta una
   publicación con revisión por pares posterior a 2010. Pista sin leer:
   Keetman, «The limits for vowel harmony in Sumerian and some remarks about
   the need of transparent data», NABU 2009/65.
2. **Fichas futuras:** LEX-003 (vocabulario monoteísta), la ficha de
   «computadora» (candidato dub ĝiš-ḫur-zu, componentes por verificar en el
   ePSD2) y la ficha de la palabra «y» (*ù* es un préstamo acadio).
3. **Forma de cita de «gibil» en el ePSD2.** Falta comprobar en el ePSD2 la
   forma de cita de `gibil` («nuevo»), que forma parte del nombre del
   proyecto. El 09-11-2026 se confirmó que la versión vigente es la 2.7.2,
   pero su glosario no se pudo abrir desde el entorno de trabajo. FUENTE POR
   VERIFICAR.

## Inconsistencias abiertas

Ninguna.

## Resuelto

### 09-11-2026: decisiones de Fabián sobre los pendientes

Fabián eligió las opciones recomendadas en las seis preguntas que se le
presentaron, cada una con sus razones a favor y en contra.

- **Fusión a `main` (antigua pregunta 6), TEC-003 y TEC-004.** La secretaría
  técnica fusiona los PR solo si la integración continua está en verde. TEC-003
  y TEC-004 pasan a `adoptada`.
- **Tipo de ficha `seleccion` (antiguo «Diseño futuro»). Descartado.** Se
  pensó para la regla de puntaje, en desuso desde el 19-10-2026. Cuando varias
  opciones tienen evidencia, decide la jerarquía de fuentes de `CLAUDE.md` §3,
  y si chocan, prevalece Jagersma (FUN-002).
- **FON-002.** Sigue `verificada`, y se busca una fuente C (pregunta abierta 1).
- **Páginas de Zólyomi.** Se cierra. El PDF de ELTE Reader es la edición
  impresa (Eötvös University Press, 2017, ISBN 978-963-284-844-0). El
  09-11-2026 se recomprobaron contra el número impreso las diez citas de las
  fichas: p. 22 (ŋ, ḫ, š), p. 28 (oclusivas sordas con aspiración), p. 29
  (/dr/, cuatro vocales escritas, longitud vocálica), p. 32 (seis vocales;
  Keetman) y p. 33 (acento de intensidad, en la última sílaba). Todas
  coinciden.
- **Licencias sin asesoría legal.** Fabián acepta MIT y CC BY-SA 4.0 sin
  revisión jurídica. Sigue en pie la condición del ETCSL: su material no puede
  usarse en materiales de pago (`README.md`).
- **Ramas antiguas.** Se borran las ramas ya contenidas en `main`; nada de su
  historial se pierde.

También se completaron las referencias (antigua inconsistencia 1): Foxvog,
CDLP 2.0 (2016-01-04); Oracc, sin número de versión, con fecha de consulta;
ETCSL, segunda edición, Oxford 1998–2006. El detalle está en `CLAUDE.md` §4.

### 08-11-2026: fusión de las dos líneas de trabajo

Entre el 27-09-2026 y el 08-11-2026 el repositorio avanzó por dos ramas que no
se conocían entre sí: `main` (sesión 2: licencias, ORT-001 con ŋ, integración
continua, TEC-003 y TEC-004) y `claude/contexto-proyecto` (alineación con la
Carta y primeras adopciones). Se fusionaron siguiendo la decisión de Fabián
del 19-10-2026: **donde el repositorio y la Carta discrepan, prevalece la
Carta**.

| Discrepancia | Rama `main` | Resolución |
|---|---|---|
| ĝ o ŋ | ORT-001 escribía ŋ y el nombre era «emegir gibil» | Rige ESC-001 (adoptada): **ĝ**, y el nombre **eme-ĝir gibil**. ORT-001 sigue `reemplazada` |
| Tipos de ficha | `puntuada` siempre se puntúa | Rige el tipo `evidencia` de la Carta; `puntuada` es histórico |
| Licencias | Resueltas en la sesión 2 | Se conservan: son compatibles con lo que prevé la Carta (una licencia abierta que obligue a citar para la norma y una licencia de software libre para el código) |
| Números de versión | v0.2.0 y v0.2.1 | Se conservan; las versiones de la Carta pasan a v0.3.0 y v0.4.0 (`CHANGELOG.md`) |

La prueba que fallaba si aparecía la letra ĝ fuera de ORT-001 se retiró, porque
contradice ESC-001. Las demás comprobaciones automáticas de `main` se
conservan.

### 19-10-2026: el repositorio se alinea con la Carta Fundacional

Decisión de Fabián: donde el repositorio y la Carta discrepan, **prevalece lo
verificado en la Carta**.

| Discrepancia | Antes | Resolución |
|---|---|---|
| ĝ o ŋ | ORT-001: usar la letra del ePSD2 | ESC-001 (adoptada): **ĝ**; al buscar en el ePSD2 se cambia por ŋ |
| *b d g* | FON-003: se admitía la pronunciación sonora en los niveles iniciales | FON-011: [p t k] sin aspiración, sin excepción por nivel |
| ř | FON-007: excluir y usar el lema del ePSD2 | FON-012: no es fonema; ante vocal [ɾ], a final de sílaba se pierde |
| Vocales largas | FON-009: excluidas | FON-013: 8 vocales, a e i u breves y largas |
| Acento | FON-010: en la raíz, sin fuente | FON-014: fijo en la última sílaba |
| Método | `E − C + FL` y un nivel de «calco del acadio» | Fichas de tipo `evidencia` y jerarquías de la Carta (`CLAUDE.md` §2 y §3); `puntuada` queda como tipo histórico |

Las fichas antiguas siguen en el directorio, en estado `reemplazada`.

Con esto también quedan resueltas tres inconsistencias anteriores:

- **Fichas puntuadas con E < 2.** Ya no queda ninguna ficha puntuada vigente.
- **`E` registrado por ficha y no por opción.** Deja de aplicar al quedar en
  desuso la regla de puntaje.
- **ORT-001 seguía abierta mientras el repositorio ya escribía ĝ.** Resuelto
  por ESC-001.

La antigua pregunta «¿qué letra usa el ePSD2?» queda contestada: según la
Carta, el ePSD2 escribe ŋ (por ejemplo, saŋ).

### 19-10-2026 (segunda parte): adopción y migración

Fabián delegó la adopción («hazlo como hemos venido trabajando y resuelve
tú») y fijó que el repositorio refleja la conversación y la Carta, no al
revés.

- **Segunda fuente.** Se cotejó Zólyomi (2017). Coincide con Jagersma en
  FON-001, FON-004, FON-005, FON-006, FON-008 y FON-011 a FON-014, que pasan
  a `adoptada` con doble fuente B. FON-002 sigue `verificada` (pregunta
  abierta 1).
- **Decisiones migradas a fichas:**
  - FUN-001 (período base).
  - FUN-002 (Jagersma, obra de referencia).
  - ESC-002 (Noto Sans Cuneiform, estilo Ur III).
  - LEX-001 (préstamos acadios antiguos).
  - LEX-002 (vocabulario religioso).
  - NOM-001 (nombre del fundador).
  - ACA-001 (paleobabilónico).
- **TEC-001 y TEC-002.** Se corrigió su texto de verificación, que hablaba
  de puntajes que no tienen, y pasan a `adoptada`.

### 27-09-2026: resoluciones de Fabián en la sesión 2 (rama `main`)

Se conservan tal como se registraron, para no perder el rastro.

- **Licencia del proyecto.** El código de `scripts/` y `tests/` se publica
  bajo la licencia MIT, en `LICENSE`, con titular «Fabián» y año 2026. El
  resto del contenido —estándar, fichas, léxico y documentación— se publica
  bajo CC BY-SA 4.0, con el aviso en `LICENSE-CONTENT`.
- **Licencias de Oracc y del ePSD2 para datos derivados.** Los datos de
  Oracc y del ePSD2 están bajo CC BY-SA 3.0: exigen atribución y compartir
  igual. El material derivado del ETCSL está bajo CC BY-NC-SA 3.0: debe
  marcarse en su procedencia y no puede usarse en materiales de pago. Queda
  registrado en la sección «Licencias y atribución» del `README.md`.
- **Qué letra usa el ePSD2 (ORT-001).** El ePSD2 usa ŋ, por ejemplo en el
  lema `diŋir`. ORT-001 recogió esa decisión con el ePSD2 como fuente.
  *(Superado el 19-10-2026 por ESC-001.)*
- **Fichas puntuadas con E < 2.** Una ficha `puntuada` siempre se puntúa,
  aunque `E < 2`; FON-002, FON-007, FON-008 y FON-009 seguían siendo
  puntuadas. *(Superado el 19-10-2026 por el tipo `evidencia`.)*
- **`E` se registra por ficha, no por opción.** El desglose por opción se
  aplazó al tipo `seleccion` (ver «Diseño futuro»).
- **Texto de `verificacion` en las fichas de convención.** FON-010, ORT-001,
  TEC-001 y TEC-002 pasaron a llevar
  `verificacion = "PENDIENTE: comprobar la convención en las fuentes"`.
