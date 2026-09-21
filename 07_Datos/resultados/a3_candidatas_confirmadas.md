# A3 — Candidatas de cita literal para el conjunto humano ENTR-04

Transcripción verificada contra el hash congelado en `06_Experimento/material_fuente/ENTR-04_fuente_congelada.md`: `5e9cf9dca6af94061ae937c47a6644dde924061c8382325515e258c377c63313`.

Cada bloque muestra hasta 3 frases del ENTREVISTADO más parecidas al requisito. Marcar con [X] la correcta, o escribir NO_LOCALIZADA si ninguna corresponde. Las filas con procedencia «Histórico del ERS» no requieren cita de ENTR-04 (trazan a EV-04 en el ERS, verificado en `07_Datos/datos_procesados/tabla_procedencia_requisitos.csv`); se incluyen igual por si el equipo decide reforzarlas con cita directa.

> **Estado de verificación — 20/09/2026.** Las decisiones de este archivo se tomaron sobre el texto de las candidatas reproducido aquí; **no** se contrastaron contra `06_Experimento/material_fuente/ENTR-04_fuente_congelada.md` ni contra su hash, porque la fuente congelada no estuvo disponible al completarlo. Los números de línea se reproducen tal como los declara este documento. Antes de cerrar A3, confirmar cada cita marcada contra la fuente congelada.
>
> **Resultado:** 22 de 25 filas con cita confirmada y 3 con NO_LOCALIZADA (H-001, H-004, H-006), las tres con procedencia «Histórico del ERS», por lo que no afectan la cobertura exigida. Las 16 filas de origen EXP-01…EXP-16 quedan todas con cita. Dos puntos requieren atención del equipo: H-010 (posible cita mejor en línea 15, listada por error en otro bloque) y H-024 (la redistribución del excedente entre plantas carece de respaldo en ENTR-04).

---

## H-001 — Diagnóstico de deficiencias nutricionales por análisis de imagen
- **Origen:** `RF-08`  ·  **Procedencia declarada:** Histórico del ERS
- **Descripción:** El sistema debe analizar la fotografía de una hoja y estimar la deficiencia nutricional presente, sugiriendo la corrección correspondiente.
- **Criterio de verificación:** Ante una hoja con deficiencia previamente conocida, el sistema indica la deficiencia, propone una corrección y almacena el registro.

**Candidatas:**

- [ ] línea 91 (similitud 0.04): "Adicional a eso, de lo que podemos observar, sería intentar ver los análisis de suelo, para definir o concluir bien por qué tenemos el problema del amarillamiento de las hojas bajeras, que normalmente puede deberse a alguna deficiencia de magnesio, aunque, según dicen que están aplicando, podría haber algún bloqueo en el suelo."
- [ ] línea 15 (similitud 0.03): "Ahí lo atiende el señor basculero, donde le indica su peso bruto, y en este caso le pregunta sus datos:"
- [ ] línea 15 (similitud 0.03): "En este caso, si tenemos una fruta rechazada, se devuelve en el mismo carro; el carro vuelve a la báscula, se le da su peso de salida y también se le da su tiquete correspondiente."

**Decisión:** NO_LOCALIZADA. Ninguna candidata enuncia el análisis de la fotografía de una hoja ni la estimación de la deficiencia. La línea 91 (análisis de suelo y amarillamiento por posible deficiencia de magnesio) aporta contexto del problema, no el requisito. Procedencia Histórico del ERS (traza a EV-04): no requiere cita de ENTR-04.

---

## H-002 — Gestión de variedades de palma
- **Origen:** `RF-10`  ·  **Procedencia declarada:** Histórico del ERS
- **Descripción:** El sistema debe registrar la variedad sembrada por lote y emplearla para parametrizar los umbrales de diagnóstico y de madurez, así como las advertencias sobre polinizadores naturales.
- **Criterio de verificación:** Para un lote guineensis, el umbral de madurez aplicado es de 3 frutos desprendidos; para un lote híbrido, de 5.

**Candidatas:**

- [X] línea 19 (similitud 0.11): "para recibir un fruto maduro debe tener, en racimos guineensis, 3 frutos desprendidos, y en el caso de híbridos, 5 frutos desprendidos."
- [ ] línea 47 (similitud 0.07): "Lo que sí tenemos que definir es que, entre los 2 materiales, el guineensis y el híbrido, el híbrido nos aguanta un poquito más de tiempo en campo."
- [ ] línea 63 (similitud 0.05): "En sí, las 2 variedades son buenas."

**Decisión:** línea 19 — "para recibir un fruto maduro debe tener, en racimos guineensis, 3 frutos desprendidos, y en el caso de híbridos, 5 frutos desprendidos." Sustenta la parametrización del umbral de madurez por variedad (criterio de verificación 3/5). Refuerzo opcional: la procedencia es Histórico del ERS. Nota: la misma frase es la cita principal de H-013 (EXP-04).

---

