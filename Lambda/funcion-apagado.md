# Lógica de la Función de Apagado (stop_instances.py)

**Propósito:** Función *serverless* idempotente en AWS Lambda (Python/boto3) del proyecto Eco-Scheduler, diseñada para detener instancias de EC2 al finalizar la jornada laboral.

**Disparador:** Amazon EventBridge (Ejecución programada a las 6:00 PM).

### Flujo Operativo:

1. **Inicialización:** Se instancia el cliente de EC2 utilizando la librería `boto3`.
2. **Consulta y Filtrado:** Se ejecuta `describe_instances` con dos filtros estrictos:
   * Etiqueta `EcoScheduler` con valor `True`.
   * Estado de la instancia en `running` (en ejecución).
3. **Extracción:** Se recopilan exclusivamente los identificadores (`InstanceId`) de las máquinas que coinciden con los filtros.
4. **Ejecución:** Si existen instancias elegibles, se invoca el método `stop_instances` aplicándolo a la lista de identificadores.
5. **Registro (CloudWatch):** 
   * **Éxito:** Se genera un log detallando fecha, hora, `InstanceId` afectados y el motivo (fin de jornada).
   * **Sin acciones:** Si la lista está vacía, se registra que no se encontraron recursos ociosos.

   ---

## Responsable

**Nombre:** Jafet Hernández 
**Rol:** Desarrollador Serverless Jr.
