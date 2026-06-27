# Estrategia de Manejo de Errores y Excepciones

Para garantizar la resiliencia de Eco-Scheduler, la lógica principal de ambas funciones Lambda se envuelve en bloques de control `try-except`. Se han tipificado y gestionado los siguientes escenarios:

* **Errores de Permisos (IAM):** Si el rol de ejecución carece de los privilegios necesarios (ej. `ec2:StopInstances`), `boto3` devolverá una excepción `ClientError (AccessDenied)`. El bloque *except* captura el error, registra el fallo crítico y finaliza la función de forma controlada.
* **Errores de Conectividad/Timeout:** Si la API de AWS no responde dentro del tiempo máximo de ejecución de Lambda, se captura y registra un error de `TimeoutException`.
* **Ausencia de Recursos Elegibles (No es error):** Si la consulta devuelve un arreglo vacío (ej. las instancias ya se apagaron manualmente), se detecta mediante la condicional `if not instancias_elegibles:`. Se registra el evento como *"Operación omitida: Sin recursos objetivo"* y termina exitosamente.
* **Registro de Fallos (Logging):** Toda excepción capturada genera un log con severidad `ERROR` en Amazon CloudWatch, incluyendo la traza del error (*stack trace*) y la fecha exacta para facilitar la depuración.

 ---

## Responsable

**Nombre:** Jafet Hernández 
**Rol:** Desarrollador Serverless Jr.