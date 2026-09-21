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

## Tratamiento propuesto (cada uso: renovar o retirar)
| Uso | Opción A: renovar | Opción B: retirar |
|---|---|---|
| LLM / transcripción externa (todos) | Adenda de consentimiento firmada por cada persona con esa cláusula | Dejar de enviar datos a servicios externos y declarar el uso pasado como limitación (ya consta en la declaración de IA) |
| Sesión con prototipo (ENTR-11, 12) | Consentimiento renovado | Retirar las respuestas sobre la interfaz y el fragmento ENTR-12 línea 55 del análisis |
| Audio y vídeo (ENTR-01 a 03) | Consentimiento renovado | Excluir esas grabaciones de todo uso del proyecto y mantenerlas solo en la carpeta cifrada |
| Depósito abierto (ENTR-01 a 08) | Consentimiento renovado | Excluir sus transcripciones del depósito abierto |
| Foto (todos) | Consentimiento renovado | Retirar fotografías donde pueda identificarse a un participante (ya se enmascaran) |

**Estado:** el equipo aún no ha decidido entre renovar y retirar. Hasta entonces, esos usos figuran como no cubiertos y no se declara la evidencia como cerrada (G5).

## Limitaciones
- Las casillas se leyeron a simple vista sobre imágenes (ENTR-07 con poca nitidez; se lee «Sí»). Conviene que dos integrantes confirmen unas cuantas.
- La matriz la elaboró un integrante con asistencia de Claude (declarado en `10_Autoria/declaracion_uso_ia.md`).
- No se contactó a ningún participante; ninguna renovación ha ocurrido.
