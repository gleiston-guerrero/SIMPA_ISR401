# Desviación metodológica — Diseño de análisis del experimento humano–LLM
## 06_Experimento/osf_deviations.md

**Proyecto:** SIMPA — Equipo AHMRV — ISR-401 — UTEQ
**Responsable de esta declaración:** Denisses Huilcapi
**Verificador:** Allan Villafuerte
**Fecha de registro de este documento:** 11/09/2026

---

## 1. Cambio declarado

| | Protocolo original (registrado en OSF, https://osf.io/4z35d/) | Diseño actualmente aplicable |
|---|---|---|
| Diseño | Cuasi-experimento con medidas apareadas y evaluación a ciegas (`06_Experimento/protocolo.tex`, línea 66) | Grupos independientes, no apareados |
| Análisis principal | Prueba $t$ apareada bilateral (o Wilcoxon con signo si no hay normalidad), corrección de Holm-Bonferroni | Modelo mixto de vínculo acumulativo para respuesta ordinal, un modelo por cada una de las cinco dimensiones: `puntuación_1-5 ~ origen + (1 | evaluador) + (1 | requisito)`, con `origen` como efecto fijo y `evaluador`/`requisito` como interceptos aleatorios cruzados. Enlace logístico de probabilidades proporcionales, salvo razón metodológica preespecificada para otro enlace. Implementación prevista: paquete `ordinal` de R (versión exacta a registrar en el momento de la ejecución) |
| Análisis de reserva | — | Si el modelo mixto no converge: U de Mann-Whitney sobre la mediana por requisito entre evaluadoras, con $\delta$ de Cliff e IC 95 % como tamaño del efecto |
| Acuerdo entre evaluadoras (RQ2) | $\kappa$ de Cohen (por pares) y $\kappa$ de Fleiss (conjunto) | $\alpha$ de Krippendorff con métrica ordinal como medida principal; $\kappa$ ponderado cuadrático por pares como medida secundaria. Se descarta $\kappa$ nominal de Cohen/Fleiss porque, en una escala ordinal de 1 a 5, penaliza igual un desacuerdo de un punto que uno de cuatro |

## 2. Motivo del cambio

El protocolo prerregistrado prevé contrastes apareados sobre veinticinco
pares. Al revisar el diseño antes de recoger puntuación alguna, se detectó
que no existe correspondencia uno a uno entre cada requisito humano y uno
generado por el LLM: ambos conjuntos proceden del mismo material fuente
(`ENTR-04`), pero no describen necesariamente las mismas funciones, de modo
que el emparejamiento carece de fundamento y el contraste apareado sería
inválido. Construir esa correspondencia a mano introduciría un juicio
subjetivo del propio equipo investigador, lo que comprometería la validez
de constructo del estudio.

Por esa razón se declara la siguiente desviación, sometida como adenda
prospectiva al registro **antes de recoger ninguna puntuación**:

1. Los dos conjuntos se tratan como grupos independientes, no apareados.
2. El análisis principal pasa a un modelo mixto ordinal (ver Sección 1),
   que respeta la naturaleza ordinal de la escala de cinco puntos y la
   estructura de evaluaciones repetidas (los mismos tres evaluadores
   puntúan ambos conjuntos) — algo que un contraste sobre medias no
   captura correctamente.
3. Como consecuencia directa del cambio de escala de análisis, el
   coeficiente de acuerdo entre evaluadoras también cambia: de $\kappa$
   nominal a $\alpha$ de Krippendorff ordinal, por la misma razón de fondo
   (una métrica nominal no distingue la gravedad de un desacuerdo en una
   escala ordinal).

Ninguna de estas tres decisiones se tomará ni se revisará en función de los
datos observados.

## 3. Fecha en que se detectó

El indicio más temprano verificable en el repositorio es el commit
`2a5412b` ("Incorporar manuscrito científico"), del **1 de septiembre de
2026, 16:54:14 (-05:00)**, autoría de Denisses Huilcapi — es el primer
commit que incorpora este razonamiento por escrito, en la sección 6.1 del
manuscrito. Si el equipo identificó el problema antes en una conversación
no versionada, esa fecha anterior no cuenta con evidencia documental
verificable, por lo que esta declaración usa el 1 de septiembre de 2026
como fecha de detección formal.

El protocolo original con diseño apareado se había cerrado y registrado
públicamente en OSF apenas el día anterior (commit `8bc6bde`, 31 de agosto
de 2026, "Cerrar P8 con registro publico OSF del protocolo experimental").
El experimento sigue sin ejecutarse a la fecha de este documento
(`06_Experimento/readme.md`: *"Protocolo diseñado y registrado
públicamente en OSF. Experimento no ejecutado."*), de modo que la
desviación queda declarada con margen amplio respecto de cualquier
recolección real de puntuaciones.

## 4. Impacto en el análisis planeado

- **Prueba estadística original prevista:** prueba $t$ apareada bilateral
  (o Wilcoxon de rangos con signo si no hay normalidad), con corrección de
  Holm-Bonferroni sobre los cinco valores $p$ (`protocolo.tex`, sección de
  plan de análisis).
- **Prueba estadística ahora aplicable:** modelo mixto ordinal (Sección 1),
  con la prueba U de Mann-Whitney + $\delta$ de Cliff como análisis de
  reserva si el modelo no converge.
- **Corrección por comparaciones múltiples:** se mantiene Holm-Bonferroni
  sobre los cinco contrastes del efecto de `origen`, uno por dimensión; se
  reportan valores $p$ crudos y corregidos, $\alpha = 0{,}05$. Esto no
  cambia respecto del protocolo original.
- **Acuerdo entre evaluadoras:** $\alpha$ de Krippendorff ordinal (principal)
  y $\kappa$ ponderado cuadrático por pares (secundario), en vez de $\kappa$
  de Cohen/Fleiss nominal.

### Potencia estadística — recalculada para el nuevo diseño

Con los mismos parámetros de referencia que fija el protocolo original
($\alpha = 0{,}05$ bilateral, potencia objetivo $1-\beta = 0{,}80$, tamaño
de efecto medio $d = 0{,}5$):

| Diseño | Potencia con la muestra disponible | Tamaño requerido para potencia 0,80 |
|---|---|---|
| Apareado (protocolo original) | — | ≈ 34 pares (25 disponibles: insuficiente — ya declarado en `07_Datos/desviaciones.md`, D-01) |
| Grupos independientes (aproximación de sensibilidad, prueba $t$ de dos muestras) | ≈ 0,41 con 25 requisitos por grupo | ≈ 64 requisitos por grupo (≈ 128 en total) |

Este cálculo de sensibilidad ya está reportado en `manuscrito_final.tex`,
sección 6.3, y se reproduce aquí como referencia cruzada. **No sustituye**
una evaluación de potencia específica para el modelo mixto ordinal, que
exigiría simulación con las distribuciones y componentes de varianza
preespecificadas — algo que el propio manuscrito reconoce como pendiente.

**Conclusión de potencia:** el cambio de diseño agrava la limitación de
potencia ya declarada para el diseño apareado, no la mantiene igual. Se
reportará como amenaza a la validez de conclusión (Sección 7 del
manuscrito), priorizando el tamaño del efecto con su intervalo de confianza
al 95 % sobre la significación estadística. No se ampliará la muestra a
posteriori para corregir esta limitación.

## 5. Relación con el protocolo original pre-registrado en OSF

Este cambio se documenta como una **desviación**, no como una modificación
retroactiva del protocolo original. El registro OSF público
(https://osf.io/4z35d/) conserva intacta la versión del protocolo
presentada al momento del registro; esta declaración se somete como adenda
prospectiva, en la sección "Deviations from pre-registration" del registro,
antes de recoger ninguna puntuación.

**Responsable de actualizar la plataforma OSF:** Allan Villafuerte (posee
las credenciales de la cuenta del registro). Esta actualización en
osf.io es una acción pendiente independiente de subir este archivo al
repositorio — ambas deben quedar hechas antes de que EXP-06 avance a la
sesión real de evaluación.

## 6. Limitación reconocida

El cambio de diseño de apareado a independiente reduce la potencia
estadística alcanzable respecto del diseño original, tal como muestra la
tabla de la Sección 4 (de ≈34 pares necesarios a ≈64 por grupo, con una
potencia observable de apenas ≈0,41 con la muestra disponible). Esta
limitación se reporta explícitamente en la sección de Amenazas a la
Validez del manuscrito (categoría: validez de conclusión), siguiendo la
misma práctica de transparencia ya aplicada en `07_Datos/desviaciones.md`
(D-01 y D-02).

---

## Actualización de la desviación — 19/09/2026

La desviación asociada al registro OSF `4z35d` quedó comunicada mediante una
actualización formal del propio registro el 19/09/2026, en la pregunta
`Explanation of foreknowledge and managing unintended influences`.

La actualización deja constancia de que:

1. el `protocolo.pdf` preservado en OSF no coincide en SHA-256 con las
   versiones disponibles en el repositorio;
2. el equipo no afirma equivalencia binaria entre esos archivos;
3. el registro OSF corresponde al 31/08/2026;
4. la rúbrica empleada posteriormente está fechada el 04/09/2026;
5. las decisiones derivadas de esa rúbrica son posteriores al registro y no
   forman parte del contenido preregistrado.

La comparación de digests se realizó descargando el archivo preservado en
OSF. Los valores constan en la entrada A5 de
`07_Datos/registro_correcciones.md`: OSF conserva la v1.0 del 3 de agosto de
2026, mientras que el repositorio contiene la v1.1 (31 de agosto) y la v1.2
(7 de septiembre), cada una con su motivo de revisión declarado en portada.

La vista `Latest` del registro muestra la respuesta actualizada; la vista
`Original` conserva el texto previo. La API pública
`/v2/registrations/4z35d/` expone la adenda.

La acción en OSF fue ejecutada por Villafuerte Rosero Allan Noé. La
documentación de esta corrección en el repositorio corresponde a Macías
Herrera Josthyn Esteban.



