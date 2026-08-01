# Lógica de la Función de Encendido (start_instances.py)

[cite_start]**Propósito:** Función *serverless* homóloga a la de apagado, diseñada para iniciar las instancias EC2 de forma automática justo antes de que comience la jornada laboral[cite: 203].

[cite_start]**Disparador:** Amazon EventBridge (Ejecución programada, por ejemplo, a las 8:00 AM)[cite: 202].

### Flujo Operativo:

1. [cite_start]**Inicialización:** Se instancia el cliente de EC2 a través de la librería `boto3`[cite: 204].
2. [cite_start]**Consulta y Filtrado:** Se aplican filtros de búsqueda para ubicar máquinas que tengan la etiqueta `EcoScheduler=True` y que su estado actual sea `stopped` (detenida)[cite: 205].
3. [cite_start]**Extracción y Ejecución:** Se recopilan los identificadores (`InstanceId`) elegibles y, si existen máquinas en la lista, se ejecuta directamente el método `start_instances`[cite: 206].
4. [cite_start]**Registro (CloudWatch):** Se documenta la acción de encendido exitoso en los logs, garantizando así la trazabilidad operativa completa del sistema[cite: 207].

  ---

## Responsable

**Nombre:** Jafet Hernández 
**Rol:** Desarrollador Serverless Jr.