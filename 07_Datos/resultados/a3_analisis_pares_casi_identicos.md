# A3 — Análisis separado de pares humano/LLM casi idénticos

Este artefacto documenta los cuatro pares señalados por el plan de mejora.
La similitud señalada por el plan no se interpreta como prueba de copia,
dependencia causal ni falta de independencia en su generación.
Por cautela metodológica, los cuatro pares se marcan para análisis separado
en cualquier comparación posterior entre orígenes.

- CSV humano base: `2d7816c27c3f41ab20433865546c4de73b0bd736:06_Experimento/conjuntos/requisitos_humano_ENTR-04.csv` · blob `9f7890d54162eefcf66cd2156a363547087ff8c7`
- Salida LLM base: `2d7816c27c3f41ab20433865546c4de73b0bd736:06_Experimento/salidas_llm/requisitos_LLM_ENTR-04.md` · blob `b048da80164dae9963154efcc74160db0bdaf03d`
- Fuente ENTR-04 congelada: `06e241b7ba0ec43d8541c8908bca31a9f7327ffb:02_Evidencias/Transcripciones/2026-07-28_ENTR-04_Transcripcion.md`

| Par | Nombre humano | Nombre LLM | Jaccard descripción | SequenceMatcher descripción | Tratamiento |
|---|---|---|---:|---:|---|
| `H-013` / `LLM-005` | Calificación de madurez por frutos desprendidos según la variedad | Verificación de frutos desprendidos según variedad | 0.371 | 0.516 | ANALIZAR_APARTE |
| `H-014` / `LLM-006` | Observación por pedúnculo superior a 5 centímetros | Registro de longitud de pedúnculo | 0.406 | 0.553 | ANALIZAR_APARTE |
| `H-015` / `LLM-007` | Rechazo por malformación superior al 30 por ciento | Registro de porcentaje de malformación | 0.333 | 0.579 | ANALIZAR_APARTE |
| `H-020` / `LLM-015` | Entrega del ticket al productor y envío por correo | Entrega física del tiquete al chofer o productor | 0.211 | 0.510 | ANALIZAR_APARTE |

## Regla de tratamiento

1. Los cuatro pares permanecen en sus archivos de origen para conservar trazabilidad.
2. No se infiere a partir de la similitud si hubo o no dependencia en su generación.
3. Cualquier análisis posterior que compare orígenes debe identificarlos explícitamente
   y reportar su sensibilidad por separado o excluirlos del análisis primario, dejando
   constancia del criterio utilizado.
4. Este archivo no atribuye intención ni establece cómo se produjo la similitud;
   únicamente documenta los pares señalados por el plan y una medida descriptiva
   reproducible de similitud textual.
