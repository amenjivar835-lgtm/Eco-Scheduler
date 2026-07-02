import boto3
import logging
from botocore.exceptions import ClientError

# Configuración básica del logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    logger.info("Iniciando ejecución de start_instances (Encendido inicio de jornada)")
    
    # Inicializar cliente de EC2
    ec2 = boto3.client('ec2')
    
    try:
        # Filtros: Etiqueta EcoScheduler=True y estado stopped
        filtros = [
            {'Name': 'tag:EcoScheduler', 'Values': ['True']},
            {'Name': 'instance-state-name', 'Values': ['stopped']}
        ]
        
        # Buscar instancias que cumplan los criterios
        respuesta = ec2.describe_instances(Filters=filtros)
        instancias_elegibles = []
        
        for reserva in respuesta['Reservations']:
            for instancia in reserva['Instances']:
                instancias_elegibles.append(instancia['InstanceId'])
                
        # Validar si hay recursos objetivo
        if not instancias_elegibles:
            logger.info("Operación omitida: Sin recursos objetivo (No hay instancias elegibles detenidas).")
            return {
                'statusCode': 200,
                'body': 'No se encontraron instancias para encender.'
            }
            
        # Ejecutar encendido
        logger.info(f"Encendiendo las siguientes instancias: {instancias_elegibles}")
        ec2.start_instances(InstanceIds=instancias_elegibles)
        logger.info("Proceso de encendido completado con éxito.")
        
        return {
            'statusCode': 200,
            'body': f'Se encendieron {len(instancias_elegibles)} instancias exitosamente.'
        }
        
    except ClientError as e:
        logger.error(f"Error crítico de permisos IAM o AWS: {e}")
        return {'statusCode': 500, 'body': 'Error de permisos al intentar encender instancias.'}
    except Exception as e:
        logger.error(f"Error inesperado: {str(e)}")
        return {'statusCode': 500, 'body': 'Error interno en la ejecución.'}