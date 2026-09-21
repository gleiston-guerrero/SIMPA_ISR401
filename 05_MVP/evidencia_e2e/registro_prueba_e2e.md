# Prueba de extremo a extremo por rol — E1

**Fecha de ejecución:** 19/09/2026, entre las 21:28 y las 21:54 (según la bitácora de la aplicación y las marcas de las capturas), para las secciones 1 a 4 · 21/09/2026 para la repetición de RF-40, RF-42 y RF-22
**Ejecuta:** Macías Herrera Josthyn Esteban (autor de los commits de las capturas del 19/09) · Arboleda Yanza Francisco Javier (transcripción de resultados y repetición de pruebas)
**Entorno probado:** https://simpa-v3-prototipo.netlify.app/
**Commit del prototipo declarado en el repositorio:** `035470cb1dfd7be9557f1c5e2db24473cbcb8c02`
**Correspondencia entorno ↔ commit:** NO SE PUDO DETERMINAR. El despliegue se publica manualmente y no está enlazado al repositorio. El comportamiento observado coincide con el código del commit declarado en cuatro puntos comprobados (menú por rol de `navItems()`, formato del CSV de RF-40, mensajes de RF-42 y textos de la bitácora), pero eso no prueba que sean el mismo commit.

> El despliegue se publica manualmente y no está enlazado al repositorio. Si
> la correspondencia no puede establecerse, se declara aquí y la prueba se
> reporta como ejecutada sobre el despliegue, no sobre el árbol versionado.

Cada rol se prueba en una ventana de incógnito distinta: la aplicación guarda
su estado en `localStorage` bajo la clave `simpa_v4`, de modo que una sesión
previa altera el resultado.

---

## 1. Acceso por rol

Se anota qué entradas del menú son **visibles** y a cuáles se **accede**
efectivamente al pulsarlas.

### Administrador (admin / admin123)

| Entrada de menú | ¿Visible? | ¿Accede? |
|---|---|---|
| Panel principal | Sí | Sí |
| Plantaciones y lotes | Sí | Sí |
| Análisis IA | Sí | Sí |
| Labores | Sí | Sí |
| Mapa GPS | Sí | Sí |
| Calidad / Extractora | Sí | Sí |
| Reportes | Sí | Sí |
| Alertas | Sí | Sí |
| Clima | Sí | Sí |
| Personal | Sí | Sí |

### Supervisor (supervisor / super123)

| Entrada de menú | ¿Visible? | ¿Accede? |
|---|---|---|
| Panel principal | Sí | Sí |
| Plantaciones y lotes | Sí | Sí |
| Análisis IA | Sí | Sí |
| Labores | Sí | Sí |
| Mapa GPS | Sí | Sí |
| Calidad / Extractora | Sí | Sí |
| Reportes | Sí | Sí |
| Alertas | Sí | Sí |
| Clima | Sí | Sí |
| Personal | No | No |

### Operario (operario / oper123)

| Entrada de menú | ¿Visible? | ¿Accede? |
|---|---|---|
| Panel principal | Sí | Sí |
| Plantaciones y lotes | Sí | Sí |
| Análisis IA | Sí | Sí |
| Labores | Sí | Sí |
| Mapa GPS | Sí | Sí |
| Calidad / Extractora | Sí | Sí |
| Reportes | No | No |
| Alertas | Sí | Sí |
| Clima | Sí | Sí |
| Personal | No | No |

**Hallazgo esperado según el código** (`navItems()`): solo `Personal` está
restringida a Administrador. Reportes, Calidad / Extractora y Clima deberían
quedar accesibles para Operario. Confirmar o refutar.
*(Texto de la plantilla, desactualizado: ver el resultado observado.)*

Resultado observado:
Lo observado coincide con el código actual (`navItems()`, línea 38 de
`Prototipo/index.html`): `Personal` es visible solo para Administrador y
`Reportes` solo para Supervisor y Administrador. Como Operario, Reportes y
Personal no aparecen en el menú y no se accede a ellos; como Supervisor,
Personal tampoco. Calidad / Extractora y Clima quedan accesibles para
Operario. Lo que **no** coincide con lo observado es el «hallazgo esperado» de
esta plantilla y la sección «Control de acceso por rol» de `05_MVP/readme.md`,
que declaran una sola entrada restringida (ver discrepancia 1).

---

## 2. RF-40 · Exportación de datos personales

