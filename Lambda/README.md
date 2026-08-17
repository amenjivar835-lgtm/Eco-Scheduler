Documentación Técnica: Lógica de Cómputo Serverless (AWS Lambda) 
Como parte del pilar de automatización y FinOps Verde del proyecto Eco-Scheduler, se desarrollaron dos funciones Serverless utilizando Python 3 y la librería boto3 para la interacción nativa con la API de AWS.
Ambas funciones (start_instances y stop_instances) comparten una arquitectura lógica idéntica, orientada a la protección de la disponibilidad y la reducción de costos mediante la evaluación dinámica de etiquetas (Tags).

1. Flujo de Ejecución y Extracción de Metadatos
Para optimizar el rendimiento, el cliente de EC2 se inicializa fuera del lambda_handler, reutilizando la conexión en invocaciones sucesivas. El flujo comienza aplicando un filtro base directo a la API de AWS para capturar únicamente las instancias que pertenecen al proyecto (tag:EcoScheduler = True) y que se encuentran en el estado objetivo (stopped para encendido, running para apagado). Posteriormente, el código extrae la matriz de metadatos devuelta por el paginador de AWS y la convierte en un diccionario de Python, permitiendo una lectura inmediata y eficiente de las variables de entorno (Environment), criticidad (Criticality) y ventanas de mantenimiento (Maintenance).

2. Manejo de Reglas de Negocio (Whitelisting y Exclusión)
Para garantizar que la estrategia de ahorro no impacte la continuidad del negocio, la automatización opera bajo un modelo de Lista Blanca (Whitelisting) y Exclusión Activa:
Exclusión de Seguridad: Si el script detecta que una instancia pertenece a Producción (Environment='Prod'), posee alta criticidad (Criticality='High') o se encuentra en mantenimiento (Maintenance='True'), la iteración se interrumpe inmediatamente para ese recurso mediante la instrucción continue. Esto asegura que nunca se emita una orden de encendido/apagado a servidores vitales.
Whitelisting: Una instancia solo se agrega a la lista de ejecución si declara explícitamente pertenecer a los entornos seguros para interrupción: Dev, Test o Sandbox. Cualquier otro valor resulta en la omisión del recurso.

3. Manejo de Errores y Trazabilidad (Auditoría)
El código integra el módulo nativo logging para garantizar la observabilidad total en Amazon CloudWatch, cumpliendo con los requisitos de auditoría. Se utilizan diferentes niveles de trazabilidad:
logger.info: Registra el inicio, fin y éxito de las operaciones.
logger.warning: Documenta el ID exacto y el motivo de exclusión cada vez que el motor ignora una máquina (ej. por ser de Producción o no tener un entorno válido).
logger.error: Integrado dentro de un bloque try/except diseñado para capturar excepciones específicas de la librería boto3 (ClientError), como credenciales inválidas o IDs malformados. Esto permite registrar el fallo detallado sin provocar una caída abrupta (crash) del servicio.

4. Código Fuente Final
Función de Encendido (start_instances.py)
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


Función de Encendido (stop_instances.py)
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
        # Filtro base de AWS
        filtros = [
            {'Name': 'tag:EcoScheduler', 'Values': ['True']},
            {'Name': 'instance-state-name', 'Values': ['running']}
        ]
        
        instancias_elegibles = []
        paginador = ec2.get_paginator('describe_instances')
        paginas = paginador.paginate(Filters=filtros)
        
        for pagina in paginas:
            for reserva in pagina['Reservations']:
                for instancia in reserva['Instances']:
                    instance_id = instancia['InstanceId']
                    
                    tags = {tag['Key']: tag['Value'] for tag in instancia.get('Tags', [])}
                    
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
                        
                    if entorno in ['Dev', 'Test', 'Sandbox']:
                        instancias_elegibles.append(instance_id)
                    else:
                        logger.warning(f"EXCLUSIÓN: La instancia {instance_id} ignorada. Entorno no reconocido o vacío: '{entorno}'")
                
        if not instancias_elegibles:
            logger.info("Operación omitida: Sin recursos objetivo tras aplicar reglas de exclusión.")
            return {'statusCode': 200, 'body': 'No se encontraron instancias válidas para apagar.'}
            
        # Ejecutar apagado
        logger.info(f"Apagando las siguientes instancias validadas: {instancias_elegibles}")
        ec2.stop_instances(InstanceIds=instancias_elegibles)
        logger.info("Proceso de apagado completado con éxito.")
        
        return {'statusCode': 200, 'body': f'Se apagaron {len(instancias_elegibles)} instancias exitosamente.'}
        
    except ClientError as e:
        codigo_error = e.response['Error']['Code']
        mensaje_error = e.response['Error']['Message']
        logger.error(f"Error crítico de AWS ({codigo_error}): {mensaje_error}")
        return {'statusCode': 500, 'body': f'Error en la operación: {codigo_error}'}
        
    except Exception as e:
        logger.error(f"Error inesperado: {str(e)}")
        return {'statusCode': 500, 'body': 'Error interno en la ejecución.'}

