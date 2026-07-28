FASE 3

Semanas 7 y 8 | Programación, monitoreo, validación y análisis FinOps

Proyecto: EcoScheduler

Rol: Analista FinOps Verde Jr.

Responsable del análisis: Yolanda Marisol Alvarenga Jacobo

Estado: Versión final consolidada para revisión y aprobación del líder. Las pruebas 3 y 9 fueron validadas según confirmación del compañero responsable técnico, sin evidencia directa revisada por la responsable FinOps.

1. Resumen ejecutivo

EcoScheduler automatiza el encendido y apagado de una instancia Amazon EC2 mediante Amazon EventBridge y funciones AWS Lambda. Durante las semanas 7 y 8 se diseñó la matriz de pruebas, se validaron ejecuciones automáticas, se revisaron registros de Amazon CloudWatch y AWS CloudTrail, se comprobaron estados finales en Amazon EC2 y se consolidó el análisis económico desde la perspectiva FinOps.

Actualmente, ocho de las diez pruebas cuentan con evidencia directa revisada y están aprobadas documentalmente. Las pruebas 3, Exclusión por etiqueta, y 9, Múltiples instancias, fueron reportadas como validadas por el compañero responsable técnico; sin embargo, la responsable FinOps no revisó evidencia directa individual de esos escenarios. La cobertura documental verificable se mantiene en 80 %.

2. Objetivo y alcance

Documentar la evolución de EcoScheduler desde la definición de escenarios y primeras ejecuciones hasta la validación técnica y económica de la automatización. El rol FinOps recopila evidencias, organiza resultados, verifica la consistencia de costos y comunica hallazgos, sin sustituir las responsabilidades de implementación del equipo técnico.

3. Arquitectura y flujo operativo

Amazon EventBridge activa las funciones eco-scheduler-start-instances y eco-scheduler-stop-instances según los horarios configurados. Las funciones evalúan elegibilidad, ejecutan el cambio de estado en Amazon EC2 y registran resultados en CloudWatch Logs. CloudTrail aporta trazabilidad sobre las llamadas StartInstances y StopInstances.

Diagrama lógico simplificado

4. Matriz de pruebas y estado actual

Prueba

Escenario

Estado

1

Apagado normal

Aprobado

2

Encendido normal

Aprobado

3

Exclusión por etiqueta

Validado por compañero*

4

Exclusión de producción

Aprobado

5

Instancia ya detenida

Aprobado

6

Instancia ya encendida

Aprobado

7

Error de permisos

Aprobado

8

Ejecución programada con EventBridge

Aprobado

9

Múltiples instancias

Validado por compañero*

10

Manejo de excepciones

Aprobado

Prueba 3 — Exclusión por etiqueta

Estado: Validada según confirmación del compañero responsable técnico; la responsable FinOps no revisó evidencia directa de esta prueba.

Observación documental: no se incorporó evidencia directa de esta prueba al entregable; el resultado se registra con base en la confirmación del compañero responsable técnico.

Resultado esperado: EcoScheduler no debe iniciar ni detener la instancia cuando no cumple el criterio EcoScheduler=True.

Prueba 9 — Múltiples instancias

Estado: Validada según confirmación del compañero responsable técnico; la responsable FinOps no revisó evidencia directa de esta prueba.

Observación documental: no se incorporó evidencia directa de esta prueba al entregable; el resultado se registra con base en la confirmación del compañero responsable técnico.

Resultado esperado: EcoScheduler debe aplicar la operación programada a todas las instancias elegibles sin afectar recursos excluidos.

5. Resultados técnicos principales

Las ejecuciones START y STOP fueron verificadas mediante CloudWatch, CloudTrail y estados finales en Amazon EC2. También se comprobó el comportamiento controlado cuando una instancia ya se encontraba en el estado esperado, evitando acciones redundantes.

La lógica desplegada utiliza EcoScheduler=True. START selecciona instancias detenidas y STOP instancias en ejecución. Se excluyen recursos con Environment=Prod, Criticality=High, Maintenance=True o entornos no reconocidos.

Un registro real de AuthFailure confirmó que los errores ClientError son capturados, registrados y finalizados de manera controlada con END y REPORT.

6. Problemas encontrados y correcciones aplicadas

Confirmación de EcoScheduler=True en el código desplegado.

Separación entre validación técnica y consolidación FinOps.

Incorporación de evidencia directa para las pruebas 4 y 7.

