# A2 — Identificabilidad del origen antes y después de normalizar

## Método

Se aplicó un clasificador simple con dos señales visibles:

1. primera palabra del criterio de verificación;
2. longitud total de los siete campos visibles.

La evaluación usa **leave-one-out cross-validation (LOOCV)** sobre 47 requisitos:
22 del conjunto humano confirmado después de A3 y 25 del conjunto LLM.

La primera palabra se modela de forma categórica con suavizado de Laplace.
La longitud se modela con una distribución gaussiana por clase.
Se usan probabilidades previas iguales (0,5 / 0,5) para evitar que la
diferencia 22/25 favorezca automáticamente al conjunto mayoritario.

No se usan IDs ni campos explícitos de procedencia como variables.

## Antes de la normalización

- Casos: 47
- Correctos: 43/47
- Acierto LOOCV: **91.49 %**
- Longitud media humana: 707.4 caracteres
- Longitud media LLM: 539.3 caracteres
- Rango humano: 558–875
- Rango LLM: 421–649
- Primeras palabras humanas: `con`=4, `configurado`=2, `el`=2, `emitido`=1, `guardada`=1, `para`=2, `programada`=1, `registrada`=2, `registrado`=2, `si`=1, `un`=2, `una`=2
- Primeras palabras LLM: `cada`=4, `el`=14, `la`=1, `ningún`=1, `se`=1, `todo`=4

Matriz real → predicho:

| Real | Humano | LLM |
|---|---:|---:|
| Humano | 19 | 3 |
| LLM | 1 | 24 |

## Después de la normalización

- Casos: 47
- Correctos: 27/47
- Acierto LOOCV: **57.45 %**
- Longitud media humana: 558.5 caracteres
- Longitud media LLM: 540.2 caracteres
- Rango humano: 420–703
- Rango LLM: 428–656
- Primeras palabras humanas: `verificación`=22
- Primeras palabras LLM: `verificación`=25

Matriz real → predicho:

| Real | Humano | LLM |
|---|---:|---:|
| Humano | 8 | 14 |
| LLM | 6 | 19 |

## Criterio A2

Criterio definido en el registro de correcciones:
el clasificador no debe superar **65 %** de acierto sobre el origen.

Resultado reproducido: **57.45 %**.

**Estado técnico del criterio: CUMPLE.**

## Nota sobre la cifra histórica 619 / 464

El registro previo documentaba medias históricas de 619 caracteres para el
conjunto humano y 464 para el LLM, pero la fórmula exacta usada para obtener
esas dos cifras no quedó versionada. Por ello, este análisis no presenta esa
fórmula como reconstruida. La medición actual fija explícitamente los siete
campos visibles y deja el procedimiento completo en este script.

## Alcance

La normalización busca reducir señales de estilo que revelaban el origen.
No demuestra que ambos conjuntos sean indistinguibles bajo cualquier
clasificador ni sustituye la evaluación humana cegada de A1.
