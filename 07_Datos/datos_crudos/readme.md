# Datos crudos y fuente histórica

**Estado:** parcialmente poblada.

La carpeta conserva las fuentes primarias disponibles y, por razones de
trazabilidad histórica, un artefacto de codificación temprana cuya ubicación no
se cambia durante el cierre.

## Principio de conservación

Los archivos que constituyen evidencia primaria se conservan sin modificación.
Las transformaciones posteriores deben producir archivos distintos y quedar
documentadas.

## Contenido actual

| Dato | Ubicación | Naturaleza |
|---|---|---|
| Exportación del cuestionario aplicado (62 respuestas) | `07_Datos/datos_crudos/Sistema Inteligente de Mantenimiento de Palma Africana(1-62).xlsx` | Exportación primaria conservada para trazabilidad |
| Codificación temática de las primeras ocho entrevistas | `07_Datos/datos_crudos/codificacion.csv` | Artefacto analítico histórico, no dato crudo en sentido estricto |

### Aclaración sobre `codificacion.csv`

`codificacion.csv` fue ubicado históricamente en `datos_crudos/`, pero su
contenido corresponde a una codificación cualitativa derivada.

Durante el cierre no se mueve ni se reescribe, para no alterar innecesariamente
su trazabilidad histórica. El análisis actualizado lo consume como fuente
heredada y combina sus resultados con:

`../datos_procesados/codificacion_tercera_ronda.csv`

El archivo histórico conserva:

- identificadores `EV-01` a `EV-08`;
- 124 fragmentos (138 hasta el 21/09/2026; ver tarea C2);
- 67 códigos únicos (68 hasta esa fecha);
- analista `VER`.

El mapeo hacia `ENTR-01` a `ENTR-08` ocurre únicamente dentro del script de
análisis y de la tabla de resultados.

## Datos pendientes del experimento humano–LLM

Los datos crudos específicos del experimento comparativo todavía dependen de la
ejecución del protocolo.

No se depositan datos sintéticos o simulados para aparentar esa ejecución.
