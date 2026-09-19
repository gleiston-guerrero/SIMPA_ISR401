# SIMPA — Sistema Inteligente de Mantenimiento de Palma Africana

Prototipo funcional de interfaz desarrollado para el proyecto grupal de Ingeniería de Requerimientos (ISR-401).

> **Estado actual:** prototipo académico frontend. La persistencia se realiza localmente en el navegador. No existe todavía un backend productivo, una base de datos remota, inferencia de IA validada ni geolocalización real.

## Repositorios

- Repositorio grupal y documentación: https://github.com/gleiston-guerrero/SIMPA_ISR401
- Repositorio del código del prototipo: https://github.com/jmaciasherr4/Prottotipo_Simpa
- Commit evaluado del prototipo (V2): `ba33002dcf680f8b39d42df04553733bd5389f6d` (2026-08-31)
- Commit al que apunta hoy el submódulo `05_MVP/prototipo/`: `deefe3d9da405ba8961a5d0d52936a85c7c5f428` (2026-09-04)

> El submódulo apunta a un commit posterior al evaluado. La diferencia entre ambos es verificable y no toca el árbol canónico: `git diff ba33002 deefe3d -- prototipo_v2/` no devuelve ninguna diferencia. Los únicos cambios entre los dos commits están en la raíz del repositorio del prototipo (`.mailmap`, `LICENSE` y una línea del `README.md`). Se mantiene el puntero actual y se declaran ambos commits para que la equivalencia sea comprobable.
- Árbol canónico evaluado de la V2: `prototipo_v2/Prottotipo_Simpa-main/Prototipo/`. La carpeta `Prototipo/` ubicada en la raíz del repositorio externo no corresponde al árbol utilizado para la evaluación de la V2.

## Ubicación del prototipo dentro de este repositorio

El código del prototipo está integrado como **submódulo git** en `05_MVP/prototipo/`. Al clonar este repositorio, esa carpeta aparece vacía hasta inicializar el submódulo:

```bash
git clone --recurse-submodules https://github.com/gleiston-guerrero/SIMPA_ISR401
# o, si ya clonaste sin esa opción:
git submodule update --init --recursive
```

Una vez inicializado, `05_MVP/prototipo/` refleja la raíz completa de `Prottotipo_Simpa`, que contiene **dos árboles**:

| Ruta dentro del submódulo | Árbol | ¿Es el evaluado? |
|---|---|---|
| `05_MVP/prototipo/prototipo_v2/Prottotipo_Simpa-main/Prototipo/` | V2 | ✅ Sí — este es el árbol canónico evaluado |
| `05_MVP/prototipo/Prototipo/` | V1 | ❌ No — versión anterior, no corresponde a la evaluación de la V2 |

**Para revisar el código evaluado, ir directamente a `05_MVP/prototipo/prototipo_v2/Prottotipo_Simpa-main/Prototipo/`.**

## Prototipo en vivo

### V2 — versión evaluada

https://prototipov2-correcion.netlify.app/

> Se publica una sola URL para que no haya ambigüedad sobre cuál es la versión evaluada. El código de la V1 permanece en el árbol `Prototipo/` del submódulo, sin despliegue de referencia.

### Cuentas de demostración

| Usuario | Contraseña | Rol |
|---|---|---|
| `admin` | `admin123` | Administrador |
| `supervisor` | `super123` | Supervisor |
| `operario` | `oper123` | Operario |

> Las cuentas son únicamente de demostración. No deben utilizarse para información real o sensible.

## Funcionalidades cubiertas por el prototipo V2

La V2 incorpora o refuerza los siguientes flujos:

