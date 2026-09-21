# Inventario de fuentes editables — AUT-03

Relaciona cada diagrama o mockup usado como evidencia con su fuente
editable real, su exportación publicada, y el estado verificado de esa
correspondencia. Verificado directamente contra el contenido del
repositorio, no declarado de memoria.

## Diagramas UML

Los 13 diagramas UML tienen fuente en texto plano PlantUML (`.puml`),
editable en cualquier editor de texto, con dos exportaciones cada uno.

| Diagrama | Fuente editable | Exportación | Ubicación | Estado |
|---|---|---|---|---|
| Casos de uso general | `01_use_cases_general.puml` | `png/use_cases_general.png`, `svg/use_cases_general.svg` | `03_Modelado/Diagramas_UML/` | Completo |
| Clases refinadas | `02_classes_refined.puml` | `png/classes_refined.png`, `svg/classes_refined.svg` | `03_Modelado/Diagramas_UML/` | Completo |
| Secuencia CU01 — analizar imagen | `03_sequence_CU01_analyze_image.puml` | `png/sequence_CU01.png`, `svg/sequence_CU01.svg` | `03_Modelado/Diagramas_UML/` | Completo |
| Secuencia CU03 — polinización GPS | `04_sequence_CU03_pollination_gps.puml` | `png/sequence_CU03.png`, `svg/sequence_CU03.svg` | `03_Modelado/Diagramas_UML/` | Completo |
| Secuencia CU06 — clasificar madurez | `05_sequence_CU06_classify_maturity.puml` | `png/sequence_CU06.png`, `svg/sequence_CU06.svg` | `03_Modelado/Diagramas_UML/` | Completo |
| Actividad — ciclo semanal | `06_activity_weekly_cycle.puml` | `png/activity_weekly_cycle.png`, `svg/activity_weekly_cycle.svg` | `03_Modelado/Diagramas_UML/` | Completo |
| Estados — racimo | `07_states_bunch.puml` | `png/states_bunch.png`, `svg/states_bunch.svg` | `03_Modelado/Diagramas_UML/` | Completo |
| Estados — alerta | `08_states_alert.puml` | `png/states_alert.png`, `svg/states_alert.svg` | `03_Modelado/Diagramas_UML/` | Completo |
| Componentes | `09_components.puml` | `png/components.png`, `svg/components.svg` | `03_Modelado/Diagramas_UML/` | Completo |
| Despliegue | `10_deployment.puml` | `png/deployment.png`, `svg/deployment.svg` | `03_Modelado/Diagramas_UML/` | Completo |
| Contexto | `11_context.puml` | `png/context.png`, `svg/context.svg` | `03_Modelado/Diagramas_UML/` | Completo |
| i* SD | `12_istar_sd.puml` | `png/istar_sd.png`, `svg/istar_sd.svg` | `03_Modelado/Diagramas_UML/` | Completo |
| i* SR | `13_istar_sr_1.puml` | `png/istar_sr.png`, `svg/istar_sr.svg` | `03_Modelado/Diagramas_UML/` | Completo |

**Verificación:** los `.puml` son texto plano; se pueden regenerar los `.png`/`.svg`
con PlantUML (`plantuml archivo.puml`) y comparar contra el archivo publicado.

## Mockups de interfaz

Las 8 capturas de interfaz (`Interfaz_*.jpeg`) provienen de un diseño hecho
en Figma Make, cuya fuente editable y código exportado sí están versionados.

| Elemento | Fuente editable | Exportación | Ubicación | Estado |
|---|---|---|---|---|
| 8 pantallas de interfaz (Login, Panel principal, Registro de labor, Detalle de lote, Mapa GPS, Alertas, Reportes, Analizar imagen) | `SIMPA_App_Interfaces_Design.make` (proyecto Figma Make) y su código fuente exportado en `SIMPA_mockups_codigo/` (React + TypeScript + Tailwind) | 8 archivos `.jpeg` | `03_Modelado/Mockups/` | Completo |

**Verificación:** `SIMPA_mockups_codigo/` contiene `package.json`, componentes
`.tsx` y estilos; es un proyecto ejecutable, no una imagen estática.

## Prototipo funcional

| Elemento | Fuente editable | Exportación | Ubicación | Estado |
|---|---|---|---|---|
| Prototipo V2 | Repositorio de código completo: `https://github.com/jmaciasherr4/Prottotipo_Simpa`, integrado como submódulo Git en el commit `deefe3d` | Desplegado entonces en `https://simpav2-prototipo.netlify.app/` (despliegue histórico; la URL vigente del prototipo es `https://simpa-v3-prototipo.netlify.app/`) | `05_MVP/prototipo` (submódulo) | Completo — repositorio verificado como público y accesible |

## Diagramas o gráficas sin fuente editable declarada

No se incluyen en este inventario porque no son diagramas de arquitectura o
interfaz sujetos a esta exigencia, sino salidas de análisis de datos
generadas por script (reproducibles desde `07_Datos/`, no desde una fuente
"editable" en el sentido de diseño):

- `07_Datos/resultados/curva_saturacion_agregada.png`
- `07_Datos/resultados/curva_saturacion_contraste.png`
- `07_Datos/resultados/curva_saturacion_dominio.png`
- `02_Evidencias/Codificacion_Tematica/curva_saturacion.png`

Su reproducibilidad se acredita por la cadena de scripts de `07_Datos/`, no
por este inventario.

**Nota de reproducibilidad:** al clonar el repositorio principal, el contenido de este submódulo no se descarga automáticamente. Requiere ejecutar `git submodule update --init --recursive` para materializarse localmente.
