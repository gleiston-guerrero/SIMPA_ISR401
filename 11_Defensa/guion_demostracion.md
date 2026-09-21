# Guion de demostración del prototipo — C13

**Duración objetivo: 5 minutos.** Expone Francisco.
**URL:** `https://simpa-v3-prototipo.netlify.app/` (V3, única versión vigente; ver `05_MVP/readme.md`)

---

## Antes de empezar

- Abrir la V3 **antes** de que empiece la defensa, con sesión cerrada.
- Tener el HTML autónomo descargado en local por si falla la red.
- **No usar ningún despliegue anterior** (`prototipo-simpa.netlify.app`, `simpav2-prototipo.netlify.app`, `prototipov2-correcion.netlify.app`): son versiones previas, sin los flujos de derechos LOPDP (RF-40 a RF-42).
- Navegador en pantalla completa, zoom al 100 %, sin pestañas personales
  visibles.

### Cuentas

| Usuario | Contraseña | Rol |
|---|---|---|
| `admin` | `admin123` | Administrador |
| `supervisor` | `super123` | Supervisor |
| `operario` | `oper123` | Operario |

---

## Secuencia

### 1 · Control de acceso por rol — 60 s

**Qué hacer:** entrar como `operario`, mostrar los módulos visibles. Cerrar
sesión. Entrar como `admin` y mostrar que aparecen módulos que el operario no
veía.

**Qué decir:** el control de acceso por rol cubre `RF-01` y es funcional, no
una maqueta. Hay tres perfiles y ocho módulos de navegación, uno restringido al
Administrador.

**Por qué se abre con esto:** demuestra en veinte segundos que hay lógica
real detrás, no pantallas enlazadas.

---

### 2 · Registro de labor agrícola — 60 s

**Qué hacer:** como `supervisor`, registrar una labor sobre un lote. Completar
el formulario y guardar. Mostrar que aparece en el listado.

**Qué decir:** cubre `RF-04`, y es el problema que abrió el proyecto: las
entrevistas recogieron que el registro se hacía en papel y no había
trazabilidad por trabajador. Este flujo es funcional.

**Enlace con la elicitación:** conviene nombrar que este requisito viene de
una entrevista concreta. Conecta el bloque 2 con el 5.

---

### 3 · Alertas tempranas — 45 s

**Qué hacer:** abrir el módulo de alertas y mostrar una alerta generada a
partir de umbrales.

**Qué decir:** cubre `RF-12`, funcional. Los umbrales se gestionan en
`RF-10`.

---

### 4 · Análisis de imagen — 60 s · **el momento delicado**

**Qué hacer:** abrir el flujo de detección de plagas por imagen y recorrerlo.

**Qué decir, sin rodeos:**

> Este flujo es **interfaz simulada**. `RF-07`, `RF-08` y la clasificación
> visual de `RF-21` están especificados y la interfaz existe, pero **no hay
> inferencia real**: no hay modelo entrenado ni conjunto de datos del dominio.
> Lo declaramos así en `05_MVP/readme.md` y en el ERS, y no reportamos ninguna
> métrica de exactitud porque no la tenemos.

**Esto no es una debilidad que se confiesa: es el criterio del proyecto.** El
docente valoró expresamente que el equipo distinga lo que funciona de lo que se
ve funcionar. Decirlo con naturalidad, sin disculparse.

**Lo que no se puede hacer:** dejar que el tribunal crea que analiza la imagen.

---

### 5 · Reportes y exportación — 45 s

**Qué hacer:** generar un reporte y exportarlo a CSV.

**Qué decir:** cubre `RF-19`, funcional con exportación real.

---

### 6 · Derechos sobre datos personales — 60 s

**Qué hacer:** mostrar los flujos de exportación, rectificación con bitácora y
supresión o disociación del histórico.

**Qué decir:** cubren `RF-40`, `RF-41` y `RF-42`, incorporados tras las
solicitudes de cambio formales aprobadas por el comité de control de cambios.
Responden a los derechos de la LOPDP, y su base legal está documentada en el
ERS.

**Por qué se cierra con esto:** es el flujo que mejor conecta el prototipo con
el trabajo normativo, y deja al tribunal con la idea de que el equipo pensó en
protección de datos, no solo en funcionalidad.

---

## Qué NO tocar

| Flujo | Motivo |
|---|---|
| GPS georreferenciado (`RF-14`) | Usa datos demostrativos, no consulta el receptor real. Mencionarlo solo si preguntan |
| Clasificación de madurez (`RF-21`) | Flujo demostrativo. Ya cubierto en el punto 4 |
| Estimación de producción (`RF-18`) | Cálculo demostrativo. No presentarlo como predicción |

Y **nunca** afirmar que hay backend, base de datos remota o persistencia más
allá de `localStorage`.

---

## Si algo falla en vivo

| Problema | Salida |
|---|---|
| No carga la web | Abrir el HTML autónomo local |
| Un flujo da error | Decirlo, seguir con el siguiente. **No insistir** |
| Se acaba el tiempo | Saltar al punto 6, que es el de mayor valor |

Un fallo reconocido y superado cuesta mucho menos que dos minutos de silencio
recargando la página.

---

## Nota de contexto para el equipo

El docente pidió expresamente que el prototipo se integre en el repositorio
principal, como submódulo de Git o publicando el código dentro, porque hoy vive
en `jmaciasherr4/Prottotipo_Simpa` y el árbol obligatorio lo sitúa en
`05_MVP/`. Si eso no llega a tiempo para la defensa, conviene decir en el
bloque 5 que se conoce la observación y cuál es el plan.

Hay además dos correcciones pendientes en ese repositorio que el tribunal
podría ver: falta el `LICENSE`, y una confirmación está firmada por
`SIMPA Dev <dev@simpa.local>`, una identidad no institucional.