## H-003 — Clasificación de madurez del racimo por desprendimiento
- **Origen:** `RF-21`  ·  **Procedencia declarada:** Histórico del ERS
- **Descripción:** El sistema debe estimar el estado de madurez de un racimo a partir de una fotografía de su parte basal, empleando el conteo de frutos desprendidos como criterio y aplicando el umbral correspondiente a la variedad del lote. El sistema no debe emplear el color del fruto como criterio de clasificación.
- **Criterio de verificación:** Para híbrido, menos de 5 frutos desprendidos se clasifica como verde y 5 o más como maduro; para guineensis el umbral aplicado es 3.

**Candidatas:**

- [X] línea 19 (similitud 0.14): "para recibir un fruto maduro debe tener, en racimos guineensis, 3 frutos desprendidos, y en el caso de híbridos, 5 frutos desprendidos."
- [ ] línea 19 (similitud 0.09): "Normalmente siempre vemos el desprendimiento de frutos para recibirlo, para determinar que está maduro."
- [ ] línea 27 (similitud 0.05): "El principal problema que tenemos actualmente es el tema de fruta verde, que la fruta no llega con desprendimiento."

**Decisión:** línea 19 (umbrales 3/5) como cita principal: es la única candidata que sustenta el criterio de verificación. Complementaria: línea 19 — "Normalmente siempre vemos el desprendimiento de frutos para recibirlo, para determinar que está maduro", que respalda la exclusión del color como criterio de clasificación. Refuerzo opcional (Histórico del ERS).

---

## H-004 — Estimación y alerta preventiva de porcentaje de fruta verde
- **Origen:** `RF-22`  ·  **Procedencia declarada:** Histórico del ERS
- **Descripción:** El sistema debe estimar, antes del despacho de un lote cosechado, el porcentaje de racimos clasificados como verdes, y emitir una alerta cuando dicho porcentaje se aproxime al umbral a partir del cual la planta extractora aplica penalización.
- **Criterio de verificación:** Configurado un umbral de penalización, un lote cuya estimación de fruta verde alcance o supere ese valor genera una alerta previa al despacho.

**Candidatas:**

- [ ] línea 87 (similitud 0.05): "También se incluye lo que es fruta verde, fruta sobremadura, malformada y pedúnculos largos."
- [ ] línea 27 (similitud 0.05): "El principal problema que tenemos actualmente es el tema de fruta verde, que la fruta no llega con desprendimiento."
- [ ] línea 39 (similitud 0.05): "Cortan fruta verde, porque a ellos les pagan por eso, para obtener su peso y tener su ingreso."

**Decisión:** NO_LOCALIZADA. Ninguna candidata menciona estimación porcentual de fruta verde, umbral de penalización ni alerta previa al despacho. La línea 27 sirve como motivación del requisito, no como cita literal. Procedencia Histórico del ERS (traza a EV-04): no requiere cita de ENTR-04.

---

## H-005 — Registro de la calificación de calidad emitida por la extractora
- **Origen:** `RF-23`  ·  **Procedencia declarada:** Histórico del ERS
- **Descripción:** El sistema debe permitir registrar los datos del ticket de pesaje emitido por la planta extractora: peso bruto, tara, peso neto y calificación de calidad (tamaño del fruto, fruta verde, sobremadura, malformada y pedúnculo largo).
- **Criterio de verificación:** Registrado un ticket, sus valores quedan asociados al lote de origen y son consultables en el histórico de entregas.

**Candidatas:**

- [X] línea 71 (similitud 0.18): "Cuando termina todo el proceso de pesaje, se emite un ticket de pesaje donde viene el peso bruto, el peso tara y el peso neto, que viene a ser el peso de la fruta."
- [ ] línea 87 (similitud 0.11): "También se incluye lo que es fruta verde, fruta sobremadura, malformada y pedúnculos largos."
- [ ] línea 15 (similitud 0.07): "Ahí lo atiende el señor basculero, donde le indica su peso bruto, y en este caso le pregunta sus datos:"

**Decisión:** línea 71 (peso bruto, tara y neto del ticket) como cita principal. Complementaria: línea 87 — "También se incluye lo que es fruta verde, fruta sobremadura, malformada y pedúnculos largos", necesaria para cubrir la parte de calificación de calidad. Refuerzo opcional (Histórico del ERS). Nota: la frase de línea 71 es también la cita principal de H-012 (EXP-03).

---

## H-006 — Trazabilidad de la calificación hasta la cuadrilla responsable
- **Origen:** `RF-24`  ·  **Procedencia declarada:** Histórico del ERS
- **Descripción:** El sistema debe permitir rastrear una calificación desfavorable de la extractora hasta el lote de origen, la fecha de corte y la cuadrilla de cosecha responsable, con el fin de distinguir si el problema proviene de la cosecha o del manejo del cultivo.
- **Criterio de verificación:** Dado un despacho con penalización por fruta verde, el sistema identifica el lote, la fecha de corte y la cuadrilla que ejecutó la cosecha.

**Candidatas:**

