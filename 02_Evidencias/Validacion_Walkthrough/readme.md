# Validación por walkthrough

**Estado: ejecutada.** Seis sesiones celebradas el 2026-09-03, con
participantes de perfil técnico y no técnico.

## Qué es una sesión de walkthrough en este proyecto

El participante interactúa con el prototipo sobre escenarios preseleccionados,
sin que el moderador le explique las pantallas de antemano. Lo que se observa es
qué comprende sin ayuda, dónde duda, qué etiquetas interpreta de otra manera y
qué información busca primero. Explicar la interfaz antes de la tarea destruiría
el dato que la sesión pretende recoger.

El prototipo evaluado en esa sesión fue la **V2**, que era el despliegue vigente en su fecha, en
`https://simpav2-prototipo.netlify.app/`, con las cuentas de demostración
documentadas en `05_MVP/readme.md`. Ese despliegue ya no es la versión entregada: la única URL vigente del prototipo es `https://simpa-v3-prototipo.netlify.app/`. Esta referencia se conserva porque describe la sesión tal como ocurrió; no se actualiza a la V3 porque eso falsearía sobre qué versión se hizo el walkthrough.

## Contenido de esta carpeta — zona pública

| Ruta | Contenido |
|---|---|
| `Acta/` | Seis actas de sesión, con la identidad de los participantes enmascarada. Las actas no llevan firma: la firma de cada sesión consta en su consentimiento (ver `Declaracion_Walkthrough_F3.md`) |
| `Consentimientos/` | Seis consentimientos informados con la firma enmascarada |
| `hallazgos_usabilidad.md` | Consolidado de los quince hallazgos, con el requisito afectado y la severidad propuesta |

Nomenclatura empleada:

```
AAAA-MM-DD_Walkthrough_<Perfil>_WT-XX_Acta.pdf
AAAA-MM-DD_Walkthrough_<Perfil>_WT-XX_Consentimiento.pdf
```

donde `<Perfil>` toma los valores `Tecnico` o `NoTecnico`.

## Dónde está el material original — zona restringida

**Ningún documento sin enmascarar ni ninguna grabación reside en este
repositorio.** El material identificable se publica cifrado como assets de
release en el repositorio complementario:

<https://github.com/erizzov-boop/SIMPA_ISR401_Evidencias>, release
`v1.0-evidencias`.

| Contenedor | Contenido |
|---|---|
| `Consentimientos_Walkthrough_Originales.7z` | Los seis consentimientos originales, con nombre y firma sin enmascarar |
| `evidencias_walkthrough_videos.7z` | Las seis grabaciones de pantalla de las sesiones |

Cada archivo de esos contenedores tiene su fila propia en
`../00_Restringido/fichas_tecnicas.csv`, con duración, códec, tamaño, SHA-256
calculado antes de cifrar, contenedor de origen y URL del release. La
verificación de que cada contenedor declarado existe consta en
`../00_Restringido/verificacion_fichas.md`.

La contraseña de descifrado se entrega únicamente al docente responsable por el
canal académico correspondiente.

## Códigos de participante

Las sesiones usan la serie **`WT-01` a `WT-06`**, independiente de la serie
`ENTR-XX` de las entrevistas semiestructuradas. Son dos estudios distintos, y
reutilizar los mismos códigos haría que un identificador designara a dos
personas diferentes según el archivo en que apareciera.

Cuando un participante de walkthrough fue también entrevistado, recibe
igualmente un código `WT-XX` propio. La correspondencia entre ambas series y la
identidad de cada participante se registra **únicamente en la zona
restringida**: publicarla aumentaría el riesgo de reidentificación, porque una
persona identificada por su rol en un estudio y por su perfil en el otro es más
fácil de reconocer que en cualquiera de los dos por separado.

## Distribución de la muestra

| Perfil | Códigos |
|---|---|
| Técnico | `WT-02`, `WT-03`, `WT-04` |
| No técnico | `WT-01`, `WT-05`, `WT-06` |

La clasificación se deriva de la experiencia manifestada con herramientas
digitales de gestión, no del cargo ni de la condición académica.

> **Reconciliación pendiente.** Aplicado con rigor, ese criterio no sostiene la
> distribución anterior: `WT-06` es estudiante de Ingeniería en Software y
> figura como no técnico, mientras `WT-02`, también estudiante de software,
> figura como técnico; y `WT-03` y `WT-04` declararon «Supervisor», que describe
> una función y no un nivel de familiaridad digital. La sección 5.2 de
> `hallazgos_usabilidad.md` desarrolla la limitación. Debe resolverse antes de
> reportar cualquier resultado por estrato.

## Autorización de grabación

La autorización de grabación de pantalla es una **casilla opcional e
independiente** de la de participación. Un participante puede aceptar la sesión
y rechazar la grabación; en ese caso no existe archivo de video para ese código
y el acta lo hace constar. La ausencia de grabación es una decisión registrada,
no un dato faltante.

## Limitaciones declaradas

Se recogen aquí en resumen y se desarrollan en la sección 5 de
`hallazgos_usabilidad.md`:

- **Conflicto de interés en `WT-02`**, que es integrante del equipo. Sus
  observaciones se conservan por transparencia pero no computan como validación
  externa independiente.
- **Desviación respecto del método** en varias sesiones, donde el moderador
  explicó módulos a petición del participante.
- **Profundidad desigual** entre sesiones: tres concentran prácticamente todos
  los hallazgos.

Estas limitaciones se declaran en lugar de omitirse, conforme al criterio que ha
guiado el proyecto.
