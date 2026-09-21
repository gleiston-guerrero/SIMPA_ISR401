# F2 — Trazabilidad del member checking

Ronda del 2026-09-04, doce enunciados, tres participantes (ENTR-01, ENTR-02, ENTR-13).

Generado por `07_Datos/scripts/plan_mejora/trazabilidad_F2.py` sobre el libro de códigos v1.0 y los 213 fragmentos con cita literal verificada en C1. La correspondencia enunciado→código es una **propuesta**; la columna `CODIGOS_VERIFICADOS` la firma una persona.

| N.º | Enunciado | ENTR-01 | ENTR-02 | ENTR-13 | Códigos propuestos | Citas | Alerta |
|---:|---|:-:|:-:|:-:|---|---:|---|
| 1 | Registro en libreta y reporte por WhatsApp sin formato fijo | R | P | C | CANAL_INFORMAL, REGISTRO_PAPEL, REGISTRO_CLIMA, PERDIDA_DATOS, HISTORIAL_LOTE | 23 | RECHAZADO por al menos un participante |
| 2 | Reporte con detalle insuficiente | R | P | C | CANAL_INFORMAL | 3 | RECHAZADO por al menos un participante |
| 3 | Brecha entre aviso y verificación en sitio | C | P | C | DIAGNOSTICO_SITIO, VERIFICACION_VISUAL, VERIFICACION_DIAGNOSTICO, SUPERVISION_RECORRIDO, LATENCIA_VERIFICACION | 14 |  |
| 4 | Conectividad estable solo en el campamento | P | P | C | CONECTIVIDAD_PARCIAL | 3 |  |
| 5 | Pago mixto y necesidad de conteo confiable | P | P | C | COLOR_NO_FIABLE, EVALUACION_DESEMPENO, ENTREGA_VERBAL, CONTEO_FLORES, CONTEO_DIARIO | 8 |  |
| 6 | Riego y control diario como factores determinantes | P | P | C | FACTOR_PRODUCTIVIDAD | 3 |  |
| 7 | Dificultad de adopción concentrada en el personal manual | R | P | P | REGISTRO_PAPEL, USUARIO_NO_EXPERTO, ESCASEZ_MANO_OBRA, EQUIPOS_TRABAJO | 17 | RECHAZADO por al menos un participante |
| 8 | Formalización del registro asociada al tamaño de la finca | R | P | C | CALIFICACION_TICKET, REGISTRO_PAPEL, REGISTRO_CLIMA, PERDIDA_DATOS, HISTORIAL_LOTE | 21 | RECHAZADO por al menos un participante |
| 9 | Cosecha programada por desgrane del fruto | C | P | P | PEPA_DESPRENDIDA, CALIDAD_COMO_INDICADOR, SOBREMADURACION, PROBLEMA_FRUTA_VERDE, CICLO_ANTESIS_COSECHA | 8 |  |
| 10 | Decisión por observación del cielo y desconfianza en reportes climáticos | R | NA | P | FALTA_ESPECIFICACION, RECOMENDACION_ACCIONABLE, MONITOREO_VISUAL | 6 | RECHAZADO por al menos un participante |
| 11 | Abandono de herramientas por resistencia al cambio | SP | NA | C | RESISTENCIA_CAMBIO | 9 |  |
| 12 | La mayor dificultad reside en lograr el uso efectivo | P | NA | C | — | 0 | SIN CITA LITERAL QUE LO SOSTENGA |

---

## Citas literales que sostienen cada enunciado

### Enunciado 1 — Registro en libreta y reporte por WhatsApp sin formato fijo

Posiciones: ENTR-01 `R` · ENTR-02 `P` · ENTR-13 `C`

> **RECHAZADO por al menos un participante**

- **CANAL_INFORMAL** · EV-07 · `2026-07-28_ENTR-07_Transcripcion.md` línea 27 · RF-30
  > Bueno, la libreta realmente la lleva al jefe de campo y los reportes nos los envían por medio de whatsapp a los que somos los administradores.
- **CANAL_INFORMAL** · EV-07 · `2026-07-28_ENTR-07_Transcripcion.md` línea 55 · RF-30
  > Nosotros solo usamos whatsapp.
- **CANAL_INFORMAL** · ENTR-10 · `2026-08-31_ENTR-10_Transcripcion.md` línea 31 · RF-30
  > Aplicaciones como WhatsApp.