- [ ] línea 27 (similitud 0.09): "El principal problema que tenemos actualmente es el tema de fruta verde, que la fruta no llega con desprendimiento."
- [ ] línea 91 (similitud 0.07): "Durante esos 2 o 3 meses vamos a tener problemas hasta que el trabajador se adapte; entonces vamos a tener un problema de formación que esperamos que en unos 2 meses se pueda solventar y tengamos mejor fruta."
- [ ] línea 87 (similitud 0.06): "En la calificación se incluye fruta grande, mediana o pequeña; esas son las 3 calificaciones."

**Decisión:** NO_LOCALIZADA. Ninguna candidata vincula la calificación desfavorable con el lote de origen, la fecha de corte ni la cuadrilla responsable; la línea 91 habla de formación del trabajador, no de trazabilidad. Procedencia Histórico del ERS (traza a EV-04): no requiere cita de ENTR-04. Si el equipo quiere respaldo directo, debe elicitarse en una entrevista posterior.

---

## H-007 — Control de la ventana entre corte y entrega
- **Origen:** `RF-25`  ·  **Procedencia declarada:** Histórico del ERS
- **Descripción:** El sistema debe registrar la fecha y hora de corte de cada lote cosechado y calcular el tiempo transcurrido hasta la entrega en la planta extractora, emitiendo una advertencia cuando dicho intervalo supere el valor recomendado para la variedad.
- **Criterio de verificación:** Configurado un umbral de 24 horas, un despacho entregado 30 horas después del corte genera la advertencia correspondiente.

**Candidatas:**

- [X] línea 55 (similitud 0.05): "Entonces, nosotros normalmente recomendamos que sea dentro de las 24 horas, aunque siempre pasan hasta 48 o un poquito más."
- [ ] línea 71 (similitud 0.05): "En ese mismo ticket viene el nombre del productor, viene la finca, viene el transportista, las placas del vehículo y la fecha y hora de ingreso."
- [ ] línea 7 (similitud 0.03): "Bien, yo trabajo ya 3 años en la extractora agrícola."

**Decisión:** línea 55 — "Entonces, nosotros normalmente recomendamos que sea dentro de las 24 horas, aunque siempre pasan hasta 48 o un poquito más." Sustenta el umbral de 24 h del criterio de verificación pese a la similitud baja (0.05): acierto semántico que el ranking no priorizó.

---

## H-008 — Compartición de la estimación de cosecha con la planta extractora
- **Origen:** `RF-32`  ·  **Procedencia declarada:** Histórico del ERS
- **Descripción:** El sistema debe permitir exportar la estimación de cosecha del período hacia la planta extractora, limitando la información compartida al conteo de racimos y al peso promedio estimado, con exclusión de cualquier dato personal o económico.
- **Criterio de verificación:** El archivo exportado contiene conteo de racimos y peso promedio por período y no incluye campos de identificación personal ni información económica.

**Candidatas:**

- [X] línea 99 (similitud 0.08): "Nosotros, sí, como empresa, igual estamos comprometidos con un proyecto de mejoramiento de la producción de los palmicultores, y para este caso necesitaríamos que se pueda llevar, quizás, cuando suban el conteo de racimos, quizás el peso promedio que tengan, para nosotros también llevar el registro, un histórico de cómo puede ir mejorando o no la producción de toda la finca."
- [ ] línea 99 (similitud 0.06): "En este caso, nosotros somos muy conscientes de que hay información sensible que no puede compartirse, que es personal."
- [ ] línea 95 (similitud 0.04): "O sea, nosotros lo veríamos útil porque, así como la finca realiza aquí un tema de estimación o proyección de cuántas toneladas puede cosechar, nosotros en la extractora también hacemos una proyección de cuántas toneladas podemos recibir y procesar, porque tenemos un límite de capacidad."

**Decisión:** línea 99 — "...necesitaríamos que se pueda llevar, quizás, cuando suban el conteo de racimos, quizás el peso promedio que tengan..." Sustenta el alcance de lo compartido. Complementaria: línea 99 — "En este caso, nosotros somos muy conscientes de que hay información sensible que no puede compartirse, que es personal", que respalda la exclusión de datos personales. Refuerzo opcional (Histórico del ERS). Nota: la primera frase es la cita principal de H-025 (EXP-16).

---

## H-009 — Registro de la guía de remisión del despacho
- **Origen:** `RF-33`  ·  **Procedencia declarada:** Histórico del ERS
- **Descripción:** El sistema debe permitir registrar el número y la fecha de la guía de remisión asociada a cada despacho de fruta, y advertir cuando un despacho se registre sin ella.
- **Criterio de verificación:** Un despacho registrado sin número de guía de remisión genera una advertencia visible para la administración antes de su cierre.

**Candidatas:**

- [X] línea 79 (similitud 0.07): "Actualmente, muchos de los palmicultores no manejan esta guía de remisión, aunque es exigida por la ley."
- [ ] línea 79 (similitud 0.06): "Estamos socializando un poco este tema porque ya ha pasado que algunos carros los han parado, porque todo carro que transporta, sea lo que sea, debe tener su guía de remisión."
- [ ] línea 83 (similitud 0.06): "Exacto, para que llegue la fruta sin problema, porque muchas veces, si hay un operativo en la vía donde esté Agrocalidad con la policía, puede causarles algún problema por no llevar la guía."

