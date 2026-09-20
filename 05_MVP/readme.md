# SIMPA — Sistema Inteligente de Mantenimiento de Palma Africana

Prototipo funcional de interfaz desarrollado para el proyecto grupal de Ingeniería de Requerimientos (ISR-401).

> **Estado actual:** prototipo académico frontend. La persistencia se realiza localmente en el navegador. No existe todavía un backend productivo, una base de datos remota, inferencia de IA validada ni geolocalización real.

## Repositorios

- Repositorio grupal y documentación: https://github.com/gleiston-guerrero/SIMPA_ISR401
- Repositorio del código del prototipo: https://github.com/jmaciasherr4/Prottotipo_Simpa
- Commit evaluado del prototipo (V2): `ba33002dcf680f8b39d42df04553733bd5389f6d` (2026-08-31)
- Commit al que apunta hoy el submódulo `05_MVP/prototipo/`: `035470cb1dfd7be9557f1c5e2db24473cbcb8c02` (2026-09-19)

> El submódulo apunta a un commit posterior al evaluado el 31/08/2026. La diferencia es real y está declarada: el árbol incorpora los flujos de derechos LOPDP (RF-40, RF-41 y RF-42) descritos más abajo, ausentes en el commit evaluado. Ambos commits se declaran para que el avance sea verificable con `git diff ba33002 035470c -- prototipo_v2/`.

## Qué código se entrega realmente

El submódulo contiene **dos aplicaciones distintas**, y conviene no confundirlas:

| Ruta dentro del submódulo | Qué es | ¿Se entrega? |
|---|---|---|
| `prototipo_v2/Prottotipo_Simpa-main/Prototipo/index.html` | Aplicación autónoma en un solo archivo (HTML + CSS + JavaScript) | ✅ **Sí — es lo que se publica y se evalúa** |
| `Prototipo/index.html` | El mismo archivo autónomo, en el árbol anterior | Equivalente al anterior |
| `src/app/App.tsx` (en ambos árboles) | Aplicación escrita en React sobre Vite | ❌ No — permanece en el repositorio pero no es lo desplegado |

Los dos `index.html` son **binariamente idénticos** (SHA-256 `2859dbb9185e2b5ed02601f9348cffdfa44651e3bc1140f1647b789b43af94d0`): un mismo archivo presente en dos rutas. Como Vite toma `index.html` como punto de entrada, el despliegue sirve esa aplicación autónoma y no el árbol React.

Ambas aplicaciones difieren en estructura de menú y en funcionalidades, de modo que **toda declaración de este documento se refiere al archivo autónomo**, salvo que se indique expresamente lo contrario. El árbol React se conserva por trazabilidad histórica —es el que existía en el commit evaluado del 31/08/2026— pero no recibe mantenimiento ni incorpora los flujos LOPDP.

## Ubicación del prototipo dentro de este repositorio

El código del prototipo está integrado como **submódulo git** en `05_MVP/prototipo/`. Al clonar este repositorio, esa carpeta aparece vacía hasta inicializar el submódulo:

```bash
git clone --recurse-submodules https://github.com/gleiston-guerrero/SIMPA_ISR401
# o, si ya clonaste sin esa opción:
git submodule update --init --recursive
```

## Prototipo en vivo

### Versión vigente

https://simpa-v3-prototipo.netlify.app/

> Esta es la única URL que debe usarse para evaluar el prototipo. Es la que
> incorpora los flujos de derechos LOPDP (RF-40, RF-41 y RF-42) descritos más
> abajo.
>
> Existieron despliegues anteriores en `prototipo-simpa.netlify.app` y
> `prototipov2-correcion.netlify.app`, correspondientes a versiones previas sin
> esos flujos. Si siguen accesibles, no deben tomarse como la versión
> entregada.

### Cuentas de demostración

| Usuario | Contraseña | Rol |
|---|---|---|
| `admin` | `admin123` | Administrador |
| `supervisor` | `super123` | Supervisor |
| `operario` | `oper123` | Operario |

