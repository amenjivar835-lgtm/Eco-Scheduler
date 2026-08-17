# Orquestación de Eventos: Amazon EventBridge

Este directorio documenta la configuración del servicio Amazon EventBridge, el cual actúa como el reloj maestro del proyecto Eco-Scheduler. 

La autonomía del sistema se logró implementando una arquitectura orientada a eventos mediante reglas Cron en Amazon EventBridge, considerando el estándar UTC para los cálculos horarios[cite: 4]. Estas reglas garantizan la ejecución puntual de las funciones Serverless para la optimización de costos (FinOps).

## Reglas de Programación Horaria

El ciclo de automatización está gobernado por dos reglas de eventos principales:

### 1. Regla de Encendido (`Encendido-Diario-8AM`)
* **Expresión Cron configurada:** `cron(0 14 ? * MON-FRI *)`[cite: 4]
* **Mecánica horaria:** Esto instruye a AWS ejecutar el encendido a las 14:00 UTC, equivalente matemáticamente a las 08:00 a.m. (hora local El Salvador, UTC-6) de lunes a viernes[cite: 4].
* **Destino (Target):** Invoca la función Lambda `eco-scheduler-start-instances`[cite: 4].
* **Objetivo:** Garantizar la disponibilidad de los entornos de desarrollo y pruebas justo al comenzar la jornada operativa de los equipos técnicos[cite: 4].

### 2. Regla de Apagado (`Apagado-Diario-6PM`)
* **Expresión Cron configurada:** `cron(0 0 ? * TUE-SAT *)`[cite: 4]
* **Mecánica horaria:** El sistema dispara el evento a la medianoche UTC, lo que se traduce con precisión a las 06:00 p.m. hora local de lunes a viernes[cite: 4].
* **Destino (Target):** Invoca la función Lambda `eco-scheduler-stop-instances`[cite: 4].
* **Objetivo:** Detener la infraestructura de cómputo en ejecución y aplicar la detención automatizada para evitar facturación por capacidad ociosa fuera del horario laboral[cite: 4].

## Consideraciones de Arquitectura
El uso de expresiones Cron desacopla la lógica de negocio del control de tiempos. Esto permite que el código de AWS Lambda sea "Stateless" (sin estado) y se ejecute únicamente cuando es estrictamente necesario, maximizando el ahorro de la arquitectura Serverless.