**Decisión:** línea 79 — "Actualmente, muchos de los palmicultores no manejan esta guía de remisión, aunque es exigida por la ley." Complementaria: línea 83 (riesgo en operativos de Agrocalidad y policía), que justifica la advertencia antes del cierre del despacho. Refuerzo opcional (Histórico del ERS).

---

## H-010 — Registro de recepción de fruta en el centro de acopio
- **Origen:** `EXP-01`  ·  **Procedencia declarada:** Elicitado durante la fase de experimentación para el mínimo de 25 RF.
- **Descripción:** El sistema debe registrar cada llegada de vehículo con fruta indicando el centro de acopio, la fecha y hora de ingreso, la finca de procedencia, el productor propietario de la fruta y el conductor del vehículo, y generar un identificador único de recepción.
- **Criterio de verificación:** Registrada una llegada con los cinco datos obligatorios, el sistema devuelve un identificador único y permite recuperar por él el centro de acopio, la finca, el productor, el conductor y la fecha y hora.

**Candidatas:**

- [X] línea 71 (similitud 0.18): "En ese mismo ticket viene el nombre del productor, viene la finca, viene el transportista, las placas del vehículo y la fecha y hora de ingreso."
- [ ] línea 43 (similitud 0.07): "En el día que estemos en la charla, en la capacitación, si ellos cortan fruta verde, ese día se hace la excepción de recibirla; pero al día siguiente, a la semana siguiente, la fruta que no cumpla con los indicadores o con las características que nosotros pedimos simplemente se devuelve al productor."
- [ ] línea 39 (similitud 0.06): "Cortan fruta verde, porque a ellos les pagan por eso, para obtener su peso y tener su ingreso."

**Decisión:** línea 71 — cubre productor, finca, transportista y fecha y hora de ingreso. PENDIENTE DE REVISIÓN: la frase de línea 15 "de dónde procede, de qué finca, quién es el dueño y quién es el chofer" —listada como candidata en H-022, no en este bloque— describe con más precisión el registro de llegada y es probablemente la cita correcta. Verificar ambas en la fuente congelada antes de cerrar. El identificador único de recepción es decisión de diseño, sin respaldo textual en ENTR-04.

---

## H-011 — Captura del peso bruto en la báscula de ingreso
- **Origen:** `EXP-02`  ·  **Procedencia declarada:** Elicitado durante la fase de experimentación para el mínimo de 25 RF.
- **Descripción:** El sistema debe registrar el peso bruto del vehículo cargado obtenido en la báscula de ingreso y asociarlo a la recepción abierta correspondiente.
- **Criterio de verificación:** Registrado un peso bruto sobre una recepción abierta, el valor queda asociado a esa recepción y un segundo registro sobre la misma recepción se conserva como corrección con su valor anterior.

**Candidatas:**

- [ ] línea 15 (similitud 0.09): "En este caso, si tenemos una fruta rechazada, se devuelve en el mismo carro; el carro vuelve a la báscula, se le da su peso de salida y también se le da su tiquete correspondiente."
- [X] línea 15 (similitud 0.06): "Ahí lo atiende el señor basculero, donde le indica su peso bruto, y en este caso le pregunta sus datos:"
- [ ] línea 39 (similitud 0.06): "Cortan fruta verde, porque a ellos les pagan por eso, para obtener su peso y tener su ingreso."

**Decisión:** línea 15 — "Ahí lo atiende el señor basculero, donde le indica su peso bruto, y en este caso le pregunta sus datos:" (segunda candidata, similitud 0.06). La primera candidata describe el peso de SALIDA de una carga rechazada y no corresponde a la captura del peso bruto de ingreso. La conservación del valor anterior ante una corrección es decisión de diseño, sin respaldo textual en ENTR-04.

---

## H-012 — Cálculo del peso neto a partir de la tara de salida
- **Origen:** `EXP-03`  ·  **Procedencia declarada:** Elicitado durante la fase de experimentación para el mínimo de 25 RF.
- **Descripción:** El sistema debe registrar el peso de salida del vehículo en la báscula como tara y calcular el peso neto de fruta como la diferencia entre el peso bruto y la tara.
- **Criterio de verificación:** Con un peso bruto de 20 000 kg y un peso de salida de 7 500 kg, el sistema calcula y conserva un peso neto de 12 500 kg en la recepción.

**Candidatas:**

- [X] línea 71 (similitud 0.21): "Cuando termina todo el proceso de pesaje, se emite un ticket de pesaje donde viene el peso bruto, el peso tara y el peso neto, que viene a ser el peso de la fruta."
- [ ] línea 15 (similitud 0.15): "En este caso, si tenemos una fruta rechazada, se devuelve en el mismo carro; el carro vuelve a la báscula, se le da su peso de salida y también se le da su tiquete correspondiente."
- [ ] línea 15 (similitud 0.08): "Ahí lo atiende el señor basculero, donde le indica su peso bruto, y en este caso le pregunta sus datos:"

