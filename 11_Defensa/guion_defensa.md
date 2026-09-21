# Guion de la defensa — SIMPA

**Equipo AHMRV · ISR-401 · Examen final, semana 19 (7–11 de septiembre de 2026)**

> **Ajustar antes de usar:** este guion asume **20 minutos de exposición**
> más turno de preguntas. Si el tiempo asignado es otro, reescalar la columna
> de minutos manteniendo las proporciones. La franja de demostración no debe
> bajar de 5 minutos.

---

## 1. Estructura y tiempos

| # | Bloque | Min | Expone | Contenido |
|---|---|---:|---|---|
| 1 | Apertura y problema | 2 | Allan | Qué es SIMPA, organización estudiada, problema real de la unidad productiva |
| 2 | Método de elicitación | 3 | Denisses | 16 entrevistas en tres rondas, cuestionario a 62 personas, codificación temática y saturación |
| 3 | Requisitos y modelado | 3 | Josthyn | 42 RF, 19 RNF, 18 CU, MoSCoW/Kano, 13 diagramas UML versionados como código |
| 4 | Componente inteligente | 2 | Allan | 18 requisitos de IA, clasificación de riesgo bajo el Reglamento (UE) 2024/1689 |
| 5 | **Demostración del prototipo** | 5 | Francisco | Ver `guion_demostracion.md` |
| 6 | Validación y evidencia | 3 | Edson | Fagan, walkthrough con 6 sesiones, trazabilidad E2E, inventario de 71 archivos verificado |
| 7 | Reproducibilidad y FAIR | 2 | Anderson | Zenodo con DOI, 92,31 % FAIR, SWHID, cadena `run_all.py` |
| 8 | Limitaciones y cierre | 1 | Allan | Qué no se ejecutó y por qué. Correcciones desde la 2B |
| | **Turno de preguntas** | — | Todos | Ver `preguntas_previsibles.md` |

**Regla de tiempo:** quien se pase de su franja se la quita al siguiente. El
bloque que nunca se sacrifica es el 5, porque C13 evalúa la demostración.

---

## 2. Reparto por rol

Cada quien expone lo que hizo. Un tribunal detecta enseguida a alguien
recitando el trabajo de otro.

| Persona | Rol | Bloques |
|---|---|---|
| Allan Villafuerte | Analista Líder | 1, 4, 8 |
| Denisses Huilcapi | Documentadora | 2 |
| Josthyn Macías | Modelador | 3 |
| Francisco Arboleda | Apoyo modelado | 5 |
| Edson Rizzo | Verificador / Evidencias | 6 |
| Anderson Alcívar | Apoyo repositorio | 7 |

**Los seis deben poder responder preguntas sobre el bloque que exponen.** C12
evalúa dominio técnico, y el tribunal suele preguntar a quien acaba de hablar.

---

## 3. Qué abrir antes de empezar

Dejar preparado, cargado y probado:

| Recurso | Dónde |
|---|---|
| Prototipo (V3, versión vigente) | `https://simpa-v3-prototipo.netlify.app/` |
| Repositorio principal | `https://github.com/gleiston-guerrero/SIMPA_ISR401` |
| ERS v2.0 en PDF | `01_ERS/ERS_SRS_2B_v2.0.pdf` |
| Depósito Zenodo | `https://zenodo.org/records/22236500` |
| Reporte FAIR | `08_Publicacion/fair_assessment.pdf` |

**Probar la conexión y el proyector el día anterior.** Si el prototipo no
carga, hay que tener el archivo HTML autónomo descargado en local como
respaldo.

---

## 4. Mensajes que deben quedar dichos

Tres cosas que el tribunal debe oír con claridad, porque son las fortalezas
que el propio docente reconoció:

1. **La evaluación FAIR de 92,31 % es la más alta del curso**, obtenida con la
   herramienta oficial F-UJI y depositada como JSON y PDF.
2. **Los diagramas UML están versionados como código PlantUML**, no como
   imágenes opacas: son auditables y regenerables.
3. **El prototipo declara, criterio por criterio, qué flujos son funcionales y
   cuáles son interfaz simulada.** Distinguir lo que funciona de lo que se ve
   funcionar es lo que se exige de un prototipo académico.

Y una cuarta que hay que decir **antes de que la pregunten**: el estudio
empírico comparativo no se ejecutó. Está el protocolo, el registro previo en
OSF y los instrumentos. Adelantarlo desarma la pregunta incómoda y es coherente
con la línea que ha seguido el equipo.

---

## 5. Cómo hablar de lo que falta

El criterio del proyecto ha sido declarar antes que maquillar, y el docente lo
elogió expresamente por reportar la métrica M6 como no conforme en lugar de
inflarla.

En la defensa eso se traduce en:

- **No decir «está casi listo»** de algo que no está. Decir qué falta y qué se
  necesita para cerrarlo.
- **No presentar como funcional** ningún flujo marcado como interfaz simulada.
- **No afirmar nada sobre precisión de la IA.** No hay modelo entrenado.
- Si el tribunal pregunta algo cuya respuesta no se sabe, decirlo. Inventar en
  la sala es el único error irreparable.

---

## 6. Ensayo

Al menos uno completo, cronometrado, con los seis y con el prototipo en vivo.

Puntos de control:

- ¿Cabe en el tiempo?
- ¿La demostración funciona desde una máquina que no sea la de siempre?
- ¿Cada quien sabe responder a lo que expone?
- ¿Las transiciones entre personas están claras?

Grabar el ensayo sirve además como elemento **A4** de la evidencia de autoría.
