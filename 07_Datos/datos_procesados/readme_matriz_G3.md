# G3 — Matriz de uso por consentimiento

Este archivo explica `matriz_uso_consentimiento_G3.csv`: qué se pudo verificar
con la evidencia pública del repositorio y qué queda pendiente porque requiere
abrir los consentimientos originales cifrados (`02_Evidencias/00_Restringido/`).

## Alcance

Cubre los 16 participantes de entrevista (`ENTR-01` a `ENTR-16`, ya
verificados en la tabla maestra de B3). El cuestionario (62 respondientes) se
trata aparte porque es anónimo y no admite matriz por persona: la cifra ya
está declarada en `02_Evidencias/Cuestionario/Respuestas/readme.md`
— 57 de 62 respuestas sin ningún consentimiento, 5 regularizadas el
15/09/2026 mediante el consentimiento complementario.

## Lo que sí se pudo verificar sin contraseña

- **`uso_repositorio_abierto_anonimizado`** y **`uso_envio_llm_externo`**:
  ambos usos ocurren para las 16 personas (transcripción anonimizada publicada
  en este repositorio; uso declarado de Claude/ChatGPT sobre las
  transcripciones en `10_Autoria/declaracion_uso_ia.md`). Esto es un hecho
  público, no depende de la contraseña.
- **El formulario de consentimiento (`09_Etica/A03_Consentimiento_Informado.pdf`,
  texto público) no contiene ninguna cláusula que autorice específicamente
  estos dos usos.** Solo pregunta "Autorizo grabación de audio/video: Sí ☐ No
  ☐". No hay casilla para "publicación en repositorio abierto" ni para "envío
  a un modelo de lenguaje externo". Por eso ambos usos se marcan
  `OCURRIO_SIN_CLAUSULA_ESPECIFICA_EN_EL_INSTRUMENTO`: no es que el
  participante haya dicho que no, es que nunca se le preguntó. Esto aplica a
  los 16 por igual y **no requiere abrir ningún archivo cifrado para
  confirmarlo** — es un defecto del instrumento, no un dato faltante por
  participante.
- **`uso_foto_entorno`**: el formulario tampoco pregunta por fotografías del
  entorno de trabajo, y sin embargo existen fotos en
  `02_Evidencias/Fotos_Entorno/` para varios participantes. Mismo caso que el
  punto anterior.

## Lo que falta y por qué no se puede completar sin la contraseña

- **`uso_audio` y `uso_video_entrevista`**: el formulario sí tiene una casilla
  específica ("Autorizo grabación de audio/video: Sí ☐ No ☐"), pero cuál se
  marcó para cada persona solo consta en el documento original firmado
  (`evidencias_entrevistas_consentimientos.7z`, cifrado). No se puede
  completar esta columna sin abrir ese contenedor.
- **`uso_video_member_checking`**: aplica solo a ENTR-01, ENTR-02 y ENTR-13
  (los tres con acta de member checking, según
  `02_Evidencias/00_Restringido/readme.md`). Su acta original firmada también
  está en el contenedor cifrado correspondiente.

## Qué hace falta para cerrar G3

1. Abrir `evidencias_entrevistas_consentimientos.7z` y
   `Actas_MemberCheck_Originales.7z` con la contraseña (mismo repositorio
   `erizzov-boop/SIMPA_ISR401_Evidencias`, release `v1.0-evidencias`), y
   completar las dos columnas pendientes con Sí/No/No consta por persona.
2. **Decisión de equipo, no técnica**: para los dos usos sin cobertura en el
   instrumento (repositorio abierto, envío a LLM externo) y para las fotos,
   hay que decidir si se declara la limitación por escrito (como ya se hizo
   con el cuestionario) o si se gestiona un consentimiento complementario
   como el que ya se aplicó a 5 personas del cuestionario el 15/09.