**Decisión:** línea 71 — "Cuando termina todo el proceso de pesaje, se emite un ticket de pesaje donde viene el peso bruto, el peso tara y el peso neto, que viene a ser el peso de la fruta." Los valores del criterio de verificación (20 000 / 7 500 / 12 500 kg) son ilustrativos y no provienen de la entrevista.

---

## H-013 — Calificación de madurez por frutos desprendidos según la variedad
- **Origen:** `EXP-04`  ·  **Procedencia declarada:** Elicitado durante la fase de experimentación para el mínimo de 25 RF.
- **Descripción:** El sistema debe calificar la madurez de la fruta descargada a partir del número de frutos desprendidos, aplicando un umbral de 3 frutos para racimos guineensis y de 5 frutos para racimos híbridos.
- **Criterio de verificación:** Un racimo guineensis con 3 frutos desprendidos cumple el indicador y con 2 no lo cumple; un racimo híbrido con 5 frutos desprendidos lo cumple y con 4 no lo cumple.

**Candidatas:**

- [X] línea 19 (similitud 0.20): "para recibir un fruto maduro debe tener, en racimos guineensis, 3 frutos desprendidos, y en el caso de híbridos, 5 frutos desprendidos."
- [ ] línea 15 (similitud 0.08): "Ahí, en este caso, tenemos a los muchachos, a los operarios, que son los encargados de descargar la fruta, y ellos realizan una calificación a la fruta de acuerdo a nuestros indicadores de calidad, que tiene que ver con el desprendimiento de frutos para determinar que una fruta esté madura."
- [ ] línea 67 (similitud 0.08): "En sí, todos los híbridos interespecíficos son más resistentes que el material guineensis normal."

**Decisión:** línea 19 — "para recibir un fruto maduro debe tener, en racimos guineensis, 3 frutos desprendidos, y en el caso de híbridos, 5 frutos desprendidos." Cita exacta y completa del requisito, incluidos ambos umbrales.

---

## H-014 — Observación por pedúnculo superior a 5 centímetros
- **Origen:** `EXP-05`  ·  **Procedencia declarada:** Elicitado durante la fase de experimentación para el mínimo de 25 RF.
- **Descripción:** El sistema debe generar una observación de calidad dirigida al productor cuando la longitud del pedúnculo medida en la base del racimo supere los 5 centímetros.
- **Criterio de verificación:** Con una longitud registrada de 5,5 cm el sistema genera la observación; con 5,0 cm o menos no la genera.

**Candidatas:**

- [X] línea 19 (similitud 0.16): "Cuando tenemos un pedúnculo largo, que estamos hablando de encima de 5 centímetros en su base, se le hace una observación, en este caso a los dueños, para que nos ayuden con eso."
- [ ] línea 19 (similitud 0.10): "O en el caso de malformación que supere el 30 por ciento, el racimo no es recibido."
- [ ] línea 23 (similitud 0.05): "El tema del pedúnculo se refiere a que, si lo podemos ver, tiene pequeños poros."

**Decisión:** línea 19 — "Cuando tenemos un pedúnculo largo, que estamos hablando de encima de 5 centímetros en su base, se le hace una observación, en este caso a los dueños, para que nos ayuden con eso." Cita exacta: umbral, punto de medición y destinatario de la observación.

---

## H-015 — Rechazo por malformación superior al 30 por ciento
- **Origen:** `EXP-06`  ·  **Procedencia declarada:** Elicitado durante la fase de experimentación para el mínimo de 25 RF.
- **Descripción:** El sistema debe marcar la fruta como no recibida cuando el porcentaje de malformación evaluado supere el 30 por ciento.
- **Criterio de verificación:** Con un 30,5 % de malformación el sistema marca la fruta como no recibida; con 30 % o menos permite continuar la recepción.

**Candidatas:**

- [X] línea 19 (similitud 0.17): "O en el caso de malformación que supere el 30 por ciento, el racimo no es recibido."
- [ ] línea 91 (similitud 0.12): "En cuanto a la cosecha, esperamos que por lo menos en unos 2 meses mejore un poco más, cuando empiece a salir la fruta polinizada al 100 por ciento."
- [ ] línea 55 (similitud 0.06): "Que evita que la fruta se oxide."

**Decisión:** línea 19 — "O en el caso de malformación que supere el 30 por ciento, el racimo no es recibido." Cita exacta: umbral y consecuencia.

---

## H-016 — Devolución de la carga rechazada y cierre en báscula
- **Origen:** `EXP-07`  ·  **Procedencia declarada:** Elicitado durante la fase de experimentación para el mínimo de 25 RF.
- **Descripción:** El sistema debe registrar la devolución de la fruta rechazada en el mismo vehículo que la transportó, exigiendo el peso de salida en báscula y la emisión del tiquete correspondiente antes de cerrar la recepción.
- **Criterio de verificación:** Una recepción rechazada no puede cerrarse mientras no se registren el peso de salida y la emisión del tiquete de devolución.

**Candidatas:**

