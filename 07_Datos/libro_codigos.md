# Libro de Códigos — C1 · SIMPA_ISR401
**Versión:** 1.0
**Fecha:** 2026-09-20
**Fuente:** 213 fragmentos codificados vigentes (227 antes de la tarea C2) — ENTR-01 a ENTR-16

---

## 1. Criterios de inclusión y exclusión

### Inclusión
- Fragmento citado **literalmente** de la transcripción del entrevistado.
- Corresponde a manifestación directa del participante.
- Se vincula con al menos un requisito derivado o código de categoría.
- La cita se encuentra verificable en el archivo y línea indicados.

### Exclusión
- Parafraseo o resumen del analista sin respaldo textual.
- Intervención del entrevistador.
- Contenido sin relación con el dominio del proyecto.
- Cita localizada en transcripción pero asignada a código incorrecto.

### Estados de verificación
| Estado | Significado |
|---|---|
| `VER` | Cita localizada literalmente en intervención del entrevistado |
| `SOLO_EN_ENTREVISTADOR` | Existe pero fue dicho por el entrevistador; no se usa como evidencia |
| `NO_LOCALIZADA` | No hallada en el archivo indicado; no se inventa texto |

---

## 2. Glosario de códigos

| # | Código | Definición | Criterio de aplicación |
|---|---|---|---|
| 1 | EQUIPOS_TRABAJO | División organizativa del personal por especialidad o área de labor | Se nombra grupos, equipos o responsabilidades por función |
| 2 | SUPERVISION_RECORRIDO | Verificación presencial de que las labores se ejecutan según lo planeado | Recorrido, inspección o control visual en campo |
| 3 | LATENCIA_INSPECCION | Tiempo que transcurre entre detección y verificación presencial | Frecuencia, retraso o periodicidad de visitas |
| 4 | MONITOREO_VISUAL | Observación directa rutinaria sin instrumentación especial | Revisión diaria o a simple vista del cultivo |
| 5 | SIGNO_VISIBLE_PLAGA | Apariencia externa que indica problema fitosanitario | Color, mancha, deformación o caída de hojas/frutos |
| 6 | PLAGA_DEFOLIADOR | Organismo que consume follaje reduciendo capacidad fotosintética | Insectos u organismos que atacan hojas |
| 7 | ENFERMEDAD_FLECHA | Afección que ataca la hoja central aún no desplegada | Daño o pudrición en la flecha/hoja central |
| 8 | CONTROL_POR_ETAPA | Tratamiento distinto según estado de desarrollo de la plaga | Producto, frecuencia o método cambia por fase |
| 9 | ESTACIONALIDAD_PLAGA | Mayor o menor incidencia según época del año | Relación plaga/enfermedad con clima, mes o estación |
| 10 | FACTOR_PRODUCTIVIDAD | Elemento que determina cantidad y calidad de producción | Riego, nutrición, polinización, clima como determinantes |
| 11 | INDICADOR_DEFICIT_HIDRICO | Señal visible de falta de agua en la planta | Marchitamiento, caída prematura, acumulación de flechas |
| 12 | CENSO_FLORES | Conteo de estructuras reproductivas para estimar cosecha | Conteo de flores/inflorescencias para proyectar producción |
| 13 | RENDIMIENTO_POR_VARIEDAD | Diferencia de producción según tipo de palma | Comparación híbrido vs guineensis u otras variedades |
| 14 | REGISTRO_CLIMA | Medición sistemática de condiciones meteorológicas | Lluvia, humedad, temperatura registrados o referidos |
| 15 | DIAGNOSTICO_POR_IMAGEN | Identificación de problemas a partir de fotografías | Tomar/enviar foto para consultar o registrar |
| 16 | USUARIO_NO_EXPERTO | El sistema debe ser comprensible para personal sin formación técnica | Referencia a jornaleros o personal con poca escolaridad |
| 17 | EVALUACION_DESEMPENO | Forma de medir cumplimiento de labor | Conteo, calidad, comparación con metas o supervisión |
| 18 | CONTEO_FLORES | Registro de unidades polinizadas o inspeccionadas por lote/persona | Número de flores contadas periódicamente |
| 19 | CALIDAD_COMO_INDICADOR | Estado del fruto/racimo refleja desempeño del trabajo | Apariencia, peso o forma que reflejan calidad |
| 20 | CONSOLIDADO_SEMANAL | Agrupación de información diaria en resúmenes semanales | Datos o resultados que se reúnen/revisan cada semana |
| 21 | ESCASEZ_MANO_OBRA | Dificultad para contratar y retener personal calificado | Falta de personal, rotación alta o dificultad de contratación |
| 22 | APP_OFFLINE_EXISTENTE | Herramienta digital que funciona sin conexión mencionada por participantes | Aplicación que guarda datos localmente sin internet |
| 23 | DISPONIBILIDAD_MOVIL | El personal cuenta con teléfono móvil como recurso disponible | Confirmación de posesión de dispositivo |
| 24 | HISTORIAL_LOTE | Registro acumulativo de intervenciones y resultados por unidad | Seguimiento de todo lo ocurrido en cada lote a lo largo del tiempo |
| 25 | LABOR_MANTENIMIENTO | Tareas rutinarias de conservación del cultivo | Chapia, corona, limpieza, deshierbe |
| 26 | PROBLEMA_NUTRICIONAL | Falta o exceso de nutrientes que afecta desarrollo | Deficiencia que se manifiesta en hojas o frutos |
| 27 | ANALISIS_LABORATORIO | Prueba técnica en suelo o tejido para determinar necesidades | Muestreo enviado a laboratorio |
| 28 | SIGNO_FOLIAR | Cambio de color o estado de la hoja como señal de deficiencia/enfermedad | Amarillamiento, manchas, bordes secos |
| 29 | PLAGA_ESTRATEGUS | Insecto que ataca el meristemo de la palma joven desde el suelo | Perforación en la base que destruye el punto de crecimiento |
| 30 | CICLO_ANTESIS_COSECHA | Tiempo desde floración hasta racimo listo para corte | Meses/semanas mencionados entre antesis y cosecha |
| 31 | META_RENDIMIENTO | Producción objetivo por superficie en periodo determinado | Toneladas por hectárea/año como referencia |
| 32 | EFECTO_DEFICIT_HIDRICO | Cambio observable por falta de agua | Menos flores, frutos pequeños, caída prematura |
| 33 | RECOMENDACION_ACCIONABLE | Indicación concreta de qué hacer para corregir/prevenir | Producto, dosis o práctica derivada de observación |
| 34 | UMBRAL_POR_VARIEDAD | Frutos desprendidos que señalan corte, distinto por variedad | 3 en guineensis / 5 en híbrido |
| 35 | CRITERIO_RECEPCION | Norma para validar si un lote cumple para ser aceptado | Revisión visual o porcentaje de defectos |
| 36 | DEFECTO_PEDUNCULO | Tallo excesivo que perjudica procesamiento | Pedúnculo mayor a 5 cm que absorbe aceite |
| 37 | DEFECTO_MALFORMACION | Deformación que reduce valor o causa rechazo | Más del 30 % = rechazo del lote |
| 38 | PROBLEMA_FRUTA_VERDE | Cosecha antes de madurez que afecta calidad y acidez | Fruta sin desprendimiento que llega verde |
| 39 | INCENTIVO_PERVERSO | Sistema de pago favorece conductas contrarias a calidad | Pago por tonelada incentiva cortar inmaduro |
| 40 | RECHAZO_LOTE | Devolución de envío que no cumple estándares | Fruta no conforme regresa al productor |
| 41 | VENTANA_CORTE_ENTREGA | Tiempo máximo admisible entre corte y recepción | 24 h recomendado / 48 h límite |
| 42 | TOLERANCIA_HIBRIDO | Mayor resistencia del híbrido al paso de tiempo sin procesar | Aguanta más sin aumentar acidez |
| 43 | TICKET_PESAJE | Comprobante generado al recibir y pesar fruta | Bruto, tara, neto y calificación |
| 44 | CALIFICACION_TICKET | Clasificación de defectos que acompaña al pesaje | Tamaño, verde, sobremadura registrados |
| 45 | GUIA_REMISION | Documento de transporte exigido por normativa | Documento oficial que ampara traslado |
| 46 | PROYECCION_CAPACIDAD | Estimación de volumen a procesar en periodo | Cálculo de toneladas para organizar recepción |
| 47 | MINIMIZACION_DATOS | No recopilar ni difundir información no estrictamente necesaria | Datos personales que no se comparten públicamente |
| 48 | DATO_COMPARTIBLE | Información que sí puede intercambiarse sin riesgo | Cantidad de racimos, peso estimado, fecha |
| 49 | CURVA_APRENDIZAJE | Tiempo de formación necesario para dominar una labor | 2-3 meses para polinizador competente |
| 50 | DIAGNOSTICO_SITIO | Identificación observando la planta en su entorno | Amarillamiento de hojas bajeras = magnesio o compactación |
| 51 | SOBREMADURACION | El racimo sobrepasa el punto óptimo de cosecha | Aumenta acidez del aceite |
| 52 | LATENCIA_VERIFICACION | Frecuencia con que supervisor comprueba lo reportado | Cada tercer día, dos veces por semana, etc. |
| 53 | REGISTRO_PAPEL | Anotación manual como soporte único de información | Datos que solo existen en cuaderno |
| 54 | ENTREGA_VERBAL | Transmisión oral de resultados al finalizar jornada | El conteo se dice al encargado sin documento |
| 55 | UNIDAD_DE_AVANCE | Medida con que se cuantifica trabajo realizado | Mata, racimo, flor según labor |
| 56 | TRANSPARENCIA_PAGO | El trabajador puede verificar su cálculo y acumulado | Consultar avance y tarifas antes de cobrar |
| 57 | CONECTIVIDAD_PARCIAL | Cobertura que no llega a todas las zonas del cultivo | Señal solo en campamento, no en lotes alejados |
| 58 | CANAL_INFORMAL | Medio no institucional usado de hecho para comunicar | Mensajería instantánea como vía principal de reporte |
| 59 | EVIDENCIA_FOTOGRAFICA | Imagen que sirve como prueba o respaldo | Foto que confirma o registra un hallazgo |
| 60 | VERIFICACION_VISUAL | Señal visible que confirma ejecución correcta | Talco sobre la flor = polinización aplicada |
| 61 | LISTA_PENDIENTES | Relación de temas/lotes que requieren revisión | Control de qué se revisó y qué falta |
| 62 | GEORREFERENCIA_INCIDENCIA | Coordenadas GPS del punto exacto detectado | Latitud/longitud para localizar sin depender solo del lote |
| 63 | RIESGO_LABORAL_POLINIZACION | Posible pérdida económica si la labor falla | Mal trabajo = hasta 50 % menos producción |
| 64 | RASTREO_GPS | Seguimiento por satélite del recorrido del trabajador | Registrar por dónde pasa y qué zonas cubre |
| 65 | POLINIZACION_CRITICA | Es la labor que más determina la producción final | Sin buena polinización no hay buenos racimos |
| 66 | ESTADO_ANTESIS | Apariencia de la flor que indica momento exacto | Color amarillo/negro = momento óptimo |
| 67 | HORAS_LUZ | Cantidad de iluminación diaria que influye en formación | 8-12 horas = ciclo completo del racimo |
| 68 | UMBRAL_DESPRENDIMIENTO | Frutos que caen solos señalan madurez | 3-5 pepas desprendidas = cortar |
| 69 | COLOR_NO_FIABLE | El color externo no es criterio confiable | Puede engañar; se prefiere desprendimiento |
| 70 | PEPA_DESPRENDIDA | Fruto que se separa naturalmente al madurar | Referencia universal de corte |
| 71 | TAMAÑO_RACIMO | Peso o volumen relacionado con edad, variedad y manejo | 3-5 kg en primer año como referencia |
| 72 | CONTEO_DIARIO | Registro que se hace cada jornada | Cantidad de racimos, flores o matas trabajadas |
| 73 | SUPERVISION_DIARIA | Revisión que ocurre todos los días | Asignación y revisión cada jornada |
| 74 | FALTA_ESPECIFICACION | Los reportes por mensajería no detallan todo | Información incompleta o ambigua |
| 75 | CORRECION_POSTERIOR | Errores detectados se ajustan después en el registro | Diferencias que se corrigen en oficina |
| 76 | GUARDADO_LOCAL | Guardar datos en dispositivo sin conexión | Sincroniza automáticamente al recuperar señal |
| 77 | CONFIRMACION_VISUAL | Mostrar en pantalla lo registrado para validar | Resumen antes de enviar o guardar |
| 78 | TRAZABILIDAD_COMPLETA | Seguimiento completo de cada acción | Quién, cuándo, dónde y qué se hizo; todo consultable |
| 79 | PRIVACIDAD_DATOS | Cada usuario ve solo lo que le corresponde | Control de acceso por rol |
| 80 | RESISTENCIA_CAMBIO | Rechazo o abandono de herramienta nueva por falta de familiaridad | Se deja de usar por no conocer o no recibir capacitación |
| 81 | RECOMENDACION_CONFIRMADA | La sugerencia automática debe respaldarse con evidencia | Confirmar lo indicado antes de confiar |
| 82 | PERDIDA_DATOS | Informe no registrada se olvida o no se recupera | Sin registro se pierde lo ocurrido |
| 83 | VERIFICACION_DIAGNOSTICO | Se requiere respaldo visual para creer una alerta | Necesitar foto o información adicional para confiar |
| 84 | CONFIANZA_DIAGNOSTICO | La credibilidad se ve afectada por errores y se recupera con aciertos | Un error desconfía; aciertos restablecen confianza |
| 85 | PLANIFICACION_LABORES | Usar registros anteriores para organizar actividades futuras | Relacionar historial con planificación venidera |
| 86 | INTERFAZ_SIMPLE | La presentación debe ser clara y orientar desde el inicio | Explicar uso y beneficio desde la primera pantalla |
| 87 | CAPACITACION_USO | Se necesita enseñar explícitamente para que se adopte | Tiempo, método o responsable de la formación |
| 88 | TUTORIAL_GUIADO | La herramienta debe guiar paso a paso antes de usar cada función | Ayuda integrada o pantalla de introducción |
| 89 | INTERFAZ_VISUAL | Usar gráficos e iconos en lugar de depender solo de números | Elementos reconocibles para facilitar comprensión |
| 90 | CONTROL_INSUMOS | Seguimiento de entrada, uso y salida de productos y materiales | Bodega, retiro, entrega o aplicación de insumos |
| 91 | DISPONIBILIDAD_MOVIL | El trabajador debe contar con dispositivo adecuado | Condicionar uso a poseer teléfono o equipo |
| 92 | GPS_EVIDENCIA_LABOR | El recorrido GPS no basta; necesita complementarse | Ubicación + foto o confirmación de la tarea |
| 93 | OPERACION_OFFLINE | Trabajar sin conexión y sincronizar al recuperarla | Recorrido, foto y coordenadas guardados localmente |
| 94 | ESTACIONALIDAD_PLAGA | Afectaciones aparecen según épocas y clima | Relación problema con temporadas del año |
| 95 | CONECTIVIDAD_PARCIAL | La señal no llega a gran parte del campo | Zonas sin internet donde se debe trabajar |

---

## 3. Cumplimiento
- ✅ **95 códigos** únicos identificados y definidos
- ✅ Cada código: definición + criterio de aplicación
- ✅ Criterios de inclusión/exclusión documentados
- ✅ Estados de verificación estandarizados
- ✅ Compatible con script de verificación