- **REGISTRO_PAPEL** · EV-05 · `2026-07-28_ENTR-05_Transcripcion.md` línea 27 · RF-04
  > Claro, nosotros le decimos, lo van a tener en una libreta hasta el día de quincena que el hombre nos pague.
- **REGISTRO_PAPEL** · EV-05 · `2026-07-28_ENTR-05_Transcripcion.md` línea 85 · RF-04
  > Sería una aplicación que uno, o sea, le vaya editando y él le vaya aguardando los días de trabajo que se hace aquí.
- **REGISTRO_PAPEL** · EV-06 · `2026-07-28_ENTR-06_Transcripcion.md` línea 43 · RF-04
  > Sí, la plantación que hizo. Lo hace de un cuadernito.
- **REGISTRO_PAPEL** · EV-07 · `2026-07-28_ENTR-07_Transcripcion.md` línea 27 · RF-04
  > Bueno, la libreta realmente la lleva al jefe de campo y los reportes nos los envían por medio de whatsapp a los que somos los administradores.
- **REGISTRO_PAPEL** · ENTR-11 · `2026-08-31_ENTR-11_Transcripcion.md` línea 43 · RF-04
  > Mediante papel.

_(y 15 citas más en el CSV)_

### Enunciado 2 — Reporte con detalle insuficiente

Posiciones: ENTR-01 `R` · ENTR-02 `P` · ENTR-13 `C`

> **RECHAZADO por al menos un participante**

- **CANAL_INFORMAL** · EV-07 · `2026-07-28_ENTR-07_Transcripcion.md` línea 27 · RF-30
  > Bueno, la libreta realmente la lleva al jefe de campo y los reportes nos los envían por medio de whatsapp a los que somos los administradores.
- **CANAL_INFORMAL** · EV-07 · `2026-07-28_ENTR-07_Transcripcion.md` línea 55 · RF-30
  > Nosotros solo usamos whatsapp.
- **CANAL_INFORMAL** · ENTR-10 · `2026-08-31_ENTR-10_Transcripcion.md` línea 31 · RF-30
  > Aplicaciones como WhatsApp.

### Enunciado 3 — Brecha entre aviso y verificación en sitio

Posiciones: ENTR-01 `C` · ENTR-02 `P` · ENTR-13 `C`

- **DIAGNOSTICO_SITIO** · EV-04 · `2026-07-28_ENTR-04_Transcripcion.md` línea 75 · RF-08
  > definir o concluir bien por qué tenemos el problema del amarillamiento de las hojas bajeras que está subiendo, que normalmente puede deberse a alguna deficiencia de magnesio, pero como dicen que están aplicando, puede haber algún bloqueo en el suelo,
- **VERIFICACION_VISUAL** · EV-03 · `2026-05-23_ENTR-03_Transcripcion.md` línea 33 · RF-13
  > La mayor, es visible, por lo que es un talco industrial más una hormona, y se puede observar a raíz desde su primer momento de aplicación.
- **VERIFICACION_DIAGNOSTICO** · ENTR-10 · `2026-08-31_ENTR-10_Transcripcion.md` línea 59 · RNF-16
  > Más que todo, la información y fotos.
- **VERIFICACION_DIAGNOSTICO** · ENTR-11 · `2026-08-31_ENTR-11_Transcripcion.md` línea 71 · RNF-16
  > Primero, una imagen donde me compruebe sobre ese problema, y lo segundo sería recurrir al lugar para probar los hechos y poder acudir a resolver el problema.
- **SUPERVISION_RECORRIDO** · EV-01 · `2026-05-23_ENTR-01_Transcripcion.md` línea 11 · RF-15
  > Entonces la función del administrador es recorrer todos los trabajos y hace la revision de que todos los equipos esten cumpliendo con su funcion.
- **SUPERVISION_RECORRIDO** · EV-02 · `2026-05-23_ENTR-02_Transcripcion.md` línea 95 · RF-15
  > actividad que está haciendo la persona. Y ahí nos damos cuenta si el trabajador o la persona que está realizando el trabajo está atrasado o va avanzando o no está haciendo nada. De esa manera también controlamos al personal de una manera que sea eficiente.