Como **Operario**, ir a `Mapa GPS` → sección *Privacidad* → «Mis datos
personales · RF-40» → pulsar «Exportar mis datos (CSV)».

Abrir el CSV descargado y transcribir su contenido
(transcrito de la captura `2026-09-19_operario_rf40_export.png`):

```
seccion,"campo","valor"
identificacion,"identificador interno","1"
identificacion,"nombre","Trabajador 1"
contacto,"telefono","0990000001"
vinculacion laboral,"equipo","Labores agrícolas"
vinculacion laboral,"lote asignado","Lote 1"
vinculacion laboral,"dispositivo inteligente","Si"
vinculacion laboral,"estado de la relacion","Activa"
consentimiento,"geolocalizacion","Otorgado"
avance registrado,"(sin registros)",""
exportacion,"fecha y hora","19/9/2026, 9:28:27 p. m."
```

**Comprobar:**

- [x] Los datos corresponden a la ficha del titular autenticado, no a otra persona
- [x] Incluye identificación, contacto, vinculación laboral y avance registrado
- [x] La solicitud quedó asentada en la bitácora con fecha y hora

Repetir como **Administrador**: al no tener ficha de personal asociada, debe
indicar que no hay datos de trabajador que exportar, en lugar de descargar
datos ajenos.

Resultado observado:
El CSV corresponde a la ficha 1 (`Trabajador 1`), que es la ficha asociada a la
cuenta `operario`; incluye identificación, contacto, vinculación laboral,
consentimiento de geolocalización y fecha y hora de la exportación. La sección
«avance registrado» aparece como «(sin registros)» porque en esa sesión no se
había registrado ningún avance; la categoría sí está incluida. La solicitud
quedó asentada en la bitácora, que solo es visible como Administrador (Personal,
al pie): «19/9/2026, 9:28:27 p. m. · Trabajador Agrícola · RF-40 · Exportación de
datos personales — Titular Trabajador 1 · 10 campos exportados» (captura
`2026-09-19_admin_rf42_bloqueo.png`); la hora coincide con la del CSV. Como
Operario no se puede consultar esa bitácora porque Personal está restringida.
Como Administrador, en Mapa GPS → Privacidad → RF-40 no aparece el botón de
exportar, consistente con que esa cuenta no tiene ficha de trabajador asociada.
Observación menor: al abrir el CSV en Excel las tildes salen dañadas
(«agrÃ­colas»), porque el archivo no lleva marca de codificación UTF-8.

---

## 3. RF-41 · Rectificación con bitácora

Como **Administrador**, en `Personal` → botón «Rectificar» de una ficha.

1. Dejar el motivo vacío y pulsar Guardar: debe rechazarlo.
2. Completar campo, valor nuevo y motivo, y guardar.
3. Revisar la bitácora al pie de la misma pantalla.

**Comprobar:**

- [x] Sin motivo no guarda
- [x] El dato queda corregido en la ficha
- [x] La bitácora registra valor anterior, fecha, autor y motivo
- [x] No existe ninguna función en la interfaz para borrar o editar entradas

Intentar la misma acción como **Operario**: debe rechazarse por rol.

Resultado observado:
RF-41 cumple sus criterios. El formulario de rectificación rechaza el guardado
sin motivo. Al completarlo, el dato queda corregido en la ficha y la bitácora
registra valor anterior, fecha, autor y motivo. No existe función de
editar/borrar en la bitácora. Como Operario, la opción «Personal» no está
disponible en el menú, por lo que la rectificación queda rechazada por rol de
forma efectiva (no se puede ni acceder a la función).

---

## 4. RF-42 · Supresión con disociación

Como **Administrador**, en `Personal`.

1. Con la relación en *Activa*, pulsar «Suprimir»: debe rechazarlo indicando
   que RF-42 exige relación terminada.
2. Pulsar el distintivo de la columna «Relación» para pasarla a *Terminada*.
3. **Antes de suprimir**, anotar los totales de la pantalla `Reportes`:

```
Producción estimada: 20.6 T | Presupuesto: $861 | Ejecución registrada: $0 | Cumplimiento: 82%
Liquidación semanal: Corona 800/1123 (71%) · Polinización 980/1200 (82%) · Chapia 1700/1800 (94%)
Estimación por lote: Lote 1: 216 racimos / 3.9 T · Lote 2: 196 / 3.5 T · Lote 3: 190 / 3.4 T ·
Lote 4: 177 / 3.2 T · Lote 5: 166 / 3.0 T · Lote 6: 202 / 3.6 T
```

