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
