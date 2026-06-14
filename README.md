# Eco-Scheduler 
**Optimización de Energía Cloud mediante Automatización Serverless**

Eco-Scheduler es un prototipo de automatización enfocado en la práctica de **FinOps Verde**. Su objetivo principal es reducir el consumo energético digital y los costos operativos mediante el apagado y encendido programado de instancias cloud de desarrollo y pruebas durante horarios no laborales.

## Arquitectura Técnica Inicial
La solución está diseñada sobre la nube de AWS utilizando:
*   **AWS Lambda:** Lógica de negocio (Python) para las acciones de Start/Stop.
*   **Amazon EventBridge:** Programador de eventos cronológicos para disparar las funciones.
*   **Amazon CloudWatch:** Registro y trazabilidad de ejecuciones.

## Estructura del Repositorio
*   `/src`: Código fuente de la automatización.
    *   `start_instances.py`: Función Lambda encargada de iniciar los recursos.
    *   `stop_instances.py`: Función Lambda encargada de detener los recursos.
    *   `requirements.txt`: Dependencias de Python (boto3).