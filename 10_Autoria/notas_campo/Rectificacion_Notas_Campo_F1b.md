# Rectificación sobre las notas de campo presentadas el 12/09/2026

**Proyecto:** Sistema Inteligente de Mantenimiento de Palma Africana (SIMPA)
**Asignatura:** Ingeniería de Requisitos · ISR-401 · UTEQ · 2026–2027 PPA
**Tarea:** F1b del Plan de mejora de los datos del proyecto (19/09/2026)
**Fecha de esta rectificación:** 21/09/2026

---

## 1. Qué se presentó

El **11/09/2026**, en el commit `b59d4ef`, este repositorio declaró por escrito
que no existían notas de campo manuscritas de las sesiones de elicitación, y
explicó por qué: el registro de las entrevistas se hizo directamente en formato
digital, sin soporte físico intermedio. **Esa declaración era correcta.**

El **12/09/2026**, en el commit `1135321`, se incorporaron a
`10_Autoria/notas_campo/` dieciséis archivos PDF presentados como notas
manuscritas de cada entrevista, uno por sesión, sustituyendo aquella
declaración. El commit fue publicado desde la cuenta `erizzov-boop`
(Rizzo Vélez Edson Nagib).

## 2. Qué se comprobó

Al revisar esos dieciséis archivos se constató que, **más allá del encabezado de
cada uno, el cuerpo completo de la escritura manuscrita era idéntico entre los
dieciséis**. No eran dieciséis notas genuinas y distintas tomadas en dieciséis
sesiones diferentes.

Un documento así no puede sostenerse como registro contemporáneo de una sesión
de campo, y su presencia contradecía además la declaración de ausencia del
11/09 que el propio repositorio ya había hecho.

## 3. Qué se ha hecho

1. Los dieciséis PDF fueron **retirados del repositorio** el 20/09/2026, en el
   commit `7ff7d4e`.
2. La **declaración de ausencia del 11/09/2026 queda restituida** como estado
   vigente de la carpeta, en `10_Autoria/notas_campo/readme.md`.
3. En su lugar se incorporó una **síntesis analítica de las dieciséis
   entrevistas**, elaborada a partir de las transcripciones reales y **rotulada
   como lo que es**: un análisis posterior, no una nota de sesión. Su origen y
   el uso de asistencia de IA en su elaboración se declaran en su encabezado y
   en `10_Autoria/declaracion_uso_ia.md`.
4. El historial no se ha reescrito: los commits `1135321` y `7ff7d4e` siguen
   siendo consultables, de modo que lo ocurrido queda verificable.

## 4. Qué reconocemos

El equipo reconoce que la incorporación de esos dieciséis archivos **presentó
como evidencia contemporánea de campo un material que no lo era**, y que
hacerlo sustituyó una declaración de ausencia que sí era veraz por una
afirmación que no podía sostenerse.

Reconocemos que el defecto no está en carecer de notas de campo —no tenerlas es
un hecho legítimo, y estaba correctamente declarado— sino en haber generado
material para cubrir ese hueco.

Asumimos como criterio, para lo que queda del proyecto y de forma expresa:

- **no se crea evidencia**: cuando un elemento no existe, se declara su
  ausencia y su motivo, y esa declaración es la entrega;
- **ningún material elaborado después de una sesión se presenta como registro
  tomado durante ella**, aunque su contenido sea correcto;
- **todo documento derivado de otro lleva rotulado su origen**, su autoría y,
  si la hubo, la asistencia de IA empleada.

## 5. Alcance de esta rectificación

Esta rectificación se refiere únicamente a los dieciséis PDF de
`10_Autoria/notas_campo/` incorporados el 12/09/2026. No afecta a las
transcripciones, a los audios y vídeos inventariados en
`02_Evidencias/00_Restringido/fichas_tecnicas.csv`, ni a los consentimientos
informados, cuya validez se trata en las tareas G3 y F3 del mismo plan.

---

## 6. Firmas

Cada persona firma escribiendo su nombre completo y la fecha en su línea, y
**publicando el cambio desde su propia cuenta de GitHub**. Una línea sin firmar
se deja sin firmar: no se firma por otra persona.

| Integrante | Nombre completo | Fecha | Cuenta que publica |
|---|---|---|---|
| Arboleda Yanza Francisco Javier | Arboleda Yanza Francisco Javier | 21/09/2026 | `farboleday-wq` |
| Macías Herrera Josthyn Esteban | | | `jmaciasherr4` |
| Villafuerte Rosero Allan Noé | | | |
| Rizzo Vélez Edson Nagib | | | `erizzov-boop` |
| Huilcapi León Denisses Fabiola | | | |
| Alcívar Vélez Anderson Adonis | | | |

> **Estado de la firma al cierre del plazo:** las líneas que queden en blanco
> significan que esa persona no firmó antes del cierre. No se completan por
> ella ni se interpreta su silencio como conformidad.
