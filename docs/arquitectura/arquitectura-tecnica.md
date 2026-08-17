Arquitectura de la solución 

La arquitectura del proyecto Eco-Scheduler está diseñada bajo un modelo Serverless (sin servidor) y orientada a eventos. Este diseño garantiza alta disponibilidad, cobro exacto por milisegundo de uso y nula intervención humana. El flujo conecta servicios de orquestación, cómputo, infraestructura y observabilidad de forma segura y automatizada. 

Componentes utilizados
La solución se integra mediante los siguientes servicios nativos de AWS:
AWS Lambda (Cómputo Serverless): Es el cerebro de la automatización. Ejecuta los scripts en Python (Boto3) que contienen la lógica de negocio, evalúan dinámicamente las etiquetas (tags) de los servidores y envían las órdenes de encendido y apagado.
Amazon EventBridge (Orquestador de Eventos): Actúa como el reloj maestro del sistema. Utiliza expresiones matemáticas Cron para disparar de forma asíncrona las funciones Lambda en los horarios estrictos definidos: 8:00 a.m. (inicio de jornada) y 6:00 p.m. (fin de jornada).
Amazon EC2 (Infraestructura): Representa los servidores virtuales objetivo. Son los recursos sobre los cuales recae el impacto de la automatización y donde se materializa el ahorro de costos del pilar FinOps.
Amazon CloudWatch (Observabilidad y Auditoría): Es el componente de trazabilidad. Captura y almacena todos los registros (logs) emitidos por Lambda, guardando evidencias verificables de ejecuciones exitosas, exclusiones preventivas de seguridad y manejo de errores.
AWS IAM (Seguridad y Control de Acceso): Proporciona el Marco de Confianza. A través de un Execution Role (Rol de Ejecución), otorga a Lambda los permisos de menor privilegio estrictamente necesarios para leer/modificar estados en EC2 y escribir registros en CloudWatch, previniendo accesos no autorizados.


Flujo de automatización
El ciclo de vida automatizado del sistema sigue este proceso paso a paso:
Desencadenador (Trigger): Amazon EventBridge detecta que se ha cumplido el horario programado (ej. 6:00 p.m. para reducir costos) e invoca automáticamente a la función Lambda correspondiente.
Evaluación de Metadatos: La función Lambda consulta a la API de EC2 para enlistar las instancias y extrae un diccionario con sus etiquetas, identificando el entorno (Environment), criticidad (Criticality) y ventanas de mantenimiento (Maintenance).
Exclusión de Seguridad (SRE): Si el código detecta que una instancia pertenece a Producción (Prod), es Altamente Crítica o está en Mantenimiento, interrumpe el proceso para ese recurso y lo ignora para evitar caídas del sistema.
Acción por Lista Blanca: Lambda emite el comando de apagado o encendido exclusivamente a las instancias validadas que pertenecen a entornos de prueba (Dev, Test, Sandbox).
Auditoría Activa: Durante todo el flujo, la función envía eventos de registro (INFO, WARNING, ERROR) hacia Amazon CloudWatch, documentando la operación completa para el informe final de la empresa.


Implementación técnica
Funciones serverless (Start / Stop) La automatización principal de Eco-Scheduler está sustentada en dos funciones AWS Lambda desarrolladas en el lenguaje Python e integradas con el SDK de AWS (boto3).
eco-scheduler-start-instances: Se encarga de evaluar la matriz de servidores detenidos y enviar el comando de inicialización al comenzar la jornada operativa.
eco-scheduler-stop-instances: Identifica la infraestructura de cómputo en ejecución y aplica la detención automatizada para evitar facturación por capacidad ociosa.
Optimización de código: Como mejora de rendimiento, el cliente de EC2 se inicializa en la capa global (fuera de la función lambda_handler), permitiendo la reutilización de la conexión de red en invocaciones sucesivas.

Programación de eventos (EventBridge) 
La autonomía del sistema se logró implementando una arquitectura orientada a eventos mediante reglas Cron en Amazon EventBridge, considerando el estándar UTC para los cálculos horarios:
Regla de Encendido (Encendido-Diario-8AM): Se configuró la expresión cron(0 14 ? * MON-FRI *). Esto instruye a AWS ejecutar el encendido a las 14:00 UTC, equivalente matemáticamente a las 08:00 a.m. (hora local El Salvador, UTC-6) de lunes a viernes.
Regla de Apagado (Apagado-Diario-6PM): Se utilizó la expresión cron(0 0 ? * TUE-SAT *). El sistema dispara el evento a la medianoche UTC, lo que se traduce con precisión a las 06:00 p.m. hora local de lunes a viernes.

Criterios de inclusión/exclusión (etiquetas) 
La interacción con los recursos no es indiscriminada; está gobernada por un motor de evaluación dinámica de etiquetas (Tags) para proteger la operación:
Filtro Base: Solo se evalúan instancias que cuenten con la etiqueta EcoScheduler=True.
Protección de Disponibilidad (Exclusión Activa): A nivel de código, se iteran las etiquetas convirtiéndolas en un diccionario de Python. Si la lógica detecta que el recurso pertenece a Producción (Environment='Prod'), es crítico (Criticality='High') o está bajo mantenimiento (Maintenance='True'), el ciclo se interrumpe inmediatamente para ese servidor mediante la instrucción continue.
Whitelisting (Lista Blanca): La función Lambda exige un enfoque de "confianza cero". Solo se aprueba la reducción de costos si la máquina declara de forma explícita pertenecer a los entornos permitidos: Dev, Test o Sandbox.

Seguridad y permisos IAM 
La arquitectura opera estrictamente bajo el principio de menor privilegio (Least Privilege). A las funciones Lambda se les asignó un rol de ejecución de IAM que las autoriza de forma granular. El código únicamente tiene la capacidad de consultar estados (DescribeInstances) y modificar el estado de encendido/apagado (StartInstances, StopInstances), sin acceso a la eliminación de infraestructura ni a la manipulación de los datos internos de los servidores. 

Monitoreo (CloudWatch Logs) 
El proyecto cuenta con trazabilidad robusta y auditoría técnica mediante la integración del módulo nativo logging de Python directamente con Amazon CloudWatch:
Registro Operativo (INFO): Documenta el inicio, el fin y la confirmación de la cantidad de instancias afectadas exitosamente.
Auditoría FinOps (WARNING): Cada vez que una instancia es omitida por reglas de negocio, se genera una alerta registrando el ID del servidor y el motivo exacto de la exclusión (por ejemplo, "ignorada porque es de Producción").
Manejo de Excepciones (ERROR): Se implementaron bloques try/except que capturan fallas de la librería boto3 (ClientError), como identificadores malformados o fallos de credenciales. Esto evita la interrupción abrupta del servicio y registra el código del error en CloudWatch para su diagnóstico.

