# Fórmula definitiva y hoja de registro de costos y ahorro

Para mantener un control riguroso durante la Fase 2 (Implementación de Automatización Serverless), he diseñado una hoja de registro en Google Sheets. Esta herramienta permitirá a todo el equipo ingresar los datos base de las instancias EC2 y calcular de manera automática tanto los costos proyectados como el ahorro estimado generado por la implementación de Eco-Scheduler.

#### Fórmulas definitivas

Para automatizar los cálculos en nuestra hoja, utilizaremos las siguientes fórmulas matemáticas:

* **Horas sin automatización:** 24 × Días del mes.
* **Horas con Eco-Scheduler:** Horas laborales por día × Días hábiles.
* **Horas evitadas:** Horas sin automatización - Horas con Eco-Scheduler.
* **Costo sin automatización:** Horas sin automatización × Precio por hora.
* **Costo con Eco-Scheduler:** Horas con Eco-Scheduler × Precio por hora.
* **Ahorro estimado:** Costo sin automatización - Costo con Eco-Scheduler.
* **Porcentaje de ahorro:** (Ahorro estimado / Costo sin automatización) × 100.

#### Estructura sugerida para Google Sheets

La hoja de cálculo debe contener las siguientes columnas para que sea fácil ingresar los datos y obtener los resultados:

| Columna | Encabezado |
| :--- | :--- |
| **A** | Recurso |
| **B** | Tipo de instancia |
| **C** | Precio por hora USD |
| **D** | Días del mes |
| **E** | Horas sin automatización |
| **F** | Horas laborales por día |
| **G** | Días hábiles |
| **H** | Horas con Eco-Scheduler |
| **I** | Horas evitadas |
| **J** | Costo sin automatización |
| **K** | Costo con Eco-Scheduler |
| **L** | Ahorro mensual estimado |
| **M** | Porcentaje de ahorro |
| **N** | Observaciones |

#### Fórmulas para Google Sheets (Fila 2)

Una vez creada la estructura, estas son las fórmulas exactas que deben pegarse en la fila 2. Solo debes arrastrarlas hacia abajo para las demás instancias:

* **E2:** `=24*D2`
* **H2:** `=F2*G2`
* **I2:** `=E2-H2`
* **J2:** `=E2*C2`
* **K2:** `=H2*C2`
* **L2:** `=J2-K2`
* **M2:** `=L2/J2` *(Recuerda aplicar el formato de Porcentaje % a esta columna)*.

#### Ejemplo con datos base

Si aplicamos nuestros datos de referencia en la primera fila, la hoja quedará así:

* **Recurso (A):** EC2 prueba
* **Tipo de instancia (B):** t3.micro
* **Precio por hora USD (C):** 0.0104
* **Días del mes (D):** 30
* **Horas sin automatización (E):** 720
* **Horas laborales por día (F):** 10
* **Días hábiles (G):** 22
* **Horas con Eco-Scheduler (H):** 220
* **Horas evitadas (I):** 500
* **Costo sin automat. (J):** $7.488
* **Costo con Eco-Sched. (K):** $2.288
* **Ahorro mensual est. (L):** $5.20
* **Porcentaje de ahorro (M):** 69.44%

> **Observación FinOps:** Es importante tener en cuenta que este cálculo se enfoca exclusivamente en el costo de cómputo directo de la instancia EC2. El ahorro financiero real puede presentar variaciones, ya que ciertos recursos pueden generar cargos adicionales (como el almacenamiento de volúmenes EBS, snapshots retenidos, direcciones IP elásticas u otros servicios asociados) aun cuando la instancia se encuentre detenida.

---


## Responsable

**Nombre:** Marisol Jacobo  
**Rol:** Analista FinOps Verde Jr.