> Las cuentas son únicamente de demostración. No deben utilizarse para información real o sensible.

## Funcionalidades cubiertas por el prototipo

| ID | Funcionalidad | Estado del prototipo |
|---|---|---|
| RF-01 | Autenticación y control de acceso por rol | ⚠️ Autenticación funcional; autorización parcial |
| RF-02 | Gestión de plantaciones y lotes | ✅ Funcional |
| RF-03 | Gestión de personal y equipos | ✅ Funcional |
| RF-04 | Registro de labores agrícolas | ✅ Funcional |
| RF-05 | Registro de monitoreo fitosanitario | ✅ Funcional |
| RF-07 | Detección de plagas por imagen | ⚠️ Interfaz simulada |
| RF-08 | Diagnóstico nutricional por imagen | ⚠️ Interfaz simulada |
| RF-10 | Gestión de variedades y umbrales | ✅ Funcional |
| RF-12 | Generación de alertas tempranas | ✅ Funcional |
| RF-13 | Registro del proceso de polinización | ✅ Funcional como tipo de labor registrable |
| RF-14 | Conteo georreferenciado de flores | ⚠️ Datos GPS simulados |
| RF-18 | Estimación de producción | ✅ Cálculo demostrativo |
| RF-19 | Generación de reportes | ✅ Funcional / exportación CSV |
| RF-21 | Clasificación de madurez del racimo | ⚠️ Flujo demostrativo |
| RF-22 | Alerta preventiva de fruta verde | ⚠️ Pendiente de verificación en prueba E2E |
| RF-26 | Planificación semanal con presupuesto | ✅ Funcional |
| RF-28 | Registro de avance por unidad de labor | ✅ Funcional |
| RF-30 | Reporte de incidencia desde campo | ✅ Funcional |
| RF-35 | Registro delegado del avance | ✅ Funcional |
| RF-36 | Catálogo de tarifas por labor | ✅ Funcional |
| RF-37 | Cálculo de remuneración semanal | ✅ Funcional |
| RF-40 | Exportación de datos personales | ✅ Implementado |
| RF-41 | Rectificación con bitácora | ✅ Implementado |
| RF-42 | Supresión/disociación del histórico | ✅ Implementado |

## Derechos LOPDP (RF-40, RF-41, RF-42)

Los tres flujos están implementados sobre la bitácora `db.audit`, que ya existía para el consentimiento de geolocalización.

**RF-40 — Exportación de datos personales.** Accesible por la propia persona titular, sin intermediación de la administración, en `Mapa GPS → Privacidad`. Genera un CSV con la totalidad de los datos que el sistema conserva sobre ella: identificación, contacto, vinculación laboral (equipo, lote, dispositivo, estado de la relación), consentimiento de geolocalización y la totalidad de sus registros de avance. La solicitud queda asentada en la bitácora con marca temporal. Las cuentas sin ficha de personal asociada no obtienen exportación: se les indica expresamente que no hay datos de trabajador que entregar.

**RF-41 — Rectificación con bitácora.** En `Personal`, reservada a Administrador. Recibe el campo a corregir, el valor nuevo y el motivo; el motivo es obligatorio y sin él no se guarda. La bitácora registra valor anterior, fecha, autor y motivo declarado. Si se rectifica un nombre, el cambio se propaga a los registros de avance y al consentimiento para no romper la trazabilidad. **La interfaz no ofrece ninguna función para eliminar ni editar entradas de bitácora**, conforme al criterio de aceptación del requisito.

**RF-42 — Supresión con disociación.** En `Personal`, reservada a Administrador. Exige como precondición que la relación laboral conste como *Terminada*; el intento sobre una ficha activa se rechaza. Al ejecutarse sustituye el nombre por un identificador disociado (`ANON-000X`), vacía el contacto y reasigna los registros de avance a ese identificador, de modo que los totales por lote y período permanecen idénticos. La operación compara los totales antes y después y deja constancia del resultado en la bitácora.

