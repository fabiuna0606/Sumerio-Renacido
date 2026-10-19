# Pendientes del proyecto

Preguntas abiertas e inconsistencias detectadas. **Aquí no se resuelve nada**:
las decisiones las toma Fabián. Este archivo solo las registra para que no se
pierdan. Lo resuelto no se borra: pasa a la sección final, con la fecha y la
ficha que lo resolvió.

## Preguntas abiertas

1. **Licencia del proyecto.** No está decidida. Hasta que lo esté, el
   repositorio no declara condiciones de uso ni de redistribución. La Carta
   prevé una licencia abierta que obligue a citar para la norma y el
   diccionario, y una licencia de software libre para el código.
2. **Licencias de Oracc y del ePSD2 para datos derivados.** Hay que comprobar
   qué permiten exactamente ambos proyectos respecto de obras derivadas antes
   de incorporar material suyo al léxico o al corpus. FUENTE POR VERIFICAR.
3. **FON-002 (no hay /o/).** Jagersma lo sostiene, pero Zólyomi (2017: 32)
   recoge propuestas de seis vocales y cita a Keetman con siete o nueve. Sin
   consenso de dos fuentes, la ficha queda `verificada` y rige Jagersma
   (FUN-002). Para cerrarla hace falta una fuente C que discuta /o/.
4. **Páginas de Zólyomi.** Se leyeron en el PDF oficial mediante extracción
   automática. Conviene confirmarlas en el libro.
5. **Fichas futuras:** LEX-003 (vocabulario monoteísta) y la ficha de
   «computadora» (candidato dub ĝiš-ḫur-zu, componentes por verificar en el
   ePSD2).

## Inconsistencias abiertas

1. **Referencias sin datos bibliográficos completos.** De Foxvog,
   *Introduction to Sumerian Grammar*, no se ha registrado año ni edición, y
   de ePSD2, Oracc y ETCSL no se ha registrado versión ni fecha de consulta.
   FUENTE POR VERIFICAR.

## Resuelto

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

La antigua pregunta 3 («¿qué letra usa el ePSD2?») queda contestada: según la
Carta, el ePSD2 escribe ŋ (por ejemplo, saŋ).

### 19-10-2026 (segunda parte): adopción y migración

Fabián delegó la adopción («hazlo como hemos venido trabajando y resuelve
tú») y fijó que el repositorio refleja la conversación y la Carta, no al
revés.

- **Segunda fuente.** Se cotejó Zólyomi (2017). Coincide con Jagersma en
  FON-001, FON-004, FON-005, FON-006, FON-008 y FON-011 a FON-014, que pasan
  a `adoptada` con doble fuente B. FON-002 sigue `verificada` (pregunta
  abierta 3).
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
