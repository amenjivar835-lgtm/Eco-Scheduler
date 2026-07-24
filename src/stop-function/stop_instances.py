import boto3
import logging
from botocore.exceptions import ClientError

# Configuración básica del logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# OPTIMIZACIÓN 1: Inicializar el cliente fuera del handler para reutilizar la conexión
ec2 = boto3.client('ec2')

def lambda_handler(event, context):
    logger.info("Iniciando ejecución de stop_instances (Apagado fin de jornada)")
    
    try:
        # Filtros: Etiqueta EcoScheduler=True y estado running
        filtros = [
            {'Name': 'tag:EcoScheduler', 'Values': ['True']},
            {'Name': 'instance-state-name', 'Values': ['running']}
        ]
        
        instancias_elegibles = []
        
        # OPTIMIZACIÓN 2: Uso de paginador para manejar escenarios con cientos de instancias
        paginador = ec2.get_paginator('describe_instances')
        paginas = paginador.paginate(Filters=filtros)
        
        for pagina in paginas:
            for reserva in pagina['Reservations']:
                for instancia in reserva['Instances']:
                    instancias_elegibles.append(instancia['InstanceId'])
                
        # Validar si hay recursos objetivo
        if not instancias_elegibles:
            logger.info("Operación omitida: Sin recursos objetivo (No hay instancias elegibles encendidas).")
            return {
                'statusCode': 200,
                'body': 'No se encontraron instancias para apagar.'
            }
            
        # Ejecutar apagado
        logger.info(f"Apagando las siguientes instancias: {instancias_elegibles}")
        ec2.stop_instances(InstanceIds=instancias_elegibles)
        logger.info("Proceso de apagado completado con éxito.")
        
        return {
            'statusCode': 200,
            'body': f'Se apagaron {len(instancias_elegibles)} instancias exitosamente.'
        }
        
    except ClientError as e:
        # OPTIMIZACIÓN 3: Captura de código de error exacto de AWS
        codigo_error = e.response['Error']['Code']
        mensaje_error = e.response['Error']['Message']
        logger.error(f"Error crítico de AWS ({codigo_error}): {mensaje_error}")
        return {'statusCode': 500, 'body': f'Error en la operación: {codigo_error}'}
        
    except Exception as e:
        logger.error(f"Error inesperado: {str(e)}")
        return {'statusCode': 500, 'body': 'Error interno en la ejecución.'}