4. Ejecutar «Suprimir» y confirmar.
5. Volver a `Reportes` y anotar los totales:

```
Producción estimada: 20.6 T | Presupuesto: $861 | Ejecución registrada: $0 | Cumplimiento: 82%
Liquidación semanal: Corona 800/1123 (71%) · Polinización 980/1200 (82%) · Chapia 1700/1800 (94%)
Estimación por lote: Lote 1: 216 racimos / 3.9 T · Lote 2: 196 / 3.5 T · Lote 3: 190 / 3.4 T ·
Lote 4: 177 / 3.2 T · Lote 5: 166 / 3.0 T · Lote 6: 202 / 3.6 T
```

**Comprobar:**

- [x] El intento sobre ficha activa se rechaza
- [x] Tras suprimir, la ficha aparece como `ANON-000X` con el distintivo «disociada»
- [ ] El contacto quedó vacío (no verificado en esta prueba)
- [x] **Los totales por lote y período son idénticos antes y después** (con la salvedad de abajo)
- [ ] Ninguna pantalla ni exportación devuelve el nombre suprimido (no se revisaron todas las pantallas tras la repetición; ver discrepancia 4)
- [x] Las entradas de bitácora previas se conservan, con el identificador disociado

Resultado observado:
Con la relación en Activa, «Suprimir» se rechaza («RF-42 exige que la relación
laboral conste como terminada»). Tras pasar la relación a Terminada y suprimir,
la ficha 1 aparece como `ANON-0001` con el distintivo «disociada», la relación
queda en «—» y la columna dice «suprimida». La bitácora registra «RF-42 ·
Supresión con disociación — Ficha 1 disociada como ANON-0001 · totales de avance
sin variación», y la entrada anterior de RF-40 pasó a decir «Titular ANON-0001»
(capturas `2026-09-19_admin_rf42_bloqueo.png` y `2026-09-19_admin_rf42_disociada.png`).
**Salvedad:** los totales de Reportes son idénticos antes y después, pero en esa
sesión «Ejecución registrada» valía $0 (no había avances registrados) y la
Liquidación semanal sale del plan, no de los avances; por eso esta comprobación
no demuestra por sí sola que la disociación conserve los totales.
  Repetición del 21/09/2026: no fue posible ejecutar las consultas en la consola del navegador (error: Warning: Don’t paste code into the DevTools Console that you don’t understand or haven’t reviewed yourself. This could allow attackers to steal your identity or take control of your computer. Please type ‘allow pasting’ below and hit Enter to allow pasting.). La permanencia del nombre en el almacenamiento local se deduce de la lectura del código (`saveLabor()`, línea 63, y `suprimirFicha()`, línea 121) y no se verificó en el despliegue.

---

## 5. RF-22 · Alerta preventiva de fruta verde

Pendiente de clasificar. Determinar si ejecuta una comprobación real contra
el umbral de la variedad o si muestra contenido fijo, y actualizar su estado
en `05_MVP/readme.md` en consecuencia.

Lectura del código (no es una observación): `saveTicket()` (línea 135) compara
el «% fruta verde» del ticket con `db.settings.greenThreshold` (3 %, un umbral
**global**) y, si lo iguala o supera, crea la alerta «Alerta preventiva de fruta
verde» (Crítica). No usa un umbral por variedad. La tarjeta «Fruta verde
estimada» usa un valor fijo de 2,4 % cuando no hay lecturas de madurez
(`greenPct()`, línea 131).

Resultado observado:
Al guardar un ticket con 10 % de fruta verde, la pantalla Alertas mostró una
alerta de nivel «Advertencia» y estado «Abierta», y ninguna de nivel «Crítica» asociada al ticket (la única alerta «Crítica» visible es otra, «Pudrición del cogollo detectada»).
Por lectura del código, la causa es un defecto: `saveTicket()` (línea 135)
solicita el nivel «Crítica», pero `addAlert()` (línea 58) solo convierte a
«Crítica» el valor «Alta»; cualquier otro valor queda como «Advertencia». La
comparación con el umbral se ejecuta de verdad, pero el umbral es global (3 %) y
no por variedad. La tarjeta «Fruta verde estimada» usa un valor fijo de 2,4 %
cuando no hay lecturas de madurez.
Clasificación: funcional parcial.

---

## 6. Discrepancias encontradas