- [X] línea 15 (similitud 0.28): "En este caso, si tenemos una fruta rechazada, se devuelve en el mismo carro; el carro vuelve a la báscula, se le da su peso de salida y también se le da su tiquete correspondiente."
- [ ] línea 39 (similitud 0.06): "Cortan fruta verde, porque a ellos les pagan por eso, para obtener su peso y tener su ingreso."
- [ ] línea 71 (similitud 0.06): "En ese mismo ticket viene el nombre del productor, viene la finca, viene el transportista, las placas del vehículo y la fecha y hora de ingreso."

**Decisión:** línea 15 — "En este caso, si tenemos una fruta rechazada, se devuelve en el mismo carro; el carro vuelve a la báscula, se le da su peso de salida y también se le da su tiquete correspondiente." Cita exacta de los tres elementos del requisito (mismo vehículo, peso de salida, tiquete).

---

## H-017 — Calificación del tamaño de la fruta
- **Origen:** `EXP-08`  ·  **Procedencia declarada:** Elicitado durante la fase de experimentación para el mínimo de 25 RF.
- **Descripción:** El sistema debe registrar en la calificación de la entrega una única categoría de tamaño de fruta entre grande, mediana y pequeña.
- **Criterio de verificación:** Guardada la calificación, la entrega conserva exactamente una de las tres categorías y el sistema no admite dos categorías simultáneas.

**Candidatas:**

- [X] línea 87 (similitud 0.25): "En la calificación se incluye fruta grande, mediana o pequeña; esas son las 3 calificaciones."
- [ ] línea 15 (similitud 0.06): "Ahí, en este caso, tenemos a los muchachos, a los operarios, que son los encargados de descargar la fruta, y ellos realizan una calificación a la fruta de acuerdo a nuestros indicadores de calidad, que tiene que ver con el desprendimiento de frutos para determinar que una fruta esté madura."
- [ ] línea 55 (similitud 0.05): "Que evita que la fruta se oxide."

**Decisión:** línea 87 — "En la calificación se incluye fruta grande, mediana o pequeña; esas son las 3 calificaciones." Cita exacta. La exclusividad de la categoría ("no admite dos simultáneas") se deriva de "esas son las 3 calificaciones", pero no la enuncia el entrevistado: es decisión de diseño.

---

## H-018 — Registro de los indicadores de defecto de la entrega
- **Origen:** `EXP-09`  ·  **Procedencia declarada:** Elicitado durante la fase de experimentación para el mínimo de 25 RF.
- **Descripción:** El sistema debe registrar en la calificación de cada entrega los indicadores de fruta verde, fruta sobremadura, fruta malformada y pedúnculos largos.
- **Criterio de verificación:** Una calificación guardada conserva los cuatro indicadores y permite recuperarlos asociados a la recepción y a su fecha.

**Candidatas:**

- [X] línea 87 (similitud 0.26): "También se incluye lo que es fruta verde, fruta sobremadura, malformada y pedúnculos largos."
- [ ] línea 15 (similitud 0.08): "Ahí, en este caso, tenemos a los muchachos, a los operarios, que son los encargados de descargar la fruta, y ellos realizan una calificación a la fruta de acuerdo a nuestros indicadores de calidad, que tiene que ver con el desprendimiento de frutos para determinar que una fruta esté madura."
- [ ] línea 43 (similitud 0.08): "En el día que estemos en la charla, en la capacitación, si ellos cortan fruta verde, ese día se hace la excepción de recibirla; pero al día siguiente, a la semana siguiente, la fruta que no cumpla con los indicadores o con las características que nosotros pedimos simplemente se devuelve al productor."

**Decisión:** línea 87 — "También se incluye lo que es fruta verde, fruta sobremadura, malformada y pedúnculos largos." Cita exacta de los cuatro indicadores.

---

## H-019 — Emisión del ticket de pesaje
- **Origen:** `EXP-10`  ·  **Procedencia declarada:** Elicitado durante la fase de experimentación para el mínimo de 25 RF.
- **Descripción:** El sistema debe emitir un ticket de pesaje que contenga peso bruto, peso tara, peso neto, nombre del productor, finca, transportista, placa del vehículo, fecha y hora de ingreso y la sección de calificación de la fruta.
- **Criterio de verificación:** El ticket emitido presenta los nueve campos declarados y el sistema impide emitirlo cuando falta el peso neto o la calificación.

**Candidatas:**

- [X] línea 71 (similitud 0.28): "En ese mismo ticket viene el nombre del productor, viene la finca, viene el transportista, las placas del vehículo y la fecha y hora de ingreso."
- [ ] línea 71 (similitud 0.20): "Cuando termina todo el proceso de pesaje, se emite un ticket de pesaje donde viene el peso bruto, el peso tara y el peso neto, que viene a ser el peso de la fruta."
- [ ] línea 39 (similitud 0.08): "Cortan fruta verde, porque a ellos les pagan por eso, para obtener su peso y tener su ingreso."

**Decisión:** línea 71 — "En ese mismo ticket viene el nombre del productor, viene la finca, viene el transportista, las placas del vehículo y la fecha y hora de ingreso." Complementaria: línea 71 — "Cuando termina todo el proceso de pesaje, se emite un ticket de pesaje donde viene el peso bruto, el peso tara y el peso neto...". Entre ambas cubren 8 de los 9 campos; el noveno (sección de calificación) se respalda con las frases de línea 87 usadas en H-017 y H-018.

