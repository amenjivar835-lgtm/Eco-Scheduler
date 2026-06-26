# Política de Etiquetas (Tagging Policy)

## Objetivo de la Política
Establecer un mecanismo de gobernanza claro, simple y seguro que defina exactamente cuáles instancias de Amazon EC2 están autorizadas para ser gestionadas de forma automática por la solución Eco-Scheduler.

## Etiqueta Requerida (Tag)
Para que una instancia EC2 forme parte del ciclo automático de encendido y apagado, debe contener obligatoriamente la siguiente etiqueta exacta:

- **Key (Clave):** `EcoScheduler`
- **Value (Valor):** `enabled`

## Regla Principal
El sistema Eco-Scheduler (a través de la función AWS Lambda) **solo debe iniciar o detener instancias que cuenten con la etiqueta `EcoScheduler=enabled`**. Cualquier instancia que no posea esta etiqueta, o que tenga un valor diferente (ej. `disabled`, vacío o errores tipográficos), debe ser ignorada por completo por el proceso de automatización.

## Justificación FinOps
Desde la perspectiva FinOps, la correcta aplicación de etiquetas permite visibilizar el consumo. Mediante esta política, los equipos de operaciones y finanzas pueden generar reportes de "Cost Explorer" en AWS agrupando los costos por la etiqueta `EcoScheduler`, permitiendo auditar fácilmente cuánto está gastando el entorno automatizado frente al entorno no automatizado.

## Justificación Operativa
Esta política implementa el principio de "Opt-in" (inclusión explícita). En un entorno donde convergen múltiples cargas de trabajo, garantiza que los recursos críticos no sean apagados por accidente. Permite a los desarrolladores controlar qué instancias de prueba o desarrollo entran en la ventana de ahorro de manera autónoma, simplemente agregando la etiqueta en la consola de AWS.

## Buenas Prácticas
1. Estandarizar la creación de recursos para que los entornos de desarrollo nazcan con la etiqueta `EcoScheduler=enabled` por defecto.
2. Mantener la consistencia entre mayúsculas y minúsculas (Case-Sensitive) tanto en la clave como en el valor de la etiqueta.
3. Auditar periódicamente la infraestructura de desarrollo para detectar instancias "huérfanas" que no cuenten con la política de ahorro activa.

## Ejemplos de Aplicación

**Ejemplo de instancia PERMITIDA (Será gestionada):**
- Nombre: `Servidor-Desarrollo-API`
- Entorno: `Dev`
- **`EcoScheduler`**: `enabled` *(Correcto)*

**Ejemplo de instancia NO PERMITIDA (Será ignorada):**
- Nombre: `BaseDatos-Produccion`
- Entorno: `Prod`
- Etiqueta faltante o diferente: `EcoScheduler=false` o sin etiqueta. *(Ignorada por seguridad)*

## Riesgos que evita esta política
- **Interrupción de Producción:** Previene el apagado accidental de servidores en producción u horas laborales.
- **Acciones destructivas generalizadas:** Evita que un error en el código de la función Lambda afecte a toda la flota de EC2 de una región.
- **Ruido en métricas:** Permite delimitar de forma precisa qué recursos se van a auditar para calcular los ahorros logrados.


---

## Responsable

**Nombre:** Marisol Jacobo  
**Rol:** Analista FinOps Verde Jr.
