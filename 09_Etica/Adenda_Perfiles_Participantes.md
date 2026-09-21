# Adenda: perfiles de los participantes (B3)

**Proyecto:** SIMPA · ISR-401 · UTEQ · **Fecha:** 21/09/2026
**Documentos que se declaran, sin modificarlos:** A.14 «Adenda de tercera ronda» (§3.3, perfiles previstos) y A.03 v3 «Consentimiento informado».
**Regla aplicada:** las discrepancias con anexos ya firmados se resuelven con documentación nueva que declare la discrepancia y su tratamiento (`09_Etica/README_Etica.md`). La A.14 no se altera.

## 1. Qué se declara

1. La A.14 §3.3 recoge los perfiles **previstos** para ENTR-09 a ENTR-16. Los perfiles **reales** se conocieron al hacer las entrevistas y difieren de lo previsto en ENTR-09, 10, 11, 13, 14 y 16.
2. Los formularios de consentimiento A.03 v3 (tercera ronda) y el formulario de segunda ronda **no tienen campo de cargo o perfil**. Solo los consentimientos de ENTR-01, 02 y 03 traen el cargo escrito a mano por el participante.
3. La única fuente con un perfil por persona, válida para todas las fuentes del proyecto, es `07_Datos/datos_procesados/tabla_maestra_participantes.csv`.
4. En los archivos, la etiqueta del **nombre** del consentimiento o del audio (por ejemplo `TecnicoEstractora`) es informal y no es fuente del perfil.

## 2. Perfil previsto (A.14) frente a perfil real

| Código | Previsto en A.14 | Real (categoría pública) | Situación |
|---|---|---|---|
| ENTR-09 | Docente / ingeniería del área agropecuaria | Profesional del área agrícola | Difiere |
| ENTR-10 | Docente / ingeniería del área agropecuaria | Estudiante de carrera afín | Difiere |
| ENTR-11 | Profesional del área agrícola | Estudiante de carrera afín | Difiere |
| ENTR-12 | Profesional o docente del área agrícola | Profesional del área agrícola | Compatible |
| ENTR-13 | Estudiantado de carrera afín | Profesional del área agrícola | Difiere |
| ENTR-14 | Estudiantado de carrera afín | Profesional del área agrícola | Difiere |
| ENTR-15 | Estudiantado de carrera afín | Estudiante de carrera afín | Coincide |
| ENTR-16 | Estudiantado de carrera afín | Profesional del área tecnológica | Difiere |

## 3. Corrección de ENTR-02

La transcripción rotulaba a ENTR-02 como «Administrador» y el CHANGELOG lo describía como «Administrador / Asesor Técnico». El participante escribió «Asesor Técnico» en su consentimiento, el acta de member checking lo llama «Asesor técnico de la plantación» y en la entrevista dice «estoy aquí dando asesoramiento». Se adopta **Asesor técnico** en todas las fuentes.

## 4. Tratamiento

- Categoría pública: se usan categorías amplias (A.14, R-14.1). `curva_saturacion.py` y `tabla_saturacion.csv` usan esa categoría, no la etiqueta específica.
- Comprobación: `07_Datos/scripts/plan_mejora/verificar_B3_perfiles.py` compara el perfil de cada fuente contra la tabla maestra (salida en `07_Datos/resultados/b3_verificacion_perfiles.txt`).

## 5. Limitaciones

- La tabla maestra fue elaborada por un analista con asistencia de Claude (declarado en B2); la lectura de los cargos manuscritos de ENTR-01 a 03 se hizo sobre las imágenes de los consentimientos.
- Para ENTR-04 a 16 el perfil proviene de la propia entrevista y de las adendas; no consta en el consentimiento.
- La fecha de ENTR-07 figura como 02/08/2026 en la adenda de segunda ronda y como 28/07/2026 en el consentimiento y la transcripción; esta adenda no la resuelve (ver G4/F4).

## 6. Firma

Firma quien verificó la correspondencia de perfiles entre todas las fuentes
declaradas, con el verificador `07_Datos/scripts/plan_mejora/verificar_B3_perfiles.py`.
Cada persona publica su firma desde su propia cuenta; una línea en blanco
queda sin firmar.

| Integrante | Firma (nombre completo) | Fecha | Cuenta que publica |
|---|---|---|---|
| Arboleda Yanza Francisco Javier | Arboleda Yanza Francisco Javier | 21/09/2026 | `farboleday-wq` |
| Macías Herrera Josthyn Esteban | | | `jmaciasherr4` |

Este documento declara discrepancias entre anexos ya firmados y el estado
real; no modifica la A.14 ni sustituye el consentimiento de ningún
participante.
