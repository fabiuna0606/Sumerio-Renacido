# Pendientes del proyecto

Preguntas abiertas e inconsistencias detectadas. **Aquí no se resuelve nada**:
las decisiones las toma Fabián. Este archivo solo las registra para que no se
pierdan. Las entradas que Fabián ya resolvió se conservan marcadas como
**RESUELTA**, con la resolución tal como la entregó, para no perder el rastro.

## Preguntas abiertas

1. **Licencia del proyecto. RESUELTA (sesión 2).** El código de `scripts/` y
   `tests/` se publica bajo la licencia MIT, en `LICENSE`, con titular
   «Fabián» y año 2026. El resto del contenido —estándar, fichas, léxico y
   documentación— se publica bajo CC BY-SA 4.0, con el aviso en
   `LICENSE-CONTENT`.
2. **Licencias de Oracc y del ePSD2 para datos derivados. RESUELTA
   (sesión 2).** Los datos de Oracc y del ePSD2 están bajo CC BY-SA 3.0:
   exigen atribución y compartir igual. El material derivado del ETCSL está
   bajo CC BY-NC-SA 3.0: debe marcarse en su procedencia y no puede usarse en
   materiales de pago. Queda registrado en la sección «Licencias y atribución»
   del `README.md`.
3. **Qué letra usa el ePSD2 (ORT-001). RESUELTA (sesión 2).** El ePSD2 usa
   `ŋ`, por ejemplo en el lema `diŋir`. ORT-001 recoge esa decisión con el
   ePSD2 como fuente, y el repositorio escribe `ŋ` en todos sus textos. La
   ficha sigue en estado `propuesta` hasta que Fabián compruebe la convención
   en las fuentes.
4. **Forma de cita de «gibil» en el ePSD2.** El nombre en sumerio del proyecto
   es «emegir gibil», porque `emegir` es la forma de cita del ePSD2 para «la
   lengua sumeria». Falta comprobar en el ePSD2 la forma de cita de `gibil`
   («nuevo»). FUENTE POR VERIFICAR.
5. **Las licencias se eligieron sin asesoría legal.** Ni la elección de MIT
   para el código, ni la de CC BY-SA 4.0 para el contenido, ni el resumen de
   las condiciones de Oracc, del ePSD2 y del ETCSL han pasado por revisión
   jurídica.

6. **¿Se automatiza la fusión a `main`?** Fabián pidió automatizar todo y
   no depender de él. Todas las comprobaciones del proyecto están ya
   automatizadas, pero la **TEC-003** reserva la fusión a Fabián, y la regla 2
   de `CLAUDE.md` impide resolver esa tensión sin él. Queda registrada sin
   resolver, con las dos vías posibles y ninguna elegida: activar la fusión
   automática de GitHub para los PR que lleguen en verde, o cambiar la
   TEC-003. Mientras la ficha diga lo que dice, la fusión es el único paso
   manual que queda.

   De esa misma fusión dependen dos cosas más: que `main` reciba el contenido
   del estándar, y que arranque la ejecución semanal de la integración
   continua, porque GitHub solo lanza los disparadores `schedule` desde la
   rama por defecto del repositorio.

## Inconsistencias detectadas

Registradas sin resolver, conforme a la regla 2 de `CLAUDE.md`. Las que Fabián
ya resolvió quedan marcadas como **RESUELTA**.

1. **Fichas puntuadas con E < 2. RESUELTA (sesión 2).** No hay
   inconsistencia: una ficha `puntuada` es una decisión binaria sobre incluir
   o no un rasgo y **siempre se puntúa**, aunque `E < 2`; un `E` bajo lleva a
   excluir por la propia fórmula. El tipo `convencion` queda reservado a la
   elección entre formas alternativas cuando ninguna alcanza `E ≥ 2`. Las
   cuatro fichas afectadas siguen siendo puntuadas y no cambian:

   | Ficha | E | Puntaje | Resultado |
   |-------|---|---------|-----------|
   | FON-002 (vocal o) | 0 | 0 | excluir |
   | FON-007 (posible fonema /ř/) | 1 | −1 | excluir |
   | FON-008 (tonos) | 1 | −1 | excluir |
   | FON-009 (vocales largas) | 1 | 0 | excluir |

   La aclaración de los dos tipos está en `CLAUDE.md`,
   `decisiones/PLANTILLA.md` y `README.md`.

2. **`E` se registra por ficha, no por opción. RESUELTA (sesión 2).** Con los
   dos tipos actuales basta un único valor de `E` por ficha: `puntuada`
   puntúa un rasgo, no opciones, y `convencion` no puntúa. El desglose por
   opción se aplaza al tipo `seleccion`, anotado en «Diseño futuro».

3. **El texto de `verificacion` menciona puntajes en fichas sin puntaje.
   RESUELTA (sesión 2).** Las cuatro fichas de convención (FON-010, ORT-001,
   TEC-001 y TEC-002) llevan ahora
   `verificacion = "PENDIENTE: comprobar la convención en las fuentes"`.

4. **ORT-001 sigue abierta y el repositorio ya escribe la letra descartada.
   RESUELTA (sesión 2).** ORT-001 decide usar `ŋ`, como el ePSD2. La letra
   descartada se reemplazó por `ŋ` en todo el repositorio —documentación,
   ficha FON-004 y nombre del proyecto—, excepto en ORT-001, donde sigue
   apareciendo al describir la opción descartada. Una prueba de
   `tests/test_decisions.py` falla si la letra descartada reaparece en
   cualquier otro archivo. ORT-001 sigue en estado `propuesta`.

5. **Referencias del proyecto sin datos bibliográficos completos.** Sigue
   abierta en la parte de Foxvog: de Foxvog, *Introduction to Sumerian
   Grammar*, no se ha registrado año ni edición. FUENTE POR VERIFICAR. Del
   ePSD2 ya se registran versión y fecha de consulta (2.7.2, compilada el
   2024-08-31, consultado el 2026-09-27); de Oracc y del ETCSL siguen sin
   registrarse versión ni fecha de consulta. FUENTE POR VERIFICAR.

## Diseño futuro

Anotado, sin implementar.

1. **Tipo de ficha `seleccion`.** Cuando haya que elegir entre alternativas y
   alguna alcance `E ≥ 2`, se creará un tipo `seleccion` con **puntaje por
   opción**. Todavía no está implementado: ni el formato de ficha, ni
   `decisiones/PLANTILLA.md`, ni `scripts/validate_decisions.py` lo admiten.