Separación entre costo estimado, consumo acumulado, costo bruto, créditos y total facturado.

Exclusión de EBS del cálculo de ahorro por apagado.

Actualización de la matriz a ocho pruebas con evidencia directa revisada y dos validadas por confirmación técnica

6.1 Registro de problemas y correcciones

Problema 1 — Etiqueta de automatización inconsistente en documentos anteriores.

Corrección aplicada: se revisó el código desplegado y se confirmó EcoScheduler=True como criterio vigente de elegibilidad.

Resultado: la matriz, las evidencias y el análisis técnico utilizan ahora la misma etiqueta.

Estado: Resuelto.

Problema 2 — Algunas pruebas habían sido comunicadas como exitosas sin evidencia individual incorporada.

Corrección aplicada: se diferenciaron los estados Aprobado y Validado por compañero*, y solo se aprobaron las pruebas respaldadas por registros o capturas verificables.

Resultado: ocho pruebas cuentan con evidencia directa revisada. Las pruebas 3 y 9 fueron confirmadas como validadas por el compañero responsable técnico, pero la responsable FinOps no revisó evidencia directa de esos escenarios.

Estado: Cerrado documentalmente con una cobertura verificable directa de 80 %. Las pruebas 3 y 9 se registran como validadas por confirmación del compañero responsable técnico, sin evidencia directa revisada por la responsable FinOps.

Problema 3 — Riesgo de mezclar costos de la ventana de prueba con costos acumulados y facturación mensual.

Corrección aplicada: se separaron el costo estimado de cómputo, el costo de EBS, el costo bruto, los créditos aplicados y el total facturado.

Resultado: el ahorro operativo estimado no se confunde con la factura neta de AWS.

Estado: Resuelto.

Problema 4 — Falta inicial de evidencia directa para exclusión de producción y manejo de errores.

Corrección aplicada: se incorporaron registros reales de CloudWatch para Environment=Prod y AuthFailure.

Resultado: las pruebas 4, 7 y 10 quedaron respaldadas y aprobadas.

Estado: Resuelto.

6.2 Comparación antes y después de las correcciones

Antes: los resultados estaban distribuidos entre diferentes registros, algunas validaciones dependían únicamente de comunicaciones del equipo, la etiqueta de automatización no estaba unificada y los costos podían interpretarse como si pertenecieran al mismo periodo.

Después: la evidencia se relaciona con cada prueba, EcoScheduler=True quedó confirmado como criterio técnico vigente, ocho pruebas cuentan con respaldo directo, los costos están separados por alcance y periodo, y las responsabilidades técnicas y FinOps están claramente diferenciadas.

Comparación específica:

• START — Antes: ejecución reportada sin cadena documental completa. Después: EventBridge, Lambda, CloudWatch, CloudTrail y EC2 confirman el encendido.

• STOP — Antes: evidencia dispersa. Después: la regla programada, la ejecución Lambda y el estado Detenida se encuentran relacionados.

• Exclusión de producción — Antes: lógica documentada sin prueba directa. Después: CloudWatch confirma la exclusión por Environment=Prod.

• Manejo de errores — Antes: comportamiento esperado descrito. Después: AuthFailure demuestra captura y finalización controlada.

• Costos — Antes: riesgo de comparar valores de periodos distintos. Después: cálculo de prueba, EBS, costo bruto, créditos y total facturado se presentan por separado.

• Trazabilidad — Antes: algunos resultados no distinguían entre reporte técnico y evidencia directa. Después: la matriz diferencia ocho pruebas con evidencia directa revisada y dos validadas por confirmación del compañero responsable técnico.

Resultado general: el entregable pasó de una validación parcial y dispersa a una estructura consolidada con matriz, resultados documentados, problemas, correcciones, comparación antes/después, evidencias analizadas y reporte ejecutivo.

  

7. Análisis FinOps

Métrica

Resultado

Ventana analizada

34 horas

Horas programadas de funcionamiento

20 horas

Horas programadas de apagado

14 horas

Tarifa referencial

USD 0.0104/h

Costo base estimado

USD 0.3536

Costo con EcoScheduler

USD 0.2080

Costo evitado

USD 0.1456

Reducción estimada

41.18 %

La factura detallada registró USD 0.12 de cómputo EC2 y USD 0.34 de EBS, con costo bruto identificado de USD 0.46. Un crédito de -USD 0.46 compensó el total, por lo que el importe facturado fue USD 0.00. EBS no forma parte del ahorro por apagado porque continúa mientras el volumen permanece aprovisionado.

