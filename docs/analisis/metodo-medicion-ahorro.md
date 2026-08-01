# Definición del método de medición del ahorro

Para evaluar el impacto real de la implementación de **Eco-Scheduler**, el método de medición se basará en la comparación directa entre el consumo proyectado de una instancia EC2 sin ningún tipo de automatización, y el consumo real tras la aplicación de nuestra solución de encendido y apagado programado. Esto nos permitirá cuantificar de manera objetiva tanto el ahorro económico como la reducción en el consumo energético, alineándonos con las mejores prácticas de FinOps y sostenibilidad digital (Green IT).

### Línea base de comparación

Para realizar la medición, estableceremos dos escenarios claros:

* **Escenario sin automatización:** Representa el modelo tradicional donde la instancia EC2 permanece encendida de forma ininterrumpida, operando 24 horas al día, los 7 días de la semana, lo que genera un gasto continuo independientemente de si los recursos están siendo utilizados.
* **Escenario con Eco-Scheduler:** Representa nuestro modelo optimizado, donde la instancia EC2 se mantiene activa exclusivamente durante el horario laboral establecido, deteniéndose automáticamente fuera de estas horas para evitar el desperdicio de recursos de cómputo.

### Fórmulas utilizadas

Para estandarizar la medición del ahorro, utilizaremos las siguientes fórmulas:

* **Horas evitadas** = Horas sin automatización - Horas con Eco-Scheduler.
* **Porcentaje de ahorro** = (Horas evitadas / Horas sin automatización) × 100.
* **Costo mensual estimado** = Horas activas mensuales × Precio por hora de la instancia.
* **Ahorro estimado** = Costo sin automatización - Costo con Eco-Scheduler.

### Aplicación de los datos base

Tomando como referencia una instancia EC2 de tipo `t3.micro`, hemos proyectado los siguientes datos que servirán como base para la validación del proyecto:

* **720 horas mensuales** de consumo en el escenario sin automatización (24 horas × 30 días).
* **220 horas mensuales** de consumo proyectado con Eco-Scheduler (10 horas diarias × 22 días hábiles).
* **500 horas evitadas** mensualmente de procesamiento innecesario.
* **69.44% de ahorro estimado** en el tiempo de ejecución y, proporcionalmente, en los costos de cómputo asociados.

### Indicadores FinOps para medir el ahorro

A continuación, se detallan los indicadores clave (KPIs) que utilizaremos para monitorear y reportar el éxito de la optimización:

| Indicador | Descripción | Cómo se mide | Utilidad para el proyecto |
| :--- | :--- | :--- | :--- |
| **Horas sin automatización** | Tiempo total mensual proyectado sin apagado. | 24 horas × total de días del mes. | Sirve como línea base principal para comparar el gasto original. |
| **Horas con Eco-Scheduler** | Tiempo real de la instancia encendida al mes. | Horas diarias de trabajo × días hábiles. | Muestra el consumo optimizado tras la implementación. |
| **Horas evitadas** | Tiempo de cómputo que se dejó de consumir. | Resta entre las horas sin automatización y las horas con Eco-Scheduler. | Cuantifica la reducción del desperdicio de recursos (waste). |
| **Porcentaje de ahorro** | Proporción del tiempo y costo reducido. | (Horas evitadas / Horas sin automatización) × 100. | Brinda una métrica rápida del éxito de la optimización FinOps. |
| **Costo mensual antes** | Gasto económico proyectado sin intervención. | Horas sin automatización × precio por hora. | Establece el presupuesto original necesario. |
| **Costo mensual después** | Gasto económico real con la solución activa. | Horas con Eco-Scheduler × precio por hora. | Demuestra el costo final del recurso optimizado. |
| **Ahorro mensual estimado** | Diferencia económica neta a favor. | Costo mensual antes - Costo mensual después. | Es el valor financiero tangible del proyecto. |
| **Evidencia de ejecución** | Confirmación del apagado y encendido. | Revisión de logs en AWS. | Garantiza que la automatización funciona correctamente. |
| **Relación con Green IT** | Reducción de la huella de carbono estimada. | Proporcional a las 500 horas evitadas. | Valida el impacto positivo en la sostenibilidad digital del proyecto. |

### Forma de comprobación en AWS

La verificación técnica de este ahorro en la infraestructura de AWS se realizará de forma sencilla y transparente mediante la revisión de:

* El estado actual e histórico de la instancia EC2.
* La configuración activa de las reglas programadas en Amazon EventBridge.
* Los registros de ejecución exitosa de las funciones de AWS Lambda.
* Los logs generados en Amazon CloudWatch.
* La comparación entre las horas activas facturadas antes de la implementación y las registradas después.
* La estimación reflejada en el explorador de costos (Cost Explorer) de AWS.

### Aclaración sobre costos adicionales

Es importante destacar que el cálculo base de este análisis mide de forma directa las horas de cómputo de nuestra instancia EC2. Aunque el detener la instancia mediante Eco-Scheduler reduce significativamente el costo de ejecución activo, esto no elimina necesariamente todos los costos asociados a la infraestructura en la nube. 

Durante el tiempo en que la instancia permanece detenida, pueden seguir generándose cargos por otros servicios y recursos que se mantienen aprovisionados. Entre estos se incluyen el almacenamiento de los volúmenes de Amazon EBS, la retención de snapshots de respaldo, o el uso de direcciones IP elásticas que sigan vinculadas al entorno. 

Por esta razón, el 69.44% calculado debe interpretarse como una estimación inicial y directa del ahorro operativo en capacidad de cómputo. Para lograr una medición financiera integral y precisa al finalizar el mes, será fundamental contrastar estos datos teóricos revisando herramientas nativas de facturación y monitoreo, como AWS Cost Explorer y los registros consolidados en Amazon CloudWatch.

La definición y seguimiento de este método nos permitirá validar con datos concretos si Eco-Scheduler cumple exitosamente con nuestros tres objetivos fundamentales: generar un ahorro económico medible, mejorar la eficiencia operativa de la nube y contribuir activamente a la sostenibilidad digital de la organización.


---

## Responsable

**Nombre:** Marisol Jacobo  
**Rol:** Analista FinOps Verde Jr.
