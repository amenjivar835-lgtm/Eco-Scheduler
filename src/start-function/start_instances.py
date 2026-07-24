import boto3
import logging
from botocore.exceptions import ClientError

# Configuración básica del logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# OPTIMIZACIÓN 1: Inicializar el cliente fuera del handler para reutilizar la conexión
ec2 = boto3.client('ec2')

def lambda_handler(event, context):
    logger.info("Iniciando ejecución de start_instances (Encendido inicio de jornada)")
    
    try:
        # Filtros: Etiqueta EcoScheduler=True y estado stopped
        filtros = [
            {'Name': 'tag:EcoScheduler', 'Values': ['True']},
            {'Name': 'instance-state-name', 'Values': ['stopped']}
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
        # OPTIMIZACIÓN 3: Captura de código de error exacto de AWS
        codigo_error = e.response['Error']['Code']
        mensaje_error = e.response['Error']['Message']
        logger.error(f"Error crítico de AWS ({codigo_error}): {mensaje_error}")
        return {'statusCode': 500, 'body': f'Error en la operación: {codigo_error}'}
        
    except Exception as e:
        logger.error(f"Error inesperado: {str(e)}")
        return {'statusCode': 500, 'body': 'Error interno en la ejecución.'}