---

## H-020 — Entrega del ticket al productor y envío por correo
- **Origen:** `EXP-11`  ·  **Procedencia declarada:** Elicitado durante la fase de experimentación para el mínimo de 25 RF.
- **Descripción:** El sistema debe permitir entregar el ticket al conductor o al productor presente y enviarlo automáticamente por correo electrónico a los productores con dirección registrada, dejando constancia del resultado del envío.
- **Criterio de verificación:** Emitido el ticket de un productor con correo registrado, el sistema genera el envío y almacena su estado; si el productor no tiene correo registrado, conserva solo la entrega física sin generar error.

**Candidatas:**

- [X] línea 87 (similitud 0.19): "El ticket se le da al chofer o al productor si está presente; en su caso, a muchos productores les tenemos registrado el correo, entonces se envía también automáticamente por correo para que lo tenga."
- [ ] línea 71 (similitud 0.05): "En ese mismo ticket viene el nombre del productor, viene la finca, viene el transportista, las placas del vehículo y la fecha y hora de ingreso."
- [ ] línea 51 (similitud 0.03): "El híbrido tiene antioxidantes."

**Decisión:** línea 87 — "El ticket se le da al chofer o al productor si está presente; en su caso, a muchos productores les tenemos registrado el correo, entonces se envía también automáticamente por correo para que lo tenga." Cita exacta de ambas vías de entrega. El registro del estado del envío es decisión de diseño.

---

## H-021 — Identificación anticipada de productores con recurrencia de fruta verde
- **Origen:** `EXP-12`  ·  **Procedencia declarada:** Elicitado durante la fase de experimentación para el mínimo de 25 RF.
- **Descripción:** El sistema debe identificar, a partir del histórico de calificaciones, los productores con mayor recurrencia de fruta verde y disponer el listado al menos un mes antes del inicio del período de baja productividad comprendido entre julio y octubre.
- **Criterio de verificación:** Configurado julio como inicio del período de baja productividad, el sistema genera durante junio el listado de productores ordenado de mayor a menor recurrencia de fruta verde.

**Candidatas:**

- [ ] línea 39 (similitud 0.11): "Ese es un problema que se presenta principalmente en los meses de julio, agosto, septiembre y parte de octubre, que son los meses de baja productividad."
- [X] línea 43 (similitud 0.08): "Normalmente, cuando tenemos estos problemas, actuamos un mes antes, realizando visitas de campo con los productores que ya tenemos identificados que tienen mayor problema."
- [ ] línea 87 (similitud 0.06): "En la calificación se incluye fruta grande, mediana o pequeña; esas son las 3 calificaciones."

**Decisión:** línea 43 — "Normalmente, cuando tenemos estos problemas, actuamos un mes antes, realizando visitas de campo con los productores que ya tenemos identificados que tienen mayor problema." (segunda candidata). Complementaria: línea 39 — "Ese es un problema que se presenta principalmente en los meses de julio, agosto, septiembre y parte de octubre, que son los meses de baja productividad", que fija la ventana del criterio de verificación. La primera candidata, por sí sola, no sustenta la identificación anticipada.

---

## H-022 — Programación de visitas de campo y capacitaciones
- **Origen:** `EXP-13`  ·  **Procedencia declarada:** Elicitado durante la fase de experimentación para el mínimo de 25 RF.
- **Descripción:** El sistema debe permitir programar visitas de campo y capacitaciones dirigidas a los productores identificados, registrando finca, fecha, motivo y participantes, y permitir cerrarlas como realizadas.
- **Criterio de verificación:** Programada una visita, el sistema conserva finca, fecha, motivo y participantes y permite listar por separado las actividades pendientes y las realizadas.

**Candidatas:**

- [X] línea 43 (similitud 0.12): "Normalmente, cuando tenemos estos problemas, actuamos un mes antes, realizando visitas de campo con los productores que ya tenemos identificados que tienen mayor problema."
- [ ] línea 71 (similitud 0.06): "En ese mismo ticket viene el nombre del productor, viene la finca, viene el transportista, las placas del vehículo y la fecha y hora de ingreso."
- [ ] línea 15 (similitud 0.03): "de dónde procede, de qué finca, quién es el dueño y quién es el chofer."

**Decisión:** línea 43 — misma frase que la cita principal de H-021: sustenta las visitas de campo a productores identificados. Sugerencia: añadir como complementaria la frase de línea 43 "En el día que estemos en la charla, en la capacitación..." (listada en H-023) para cubrir el término "capacitaciones". Los campos finca, fecha, motivo y participantes y el cierre como realizadas son decisión de diseño, sin respaldo textual en ENTR-04.

---