- **SUPERVISION_RECORRIDO** · EV-03 · `2026-05-23_ENTR-03_Transcripcion.md` línea 45 · RF-15
  > Con un rastreador GPS.
- **SUPERVISION_RECORRIDO** · EV-05 · `2026-07-28_ENTR-05_Transcripcion.md` línea 15 · RF-03
  > El administrador.

_(y 6 citas más en el CSV)_

### Enunciado 4 — Conectividad estable solo en el campamento

Posiciones: ENTR-01 `P` · ENTR-02 `P` · ENTR-13 `C`

- **CONECTIVIDAD_PARCIAL** · EV-06 · `2026-07-28_ENTR-06_Transcripcion.md` línea 59 · RNF-11
  > En esta parte nomás, la parte principal.
- **CONECTIVIDAD_PARCIAL** · EV-07 · `2026-07-28_ENTR-07_Transcripcion.md` línea 59 · RNF-11
  > Hay ciertas partes donde te coge el internet satelital, pero realmente donde hay internet es en el campamento.
- **CONECTIVIDAD_PARCIAL** · ENTR-15 · `2026-09-01_ENTR-15_Transcripcion.md` línea 50 · RNF-11
  > Porque como le digo, en parte del campo cuando uno está en en sus labores no no no no tiene señal, en la mayor la mayor parte de la finca no no hay señal.

### Enunciado 5 — Pago mixto y necesidad de conteo confiable

Posiciones: ENTR-01 `P` · ENTR-02 `P` · ENTR-13 `C`

- **COLOR_NO_FIABLE** · EV-08 · `2026-07-28_ENTR-08_Transcripcion.md` línea 23 · RD-07
  > Bueno, en sí maduración solo nosotros manejamos con el método de desprendimiento. Porque si nosotros cortamos, a veces el color engaña.
- **COLOR_NO_FIABLE** · EV-08 · `2026-07-28_ENTR-08_Transcripcion.md` línea 23 · RD-07
  > Bueno, en sí maduración solo nosotros manejamos con el método de desprendimiento. Porque si nosotros cortamos, a veces el color engaña.
- **EVALUACION_DESEMPENO** · EV-01 · `2026-05-23_ENTR-01_Transcripcion.md` línea 75 · RF-16
  > Eh por rendimiento y producción, o sea este en el tema de los polinizadores pues ellos cuentan las flores que han polinizado en el día
- **ENTREGA_VERBAL** · EV-05 · `2026-07-28_ENTR-05_Transcripcion.md` línea 31 · RF-28
  > Ese conteo se le entrega en la tarde, a las 4 o 5 de la tarde, a la hora que uno se alza de la labor de trabajo.
- **ENTREGA_VERBAL** · EV-07 · `2026-07-28_ENTR-07_Transcripcion.md` línea 39 · RF-30
  > Por lo general nada, pero diría que los seguimientos, que no suelen llegar los reportes lo suficientemente especificados por parte del jefe de campo.
- **ENTREGA_VERBAL** · EV-07 · `2026-07-28_ENTR-07_Transcripcion.md` línea 35 · RF-29
  > Por lo general no suele suceder, pero sí suele haber errores, pero todo eso se corrige al momento de revisar.
- **CONTEO_FLORES** · EV-01 · `2026-05-23_ENTR-01_Transcripcion.md` línea 75 · RF-14
  > ellos cuentan las flores que han polinizado en el día
- **CONTEO_FLORES** · EV-03 · `2026-05-23_ENTR-03_Transcripcion.md` línea 49 · RF-14
  > Que el rastreador GPS tenga marcaciones para poder marcar el número de flores polinizadas diariamente.

### Enunciado 6 — Riego y control diario como factores determinantes

Posiciones: ENTR-01 `P` · ENTR-02 `P` · ENTR-13 `C`

- **FACTOR_PRODUCTIVIDAD** · EV-01 · `2026-05-23_ENTR-01_Transcripcion.md` línea 39 · RF-04
  > Eh el tema de producción eso se basa en en un buen riego y una buena nutrición o fertilización. Eso serían lo lo lo lo principal para poder ser este productivo.
- **FACTOR_PRODUCTIVIDAD** · EV-02 · `2026-05-23_ENTR-02_Transcripcion.md` línea 59 · RF-04
  > Entonces ahí hay un un tiempo muy largo para que la planta pueda manejarse con sus nutrientes y su humedad. Si no hay eso, la planta no va a producir sino mínimas cantidades que ya no sería rentable.
