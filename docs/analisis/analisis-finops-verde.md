# Análisis FinOps Verde

**Rol Responsable:** Analista FinOps Verde Jr.

## Objetivo del Análisis
El objetivo de este documento es establecer la justificación financiera y ambiental del proyecto Eco-Scheduler, demostrando cómo la automatización de la infraestructura en la nube genera un impacto positivo directo tanto en la reducción de costos operativos como en la disminución de la huella de carbono.

## Problema Identificado: Consumo Ocioso de Instancias EC2
En entornos de desarrollo y pruebas, es común que las instancias de Amazon EC2 permanezcan encendidas 24/7. Sin embargo, estas instancias solo son utilizadas activamente durante las jornadas laborales (aproximadamente 10 horas al día, de lunes a viernes). El tiempo restante, la infraestructura sigue consumiendo energía y generando facturación sin aportar ningún valor real al negocio.

## ¿Qué es el Cloud Waste?
El "Cloud Waste" o desperdicio en la nube se refiere a la subutilización de recursos computacionales aprovisionados por los que se está pagando. En este contexto, mantener instancias de desarrollo encendidas durante la noche, fines de semana o días festivos constituye un claro ejemplo de Cloud Waste, impactando negativamente los presupuestos tecnológicos.

## Enfoque FinOps
La metodología FinOps promueve una cultura de responsabilidad financiera en el uso de la nube. Bajo este enfoque, el objetivo principal es maximizar el valor de cada dólar invertido. Eco-Scheduler se alinea con este principio garantizando que la organización **pague únicamente por los recursos durante el tiempo exacto en que aportan valor**, eliminando el gasto asociado a horas ociosas.

## Enfoque Green IT (TI Sostenible)
El consumo energético de los centros de datos es una fuente significativa de emisiones de carbono. El enfoque Green IT busca minimizar este impacto ambiental. Al reducir el tiempo de ejecución innecesario de las instancias EC2 mediante Eco-Scheduler, disminuimos la demanda de recursos físicos subyacentes, promoviendo una infraestructura tecnológica más sostenible y ecológica.

## Aporte del Rol dentro del Proyecto
Como Analista FinOps Verde Jr., mi responsabilidad radica en medir, analizar y visibilizar el impacto de estas automatizaciones. Esto implica definir las líneas base de consumo, estimar las proyecciones de ahorro económico y documentar cómo la solución técnica elegida se traduce en un modelo operativo eficiente y responsable con el medio ambiente.

## Relación con los Servicios Core de AWS
El ecosistema de Eco-Scheduler utiliza servicios nativos de AWS para ejecutar este modelo de eficiencia:
- **Amazon EC2:** El recurso final que se optimiza, evitando su ejecución ociosa.
- **Amazon EventBridge:** Actúa como el cronómetro del sistema, disparando reglas programadas en horarios específicos (inicio de jornada y fin de jornada) sin requerir intervención humana.
- **AWS Lambda:** Ejecuta la lógica "Serverless" que enciende o apaga las instancias EC2, operando de manera altamente eficiente y cobrando solo por los milisegundos de ejecución.
- **Amazon CloudWatch:** Permite observar el comportamiento del sistema, registrando las ejecuciones de Lambda para garantizar la trazabilidad, depuración y validación del cumplimiento de las reglas.

## Conclusión
Eco-Scheduler no es solo un proyecto de automatización técnica; es una iniciativa integral que responde a la necesidad de implementar prácticas de FinOps y Green IT. Demuestra de manera tangible cómo una gestión inteligente de recursos cloud puede proteger el presupuesto corporativo mientras promueve la responsabilidad medioambiental.


---

## Responsable

**Nombre:** Marisol Jacobo  
**Rol:** Analista FinOps Verde Jr.
