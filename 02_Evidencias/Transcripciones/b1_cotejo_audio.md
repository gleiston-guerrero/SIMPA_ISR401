# Cotejo B1: estado de la comprobación de las transcripciones contra el audio

**Fecha:** 21/09/2026 · **Alcance:** transcripciones de ENTR-01 a ENTR-08 (rondas 1 y 2)

## 1. Lo que sí está comprobado con datos

- **Marcas de tiempo:** las ocho transcripciones tienen marcas `[mm:ss]`.
- **Cobertura frente al audio:** siete de las ocho transcripciones cubren el audio dentro de ±10 %. ENTR-03 no (81 % a 82 %, unos 57 segundos finales sin transcribir). La tabla y su método están en `02_Evidencias/Transcripciones/readme.md`, sección «Cobertura de cada transcripción frente a la duración del audio».

## 2. Cotejo de oído (criterio: menos de 5 % de discrepancia en muestras de 3 minutos)

1. Se definieron **10 tramos** (unos 26 minutos de audio) mediante un sorteo con semilla 20260921, más dos tramos elegidos a propósito: la parte de ENTR-02 posterior a 16:32 y el final de ENTR-03. Se preparó una hoja de cotejo con el texto exacto de cada tramo.
2. El revisor, Arboleda Yanza Francisco Javier, declara haber escuchado los diez tramos el 21/09/2026 y entregó un registro que declara **64 diferencias** (entre 1,15 % y 3,44 % por tramo), de las cuales **detalla 27 ejemplos**.
3. Ese registro se sometió a una comprobación contra las transcripciones: **22 de los 27 ejemplos coinciden** con el texto en el minuto indicado y **5 no**. Tres ejemplos atribuidos a ENTR-01 corresponden a frases de ENTR-02, uno escribe una palabra que no está en el texto y en otro lo «oído» es idéntico a lo escrito.
4. Por eso, **las cifras de discrepancia de ese registro no se aceptan como evidencia**: no pueden respaldarse fila por fila (solo 27 de 64 diferencias se detallan, y algunas no se sostienen).

## 3. Conclusión

El criterio de B1 «menos de 5 % de discrepancia en muestras de 3 minutos» queda **NO ACREDITADO**. Las transcripciones no se dan por cotejadas contra el audio. No se modificó ninguna transcripción a partir de este cotejo.

## 4. Qué falta para acreditarlo

- Un registro **de una fila por cada diferencia**, con la frase escrita copiada de la transcripción y lo oído en forma literal, verificado con `07_Datos/scripts/plan_mejora/verificar_cotejo_B1.py`. De esa lista se calcula el porcentaje de cada tramo, en lugar de escribirlo a mano.
- Repetir el tramo de ENTR-01, cuyos tres ejemplos no pertenecen a esa entrevista, y confirmar con el audio el final de ENTR-03 (de 04:15 a 05:14).
- Si esto no se completa antes del cierre, se declara como no ejecutado por falta de tiempo.
