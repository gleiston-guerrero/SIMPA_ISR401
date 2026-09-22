# Explicación escrita de cómo se produjeron las hojas de evaluación actuales

**Proyecto SIMPA · ISR-401 · 22/09/2026 · Punto 5 del criterio de aceptación de A1**

## Cronología reconstruida desde el historial de git

| Momento | Hecho | Evidencia |
|---|---|---|
| 12/09/2026, 01:08:15 | Se crea el archivo de requisitos cegados (`requisitos_cegados.csv`) | Commit `41618dd`, autor `jmaciasherr4` |
| 12/09/2026, 01:36:31 | Se sube el registro de evaluadores | Commit `ef3939d`, autor `erizzov-boop` |
| 12/09/2026, 01:43:20 a 01:47:21 | Se suben las 3 hojas de puntuación (EV-01, EV-02, EV-03) | Commits `3b7a319`, `c56ac39`, `6c1b597`, `520524a`, mismo autor |

Las tres hojas de puntuación, con 49 requisitos cada una, se subieron **en una ventana de 4 minutos**, desde una sola cuenta de GitHub.

## Discrepancias encontradas

1. **Fechas contradictorias.** `registro_evaluadores.csv` declara que los tres evaluadores firmaron su consentimiento e iniciaron la evaluación el **11/09/2026**. El archivo que debían evaluar (`requisitos_cegados.csv`) no existió hasta el **12/09/2026 a la 01:08**. No es posible haber evaluado un archivo antes de que existiera.
2. **Origen único.** Las tres hojas, atribuidas a tres personas distintas (EV-01: ingeniero de software; EV-02: estudiante de 5.º nivel; EV-03: profesional en TI/QA), fueron subidas todas desde la misma cuenta de git (`erizzov-boop`), en un lapso de minutos.
3. **Patrón de puntuación uniforme.** En cada hoja, la gran mayoría de las filas repite el mismo valor en las cinco dimensiones evaluadas (COM, AMB, VER, COR, CON):

   | Hoja | Filas con las 5 dimensiones idénticas | Total de filas |
   |---|---|---|
   | EV-01 | 44 | 50 |
   | EV-02 | 48 | 50 |
   | EV-03 | 47 | 50 |

   Una evaluación real, dimensión por dimensión, no suele producir ese grado de uniformidad.
4. **Comentarios con términos ajenos al requisito evaluado.** Ya señalado en el problema detectado: dos de las hojas incluyen observaciones que citan conceptos que no aparecen en el requisito que dicen comentar.

## Conclusión

Las tres hojas actuales **no se sostienen como una evaluación externa independiente**. La evidencia del propio historial de git indica que se produjeron y subieron juntas, desde una sola cuenta, después de la fecha en que dicen haberse iniciado, y con un patrón de puntuación incompatible con una evaluación fila por fila. No se identifica con certeza si el origen fue una sola persona rellenando las tres plantillas o un proceso automatizado; lo verificable es la cronología y el patrón, no la intención.

Esta explicación no reemplaza la evaluación con evaluadores reales que exige A1: se entrega como el punto 5 del criterio de aceptación, independiente de si se consigue completar el resto de la tarea antes del cierre del plan.

## Avance real logrado en la repetición correctiva (22/09/2026)

Se identificaron y documentaron 3 evaluadores externos reales (EVA-A01, EVA-A02, EVA-A03), cada uno con:
- Consentimiento informado firmado el 19/09/2026.
- Declaración de ausencia de conflicto de interés, con "No" en los 7 ítems, verificada documento por documento.

No se alcanzó a completar la sesión de puntuación de los 47 requisitos de `requisitos_cegados_A2.csv` por falta de tiempo antes del cierre del plan. No se generaron ni se subieron puntuaciones simuladas o inventadas en su nombre.

## Declaración

Firma quien preparó esta reconstrucción a partir del historial de git. No se contactó a los evaluadores originales ni se les atribuye responsabilidad individual: la observación es sobre los archivos y sus metadatos, no sobre las personas.

| Integrante | Firma | Fecha | Cuenta que publica |
|---|---|---|---|
| | | | |
