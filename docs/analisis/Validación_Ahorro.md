# **10\. Matriz de pruebas y resultados**

### **Escenarios evaluados**

Se evaluaron 10 casos de prueba para validar el encendido, apagado, exclusiones, manejo de errores y ejecución programada de EcoScheduler.

La tabla siguiente presenta la matriz completa de los 10 casos validados, incorporando condición de prueba, resultado esperado, resultado obtenido, fecha, responsable y rol, estado, evidencia y referencia del repositorio.

| ID | Escenario | Estado | Condición de prueba | Resultado esperado | Resultado obtenido |
| :---- | :---- | :---- | :---- | :---- | :---- |
| 1 | Apagado normal | Aprobado | Instancia en estado Running con EcoScheduler=True y perteneciente a un entorno elegible. | La instancia se detiene correctamente. | EventBridge ejecutó STOP; CloudWatch registró la ejecución y Amazon EC2 mostró la instancia en estado Detenida. |
| 2 | Encendido normal | Aprobado | Instancia en estado Stopped con EcoScheduler=True y perteneciente a un entorno elegible. | La instancia se inicia correctamente. | CloudWatch registró START exitoso y Amazon EC2 confirmó el estado Running. |
| 3 | Exclusión por etiqueta | Aprobado | Instancia sin EcoScheduler=True o con un valor distinto al criterio elegible. | La instancia es ignorada. | CloudWatch confirmó que, con EcoScheduler=False, la instancia quedó fuera de la ejecución y la función finalizó de forma controlada. |
| 4 | Exclusión de producción | Aprobado | Instancia con Environment=Prod. | La instancia es ignorada. | CloudWatch registró la exclusión por Environment=Prod; la lógica también contempla Criticality=High y Maintenance=True. |
| 5 | Instancia ya detenida | Aprobado | Ejecutar la función de apagado cuando la instancia ya se encuentra Stopped. | No se ejecuta una acción redundante. | CloudWatch registró la omisión; la función de apagado procesa solo instancias running. |
| 6 | Instancia ya encendida | Aprobado | Ejecutar la función de encendido cuando la instancia ya se encuentra Running. | No se ejecuta una acción redundante. | CloudWatch registró START omitido; la función de encendido procesa solo instancias stopped. |
| 7 | Error de permisos | Aprobado | Ejecutar la función con el permiso necesario de Amazon EC2 denegado. | Se genera un error claro y queda registrado. | CloudWatch registró AuthFailure / ClientError y la ejecución finalizó de forma controlada. |
| 8 | Ejecución programada (EventBridge) | Aprobado | Regla habilitada, horario configurado y función Lambda establecida como destino. | La función se ejecuta automáticamente en el horario programado. | START y STOP fueron comprobados mediante EventBridge, CloudWatch y estados finales de Amazon EC2. |
| 9 | Múltiples instancias | Aprobado | Dos o más instancias elegibles con estados compatibles con la acción. | Todas las instancias elegibles son procesadas. | CloudWatch registró una ejecución con dos instancias elegibles y Amazon EC2 mostró ambas instancias detenidas. |
| 10 | Manejo de excepciones | Aprobado | Provocar un error controlado o usar un dato inválido. | El error es capturado y registrado sin terminación abrupta. | ClientError capturó el error, registró código y mensaje y la invocación finalizó con END y REPORT. |

### **Trazabilidad de evidencias y responsables**

La información de fecha, responsable, evidencia y commit se presenta en una segunda tabla para mantener la matriz legible sin perder ningún dato solicitado.  
*Nota: Para mejorar la legibilidad, en esta tabla se utilizan nombres y fuentes resumidos. Los nombres completos y las referencias completas se conservan en la matriz consolidada y en los documentos técnicos de respaldo*.

### 

### 

