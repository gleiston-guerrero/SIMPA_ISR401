# Prueba de extremo a extremo por rol — E1

**Fecha de ejecución:**
**Ejecuta:** Macías Herrera Josthyn Esteban
**Entorno probado:** https://simpa-v3-prototipo.netlify.app/
**Commit del prototipo declarado en el repositorio:** `035470cb1dfd7be9557f1c5e2db24473cbcb8c02`
**Correspondencia entorno ↔ commit:** `[VERIFICADA | NO SE PUDO DETERMINAR]`

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

### Administrador (`admin` / `admin123`)

| Entrada de menú | ¿Visible? | ¿Accede? |
|---|---|---|
| Panel principal | | |
| Plantaciones y lotes | | |
| Análisis IA | | |
| Labores | | |
| Mapa GPS | | |
| Calidad / Extractora | | |
| Reportes | | |
| Alertas | | |
| Clima | | |
| Personal | | |

### Supervisor (`supervisor` / `super123`)

| Entrada de menú | ¿Visible? | ¿Accede? |
|---|---|---|
| Panel principal | | |
| Plantaciones y lotes | | |
| Análisis IA | | |
| Labores | | |
| Mapa GPS | | |
| Calidad / Extractora | | |
| Reportes | | |
| Alertas | | |
| Clima | | |
| Personal | | |

### Operario (`operario` / `oper123`)

| Entrada de menú | ¿Visible? | ¿Accede? |
|---|---|---|
| Panel principal | | |
| Plantaciones y lotes | | |
| Análisis IA | | |
| Labores | | |
| Mapa GPS | | |
| Calidad / Extractora | | |
| Reportes | | |
| Alertas | | |
| Clima | | |
| Personal | | |

**Hallazgo esperado según el código** (`navItems()`): solo `Personal` está
restringida a Administrador. Reportes, Calidad / Extractora y Clima deberían
quedar accesibles para Operario. Confirmar o refutar.

Resultado observado:

---

## 2. RF-40 · Exportación de datos personales

Como **Operario**, ir a `Mapa GPS` → sección *Privacidad* → «Mis datos
personales · RF-40» → pulsar «Exportar mis datos (CSV)».

Abrir el CSV descargado y transcribir su contenido:

```
[pegar el contenido del CSV]
```

**Comprobar:**

- [ ] Los datos corresponden a la ficha del titular autenticado, no a otra persona
- [ ] Incluye identificación, contacto, vinculación laboral y avance registrado
- [ ] La solicitud quedó asentada en la bitácora con fecha y hora

Repetir como **Administrador**: al no tener ficha de personal asociada, debe
indicar que no hay datos de trabajador que exportar, en lugar de descargar
datos ajenos.

Resultado observado:

---

## 3. RF-41 · Rectificación con bitácora

Como **Administrador**, en `Personal` → botón «Rectificar» de una ficha.

1. Dejar el motivo vacío y pulsar Guardar: debe rechazarlo.
2. Completar campo, valor nuevo y motivo, y guardar.
3. Revisar la bitácora al pie de la misma pantalla.

**Comprobar:**

- [ ] Sin motivo no guarda
- [ ] El dato queda corregido en la ficha
- [ ] La bitácora registra valor anterior, fecha, autor y motivo
- [ ] No existe ninguna función en la interfaz para borrar o editar entradas

Intentar la misma acción como **Operario**: debe rechazarse por rol.

Resultado observado:

---

## 4. RF-42 · Supresión con disociación

Como **Administrador**, en `Personal`.

1. Con la relación en *Activa*, pulsar «Suprimir»: debe rechazarlo indicando
   que RF-42 exige relación terminada.
2. Pulsar el distintivo de la columna «Relación» para pasarla a *Terminada*.
3. **Antes de suprimir**, anotar los totales de la pantalla `Reportes`:

```
[totales por lote antes de la supresión]
```

4. Ejecutar «Suprimir» y confirmar.
5. Volver a `Reportes` y anotar los totales:

```
[totales por lote después de la supresión]
```

**Comprobar:**

- [ ] El intento sobre ficha activa se rechaza
- [ ] Tras suprimir, la ficha aparece como `ANON-000X` con el distintivo «disociada»
- [ ] El contacto quedó vacío
- [ ] **Los totales por lote y período son idénticos antes y después**
- [ ] Ninguna pantalla ni exportación devuelve el nombre suprimido
- [ ] Las entradas de bitácora previas se conservan, con el identificador disociado

Resultado observado:

---

## 5. RF-22 · Alerta preventiva de fruta verde

Pendiente de clasificar. Determinar si ejecuta una comprobación real contra
el umbral de la variedad o si muestra contenido fijo, y actualizar su estado
en `05_MVP/readme.md` en consecuencia.

Resultado observado:

---

## 6. Discrepancias encontradas

Toda diferencia entre lo que declara `05_MVP/readme.md` y lo observado se
anota aquí, aunque no estuviera prevista. No se omite ninguna.

| # | Qué declara el README | Qué se observó | Evidencia |
|---|---|---|---|
| 1 | | | |

---

## 7. Veredicto

- [ ] Ningún RF marcado como funcional resultó simulado
- [ ] El control de acceso por rol coincide con lo declarado
- [ ] Los tres flujos LOPDP cumplen sus criterios de aceptación
- [ ] Todas las discrepancias encontradas quedaron documentadas

**Conclusión:**

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
| `2026-09-19_admin_rf42_totales.png` | Totales de Reportes antes y después |
