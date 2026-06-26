# Cálculo de Ahorro Estimado

Este documento presenta la línea base de costos y la proyección del impacto financiero al implementar la solución Eco-Scheduler. Las estimaciones aquí descritas sirven como indicador fundamental para evaluar el éxito de la optimización FinOps.

## Supuestos y Parámetros del Cálculo

Las siguientes métricas definen el escenario base para nuestra estimación:
- **Instancia de referencia:** `t3.micro` (Linux, bajo demanda)
- **Precio referencial por hora:** $0.0104 USD
- **Mes de referencia:** 30 días
- **Escenario sin automatización:** Instancia encendida 24 horas al día, 30 días al mes.
  - *24 horas × 30 días = 720 horas/mes*
- **Escenario con Eco-Scheduler:** Instancia encendida solo 10 horas al día, durante 22 días hábiles.
  - *10 horas × 22 días hábiles = 220 horas/mes*

## Fórmulas y Resultados

A partir de los supuestos, se aplican los siguientes cálculos para obtener las proyecciones:

- **Horas reducidas (Cloud Waste evitado):**
  - 720 h - 220 h = **500 horas mensuales ahorradas**
- **Porcentaje de ahorro de tiempo:**
  - (500 ÷ 720) × 100 = **69.44%**
- **Costo mensual sin Eco-Scheduler:**
  - 720 h × $0.0104 USD = **$7.49 USD/mes**
- **Costo mensual con Eco-Scheduler:**
  - 220 h × $0.0104 USD = **$2.29 USD/mes**

### Proyección de Ahorro Financiero
- **Ahorro mensual estimado:** $7.49 - $2.29 = **$5.20 USD por instancia.**
- **Ahorro anual proyectado:** $5.20 × 12 meses = **$62.40 USD por instancia.**

## Tabla Comparativa

| Métrica (1 Instancia `t3.micro`) | Sin Automatización (24/7) | Con Eco-Scheduler | Diferencia (Ahorro) |
| :--- | :--- | :--- | :--- |
| **Horas activas al mes** | 720 h | 220 h | **500 h menos** |
| **Costo mensual estimado** | $7.49 USD | $2.29 USD | **$5.20 USD** |
| **Costo anual estimado** | $89.88 USD | $27.48 USD | **$62.40 USD** |
| **Porcentaje de ahorro** | 0% | 69.44% | **69.44%** |

## Interpretación del Resultado
La implementación de Eco-Scheduler elimina de manera contundente el desperdicio generado por entornos inactivos durante noches y fines de semana. Lograr una reducción de casi el **70% del consumo de horas computacionales** demuestra un alto grado de eficiencia en la gestión de infraestructura no productiva. Además, si este modelo se escala a flotas de 10, 50 o 100 instancias de mayor tamaño, el ahorro económico y ambiental será exponencialmente mayor.

> [!NOTE]
> **Nota Metodológica:** Los precios mostrados ($0.0104 USD/h para `t3.micro`) son referenciales y utilizados exclusivamente con fines de estimación académica para la región seleccionada. El costo real en una factura de AWS puede variar dependiendo de la región específica de la cuenta, tipo de sistema operativo, consumo de almacenamiento (los volúmenes EBS se cobran independientemente de si la instancia está apagada), costos de transferencia de datos de red, impuestos locales y posibles cambios tarifarios realizados por AWS.


---

## Responsable

**Nombre:** Marisol Jacobo  
**Rol:** Analista FinOps Verde Jr.
