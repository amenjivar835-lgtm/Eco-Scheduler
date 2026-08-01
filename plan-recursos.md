# Plan de Recursos Tecnológicos - Eco-Scheduler

## 1. Información del Proyecto
- **Nombre:** Eco-Scheduler – Optimización de Energía Cloud
- **Fase actual:** Fase 0 - Onboarding
- **Fecha:** 14 de Junio de 2026

## 2. Recursos Tecnológicos

| Recurso                        | Proveedor / Plataforma      | Responsable                  | Tipo / Plan      | Uso previsto en el proyecto                          | Límites / Observaciones                     |
|-------------------------------|-----------------------------|------------------------------|------------------|-----------------------------------------------------|---------------------------------------------|
| Entorno Cloud Principal       | AWS                         | Ingeniero Cloud Jr.          | Free Tier        | Funciones Lambda, EventBridge y EC2 de prueba       | Solo usar recursos de bajo costo            |
| Funciones Serverless          | AWS Lambda                  | Desarrollador Serverless Jr. | Free Tier        | Lógica de apagado y encendido automático            | Monitorear duración de ejecución (< 15s)    |
| Programador de Eventos        | Amazon EventBridge          | Ing Cloud / Analista Jr.     | Free Tier        | Disparar funciones según horario laboral            | Configurar zona horaria correcta            |
| Instancias Objetivo           | Amazon EC2 (t2.micro / t3.micro) | Ing Cloud /Lider Jr.    | Free Tier        | Simular ambientes de desarrollo y pruebas           | Máximo 2-3 instancias                       |
| Logs y Monitoreo              | Amazon CloudWatch Logs      | QA / Documentador Jr.        | Incluido         | Registro de ejecuciones, errores y resultados       | Mantener logs por 30 días                   |
| Repositorio de Código         | GitHub                      | Ing Cloud, Desarrollador, Lider   | Free        | Versionamiento y documentación                      | No subir credenciales ni llaves             |
| Reporte de Ahorro             | Google Sheets / Excel       | Analista FinOps Verde Jr.    | Free             | Cálculo y seguimiento de ahorro estimado            | Fórmula simple de horas ahorradas           |
| Canal de Comunicación         | WhatsApp / Google Meet      | Líder de Proyecto Jr.        | Free             | Coordinación diaria del equipo                      | Registrar decisiones importantes            |

## 3. Observaciones Generales
- Se priorizará el uso de **Free Tier** para evitar costos.
- Todos los recursos se gestionarán bajo el principio de **menor privilegio**.
- No se utilizarán recursos de entornos productivos.

---

**Aprobado por:** René Pérez - Líder de Proyecto Jr.  
**Fecha de aprobación:** 14 de Junio de 2026
