import boto3
import logging

# Configuración básica del logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    """
    Función Lambda para encender instancias EC2 elegibles al inicio de la jornada.
    Fase 2: Pendiente de implementar lógica de filtrado por etiquetas (tags).
    """
    logger.info("Iniciando ejecución de start_instances")
    
    # TODO: Inicializar cliente de EC2 (boto3)
    # TODO: Buscar instancias con la etiqueta correspondiente
    # TODO: Ejecutar start_instances()
    
    logger.info("Ejecución finalizada")
    return {
        'statusCode': 200,
        'body': 'Proceso de encendido completado.'
    }