- **FACTOR_PRODUCTIVIDAD** · EV-03 · `2026-05-23_ENTR-03_Transcripcion.md` línea 21 · RF-13
  > La labor de polinización es la labor más importante porque es donde determinamos la producción de la finca.

### Enunciado 7 — Dificultad de adopción concentrada en el personal manual

Posiciones: ENTR-01 `R` · ENTR-02 `P` · ENTR-13 `P`

> **RECHAZADO por al menos un participante**

- **REGISTRO_PAPEL** · EV-05 · `2026-07-28_ENTR-05_Transcripcion.md` línea 27 · RF-04
  > Claro, nosotros le decimos, lo van a tener en una libreta hasta el día de quincena que el hombre nos pague.
- **REGISTRO_PAPEL** · EV-05 · `2026-07-28_ENTR-05_Transcripcion.md` línea 85 · RF-04
  > Sería una aplicación que uno, o sea, le vaya editando y él le vaya aguardando los días de trabajo que se hace aquí.
- **REGISTRO_PAPEL** · EV-06 · `2026-07-28_ENTR-06_Transcripcion.md` línea 43 · RF-04
  > Sí, la plantación que hizo. Lo hace de un cuadernito.
- **REGISTRO_PAPEL** · EV-07 · `2026-07-28_ENTR-07_Transcripcion.md` línea 27 · RF-04
  > Bueno, la libreta realmente la lleva al jefe de campo y los reportes nos los envían por medio de whatsapp a los que somos los administradores.
- **REGISTRO_PAPEL** · ENTR-11 · `2026-08-31_ENTR-11_Transcripcion.md` línea 43 · RF-04
  > Mediante papel.
- **REGISTRO_PAPEL** · ENTR-13 · `2026-09-01_ENTR-13_Transcripcion.md` línea 25 · RF-04
  > Como le decía, inicialmente, en las fincas pequeñas, muchos llevan registros empíricos. Se lleva una libreta, una agenda, donde se registran las labores que hacen en el día.
- **REGISTRO_PAPEL** · ENTR-14 · `2026-09-01_ENTR-14_Transcripcion.md` línea 15 · RF-04
  > Hay unas que se hacen escritas con una bitácora; otra, empíricamente, se le dice al trabajador qué es lo que va a realizar en el día de trabajo.
- **REGISTRO_PAPEL** · ENTR-15 · `2026-09-01_ENTR-15_Transcripcion.md` línea 14 · RF-04
  > Por lo general solo hacen con papel.

_(y 9 citas más en el CSV)_

### Enunciado 8 — Formalización del registro asociada al tamaño de la finca

Posiciones: ENTR-01 `R` · ENTR-02 `P` · ENTR-13 `C`

> **RECHAZADO por al menos un participante**

- **CALIFICACION_TICKET** · EV-04 · `2026-07-28_ENTR-04_Transcripcion.md` línea 71 · RF-23
  > En la calificación se incluye fruta grande, mediana o pequeña, las tres calificaciones; y se incluye también lo que es fruta verde, fruta sobremadura, malformada y pedúnculos largos.
- **REGISTRO_PAPEL** · EV-05 · `2026-07-28_ENTR-05_Transcripcion.md` línea 27 · RF-04
  > Claro, nosotros le decimos, lo van a tener en una libreta hasta el día de quincena que el hombre nos pague.
- **REGISTRO_PAPEL** · EV-05 · `2026-07-28_ENTR-05_Transcripcion.md` línea 85 · RF-04
  > Sería una aplicación que uno, o sea, le vaya editando y él le vaya aguardando los días de trabajo que se hace aquí.
- **REGISTRO_PAPEL** · EV-06 · `2026-07-28_ENTR-06_Transcripcion.md` línea 43 · RF-04
  > Sí, la plantación que hizo. Lo hace de un cuadernito.
- **REGISTRO_PAPEL** · EV-07 · `2026-07-28_ENTR-07_Transcripcion.md` línea 27 · RF-04
  > Bueno, la libreta realmente la lleva al jefe de campo y los reportes nos los envían por medio de whatsapp a los que somos los administradores.
