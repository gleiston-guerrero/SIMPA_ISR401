# Evidencia fotográfica del cuestionario

Esta carpeta contiene dos tipos de archivos distintos que deben interpretarse
por separado.

## 1. Fotografías reales de la sesión complementaria

Los siguientes archivos corresponden a una **sesión complementaria real**
realizada el **15 de septiembre de 2026** con trabajadores de Palmicultora M:

- `2026-09-15_ConsentimientoComplementario_Foto-01.jpg`
- `2026-09-15_ConsentimientoComplementario_Foto-02.jpg`
- `2026-09-15_ConsentimientoComplementario_Foto-03.jpg`
- `2026-09-15_ConsentimientoComplementario_Foto-04.jpg`
- `2026-09-15_ConsentimientoComplementario_Foto-05.jpg`

Estas cinco fotografías conservan metadatos EXIF verificables.

La comprobación técnica de `DateTimeOriginal` y modelo de dispositivo se
encuentra en:

`../../../10_Autoria/verificacion_exif_aplicacion.md`

## 2. Capturas del instrumento

Los archivos:

`cuestionario_p01_*.png` a `cuestionario_p15_*.png`

son **capturas del instrumento utilizado en el cuestionario**.

Estas imágenes documentan preguntas y elementos de la interfaz del formulario.
No son fotografías de trabajadores durante una aplicación presencial y no deben
utilizarse como evidencia fotográfica de trabajo de campo.

## Relación con las 62 respuestas originales

El cuestionario original fue distribuido mediante Google Forms.

Allan Villafuerte compartió el enlace con el administrador de Palmicultora M,
quien posteriormente lo distribuyó entre trabajadores operativos. De esa
aplicación se obtuvieron **62 respuestas**.

La documentación y tratamiento de esas respuestas se encuentran en:

`../Respuestas/readme.md`

La aplicación original no generó fotografías presenciales verificables de cada
participante ni un registro independiente de consentimiento informado
individual.

## Sesión complementaria del 15 de septiembre

Como acción correctiva de cierre, el 15 de septiembre de 2026 se realizó una
sesión complementaria con **cinco trabajadores localizables**.

La evidencia asociada incluye:

- las cinco fotografías JPG conservadas en esta carpeta;
- el formulario de consentimiento informado complementario;
- las respuestas de consentimiento mantenidas en la zona restringida;
- la verificación EXIF de las cinco fotografías.

La documentación del consentimiento se encuentra en:

`../Consentimiento_Complementario/readme.md`

## Regla de no vinculación

La sesión complementaria **no reemplaza ni reconstruye** la aplicación original
de las 62 respuestas.

Los cinco participantes de la sesión complementaria no se vinculan con ninguna
respuesta específica del conjunto original.

No existe una clave que permita determinar cuál de las 62 respuestas
correspondería a una persona concreta de la sesión complementaria.

Por esta razón, las fotografías JPG se presentan exclusivamente como evidencia
de la actividad correctiva realizada el 15 de septiembre de 2026.

## Criterio de integridad

No se modifican fechas EXIF, no se reconstruyen fotografías inexistentes y no
se presentan las capturas PNG del instrumento como si fueran fotografías de una
aplicación presencial.

La separación entre capturas del instrumento, respuestas originales y sesión
complementaria se mantiene explícita para preservar la trazabilidad y evitar
interpretaciones retrospectivas incorrectas.

## Aclaración de commits y nombres (H2)

Los commits `34ce578` y `0792213` (12/09/2026) llevan mensajes que hablan de "fotografías reales de aplicación del cuestionario", pero contienen únicamente las 15 capturas del instrumento (`cuestionario_p01_*.png` a `cuestionario_p15_*.png`). No incluyen ninguna fotografía de trabajadores. Por la regla de no reescribir el historial, esos mensajes no se modifican y esta nota los corrige.

Las cinco fotografías reales (`2026-09-15_ConsentimientoComplementario_Foto-01.jpg` a `Foto-05.jpg`) son de la sesión complementaria de consentimiento del 15/09/2026, no de la aplicación original del cuestionario. El nombre de la carpeta `Fotos_Aplicacion` se conserva para no romper enlaces; su contenido es el descrito en este readme.

La `Foto-01` fue editada el 19/09/2026 (commit `e837e32`) para cubrir un rasgo identificable de una persona. Su contenido y su SHA-256 ya no coinciden con los registrados en `checksums.sha256` y en `10_Autoria/exif_inventario.csv`, que corresponden a la versión original. Conserva la fecha y el modelo EXIF (2026-09-15 10:08:42, BRP-NX3), pero no todos los campos EXIF originales.
