# Auditoría de cierre — §15 Evidencia de autoría

Fecha de verificación: 2026-09-15
Responsable: Jhostyn Macías

## Resultado

| Elemento | Estado |
|---|---|
| Correspondencia/acta firmada | OK — acta firmada por responsable de Palmicultora M incorporada 2026-09-16 |
| Capturas Allan | OK (3) |
| Capturas Denisses | OK (5) |
| Capturas Edson | OK (4) |
| Capturas Jhostyn | OK (3) |
| Capturas Francisco | OK (3) |
| Capturas Alcívar | OK (3) — correcciones del 17–18/09/2026, ver actualizaciones abajo |
| 30 sesiones de bitácora | OK — 26 NO_APLICA + 4 con nota real |
| Notas de campo | NO VERIFICADO — los 16 PDF se rotulan como material no contemporáneo; ver `10_Autoria/notas_campo/readme.md` y la tarea F1 |

## Conclusión

Con la incorporación del acta firmada por el responsable de la Palmicultora M
el 2026-09-16 se completó el último elemento pendiente de §15 según la
verificación interna de esa fecha. Esta conclusión es anterior a la evaluación
oficial del 17/09/2026; ver las actualizaciones posteriores al final de este
documento.

## Actualización — 2026-09-17

La evaluación oficial del docente (17/09/2026) señaló que las tres capturas
de Alcívar subidas el 15/09 (listado de GitHub e inventario EXIF) no
mostraban un artefacto propio identificable, y calificó ese elemento como
"Por modificar".

Se sustituyeron por tres capturas nuevas, cada una mostrando el historial
de Git (`git log`) de un archivo real escrito por Alcívar antes de su
retiro del proyecto activo: `11_Defensa/guion_defensa.md`,
`11_Defensa/guion_demostracion.md`, y el script de verificación de fichas
técnicas. Verificadas visualmente el 17/09/2026 por Josthyn Macías,
cumpliendo terminal, archivo real, usuario del sistema visibles.

Su aceptación final queda sujeta a la revisión del docente en la próxima
evaluación del repositorio.

## Segunda actualización — 2026-09-18, posterior a la evaluación de las 17:50

La primera corrección fue incompleta. La evaluación del docente verificó que
una de las tres capturas depositadas, `2026-09-17_AdonisAlcivar_scriptVerificarFichas.png`,
no se tomó en el equipo de Alcívar: el símbolo del sistema mostraba
`Admin@ELPROPIO` y la ruta `/c/Users/Admin/SIMPA_ISR401`, correspondientes al
equipo de Macías Herrera, y la añadió él en `7d022dd`. La verificación visual
declarada más arriba no detectó ese detalle. Se deja constancia del error de
verificación en vez de corregirlo en silencio.

### Operaciones realizadas sobre esta evidencia

| # | Commit | Fecha | Autor | Operación |
|---|---|---|---|---|
| 1 | `7d022dd` | 17/09 | Macías Herrera | Añade `..._scriptVerificarFichas.png`, tomada en su propio equipo. Cuestionada por el docente. |
| 2 | `32a8e7f` | 17/09 18:13 | Alcívar Vélez | Deposita `..._scriptGenerarFichas.png`, tomada en su equipo (`Usuario@DESKTOP-4PFJJQ5`). |
| 3 | `5a787f2` | 17/09 18:14 | Macías Herrera | Retira la captura cuestionada. |
| 4 | `d0b32f2` | 17/09 23:27 | Alcívar Vélez | Renombra a `..._scriptVerificarFichas.png`. |
| 5 | cierre posterior | 18/09 | Huilcapi León Denisses Fabiola | Renombra a `..._gitlog_verificar_fichas.png` para evitar colisión histórica y describir el contenido real; no modifica el contenido de la captura. |

### Por qué el nombre final es distinto

La operación 4 devolvió al árbol el nombre exacto de la captura retirada,
aplicado a un archivo distinto. Eso hacía coincidir en el historial dos objetos
diferentes bajo un mismo nombre —uno cuestionado por autoría y otro válido— y
provocó que `sha256sum -c checksums.sha256` reportara un hash no coincidente
sobre esa ruta.

El nombre `scriptGenerarFichas` de la operación 2 tampoco era correcto: la
imagen muestra `git log` sobre `verificar_fichas.py`, y el repositorio contiene
también `generar_fichas.py`. El nombre definitivo no colisiona con el de la
evidencia retirada y describe el contenido mostrado.

La captura que figura actualmente en el árbol no es la que el docente
cuestionó, aunque llegó a utilizar temporalmente el mismo nombre.

### Estado de las tres capturas de Alcívar

Verificadas visualmente y contrastadas contra `git log --follow`:

| Captura | Artefacto | Commit de autoría | Equipo |
|---|---|---|---|
| `..._guion_defensa.png` | `11_Defensa/guion_defensa.md` | `07deee4` AdonisAlcivar 04/09 | `Usuario@DESKTOP-4PFJJQ5` |
| `..._guion_demostracion.png` | `11_Defensa/guion_demostracion.md` | `27a108b` AdonisAlcivar 04/09 | `Usuario@DESKTOP-4PFJJQ5` |
| `..._gitlog_verificar_fichas.png` | `07_Datos/scripts/verificar_fichas.py` | `25635ac` AdonisAlcivar 04/09 | `Usuario@DESKTOP-4PFJJQ5` |

Las tres acreditan autoría pasada mediante `git log`, no trabajo en curso.
El equipo deja constancia de esa limitación en vez de presentarlas como
evidencia de trabajo activo durante el examen suspenso. La aceptación final
del ítem corresponde al docente.
