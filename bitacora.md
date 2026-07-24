# Bitácora del Proyecto Eco-Scheduler

## Información General
- **Proyecto:** Eco-Scheduler – Optimización de Energía Cloud
- **Cliente:** AARD – Agencia de Administración y Recursos Digitales
- **Equipo:** René Ovidio Pérez Ramírez, Yolanda Marisol Alvarenga Jacobo, Adonay Jeshua Menjívar Martínez, José Jafet Hernández Ortiz
- **Duración:** 10 semanas
- **Repositorio:** GitHub y Google Drive

---

## Semana 1 - Fase 0: Onboarding y Planificación

**Fecha:**  14 de junio de 2026

### Actividades realizadas:
- Reunión de kick-off y asignación de roles
- Creación del repositorio en GitHub
- Definición del canal de comunicación
- Elaboración del Plan de Recursos Tecnológicos
- Creación de la estructura inicial de carpetas
- Redacción del Documento de Onboarding

### Decisiones importantes:
- Se seleccionó **AWS** como plataforma principal (Lambda + EventBridge)
- Se usará Python para las funciones serverless
- El proyecto se trabajará de forma asincrónica con revisiones semanales

### Evidencias:
- Repositorio creado y configurado
- Roles asignados
- Documento de Fase 0 en proceso

### Próximos pasos (Semana 2):
- Iniciar Fase 1: Análisis del problema energético
- Definir instancias objetivo y horarios laborales

## Semana 2 - Fase 1: Análisis del problema energético

**Fecha:**  18 de junio de 2026

### Actividades realizadas:
- Reunión de seguimiento
- Identificar tipos de instancias cloud 
- Investigar cómo identificar recursos mediante etiquetas
- Analizar impacto económico y ambiental del consumo ocioso
- Estimación inicial de ahorro
- Recopilar información y estructurar el documento

## Semana 3 - Fase 1: Diseño de la solución

**Fecha:**  25 de junio de 2026

### Actividades realizadas:
- Reunión de seguimiento
- Diseñar arquitectura general 
- Diseñar la lógica de las funciones Start/Stop
- Establecer permisos IAM
- Definir cómo se medirá el ahorro
- Crear diagramas de flujo y organizar el documento

### Incidencia - Semana 3 Fase 1
- Segunda ocasión que no finaliza su aporte con el archivo entregable y sin tener respuesta del miembro Carlos Cordova (rol: QA / Documentador Jr.).
- Se envió comunicación formal por ESIT sin obtener respuesta hasta el momento.
- El equipo (principalmente el Líder) ha absorbido sus responsabilidades para cumplir con los plazos de la Fase 1.
- Se registrará esta situación para efectos de evaluación individual.

## Semana 4 - Fase 2: Implementación de automatización Serveless

**Fecha:**  01 de julio de 2026

### Actividades realizadas:
- Reunión de seguimiento
- Crear y configurar cuenta AWS 
- Configurar permisos IAM y Roles
- Crear instancias EC2 de prueba
- Crear estructura completa de carpetas en el repositorio
- Configurar proyecto local y crear plantillas base de funciones lambda
- Preparar hoja de cálculo para registros de costos y ahorro

## Semana 5 - Fase 2: Función de apagado

**Fecha:**  07 de julio de 2026

### Actividades realizadas:
- Reunión de seguimiento
- Revisión de código y logs 
- Validar instancias que se puedan detener correctamente
- Revisar y ajustar políticas IAM
- Desarrollo de la función Lambda de Stop
- Manejar errores comunes y probar la función
- Registrar tiempos de ejecución y primeros cálculos de ahorro

## Semana 6 - Fase 2: Función de encendido

**Fecha:**  11 de julio de 2026

### Actividades realizadas:
- Reunión de seguimiento
- Validar funcionamiento completo de Start 
- Revisar configuración general
- Desarrollo de la función Lambda de Start
- Probar secuencia completa de Stop-Start
- Actualizar métricas de ahorro con datos de pruebas reales

## Semana 7 - Fase 3: Programación y Monitoreo

**Fecha:**  20 de julio de 2026

### Actividades realizadas:
- Reunión de seguimiento
- Configurar reglas de EventBridge
- Integrar las funciones Lambda con EventBridge
- Mejorar Logging y preparar pruebas completas
- Preparar matriz de pruebas con escenarios
- Registrar resultados de ejecución automática


---

**Registro de Cambios:**
| Fecha       | Autor                  | Descripción del cambio                  |
|-------------|------------------------|-----------------------------------------|
| 14/06/2026  | René Pérez - Líder    | Creación inicial de la bitácora          |
| 18/06/2026  | René Pérez - Líder    | Semana dos Análisis del problema         |
| 25/06/2026  | René Pérez - Líder    | Semana tres Diseño de la solución        |
| 01/07/2026  | René Pérez - Líder    | Semana cuatro Implementación             |
| 07/07/2026  | René Pérez - Líder    | Semana cinco Función de apagado          |
| 11/07/2026  | René Pérez - Líder    | Semana seis Función de encendido         |
| 20/07/2026  | René Pérez - Líder    | Semana siete Programación y monitoreo    |

