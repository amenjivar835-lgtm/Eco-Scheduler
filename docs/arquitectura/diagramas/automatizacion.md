# Diagrama de Flujo: Automatización Serverless Eco-Scheduler

Este documento detalla la secuencia de ejecución, toma de decisiones y trazabilidad del motor de automatización del proyecto Eco-Scheduler. El flujo ilustra cómo interactúan los servicios administrados de AWS para garantizar la optimización de costos (FinOps) sin afectar la disponibilidad operativa.

## Secuencia de Automatización

El ciclo de vida del proceso de automatización sigue un modelo orientado a eventos, ejecutándose de manera estrictamente secuencial:

1. **Desencadenador de Tiempo (Calendario):** El proceso inicia validando el calendario laboral y las reglas horarias definidas. Si no existe un evento programado para ese momento, el proceso finaliza sin ejecutar ninguna automatización.
2. **Orquestación del Evento:** Si el horario coincide con una regla activa, **Amazon EventBridge** dispara el evento de automatización.
3. **Invocación del Cómputo:** **AWS Lambda** recibe el evento emitido por EventBridge e inicializa el entorno de ejecución.
4. **Consulta de Infraestructura:** El script Serverless se conecta a la API de AWS para consultar la matriz de instancias **Amazon EC2** disponibles.
5. **Motor de Validación (Whitelisting):** El código evalúa individualmente cada instancia mediante dos filtros de seguridad secuenciales:
   * ¿La instancia cumple con los criterios de inclusión operativos?
   * ¿La instancia posee las etiquetas (tags) autorizadas de entorno seguro?
6. **Ejecución de Acción de Negocio:** Una vez validada la instancia, el sistema aplica la acción correspondiente según el horario:
   * **Inicio de jornada:** Ejecuta la orden `START` para encender el servidor.
   * **Fin de jornada / Horario no laboral:** Ejecuta la orden `STOP` para detener el servidor y reducir costos.
7. **Verificación de Estado:** Se valida si el comando de encendido o apagado fue procesado con éxito por la infraestructura. En caso de fallo, se levanta una alerta registrando el error o la excepción.

## Manejo de Exclusiones y Trazabilidad

Para cumplir con los estándares de auditoría y la metodología SRE (Site Reliability Engineering), el flujo incorpora puntos de control y registro detallado:

* **Gestión de Exclusiones:** Si una instancia EC2 no supera los criterios de inclusión o carece de la etiqueta autorizada (por ejemplo, si pertenece a un entorno de Producción), el flujo se desvía. La instancia se registra como "excluida", se guarda la advertencia en CloudWatch Logs y el proceso finaliza de forma segura para ese recurso en específico.
* **Auditoría de Ejecución:** Todas las acciones exitosas guardan metadatos críticos, incluyendo la fecha, hora, tipo de acción, ID de la instancia, resultado obtenido y la regla horaria aplicada.
* **Registro Centralizado:** Toda la información recopilada se envía y almacena de manera inmutable en **Amazon CloudWatch Logs**.

## Impacto FinOps

El proceso concluye con la generación de evidencia técnica y la actualización de los reportes de uso. Estos datos son la fuente principal para calcular las horas de cómputo interrumpidas y el ahorro económico y energético estimado derivado de la detención automatizada de los servidores virtuales.
