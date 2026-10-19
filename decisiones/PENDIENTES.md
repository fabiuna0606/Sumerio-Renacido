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
3. **Adopción de la fonología.** FON-001, FON-002, FON-004, FON-005, FON-006,
   FON-008 y FON-011 a FON-014 están en estado `verificada`: sus páginas de
   Jagersma (2010) están cotejadas. Falta que Fabián las pase a `adoptada`.
4. **Segunda fuente para las capas 0 a 3.** La Carta exige dos fuentes
   independientes de rango B o C para dar por firme un rasgo de estas capas.
   Las fichas de fonología solo tienen cotejado a Jagersma. Zólyomi (2017:
   28) está citado en la Carta para FON-011, pero sin cotejar contra el libro.
5. **Decisiones aprobadas en la Carta que aún no tienen ficha aquí:**
   - Capa 1: período base, corpus, jerarquía de evidencia y Jagersma como
     obra de referencia principal.
   - ESC-002: fuente Noto Sans Cuneiform, con glifos de estilo Ur III.
   - LEX-001: los préstamos acadios antiguos se reemplazan solo si hay un
     equivalente sumerio nativo atestiguado; si no, se marcan
     `[ANTIGUO-PRÉSTAMO]`.
   - LEX-002: el vocabulario religioso es solo para lectura; norma neutral y
     variante `[TRADICIONAL]` opcional.

   En la Carta siguen pendientes, además, LEX-003 (vocabulario monoteísta) y
   la ficha de «computadora».

## Inconsistencias abiertas

1. **El campo `verificacion` de TEC-001 y TEC-002** dice
   `"PENDIENTE: puntajes provisionales, comprobar en Jagersma y Zólyomi"`.
   Son fichas de convención técnica: ni llevan puntajes ni dependen de esas
   obras.
2. **Referencias sin datos bibliográficos completos.** De Foxvog,
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