## H-023 — Excepción de recepción limitada al día de la capacitación
- **Origen:** `EXP-14`  ·  **Procedencia declarada:** Elicitado durante la fase de experimentación para el mínimo de 25 RF.
- **Descripción:** El sistema debe permitir registrar una excepción que autorice recibir fruta que no cumple los indicadores únicamente en la fecha de la capacitación y para el productor participante, y debe impedir su aplicación en fechas posteriores.
- **Criterio de verificación:** Registrada una excepción para el 10 de julio, una entrega del mismo productor el 11 de julio que incumple los indicadores no recibe la excepción y se procesa como devolución.

**Candidatas:**

- [X] línea 43 (similitud 0.12): "En el día que estemos en la charla, en la capacitación, si ellos cortan fruta verde, ese día se hace la excepción de recibirla; pero al día siguiente, a la semana siguiente, la fruta que no cumpla con los indicadores o con las características que nosotros pedimos simplemente se devuelve al productor."
- [ ] línea 71 (similitud 0.08): "En ese mismo ticket viene el nombre del productor, viene la finca, viene el transportista, las placas del vehículo y la fecha y hora de ingreso."
- [ ] línea 15 (similitud 0.05): "En este caso, si tenemos una fruta rechazada, se devuelve en el mismo carro; el carro vuelve a la báscula, se le da su peso de salida y también se le da su tiquete correspondiente."

**Decisión:** línea 43 — "En el día que estemos en la charla, en la capacitación, si ellos cortan fruta verde, ese día se hace la excepción de recibirla; pero al día siguiente, a la semana siguiente, la fruta que no cumpla con los indicadores o con las características que nosotros pedimos simplemente se devuelve al productor." Cita exacta: incluye la limitación al día de la capacitación y el efecto de devolución posterior.

---

## H-024 — Proyección de recepción frente a la capacidad de las extractoras
- **Origen:** `EXP-15`  ·  **Procedencia declarada:** Elicitado durante la fase de experimentación para el mínimo de 25 RF.
- **Descripción:** El sistema debe consolidar las estimaciones de cosecha informadas por las fincas para un período y compararlas con la capacidad de procesamiento declarada de cada extractora, señalando el excedente y permitiendo redistribuirlo entre las plantas con capacidad disponible.
- **Criterio de verificación:** Si la proyección de una planta supera su capacidad configurada, el sistema muestra el excedente en toneladas y permite reasignarlo a otra planta cuya capacidad restante lo admita.

**Candidatas:**

- [X] línea 95 (similitud 0.08): "O sea, nosotros lo veríamos útil porque, así como la finca realiza aquí un tema de estimación o proyección de cuántas toneladas puede cosechar, nosotros en la extractora también hacemos una proyección de cuántas toneladas podemos recibir y procesar, porque tenemos un límite de capacidad."
- [ ] línea 95 (similitud 0.05): "Entonces también nos serviría, en ese caso, para tener las estimaciones de las fincas."
- [ ] línea 23 (similitud 0.05): "Estos poros, lo que hacen al momento de entrar al proceso en las plantas extractoras, es quitarnos aceite, porque hace lo que hace una esponja:"

**Decisión:** línea 95 — "...nosotros en la extractora también hacemos una proyección de cuántas toneladas podemos recibir y procesar, porque tenemos un límite de capacidad." Complementaria: línea 95 — "Entonces también nos serviría, en ese caso, para tener las estimaciones de las fincas." BRECHA: la redistribución del excedente entre plantas con capacidad disponible no tiene respaldo en ENTR-04; conviene atenuar esa cláusula del RF o elicitarla de forma explícita.

---

## H-025 — Histórico de producción por finca
- **Origen:** `EXP-16`  ·  **Procedencia declarada:** Elicitado durante la fase de experimentación para el mínimo de 25 RF.
- **Descripción:** El sistema debe mantener un histórico por finca con el conteo de racimos y el peso promedio informados y con el peso neto efectivamente recibido, de modo que pueda observarse la evolución de la producción entre períodos sin incorporar datos personales del productor.
- **Criterio de verificación:** Con dos períodos registrados, el sistema muestra para la finca el conteo de racimos, el peso promedio y el peso neto de cada período y la variación entre ambos, sin campos de identificación personal.

**Candidatas:**

- [X] línea 99 (similitud 0.16): "Nosotros, sí, como empresa, igual estamos comprometidos con un proyecto de mejoramiento de la producción de los palmicultores, y para este caso necesitaríamos que se pueda llevar, quizás, cuando suban el conteo de racimos, quizás el peso promedio que tengan, para nosotros también llevar el registro, un histórico de cómo puede ir mejorando o no la producción de toda la finca."
- [ ] línea 15 (similitud 0.05): "Ahí lo atiende el señor basculero, donde le indica su peso bruto, y en este caso le pregunta sus datos:"
- [ ] línea 71 (similitud 0.05): "En ese mismo ticket viene el nombre del productor, viene la finca, viene el transportista, las placas del vehículo y la fecha y hora de ingreso."

**Decisión:** línea 99 — "...necesitaríamos que se pueda llevar, quizás, cuando suban el conteo de racimos, quizás el peso promedio que tengan, para nosotros también llevar el registro, un histórico de cómo puede ir mejorando o no la producción de toda la finca." Cita exacta: alcance de los datos, propósito histórico y comparación entre períodos.

---