- **REGISTRO_PAPEL** · ENTR-11 · `2026-08-31_ENTR-11_Transcripcion.md` línea 43 · RF-04
  > Mediante papel.
- **REGISTRO_PAPEL** · ENTR-13 · `2026-09-01_ENTR-13_Transcripcion.md` línea 25 · RF-04
  > Como le decía, inicialmente, en las fincas pequeñas, muchos llevan registros empíricos. Se lleva una libreta, una agenda, donde se registran las labores que hacen en el día.
- **REGISTRO_PAPEL** · ENTR-14 · `2026-09-01_ENTR-14_Transcripcion.md` línea 15 · RF-04
  > Hay unas que se hacen escritas con una bitácora; otra, empíricamente, se le dice al trabajador qué es lo que va a realizar en el día de trabajo.

_(y 13 citas más en el CSV)_

### Enunciado 9 — Cosecha programada por desgrane del fruto

Posiciones: ENTR-01 `C` · ENTR-02 `P` · ENTR-13 `P`

- **CALIDAD_COMO_INDICADOR** · EV-01 · `2026-05-23_ENTR-01_Transcripcion.md` línea 75 · RF-16
  > Si si tienes una fruta eh en buena en buena calidad es porque te ha dado ha hecho eh el operador ha hecho un buen trabajo y si no pues eh efectivamente se da cuenta uno de que el operador no está cumpliendo con su trabajo.
- **CALIDAD_COMO_INDICADOR** · EV-03 · `2026-05-23_ENTR-03_Transcripcion.md` línea 29 · RF-16
  > Porque si el polinizador, o la persona que está ejerciendo la labor, no la hace de una manera eficiente, no contamos con un buen racimo. Entonces, perderíamos el 50% de la producción en caso de ser así.
- **CALIDAD_COMO_INDICADOR** · EV-03 · `2026-05-23_ENTR-03_Transcripcion.md` línea 21 · RF-13
  > Y que cada racimo salga al 100%.
- **PROBLEMA_FRUTA_VERDE** · EV-04 · `2026-07-28_ENTR-04_Transcripcion.md` línea 31 · RF-22
  > Ya, el principal problema que nosotros tenemos actualmente es el tema de fruta verde. Sí, el tema de que la fruta no llega con desprendimiento.
- **PROBLEMA_FRUTA_VERDE** · EV-08 · `2026-07-28_ENTR-08_Transcripcion.md` línea 43 · RF-25
  > Entonces vemos si tiene mayor este sobremaduración, entonces eso también causa acidez.
- **PROBLEMA_FRUTA_VERDE** · EV-08 · `2026-07-28_ENTR-08_Transcripcion.md` línea 39 · RF-22
  > Entonces a eso vemos el porcentaje, es decir si ya vemos que pasa el 3, 4%, eh... ya 5% ya sería un castigo.
- **PROBLEMA_FRUTA_VERDE** · EV-08 · `2026-07-28_ENTR-08_Transcripcion.md` línea 59 · RF-21
  > Entonces esa es la mejor explicación de ejemplo que nosotros le damos, como ejemplo así de un racimo verde. Si traemos un fruto verde, no saca nada de de extracción de aceite.
- **CICLO_ANTESIS_COSECHA** · EV-02 · `2026-05-23_ENTR-02_Transcripcion.md` línea 59 · RF-18
  > para botar el racimo ya maduro está a a 6 meses de que de la antesis así adelante, 6 meses para cosecharla.

### Enunciado 10 — Decisión por observación del cielo y desconfianza en reportes climáticos

Posiciones: ENTR-01 `R` · ENTR-02 `NA` · ENTR-13 `P`

> **RECHAZADO por al menos un participante**

- **RECOMENDACION_ACCIONABLE** · ENTR-10 · `2026-08-31_ENTR-10_Transcripcion.md` línea 91 · RNF-16
  > Un aviso ni tan largo ni tan corto, que sea específico.
- **RECOMENDACION_ACCIONABLE** · ENTR-15 · `2026-09-01_ENTR-15_Transcripcion.md` línea 34 · RNF-16
  > Realizar lo que es un monitoreo eh del de la de la parcela, ver qué tanto ha afectado a la a las plagas, calcular qué tan incidencia de insectos hay, eh y a través de eso pues realizar lo que es un un control, establecer prácticas culturales o si no trampas eh que ayuden a reducir la incidencia sea 
