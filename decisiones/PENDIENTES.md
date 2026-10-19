# Pendientes del proyecto

Preguntas abiertas e inconsistencias detectadas. **Aquí no se resuelve nada**:
las decisiones las toma Fabián. Este archivo solo las registra para que no se
pierdan.

## Preguntas abiertas

1. **Licencia del proyecto.** No está decidida. Hasta que lo esté, el
   repositorio no declara condiciones de uso ni de redistribución.
2. **Licencias de Oracc y del ePSD2 para datos derivados.** Hay que comprobar
   qué permiten exactamente ambos proyectos respecto de obras derivadas antes
   de incorporar material suyo al léxico o al corpus. FUENTE POR VERIFICAR.
3. **Qué letra usa el ePSD2 (ORT-001).** La ficha ORT-001 decide usar la misma
   letra que el ePSD2 como regla de coordinación, pero falta comprobar si el
   ePSD2 escribe `ĝ` o `ŋ`. Mientras no se compruebe, la decisión está tomada
   pero su contenido concreto es desconocido.

## Inconsistencias detectadas

Registradas sin resolver, conforme a la regla 2 de `CLAUDE.md`.

1. **Fichas puntuadas con E < 2.** La regla de decisión dice que si ninguna
   opción alcanza `E ≥ 2`, la ficha es de tipo `convencion` y no se puntúa.
   Cuatro fichas iniciales llevan `tipo = "puntuada"` con `E < 2`:

   | Ficha | E | Puntaje | Resultado |
   |-------|---|---------|-----------|
   | FON-002 (vocal o) | 0 | 0 | excluir |
   | FON-007 (posible fonema /ř/) | 1 | −1 | excluir |
   | FON-008 (tonos) | 1 | −1 | excluir |
   | FON-009 (vocales largas) | 1 | 0 | excluir |

   Se han registrado como puntuadas, tal como se entregaron. Queda por decidir
   si la regla del tipo `convencion` se aplica solo a las fichas que deben
   fijar una forma positiva, o también a las que excluyen un rasgo.

2. **`E` se registra por ficha, no por opción.** La regla habla de que
   *ninguna opción* alcance `E ≥ 2`, pero el formato de ficha guarda un único
   valor de `E`, sin desglose por opción. Si se quiere puntuar cada opción por
   separado, hay que cambiar el formato.

3. **El texto de `verificacion` menciona puntajes en fichas sin puntaje.** Las
   trece fichas iniciales llevan
   `verificacion = "PENDIENTE: puntajes provisionales, comprobar en Jagersma y Zólyomi"`,
   incluidas las cuatro de convención (FON-010, ORT-001, TEC-001 y TEC-002),
   que por definición no tienen puntajes. Se ha copiado tal cual.

4. **ORT-001 sigue abierta y el repositorio ya escribe `ĝ`.** La
   documentación, el nombre del proyecto (eme-ĝir gibil) y la ficha FON-004
   usan `ĝ` antes de que ORT-001 esté verificada. Si el ePSD2 usara `ŋ`,
   habría que reescribir esos textos.

5. **Referencias del proyecto sin datos bibliográficos completos.** De Foxvog,
   *Introduction to Sumerian Grammar*, no se ha registrado año ni edición, y
   de ePSD2, Oracc y ETCSL no se ha registrado versión ni fecha de consulta.
   FUENTE POR VERIFICAR.

## Inconsistencias con la Carta Fundacional (detectadas el 19-10-2026)

Entre el 17 y el 19-10-2026, Fabián aprobó en conversación una Carta Fundacional (Claude Docs, privada). Algunas de sus decisiones contradicen fichas de este repositorio. Se registran **sin resolver**: decide Fabián.

| Ficha del repositorio | Lo que dice | Lo que aprobó Fabián en la Carta |
|---|---|---|
| ORT-001 | Usar la misma letra que el ePSD2 (regla de coordinación) | ESC-001: escribir **ĝ**, aunque el ePSD2 y Oracc usan ŋ |
| FON-003 | Admite la pronunciación sonora tradicional de *b d g* en los niveles iniciales | FON v1: *b d g* = [p t k] sin aspiración, sin excepción por nivel |
| FON-007 | Excluye /ř/ y usa la forma del lema en el ePSD2 | FON v1: en el neosumerio estándar, ř pasa a [ɾ] |
| FON-009 | Excluye las vocales largas | FON v1: 8 vocales, a e i u breves y largas |
| FON-010 | Acento en la sílaba de la raíz | FON v1: acento en la última sílaba |
| `CLAUDE.md` §2 y §3 | Regla `E − C + FL` y jerarquía de evidencia por épocas | Q(w) y jerarquía de fuentes A–E (textos primarios > gramáticas > artículos > ePSD2/Oracc > Wikipedia/IA) |

Sobre la pregunta abierta 3 de este archivo: según la Carta, el ePSD2 escribe `ŋ`. FUENTE POR VERIFICAR por Fabián.
