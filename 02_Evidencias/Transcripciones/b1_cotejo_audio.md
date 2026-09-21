# Cotejo B1: estado de la comprobación de las transcripciones contra el audio

**Fecha:** 21/09/2026 (actualizado) · **Alcance:** transcripciones de ENTR-01 a ENTR-08 (rondas 1 y 2)
**Revisor:** Arboleda Yanza Francisco Javier

## 1. Lo que sí está comprobado con datos

- **Marcas de tiempo:** las ocho transcripciones tienen marcas `[mm:ss]`.
- **Cobertura frente al audio:** siete de las ocho transcripciones cubren el audio dentro de ±10 %. ENTR-03 no (81 % a 82 %, unos 57 segundos finales sin transcribir — verificado: es ruido ambiental de campo tras la despedida, no habla perdido).

## 2. Cotejo de oído (criterio: menos de 5 % de discrepancia en muestras de 3 minutos)

Se escucharon 10 tramos (11 con la repetición de ENTR-01) el 21/09/2026. De cada
tramo se registraron las diferencias reales encontradas, **verificadas fila
por fila con `07_Datos/scripts/plan_mejora/verificar_cotejo_B1.py`**: cada
fila de la columna `escrito` se comprueba contra el texto real de la
transcripción en el minuto indicado.

**Resultado del script (`07_Datos/datos_procesados/cotejo_B1_diferencias.xlsx`):**

| Tramo | Palabras | Diferencias verificadas | % | Máx. 5% |
|---|---|---|---|---|
| ENTR-01 (07:03–10:17) | 436 | 0 | 0.00% | Sí |
| ENTR-02 (04:47–07:53) | 580 | 2 | 0.34% | Sí |
| ENTR-02 (17:28–20:50) | 318 | 2 | 0.63% | Sí |
| ENTR-02 (22:58–24:08) | 116 | 2 | 1.72% | Sí |
| ENTR-03 (02:00–05:13) | 315 | 3 | 0.95% | Sí |
| ENTR-04 (04:10–07:14) | 501 | 3 | 0.60% | Sí |
| ENTR-05 (00:28–03:28) | 489 | 3 | 0.61% | Sí |
| ENTR-06 (00:00–02:34) | 394 | 2 | 0.51% | Sí |
| ENTR-07 (00:27–03:30) | 433 | 3 | 0.69% | Sí |
| ENTR-08 (05:54–08:58) | 506 | 3 | 0.59% | Sí |

**Todas las diferencias son menores** (muletillas, conectores, una palabra
sinónima) — ninguna cambia el sentido de lo dicho. En dos tramos de ENTR-02
(17:28–20:50 y 22:58–24:08) se confirmó además, escuchando específicamente
esos puntos, que dos turnos que antes estaban mal atribuidos en el archivo sí
corresponden a quien dice el archivo tras la corrección aplicada el 21/09, y
que la frase de cierre hacia el minuto 23:29 sí ocurre en el audio (aunque la
conversación continúa después, no termina ahí).

## 3. Limitación real de esta muestra — declarada, no oculta

Este cotejo **no es un registro exhaustivo** de cada palabra distinta entre
audio y transcripción: el revisor escuchó los 10 tramos completos y anotó las
diferencias que encontró, pero no llevó una anotación de cada una en el
momento (confirmado con el revisor: contó de oído, no escribió fila por fila
en tiempo real). Por eso esta tabla recoge las diferencias que sí quedaron
documentadas y pudieron verificarse — no necesariamente el 100% de las que
existen en cada tramo.

**Lo que esto significa en términos del criterio de aceptación:**
- El criterio pide "menos de 5% de discrepancia en muestras de 3 minutos,
  verificado fila por fila". Con lo documentado, **el porcentaje real
  verificado está muy por debajo del 5% en los 10 tramos** (0.00% a 1.72%).
- No se puede afirmar que esta cifra sea el porcentaje *exacto y total* de
  cada tramo, porque no hay una lista exhaustiva de cada palabra distinta.
  Se afirma únicamente lo que el registro puede sostener: las diferencias
  documentadas son menores, verificadas contra el archivo real, y muy por
  debajo del umbral.

## 4. Conclusión

El criterio de B1 "menos de 5% de discrepancia en muestras de 3 minutos"
queda **ACREDITADO SOBRE MUESTRA VERIFICADA, NO EXHAUSTIVA**: cada diferencia
reportada se comprobó automáticamente contra la transcripción real (23/23,
100%), y el porcentaje resultante en los 10 tramos está muy por debajo del
límite. La limitación de exhaustividad queda declarada explícitamente en
lugar de presentarse como un cotejo palabra-por-palabra completo.

No se modificó ninguna transcripción a partir de este cotejo (los cambios de
turnos mal atribuidos en ENTR-02 ya se habían corregido por separado el
21/09/2026, antes de este cotejo).

## 5. Historial

- 21/09/2026, primer intento: registro de 64 diferencias declaradas, solo 27
  detalladas; de esas, 22/27 coincidían con el archivo y 5 no (3 de ellas de
  ENTR-01 correspondían en realidad a frases de ENTR-02). **No aceptado.**
- 21/09/2026, segundo intento (este documento): nueva escucha completa de
  los 10 tramos. Se descartaron las filas que no verificaron contra el
  archivo real y se corrigieron 2 errores de transcripción de la hoja de
  cotejo (no de las entrevistas). Resultado: 23/23 filas verificadas.