**Decisión de diseño declarada.** RF-41 exige conservar el valor anterior de forma indefinida y RF-42 exige que ninguna consulta devuelva el nombre suprimido. Ambos requisitos entran en tensión cuando se suprime a una persona cuyo nombre figura en entradas previas de bitácora. La implementación resuelve la tensión **sin borrar entradas**: sustituye el identificador dentro de ellas por el identificador disociado. La entrada se conserva íntegra y la identidad queda disociada.

## Limitaciones declaradas

**Análisis de imagen: resultado fijo por tipo, no inferencia.** `runAnalysis()` devuelve un objeto predeterminado según el tipo de análisis seleccionado: para «plaga» siempre «Posible Rhynchophorus palmarum» con 89 % de confianza y severidad «Alta». El resultado no depende de la imagen cargada; no hay modelo ni inferencia. La interfaz lo rotula explícitamente como «⚠ IA de demo» y «resultado de demostración». Afecta a RF-07, RF-08, RF-09 y RF-21.

**Credenciales en el código.** Las tres cuentas de demostración están escritas en claro en el objeto `defaults.accounts`, con la contraseña en texto plano, y se persisten en `localStorage` bajo la clave `simpa_v4`. No hay hash ni backend de autenticación. RF-01 se cumple en cuanto a autenticación, no en cuanto a gestión segura de credenciales.

**Control de acceso por rol: parcialmente implementado.** `navItems()` restringe una sola entrada de navegación, `Personal`, reservada a Administrador mediante `isAdmin()`. Las demás pantallas no declaran restricción, por lo que la cuenta Operario accede a Reportes, Calidad / Extractora, Clima y el resto del menú. Dentro de `Personal`, las acciones de rectificación (RF-41), supresión (RF-42) y cambio de estado de la relación laboral sí comprueban el rol antes de ejecutarse. RF-01 debe leerse con esa limitación: hay autenticación, pero la autorización diferenciada es parcial.

**GPS.** RF-14 usa información demostrativa. La versión entregada no consulta necesariamente el receptor GPS real del dispositivo.

**Persistencia y seguridad.** La información del prototipo se almacena en `localStorage`, en el navegador de cada persona. Esto permite probar los flujos sin servidor, pero no sustituye una arquitectura con API, base de datos, control de sesiones, cifrado, respaldo y auditoría de producción. En consecuencia, la bitácora de RF-41 es local a cada navegador y no constituye un registro de auditoría centralizado.

**Correspondencia entre el repositorio y el despliegue.** El despliegue de Netlify se publica manualmente y no está enlazado a este repositorio, por lo que puede no corresponder exactamente al archivo versionado. Cualquier verificación que exija equivalencia estricta debe hacerse sobre el archivo del repositorio, no sobre la URL.

## Tecnologías

El archivo entregado es HTML, CSS y JavaScript sin dependencias ni proceso de compilación: se abre directamente en el navegador.

El árbol React que permanece en el submódulo, no desplegado, utiliza React · Vite · TypeScript · Tailwind CSS · Radix UI · Recharts · Lucide.

## Ejecución local

Abrir `prototipo_v2/Prottotipo_Simpa-main/Prototipo/index.html` directamente en un navegador moderno. No requiere instalar nada ni ejecutar ningún comando.

Para ejecutar el árbol React, no desplegado:

```bash
cd prototipo_v2/Prottotipo_Simpa-main/Prototipo
npm install
npm run dev
```

## Trabajo pendiente para una versión productiva

- Integrar backend y base de datos.
- Implementar autenticación segura y manejo de sesiones.
- Extender la comprobación de rol al resto de pantallas, no solo a `Personal`.
- Trasladar la bitácora a un registro de auditoría centralizado e inmutable.
- Añadir servicio real de respaldo.
- Entrenar y validar modelos de IA con datos del cultivo.
- Integrar geolocalización real y permisos del dispositivo.
- Crear pruebas automatizadas y trazabilidad verificable entre requisitos, código y evidencias.
- Validar los RNF de rendimiento, seguridad, disponibilidad y recuperación sobre infraestructura real.
- Enlazar el despliegue al repositorio para que ambos no puedan divergir.
