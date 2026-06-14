import boto3
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    """
    Función Lambda para apagar instancias EC2 elegibles al final de la jornada.
    Fase 2: Pendiente de implementar lógica de filtrado por etiquetas (tags).
    """
    logger.info("Iniciando ejecución de stop_instances")
    
    # TODO: Inicializar cliente de EC2 (boto3)
    # TODO: Buscar instancias con la etiqueta correspondiente
    # TODO: Ejecutar stop_instances()
    
    logger.info("Ejecución finalizada")
    return {
        'statusCode': 200,
        'body': 'Proceso de apagado completado.'
    }