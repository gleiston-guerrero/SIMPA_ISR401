# Codificación temática — tercera ronda

**Estado:** codificación realizada, validada localmente y revisada de forma cruzada.
**Responsable principal:** Villafuerte Rosero Allan Noé
**Identificador del analista en el CSV:** `AVR`
**Revisión cruzada:** Macías Herrera Josthyn Esteban

## Alcance

Este bloque contiene la codificación temática de las ocho entrevistas ejecutadas
en la tercera ronda:

- `ENTR-09` a `ENTR-12`: 31 de agosto de 2026.
- `ENTR-13` a `ENTR-16`: 1 de septiembre de 2026.

> **Nota del 21/09/2026.** Las cifras de este documento describen la codificación del
> 07/09/2026 (31 códigos distintos). El 20/09/2026 la codificación de contraste se normalizó
> al libro de códigos v1.0 (commit `bf0354c`) y hoy tiene **36 códigos únicos** (21 compartidos
> con dominio y 15 nuevos frente a dominio). Los 89 fragmentos no cambiaron.

Se codificaron **89 fragmentos**, correspondientes a **31 códigos temáticos
distintos**.

De esos códigos:

- **20** reutilizan códigos ya presentes en la codificación histórica;
- **11** aparecen por primera vez frente al estrato de dominio.

La revisión cruzada fue realizada antes de integrar este bloque al análisis de
saturación estratificado.

## Fuente

La codificación se deriva únicamente de las transcripciones anonimizadas
versionadas en:

`02_Evidencias/Transcripciones/`

No se incorporaron fragmentos ni requisitos sin respaldo en esas
transcripciones o en el ERS vigente.

## Convención de identificadores

La adenda A.14 identifica a los participantes de la tercera ronda como
`ENTR-09` a `ENTR-16`. Esos identificadores se conservan aquí.

No se usan `EV-09` a `EV-16` para estas entrevistas porque el catálogo de
evidencias del ERS ya utiliza identificadores `EV-09`, `EV-10`, `EV-11`,
`EV-12` y `EV-13` para otros artefactos. Reutilizarlos produciría una colisión
de trazabilidad.

La codificación histórica de las ocho primeras entrevistas se conserva sin
cambios en:

`../datos_crudos/codificacion.csv`

El análisis de saturación integra ambos bloques manteniendo separados el estrato
de dominio y el estrato de contraste conforme a la medida metodológica
documentada en A.14.

## Códigos nuevos de la tercera ronda

- `CAPACITACION_USO`
- `CONFIANZA_DIAGNOSTICO`
- `CONTROL_INSUMOS`
- `GPS_EVIDENCIA_LABOR`
- `INTERFAZ_SIMPLE`
- `INTERFAZ_VISUAL`
- `OPERACION_OFFLINE`
- `PLANIFICACION_LABORES`
- `RESISTENCIA_CAMBIO`
- `TUTORIAL_GUIADO`
- `VERIFICACION_DIAGNOSTICO`

Los demás códigos reutilizan el vocabulario temático ya existente para evitar
inflar artificialmente la saturación.

## Criterio de codificación

Cada fila contiene un fragmento analítico resumido, un código temático, su
categoría, el requisito derivado cuando existe una correspondencia verificable,
el identificador de la entrevista y el analista codificador.

Cuando una observación no permite vincular responsablemente un requisito
concreto, `Requisito_derivado` se deja vacío en lugar de inventar una asociación.

## Validación realizada

La validación confirmó:

- 89 filas;
- 8 identificadores únicos;
- `ENTR-09` a `ENTR-16` sin faltantes;
- todas las filas con `Analista_codificador = AVR`.

El análisis integrado posterior confirmó:

- 31 códigos distintos en contraste;
- 20 compartidos con dominio;
- 11 nuevos frente al dominio.