| ID | Funcionalidad | Estado del prototipo |
|---|---|---|
| RF-01 | Autenticación y control de acceso por rol | ✅ Funcional |
| RF-02 | Gestión de plantaciones y lotes | ✅ Funcional |
| RF-03 | Gestión de personal y equipos | ✅ Funcional |
| RF-04 | Registro de labores agrícolas | ✅ Funcional |
| RF-05 | Registro de monitoreo fitosanitario | ✅ Funcional |
| RF-07 | Detección de plagas por imagen | ⚠️ Interfaz simulada |
| RF-08 | Diagnóstico nutricional por imagen | ⚠️ Interfaz simulada |
| RF-10 | Gestión de variedades y umbrales | ✅ Funcional |
| RF-12 | Generación de alertas tempranas | ✅ Funcional |
| RF-13 | Registro del proceso de polinización | ✅ Flujo incorporado |
| RF-14 | Conteo georreferenciado de flores | ⚠️ Datos GPS simulados |
| RF-18 | Estimación de producción | ✅ Cálculo demostrativo |
| RF-19 | Generación de reportes | ✅ Funcional / exportación CSV |
| RF-21 | Clasificación de madurez del racimo | ⚠️ Flujo demostrativo |
| RF-22 | Alerta preventiva de fruta verde | ✅ Flujo incorporado |
| RF-26 | Planificación semanal con presupuesto | ✅ Funcional |
| RF-28 | Registro de avance por unidad de labor | ✅ Funcional |
| RF-30 | Reporte de incidencia desde campo | ✅ Funcional |
| RF-35 | Registro delegado del avance | ✅ Funcional |
| RF-36 | Catálogo de tarifas por labor | ✅ Funcional |
| RF-37 | Cálculo de remuneración semanal | ✅ Funcional |
| RF-40 | Exportación de datos personales | ✅ Flujo incorporado |
| RF-41 | Rectificación con bitácora | ✅ Flujo incorporado |
| RF-42 | Supresión/disociación del histórico | ✅ Flujo incorporado |

## Limitaciones declaradas

**Análisis de imagen: resultado fijo, no inferencia.** `handleAnalyze` (`src/app/App.tsx`, líneas 296–302 del árbol V2) devuelve siempre el mismo objeto: condición «Deficiencia de Magnesio», confianza 87 %, severidad «Moderada» y la misma recomendación, tras un `setTimeout` de 2 500 ms que solo simula tiempo de procesamiento. El resultado no depende de la imagen capturada: no hay modelo ni inferencia. Esto afecta a RF-07, RF-08 y a la clasificación visual de RF-21.

**Calidad de cámara: valor aleatorio.** `handleCameraActivate` (línea 304 en adelante) calcula el indicador con `Math.min(q + 8 + Math.floor(Math.random() * 6), 92)` (línea 308). El porcentaje que se muestra en pantalla no mide la imagen real; es un número generado aleatoriamente.

**Credenciales fijas en el código.** Las tres cuentas de demostración están escritas en claro en `DEFAULT_ACCOUNTS` (líneas 58–61), con la contraseña en texto plano, y se persisten en `localStorage`. No hay hash ni backend de autenticación. RF-01 debe leerse con esa limitación.

**IA / análisis de imágenes.** RF-07, RF-08 y la clasificación visual relacionada con RF-21 se presentan como flujos de interfaz. La versión entregada no debe afirmar que realiza inferencia real o que cumple métricas de exactitud sin un modelo entrenado y un conjunto de datos del dominio.

**GPS.** RF-14 usa información demostrativa. La versión entregada no consulta necesariamente el receptor GPS real del dispositivo.

**Persistencia y seguridad.** La información del prototipo se almacena en `localStorage`. Esto permite probar los flujos sin servidor, pero no sustituye una arquitectura con API, base de datos, control de sesiones, cifrado, respaldo y auditoría de producción.

## Tecnologías

React · Vite · TypeScript/JavaScript · Tailwind CSS · Radix UI · Recharts · Lucide.

También se proporciona, en el árbol V1 del repositorio (`Prototipo/SIMPA_COMPLETO.html`), un archivo HTML independiente para demostración rápida sin instalar dependencias. Este archivo pertenece al árbol V1, no al árbol canónico V2 evaluado.

## Ejecución local del proyecto V2

```bash
git clone https://github.com/jmaciasherr4/Prottotipo_Simpa.git
cd Prottotipo_Simpa/prototipo_v2/Prottotipo_Simpa-main/Prototipo
npm install
npm run dev
```

Vite mostrará en la terminal la URL local, normalmente `http://localhost:5173`.

## Ejecución del HTML independiente (árbol V1)

Abre `Prototipo/SIMPA_COMPLETO.html` directamente en un navegador moderno. El archivo contiene HTML, CSS y JavaScript en un solo documento y guarda los registros de demostración en `localStorage`. Nota: este archivo corresponde al árbol V1 del prototipo; el árbol V2 evaluado no incluye una versión HTML independiente equivalente.

## Trabajo pendiente para una versión productiva

- Integrar backend y base de datos.
- Implementar autenticación segura y manejo de sesiones.
- Añadir servicio real de respaldo.
- Entrenar y validar modelos de IA con datos del cultivo.
- Integrar geolocalización real y permisos del dispositivo.
- Crear pruebas automatizadas y trazabilidad verificable entre requisitos, código y evidencias.
- Validar los RNF de rendimiento, seguridad, disponibilidad y recuperación sobre infraestructura real.