| ID | Fecha | Responsable y rol | Evidencia / fuente | Commit / referencia |
| :---- | :---- | :---- | :---- | :---- |
| 1 | 27/07/2026 | Jafet Hernández (Desarrollador Serverless Jr.) / Adonay Menjívar (Ingeniero Cloud Jr.) | Fase 3 Serverless Jr., Prueba 1; Programación y Monitoreo | [a075a310a33b8eb91bac50a471a601edf5b01099](https://github.com/amenjivar835-lgtm/Eco-Scheduler/commit/a075a310a33b8eb91bac50a471a601edf5b01099) |
| 2 | 27/07/2026 | Jafet Hernández (Desarrollador Serverless Jr.) / Adonay Menjívar (Ingeniero Cloud Jr.) | Fase 3 Serverless Jr., Prueba 2; Programación y Monitoreo | [a075a310a33b8eb91bac50a471a601edf5b01099](https://github.com/amenjivar835-lgtm/Eco-Scheduler/commit/a075a310a33b8eb91bac50a471a601edf5b01099) |
| 3 | 27/07/2026 | Jafet Hernández (Desarrollador Serverless Jr.) | Fase 3 Serverless Jr., Prueba 3 | [95b5a911144697e9c510d4f7380fa8fe92d70f68](https://github.com/amenjivar835-lgtm/Eco-Scheduler/commit/95b5a911144697e9c510d4f7380fa8fe92d70f68) |
| 4 | 27/07/2026 | Jafet Hernández (Desarrollador Serverless Jr.) | Fase 3 Serverless Jr., Prueba 4 | [95b5a911144697e9c510d4f7380fa8fe92d70f68](https://github.com/amenjivar835-lgtm/Eco-Scheduler/commit/95b5a911144697e9c510d4f7380fa8fe92d70f68) |
| 5 | 27/07/2026 | Jafet Hernández (Desarrollador Serverless Jr.) | Fase 3 Serverless Jr., Prueba 5 | [a075a310a33b8eb91bac50a471a601edf5b01099](https://github.com/amenjivar835-lgtm/Eco-Scheduler/commit/a075a310a33b8eb91bac50a471a601edf5b01099) |
| 6 | 27/07/2026 | Jafet Hernández (Desarrollador Serverless Jr.) | Fase 3 Serverless Jr., Prueba 6 | [a075a310a33b8eb91bac50a471a601edf5b01099](https://github.com/amenjivar835-lgtm/Eco-Scheduler/commit/a075a310a33b8eb91bac50a471a601edf5b01099) |
| 7 | 27/07/2026 | Jafet Hernández (Desarrollador Serverless Jr.) | Fase 3 Serverless Jr., Prueba 7 | [a075a310a33b8eb91bac50a471a601edf5b01099](https://github.com/amenjivar835-lgtm/Eco-Scheduler/commit/a075a310a33b8eb91bac50a471a601edf5b01099) |
| 8 | 27/07/2026 | Adonay Menjívar (Ingeniero Cloud Jr.) / Jafet Hernández (Desarrollador Serverless Jr.) | Programación y Monitoreo; Fase 3 Serverless Jr., Prueba 8 | [8216dbe4c50f9d3ec8d0f51cb344d8469fe88661](https://github.com/amenjivar835-lgtm/Eco-Scheduler/commit/8216dbe4c50f9d3ec8d0f51cb344d8469fe88661) |
| 9 | 27/07/2026 | Jafet Hernández (Desarrollador Serverless Jr.) | Fase 3 Serverless Jr., Prueba 9 | [a075a310a33b8eb91bac50a471a601edf5b01099](https://github.com/amenjivar835-lgtm/Eco-Scheduler/commit/a075a310a33b8eb91bac50a471a601edf5b01099) |
| 10 | 27/07/2026 | Jafet Hernández (Desarrollador Serverless Jr.) | Fase 3 Serverless Jr., Prueba 10 | [a075a310a33b8eb91bac50a471a601edf5b01099](https://github.com/amenjivar835-lgtm/Eco-Scheduler/commit/a075a310a33b8eb91bac50a471a601edf5b01099) |

### 

### **Resultados obtenidos**

Se alcanzó una cobertura de pruebas del 100 %, con 10 de 10 casos validados.

### **Evidencias principales**

Evidencias utilizadas:

* Registros reales en Amazon CloudWatch Logs que demuestran la ejecución de las funciones AWS Lambda para encendido y apagado.  
* Amazon CloudWatch Logs con registro de AuthFailure y finalización controlada de la ejecución.  
* Validación de criterios de exclusión para recursos no elegibles, incluyendo Environment=Prod, Criticality=High y Maintenance=True.  
* Comprobaciones en la consola de Amazon EC2 mostrando los cambios efectivos de estado de la instancia entre Running y Stopped.  
* Evidencias de ejecución programada y trazabilidad de las acciones realizadas por la automatización.  
* Matriz general de pruebas con 10/10 casos validados (100 %).

# **11\. Análisis FinOps y medición del ahorro**

### **Metodología de cálculo**

La metodología FinOps compara un escenario base de operación continua, sin automatización, frente a un escenario optimizado mediante EcoScheduler.  
Los cálculos utilizan como referencia una instancia Amazon EC2 t3.micro con una tarifa de cómputo de USD 0.0104 por hora.

Fórmulas utilizadas:

* **Horas evitadas \=** Horas del escenario base \- Horas con EcoScheduler  
* **Porcentaje de reducción \=** (Horas evitadas / Horas del escenario base) × 100  
* **Costo de cómputo \=** Horas activas × USD 0.0104/h  
* **Costo de cómputo evitado \=** Costo base \- Costo con EcoScheduler

**Nota metodológica:**    
El análisis FinOps contabiliza únicamente el componente de cómputo EC2 directamente afectado por el encendido y apagado de la instancia. Otros conceptos de facturación, como almacenamiento Amazon EBS, EC2-Other, Amazon VPC, direcciones IPv4 o transferencia de datos, pueden continuar generando cargos aunque la instancia se encuentre detenida.

### **Tabla completa de resultados FinOps — Semanas 7 a 10**

Para el cierre del proyecto se presenta el detalle validado de las Semanas 7 a 10 y su acumulado final, conforme a los resultados registrados en los informes y en la comparación FinOps.

| Semana |  horas evaluadas | Horas encendidas | Horas apagadas | Reducción | Estado |
| ----- | :---: | :---: | :---: | :---: | :---: |
| Semana 7 |  jue 08:00–vie 18:00 | 20 h | 14 h | 41.18 % | Validado |
| Semana 8 | lun–vie 08:00–18:00 | 50 h | 70 h | 58.33 % | Validado |
| Semana 9 | lun–vie 08:00–18:00 | 50 h | 70 h | 58.33 % | Validado |
| Semana 10 | lun–vie 08:00–18:00 | 50 h | 70 h | 58.33 % | Validado |
| Acumulado S7–S10 | 394 h acumuladas | 170 h | 224 h | 56.85 % | Validado |

### 

### 

### **Impacto económico de cómputo por semana**

## Esta tabla complementa los resultados operativos anteriores y conserva el detalle de tarifa y costos por semana.

## 

| Semana | Tarifa referencial | Costo base | Costo con EcoScheduler | Costo evitado |
| :---- | :---- | :---- | :---- | :---- |
| Semana 7 | USD 0.0104/h | USD 0.3536 | USD 0.2080 | USD 0.1456 |
| Semana 8 | USD 0.0104/h | USD 1.2480 | USD 0.5200 | USD 0.7280 |
| Semana 9 | USD 0.0104/h | USD 1.2480 | USD 0.5200 | USD 0.7280 |
| Semana 10 | USD 0.0104/h | USD 1.2480 | USD 0.5200 | USD 0.7280 |
| Acumulado S7–S10 | USD 0.0104/h | USD 4.0976 | USD 1.7680 | USD 2.3296 |

## 

## 

## **Comparación — Lo estipulado al inicio vs. resultado obtenido en la prueba**

| Métrica | Estipulado al inicio | Resultado obtenido en la prueba |
| :---- | :---- | :---- |
| Periodo | 168 h | 120 h |
| Horas encendidas | 50 h | 50 h |
| Horas apagadas / evitadas | 118 h | 70 h |
| Costo base de cómputo | USD 1.7472 | USD 1.2480 |
| Costo con EcoScheduler | USD 0.5200 | USD 0.5200 |
| Costo evitado | USD 1.2272 | USD 0.7280 |
| Reducción | 70.24 % | 58.33 % |

### **Análisis de la comparación**

El objetivo operativo definido al inicio se mantuvo: tanto en la estimación como en la prueba se consideran 50 h de funcionamiento. La diferencia principal está en la duración del periodo evaluado. La estimación inicial tomó una semana completa de 168 h, mientras que la prueba real contabilizó 120 h. Por esta razón se observaron 70 h apagadas en lugar de 118 h, una diferencia de 48 h asociada al menor periodo de evaluación.

La reducción pasó de 70.24 % estimado a 58.33 % obtenido, una diferencia de 11.91 puntos porcentuales. El costo de cómputo evitado pasó de USD 1.2272 estimados a USD 0.7280 obtenidos, una diferencia de USD 0.4992. Esta diferencia no representa un fallo de EcoScheduler: los dos resultados corresponden a periodos distintos. Durante la ventana real de 120 h, EcoScheduler mantuvo las 50 h de operación previstas y evitó 70 h de cómputo innecesario.

### **Proyección mensual y anual**

La proyección mensual original se mantiene como referencia de potencial y no como resultado medido: 720 h/mes sin automatización, 220 h/mes con EcoScheduler, 500 h/mes evitadas, 69.44 % de reducción, USD 5.20 de ahorro mensual y USD 62.40 de ahorro anual por instancia.

## **Reflexión ambiental / sostenibilidad digital**

EcoScheduler no solo contribuye a la optimización financiera, sino también a una utilización más eficiente de los recursos cloud.

Desde la perspectiva de Green IT, reducir horas de cómputo que no aportan trabajo productivo disminuye el uso innecesario de infraestructura y ayuda a reducir el cloud waste. En el periodo evaluado, el beneficio ambiental se expresa mediante la reducción de horas de operación innecesaria.

No se presenta una cifra exacta de emisiones de CO2e evitadas, debido a que el proyecto no utilizó una herramienta específica de medición directa de huella de carbono. Por esta razón, el análisis mantiene una postura conservadora y evita atribuir una reducción de emisiones que no haya sido medida de forma verificable.

Como recomendación para futuras fases, se propone incorporar una herramienta específica de medición de sostenibilidad, como AWS Customer Carbon Footprint Tool, para complementar el análisis económico con indicadores ambientales medidos directamente.

## **Anexo para bitácora — Sección 11\. Pruebas,** 

## 

| Integrante | Tipo de prueba / validación | Elemento intervenido | Resultado | Evidencia |
| :---- | :---- | :---- | :---- | :---- |
| Yolanda Marisol Alvarenga Jacobo | Validación de casos de prueba | Matriz de pruebas EcoScheduler | 10/10 aprobados (100 %) | Matriz de pruebas y registros técnicos |
| Yolanda Marisol Alvarenga Jacobo | Validación FinOps de ahorro | Métricas FinOps S7–S10 | 394 h evaluadas; 224 h apagadas; 56.85 %; USD 2.3296 evitados | Informes S7–S10 y Dashboard FinOps |

## **configuraciones o validaciones por estudianteAnexo para bitácora — Sección 12\. Participación en demo o explicación técnica**

| Integrante | Parte explicada o demostrada | Evidencia presentada | Nivel de dominio observado |
| :---- | :---- | :---- | :---- |
| Yolanda Marisol Alvarenga Jacobo | Presentación de resultados FinOps: comparación entre estimación inicial y prueba real, ahorro acumulado , proyección y sostenibilidad | Video grabado con narración y visualización del Dashboard FinOps y sus gráficos | Por completar durante la revisión del video |

Guión utilizado en el video

Desde mi rol como Analista FinOps Verde Jr., mi responsabilidad fue analizar el impacto económico de EcoScheduler y validar los resultados obtenidos durante las pruebas.

Al inicio se estimó una semana completa de 168 horas, con 50 horas de operación y 118 horas evitadas, lo que representaba una reducción esperada del 70.24 %.

Durante la prueba real se evaluaron 120 horas. La instancia permaneció encendida las 50 horas previstas y apagada durante 70 horas. Esto permitió obtener una reducción real del 58.33 % y un ahorro de cómputo de USD 0.7280 para ese periodo.

La diferencia con la estimación inicial se debe principalmente a que los periodos comparados no tuvieron la misma duración. Por lo tanto, no representa una falla de EcoScheduler, ya que durante la ventana real de prueba se mantuvo el tiempo de operación previsto y se evitaron horas de cómputo innecesarias.

En el acumulado de las Semanas 7 a 10 se evaluaron 394 horas, de las cuales 224 permanecieron apagadas. Esto representa una reducción acumulada del 56.85 % y un costo de cómputo evitado de USD 2.3296.

Como proyección, EcoScheduler podría evitar alrededor de 500 horas de ejecución al mes por instancia, equivalente a un ahorro aproximado de USD 5.20 mensuales y USD 62.40 anuales.

Desde la perspectiva FinOps y de sostenibilidad, estos resultados demuestran que automatizar los horarios de los recursos ayuda a reducir costos, disminuir el uso innecesario de infraestructura y evitar desperdicio en la nube.  