- **MONITOREO_VISUAL** · EV-01 · `2026-05-23_ENTR-01_Transcripcion.md` línea 19 · RF-05
  > el cual hace un monitoreo diario que es del cultivo en el cual a la semana tiene que ya dar la vuelta a toda la plantación y el va monitoriando y revisando que las plantas se encuentren en buen estado
- **MONITOREO_VISUAL** · EV-02 · `2026-05-23_ENTR-02_Transcripcion.md` línea 35 · RF-05
  > diariamente viendo, rodando, visitando la plantación para detectar algún problema, enfermedad
- **MONITOREO_VISUAL** · EV-08 · `2026-07-28_ENTR-08_Transcripcion.md` línea 99 · RF-05
  > En sí nosotros recomendamos ver este... eh sí que mande bien, por ejemplo en la mañana para ver si la insect- qué tanto insecto hay y para ver también, hacemos monitoreo de insectos.
- **MONITOREO_VISUAL** · ENTR-12 · `2026-08-31_ENTR-12_Transcripcion.md` línea 63 · RF-05
  > Por ejemplo, el estado de las plantaciones.

### Enunciado 11 — Abandono de herramientas por resistencia al cambio

Posiciones: ENTR-01 `SP` · ENTR-02 `NA` · ENTR-13 `C`

- **RESISTENCIA_CAMBIO** · ENTR-09 · `2026-08-31_ENTR-09_Transcripcion.md` línea 39 · RNF-08
  > Normalmente la dejan de usar porque no la conocen, no son capaces o no se capacitan esas personas para llevar un software nuevo.
- **RESISTENCIA_CAMBIO** · ENTR-11 · `2026-08-31_ENTR-11_Transcripcion.md` línea 119 · RNF-08
  > Que no me ayude a organizar bien el personal.
- **RESISTENCIA_CAMBIO** · ENTR-12 · `2026-08-31_ENTR-12_Transcripcion.md` línea 47 · RNF-08
  > Bueno, yo creo que la mayoría de nosotros, como ingenieros, es nuestra responsabilidad utilizar estas herramientas o estadísticas para poder trabajar con cualquier análisis o para poder seguir evaluando cualquier trabajo que estamos realizando. Y si no se trabaja con esa herramienta, tal vez sería, 
- **RESISTENCIA_CAMBIO** · ENTR-13 · `2026-09-01_ENTR-13_Transcripcion.md` línea 67 · RNF-08
  > Entonces, hay resistencia y eso hace que a veces se deje de usar, porque la gente no quiere adaptarse al cambio.
- **RESISTENCIA_CAMBIO** · ENTR-13 · `2026-09-01_ENTR-13_Transcripcion.md` línea 85 · RNF-08
  > Lo más difícil es hacer que la gente lo use, porque hacerlo, elaborar el programa para un ingeniero especializado en informática es fácil, pero lo más difícil es hacer que cale en la gente. Que la gente se adapte a ese sistema para que lo use.
- **RESISTENCIA_CAMBIO** · ENTR-14 · `2026-09-01_ENTR-14_Transcripcion.md` línea 39 · RNF-08
  > Es la práctica. A veces, con una herramienta que usted le lleve nueva al trabajador, dice: “No, yo trabajo con el machete y no quiero con el palín”.
- **RESISTENCIA_CAMBIO** · ENTR-14 · `2026-09-01_ENTR-14_Transcripcion.md` línea 59 · RNF-08
  > Lograr que la gente lo use. Hacerlo ahorita con la inteligencia y hacer que el personal lo utilice, eso es muy complicado.
- **RESISTENCIA_CAMBIO** · ENTR-16 · `2026-09-01_ENTR-16_Transcripcion.md` línea 38 · RNF-08
  > Por lo general se abandona por la falta de costumbre, tanto académica por la falta de aprendizaje, como la practicidad también de la misma.

_(y 1 citas más en el CSV)_

### Enunciado 12 — La mayor dificultad reside en lograr el uso efectivo

Posiciones: ENTR-01 `P` · ENTR-02 `NA` · ENTR-13 `C`

> **SIN CITA LITERAL QUE LO SOSTENGA**

_Ninguna cita literal verificada corresponde a los códigos propuestos._
