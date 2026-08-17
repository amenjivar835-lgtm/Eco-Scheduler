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
        # Filtro base de AWS
        filtros = [
            {'Name': 'tag:EcoScheduler', 'Values': ['True']},
            {'Name': 'instance-state-name', 'Values': ['stopped']}
        ]
        
        instancias_elegibles = []
        paginador = ec2.get_paginator('describe_instances')
        paginas = paginador.paginate(Filters=filtros)
        
        for pagina in paginas:
            for reserva in pagina['Reservations']:
                for instancia in reserva['Instances']:
                    instance_id = instancia['InstanceId']
                    
                    # Convertir lista de diccionarios de tags a un solo diccionario para fácil acceso
                    tags = {tag['Key']: tag['Value'] for tag in instancia.get('Tags', [])}
                    
                    # Extraer valores de las etiquetas de negocio
                    entorno = tags.get('Environment', '')
                    es_critico = tags.get('Criticality', '') == 'High'
                    en_mantenimiento = tags.get('Maintenance', '') == 'True'
                    
                    # --- LÓGICA DE EXCLUSIÓN DE NEGOCIO ---
                    if entorno == 'Prod':
                        logger.warning(f"EXCLUSIÓN: La instancia {instance_id} fue ignorada porque es de Producción (Environment=Prod).")
                        continue
                        
                    if es_critico:
                        logger.warning(f"EXCLUSIÓN: La instancia {instance_id} fue ignorada por alta criticidad (Criticality=High).")
                        continue
                        
                    if en_mantenimiento:
                        logger.warning(f"EXCLUSIÓN: La instancia {instance_id} fue ignorada por mantenimiento (Maintenance=True).")
                        continue
                        
                    # Validar entornos permitidos
                    if entorno in ['Dev', 'Test', 'Sandbox']:
                        instancias_elegibles.append(instance_id)
                    else:
                        logger.warning(f"EXCLUSIÓN: La instancia {instance_id} ignorada. Entorno no reconocido o vacío: '{entorno}'")
                
        # Validar si hay recursos objetivo tras los filtros
        if not instancias_elegibles:
            logger.info("Operación omitida: Sin recursos objetivo tras aplicar reglas de exclusión.")
            return {'statusCode': 200, 'body': 'No se encontraron instancias válidas para encender.'}
            
        # Ejecutar encendido
        logger.info(f"Encendiendo las siguientes instancias validadas: {instancias_elegibles}")
        ec2.start_instances(InstanceIds=instancias_elegibles)
        logger.info("Proceso de encendido completado con éxito.")
        
        return {'statusCode': 200, 'body': f'Se encendieron {len(instancias_elegibles)} instancias exitosamente.'}
        
    except ClientError as e:
        codigo_error = e.response['Error']['Code']
        mensaje_error = e.response['Error']['Message']
        logger.error(f"Error crítico de AWS ({codigo_error}): {mensaje_error}")
        return {'statusCode': 500, 'body': f'Error en la operación: {codigo_error}'}
        
    except Exception as e:
        logger.error(f"Error inesperado: {str(e)}")
        return {'statusCode': 500, 'body': 'Error interno en la ejecución.'}