7.1 Comparación FinOps — Semanas 7 y 8

La siguiente tabla resume los principales indicadores operativos y económicos validados de las semanas 7 y 8.

Métrica

Semana 7 (validada)

Semana 8 (validada)

Periodo analizado

23 y 24 de julio de 2026

Lunes a viernes, 8:00 a. m.–6:00 p. m.

Horas de funcionamiento

20 horas

50 horas

Horas de apagado programado

14 horas

70 horas

Tarifa referencial

USD 0.0104/h

USD 0.0104/h

Costo sin EcoScheduler

USD 0.3536

USD 1.2480

Costo con EcoScheduler

USD 0.2080

USD 0.5200

Costo de cómputo evitado

USD 0.1456

USD 0.7280

Reducción estimada

41.18 %

58.33 % 

Cierre validado de la Semana 8: se analizaron 120 horas, con 50 horas de funcionamiento y 70 horas de apagado programado. Con una tarifa referencial de USD 0.0104/h, el costo estimado sin EcoScheduler fue de USD 1.2480, el costo optimizado de USD 0.5200 y el costo de cómputo evitado de USD 0.7280.

Estado de los resultados: Las semanas 7 y 8 se consideran validadas con base en los registros técnicos disponibles y el análisis FinOps consolidado.

Interpretación FinOps: La comparación evidencia que EcoScheduler reduce las horas de uso de cómputo y, en consecuencia, el costo estimado de la instancia. La Semana 7 presenta un ahorro validado de USD 0.1456, equivalente a una reducción de 41.18 %. La Semana 8 presenta un ahorro validado de USD 0.7280 y una reducción de 58.33 %.

8. Dashboard ejecutivo

Indicadores incluidos en el dashboard FinOps:

Semana 7: ahorro validado de USD 0.1456 y reducción de 41.18 %

Semana 8: ahorro validado de USD 0.7280 y reducción de 58.33 %

Comparación de horas encendidas y apagadas

Comparación de costo sin EcoScheduler y costo optimizado

Ahorro acumulado estimado

El dashboard ejecutivo está disponible en el archivo Comparacion_FinOps_Semanas_7_y_8. Presenta las semanas 7 y 8 como validadas y muestra un total acumulado de 154 horas evaluadas: 70 horas encendidas y 84 horas apagadas. El estado de las diez pruebas se mantiene documentado únicamente en la matriz de pruebas.

8.1 Evidencia visual del dashboard

Figura 6: Dashboard ejecutivo FinOps de EcoScheduler — Semanas 7 y 8. Fuente: elaboración propia.

Nota metodológica: El dashboard consolida 154 horas evaluadas: 34 horas de la Semana 7 y 120 horas de la Semana 8. De ese total, 70 horas corresponden a funcionamiento y 84 horas a apagado programado. Los costos se calcularon con una tarifa referencial de USD 0.0104 por hora para el cómputo de la instancia Amazon EC2. El cálculo excluye EBS, IPv4, transferencia de datos, impuestos, AWS Lambda, Amazon EventBridge, Amazon CloudWatch y otros cargos.

Descripción: El dashboard ejecutivo consolida los resultados validados de ambas semanas. Las 154 horas evaluadas corresponden a 34 horas de la Semana 7 y 120 horas de la Semana 8. Del total acumulado, 70 horas corresponden a funcionamiento y 84 horas a apagado programado. El costo de cómputo evitado acumulado es de USD 0.8736, calculado con una tarifa referencial de USD 0.0104 por hora.

Análisis: La visualización facilita la comparación entre el escenario base y el escenario optimizado con EcoScheduler. Permite identificar de manera rápida el efecto de la automatización sobre el tiempo de uso de la instancia y el costo de cómputo, sin mezclar los valores de almacenamiento EBS, créditos o facturación neta.

Conclusión: El dashboard funciona como reporte ejecutivo del proyecto y complementa la matriz de pruebas y las evidencias técnicas. Su contenido permite comunicar el impacto operativo y económico de EcoScheduler de forma clara y verificable.

9. Evidencias seleccionadas

Se incorporan seis capturas representativas para demostrar programación, ejecución, configuración, manejo de errores, costos y resultados ejecutivos. Las pruebas 3 y 9 fueron reportadas como validadas por el compañero responsable técnico, aunque la responsable FinOps no revisó evidencia directa individual de esos escenarios.

