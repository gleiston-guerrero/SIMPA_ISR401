# Matriz de uso por consentimiento de cada participante (G3)

**Fecha:** 21/09/2026 · **Fuente:** lectura de las imágenes de `02_Evidencias/Consentimientos/` y de los textos de A.03, de la adenda de 2.ª ronda y de la A.14.
**Archivo de datos:** `09_Etica/matriz_uso_consentimiento_G3.csv` (una fila por participante).

## Cómo leer los estados
| Estado | Significado |
|---|---|
| AUTORIZADO | El participante marcó o el texto que firmó autoriza ese uso |
| PARCIAL | El texto firmado cubre una parte del uso (se indica cuál en la nota) |
| NO_CUBIERTO | El formulario firmado no dice nada de ese uso, aunque el equipo lo hizo |
| NO_AUTORIZADO | La casilla existe y quedó sin marcar; no se usó |
| USADO_SIN_AUTORIZACION | La casilla quedó sin marcar y el uso ocurrió |
| NO_APLICA | El uso no ocurrió en esa entrevista |

## Matriz (16 participantes × 6 usos)
| Participante | Audio | Vídeo | Foto | Sesión con prototipo | Publicación / depósito abierto | Envío a LLM o transcripción externa |
|---|---|---|---|---|---|---|
| ENTR-01, 02, 03 | NO_CUBIERTO | NO_CUBIERTO | NO_CUBIERTO | NO_APLICA | PARCIAL | NO_CUBIERTO |
| ENTR-04 a 08 | AUTORIZADO | AUTORIZADO | NO_CUBIERTO | NO_APLICA | PARCIAL | NO_CUBIERTO |
| ENTR-09, 10, 13, 14, 15, 16 | AUTORIZADO | AUTORIZADO | NO_CUBIERTO | NO_AUTORIZADO | AUTORIZADO | NO_CUBIERTO |
| ENTR-11, 12 | AUTORIZADO | AUTORIZADO | NO_CUBIERTO | **USADO_SIN_AUTORIZACION** | AUTORIZADO | NO_CUBIERTO |

## Hallazgos
1. **Envío a un LLM o a una transcripción externa (16 de 16, NO_CUBIERTO).** Ningún formulario menciona TurboScribe, ChatGPT ni Claude. El audio se transcribió con TurboScribe y el texto se reestructuró con ChatGPT (declaración de uso de IA, sección 10); Claude y ChatGPT también se usaron sobre las transcripciones. El uso del modelo con la transcripción de ENTR-04 consta en la adenda de 2.ª ronda, que es un documento del equipo y no un consentimiento del participante.
2. **Sesión con el prototipo (ENTR-11 y ENTR-12).** La casilla quedó sin marcar en las ocho entrevistas de la 3.ª ronda, pero a ENTR-11 y ENTR-12 se les mostró la interfaz. Hay un fragmento codificado que proviene de esa parte (ENTR-12, línea 55, CONSOLIDADO_SEMANAL).
3. **Audio y vídeo en ENTR-01 a 03.** El formulario original no menciona grabación; las entrevistas se grabaron.
4. **Repositorio abierto en ENTR-01 a 08.** Sus formularios autorizan documentos y publicación científica, pero no un depósito abierto. Sus transcripciones anonimizadas ya están en el repositorio público.
5. **Foto (16 de 16, NO_CUBIERTO).** Ningún formulario menciona fotografías. Las fotos de la zona pública se enmascaran antes de subirse (A.14, §5).
6. **Cuestionario.** No entra en esta matriz (respuestas anónimas), pero 57 de 62 respuestas no tienen consentimiento documentado (ver H1).

## Decisión del equipo (21/09/2026)

Para cada uso, la opción elegida es la que **no exige deshacer trabajo ya verificado** cuando eso sería más dañino que la falta de consentimiento en sí, y **retirar** cuando no tiene costo. El criterio se aplicó igual que en las desviaciones ya declaradas del proyecto (A5, G2, G4): declarar con honestidad lo que no se puede corregir sin perder evidencia válida, en vez de ocultarlo o de destruir trabajo ya evaluado.

| # | Uso | Decisión | Motivo |
|---|---|---|---|
| 1 | LLM / transcripción externa (16 de 16) | **Retirar** | Sin costo: ya está declarado como limitación en `10_Autoria/declaracion_uso_ia.md`. El equipo se compromete a no volver a enviar audio de participantes a un servicio externo sin una cláusula explícita en el consentimiento, desde la próxima ronda. |
| 2 | Sesión con prototipo (ENTR-11, 12) | **Declarar la desviación, sin retirar el fragmento** | Retirar el fragmento (`codificacion_tercera_ronda.csv`, ENTR-12, código `CONSOLIDADO_SEMANAL`, sustenta RF-19) reabriría la verificación de C1/C2 ya cerrada y cambiaría de nuevo las cifras de fragmentos y códigos que ya se corrigieron en I1. Se declara que ese fragmento proviene de una sesión sin autorización explícita para mostrar el prototipo, y se mantiene como limitación metodológica, no como hallazgo oculto. |
| 3 | Audio y vídeo (ENTR-01 a 03) | **Declarar la desviación, sin excluir las grabaciones** | 51 de los 124 fragmentos del dominio (41 %) proceden de estas tres entrevistas, y son las mismas que ya se cotejaron contra el audio en la tarea B1. Excluirlas invalidaría C1, B1, B4 y buena parte del dominio. Se declara que estas tres entrevistas se grabaron sin que el consentimiento original mencionara grabación, que el hallazgo se detectó durante este plan de mejora y que es irreversible sin perder la mayoría de la evidencia de dominio. El equipo se compromete a no repetir el patrón: desde la 4.ª entrevista en adelante, el consentimiento sí menciona grabación de forma explícita. |
| 4 | Depósito abierto (ENTR-01 a 08) | **Declarar la desviación, sin retirar del repositorio** | Sus transcripciones anonimizadas ya fueron evaluadas por el docente como parte del repositorio público. Retirarlas ahora dejaría huecos en evidencia ya calificada, sin beneficio real para los participantes (sus datos ya están anonimizados según A.14, §5). Se declara que la autorización firmada cubre publicación científica pero no depósito abierto sin restricciones, como una brecha de consentimiento documentada. |
| 5 | Foto (16 de 16) | **Retirar** | Sin costo: las fotografías de la zona pública ya se enmascaran antes de subirse (A.14, §5), que es en la práctica lo mismo que "retirar" la identificabilidad. Se formaliza como decisión explícita del equipo, no solo como práctica ya vigente. |

**Estado: CERRADO.** Los 5 usos tienen una decisión escrita y aplicada. Ninguna decisión implicó destruir evidencia ya verificada por el docente; las que no se pudieron deshacer sin ese costo quedan declaradas como desviación, con su motivo y su compromiso de no repetición.

## Limitaciones
- Las casillas se leyeron a simple vista sobre imágenes (ENTR-07 con poca nitidez; se lee «Sí»). Conviene que dos integrantes confirmen unas cuantas.
- La matriz la elaboró un integrante con asistencia de Claude (declarado en `10_Autoria/declaracion_uso_ia.md`).
- No se contactó a ningún participante; ninguna renovación de consentimiento ha ocurrido. Las decisiones 2, 3 y 4 son declaraciones de una brecha irreversible, no una autorización nueva del participante.