Toda diferencia entre lo que declara `05_MVP/readme.md` y lo observado se
anota aquí, aunque no estuviera prevista. No se omite ninguna.

| # | Qué declara el README | Qué se observó | Evidencia |
|---|---|---|---|
| 1 | «Control de acceso por rol: parcialmente implementado»: `navItems()` restringe una sola entrada, `Personal` (README, líneas 112 y 142) | `Personal` es solo para Administrador y `Reportes` solo para Supervisor y Administrador; el Operario no ve ni accede a Reportes, el Supervisor no accede a Personal | `2026-09-19_operario_menu.png`, `2026-09-19_operario_reportes.png`; `navItems()` línea 38 |
| 2 | RF-42: los totales por lote y período no cambian tras la supresión | Los totales no cambiaron, pero con «Ejecución registrada $0» la prueba no es concluyente | `2026-09-19_admin_rf42_totales.png` |
| 3 | RF-40: exportación de todos los datos que el sistema conserva | Correcta, pero el CSV se abre con tildes dañadas en Excel (falta la marca UTF-8) | `2026-09-19_operario_rf40_export.png` |
| 4 | RF-42 (README, línea 102): «sustituye el nombre por un identificador disociado (`ANON-000X`), vacía el contacto y reasigna los registros de avance a ese identificador» | Por lectura del código, el nombre suprimido permanece en `localStorage`, en el campo interno `registeredBy` de los avances, porque `suprimirFicha()` solo reasigna `worker`. No se pudo verificar en el despliegue. No se muestra en pantallas ni en la bitácora según las capturas del 19/09 | Lectura del código: `saveLabor()` línea 63 y `suprimirFicha()` líneas 115 a 129 |
| 5 | RF-22 (README, línea 83): «Pendiente de verificación en prueba E2E» | La alerta se genera con un umbral global (3 %), pero con nivel «Advertencia» por un defecto de `addAlert()`; no hay umbral por variedad; la tarjeta «Fruta verde estimada» usa 2,4 % fijo sin lecturas | `2026-09-21_admin_rf22_alertas.png` |

---

## 7. Veredicto

- [x] Ningún RF marcado como funcional resultó simulado (RF-22 se reclasifica como funcional parcial en el README)
- [x] El control de acceso por rol coincide con lo declarado (tras corregir el README en este mismo commit)
- [ ] Los tres flujos LOPDP cumplen sus criterios de aceptación (RF-40 y RF-41 cumplen; RF-42 tiene una posible limitación por verificar: ver discrepancia 4)
- [x] Todas las discrepancias encontradas quedaron documentadas

**Conclusión:**
RF-40 y RF-41 se comportan como declara el README. RF-42 rechaza la supresión con relación activa, sustituye el nombre por `ANON-000X` en pantalla y bitácora y conserva los totales; sin embargo, por lectura del código, el nombre suprimido permanece en el almacenamiento local (campo interno `registeredBy`), lo que no se pudo verificar en el despliegue; de confirmarse, la supresión sería parcial. RF-22 es funcional parcial: compara con un umbral global de 3 % y genera la alerta con nivel Advertencia por un defecto de `addAlert()`. El control de acceso por rol es más amplio que lo que declaraba el README (Personal y Reportes), que se corrige en este commit. La prueba se ejecutó sobre el despliegue y no se pudo verificar su correspondencia con el commit declarado.

---

## 8. Evidencia gráfica

| Archivo | Qué muestra |
|---|---|
| `2026-09-19_operario_menu.png` | Menú lateral como Operario |
| `2026-09-19_operario_reportes.png` | Reportes abierto con cuenta Operario |
| `2026-09-19_operario_rf40_export.png` | Exportación RF-40 y CSV descargado |
| `2026-09-19_admin_rf41_rectificar.png` | Formulario de rectificación completo |
| `2026-09-19_admin_rf41_bitacora.png` | Entrada de bitácora con valor anterior y motivo |
| `2026-09-19_admin_rf42_bloqueo.png` | Rechazo de supresión sobre ficha activa |
| `2026-09-19_admin_rf42_disociada.png` | Ficha como `ANON-0001` |
| `2026-09-19_admin_rf42_totales.png` | Totales de Reportes (Ejecución registrada $0) |
| `2026-09-21_admin_rf22_alertas.png` | Pantalla Alertas tras el ticket con 10 % de fruta verde (nivel Advertencia) |
