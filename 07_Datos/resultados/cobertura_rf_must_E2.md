# E2 — Cobertura de los RF Must en el prototipo

Prototipo analizado: `../../proto` · 14095 líneas en 106 archivos.

**RF con prioridad Must en el ERS: 24.**

| Categoría | RF | Qué sostiene |
|---|---:|---|
| EJERCITADO_EN_E1 | 5 | ejecutado con resultado observado y registrado |
| DECLARADO_EN_PANTALLA | 18 | el código lo rotula, pero nadie ha comprobado que funcione |
| SOLO_INDICIO | 1 | coincidencia de nombre, nada más |
| SIN_MENCION | 0 | no aparece en el código |

**Cifra reproducible:** 23 de 24 RF Must aparecen declarados en el rótulo de alguna pantalla del prototipo; de ellos, **5 han sido ejercitados** con resultado registrado en la prueba de extremo a extremo de E1. El resto no tiene comprobación de funcionamiento.

| RF | Nombre | Categoría | Pantalla | Evidencia |
|---|---|---|---|---|
| RF-01 | Autenticación y control de acceso por rol | EJERCITADO_EN_E1 |  | `05_MVP/evidencia_e2e/registro_prueba_e2e.md` |
| RF-02 | Gestión de plantaciones y lotes | DECLARADO_EN_PANTALLA | Plantaciones y lotes | `Prototipo/index.html:49; prototipo_v2/Prottoti` |
| RF-03 | Gestión de personal y equipos de trabajo | DECLARADO_EN_PANTALLA | Personal, equipos y cuentas | `Prototipo/index.html:149; prototipo_v2/Prottot` |
| RF-04 | Registro de labores agrícolas | DECLARADO_EN_PANTALLA | Labores y avance | `Prototipo/index.html:59; prototipo_v2/Prottoti` |
| RF-05 | Registro de monitoreo fitosanitario | SOLO_INDICIO |  | `Prototipo/index.html:55; Prototipo/index.html:` |
| RF-07 | Detección de plagas y enfermedades por análisi | DECLARADO_EN_PANTALLA | Análisis asistido por IA | `Prototipo/index.html:55; prototipo_v2/Prottoti` |
| RF-08 | Diagnóstico de deficiencias nutricionales por  | DECLARADO_EN_PANTALLA | Análisis asistido por IA | `Prototipo/index.html:55; prototipo_v2/Prottoti` |
| RF-10 | Gestión de variedades de palma | DECLARADO_EN_PANTALLA | Plantaciones y lotes | `Prototipo/index.html:49; prototipo_v2/Prottoti` |
| RF-12 | Generación de alertas tempranas | DECLARADO_EN_PANTALLA | Alertas tempranas | `Prototipo/index.html:145; prototipo_v2/Prottot` |
| RF-13 | Registro del proceso de polinización | DECLARADO_EN_PANTALLA | Labores y avance / Mapa GPS y po | `Prototipo/index.html:59; Prototipo/index.html:` |
| RF-14 | Conteo georreferenciado de flores polinizadas | DECLARADO_EN_PANTALLA | Mapa GPS y polinización | `Prototipo/index.html:69; prototipo_v2/Prottoti` |
| RF-18 | Estimación de producción y rendimiento | DECLARADO_EN_PANTALLA | Reportes, estimación e histórico | `Prototipo/index.html:137; prototipo_v2/Prottot` |
| RF-19 | Generación de reportes | DECLARADO_EN_PANTALLA | Reportes, estimación e histórico | `Prototipo/index.html:137; prototipo_v2/Prottot` |
| RF-21 | Clasificación de madurez del racimo por despre | DECLARADO_EN_PANTALLA | Análisis asistido por IA / Calid | `Prototipo/index.html:130; Prototipo/index.html` |
| RF-22 | Estimación y alerta preventiva de porcentaje d | EJERCITADO_EN_E1 | Calidad y relación con extractor | `Prototipo/index.html:130; Prototipo/index.html` |
| RF-26 | Planificación semanal de labores con presupues | DECLARADO_EN_PANTALLA | Labores y avance | `Prototipo/index.html:59; prototipo_v2/Prottoti` |
| RF-28 | Registro de avance por unidad de labor | DECLARADO_EN_PANTALLA | Labores y avance | `Prototipo/index.html:59; prototipo_v2/Prottoti` |
| RF-30 | Reporte de incidencia desde campo con evidenci | DECLARADO_EN_PANTALLA | Mapa GPS y polinización | `Prototipo/index.html:69; prototipo_v2/Prottoti` |
| RF-35 | Registro delegado para personal sin dispositiv | DECLARADO_EN_PANTALLA | Labores y avance / Personal, equ | `Prototipo/index.html:149; Prototipo/index.html` |
| RF-36 | Catálogo codificado de labores con tarifa por  | DECLARADO_EN_PANTALLA | Labores y avance | `Prototipo/index.html:59; prototipo_v2/Prottoti` |
| RF-37 | Liquidación semanal de presupuesto contra ejec | DECLARADO_EN_PANTALLA | Labores y avance | `Prototipo/index.html:59; prototipo_v2/Prottoti` |
| RF-40 | Exportación de los datos personales de la pers | EJERCITADO_EN_E1 |  | `05_MVP/evidencia_e2e/registro_prueba_e2e.md` |
| RF-41 | Rectificación de datos con conservación en bit | EJERCITADO_EN_E1 |  | `05_MVP/evidencia_e2e/registro_prueba_e2e.md` |
| RF-42 | Supresión de datos personales con disociación  | EJERCITADO_EN_E1 |  | `05_MVP/evidencia_e2e/registro_prueba_e2e.md` |