Evidencia 1 — Ejecución START exitosa en CloudWatch

Figura 1: Ejecución START exitosa en CloudWatch. Fuente: Amazon CloudWatch Logs.

Análisis: El registro de Amazon CloudWatch muestra una ejecución correcta de la función eco-scheduler-start-instances. La secuencia confirma el inicio de la función, la identificación del recurso elegible y la finalización exitosa del proceso sin errores visibles. Esta evidencia se relaciona con la prueba 2, Encendido normal, y complementa la prueba 8, Ejecución programada con EventBridge.

Conclusión: La función START procesó la instancia elegible y dejó un registro verificable de la ejecución, por lo que el resultado se considera validado con evidencia directa.

Evidencia 2 — Programación de STOP en EventBridge

Figura 2: Programación de STOP en EventBridge. Fuente: Amazon EventBridge.

Análisis: La captura de Amazon EventBridge muestra la programación configurada para ejecutar la función de apagado. La regla se encuentra vinculada con la función Lambda correspondiente y representa el inicio de la cadena automática EventBridge → Lambda STOP → Amazon EC2. Esta evidencia se relaciona con la prueba 8, Ejecución programada con EventBridge, y complementa la prueba 1, Apagado normal.

Conclusión: La automatización de STOP dispone de una regla programada y de un destino técnico identificable, lo que respalda su ejecución automática.

Evidencia 3 — Etiquetas de la instancia de prueba

Figura 3: Etiquetas de la instancia de prueba. Fuente: Amazon EC2.

Análisis: La captura de Amazon EC2 muestra las etiquetas de la instancia de prueba, incluyendo Environment=Dev y EcoScheduler=True. Esto confirma que el recurso observado cumple el criterio vigente de elegibilidad y que no pertenece a un ambiente de producción. La evidencia respalda la consistencia entre el código desplegado, la matriz de pruebas y la documentación técnica.

Conclusión: La etiqueta EcoScheduler=True queda confirmada como condición activa de selección para las funciones START y STOP.

Evidencia 4 — Error AuthFailure capturado

Figura 4: Error AuthFailure capturado. Fuente: Amazon CloudWatch Logs.

Análisis: El registro de CloudWatch muestra un error AuthFailure capturado por la función Lambda. El código y el mensaje del error quedaron registrados y la ejecución finalizó de forma controlada con END y REPORT, sin una terminación abrupta. Esta evidencia se relaciona directamente con la prueba 7, Error de permisos, y también respalda la prueba 10, Manejo de excepciones.

Conclusión: La función registra el fallo de AWS de forma clara y mantiene un comportamiento controlado, por lo que ambas pruebas cuentan con evidencia directa.

Evidencia 5 — Costos y facturación observados

Figura 5: Costos y facturación observados. Fuente: AWS Billing and Cost Management.

Análisis: La captura muestra el resumen de costos y facturación disponible en AWS. La información permite diferenciar el costo bruto identificado, el crédito aplicado y el total facturado. Esta evidencia respalda el análisis FinOps de la Semana 7 y confirma que el ahorro operativo estimado de USD 0.1456 debe mantenerse separado de la factura neta de AWS. También confirma que el costo de EBS continúa aunque la instancia se encuentre detenida, por lo que no forma parte del ahorro por apagado.

Conclusión: La evidencia económica es consistente con la metodología utilizada y evita mezclar costos de cómputo, almacenamiento, créditos y total facturado.

10. Conclusiones

EcoScheduler demostró que puede automatizar de manera controlada el encendido y apagado de una instancia de prueba mediante una cadena verificable de EventBridge, Lambda, EC2, CloudWatch y CloudTrail. En conjunto, las semanas 7 y 8 acumulan 154 horas evaluadas: 70 horas de funcionamiento y 84 horas de apagado programado. La Semana 7 registró una reducción de 41.18 % y un costo evitado de USD 0.1456; la Semana 8 registró una reducción de 58.33 % y un costo evitado de USD 0.7280. El costo de cómputo evitado acumulado es de USD 0.8736.

11. Recomendaciones

Mantener la matriz como fuente principal del estado de las pruebas, conservar EcoScheduler=True como criterio documentado y mantener separados los costos de cómputo y almacenamiento. Las pruebas 3 y 9 deben permanecer identificadas como validadas por confirmación del compañero responsable técnico, aclarando que la responsable FinOps no revisó evidencia directa.