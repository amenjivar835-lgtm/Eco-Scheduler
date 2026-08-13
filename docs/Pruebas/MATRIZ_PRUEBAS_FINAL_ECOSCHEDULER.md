# Matriz Final de Pruebas — EcoScheduler

## 1. Resultados de las pruebas

| ID | Escenario | Condición de prueba | Resultado esperado | Resultado obtenido | Estado |
|---:|---|---|---|---|:---:|
| **01** | **Apagado normal** | Instancia en estado `Running` con `EcoScheduler=True` y perteneciente a un entorno elegible. | La instancia se detiene correctamente. | EventBridge ejecutó **STOP**; CloudWatch registró la ejecución y Amazon EC2 mostró la instancia en estado **Detenida**. | ✅ Aprobado |
| **02** | **Encendido normal** | Instancia en estado `Stopped` con `EcoScheduler=True` y perteneciente a un entorno elegible. | La instancia se inicia correctamente. | CloudWatch registró **START** exitoso y Amazon EC2 confirmó el estado **Running**. | ✅ Aprobado |
| **03** | **Exclusión por etiqueta** | Instancia sin `EcoScheduler=True` o con un valor diferente al criterio elegible. | La instancia es ignorada. | CloudWatch confirmó que, con `EcoScheduler=False`, la instancia quedó fuera de la ejecución y la función finalizó de forma controlada. | ✅ Aprobado |
| **04** | **Exclusión de producción** | Instancia con `Environment=Prod`. | La instancia es ignorada. | CloudWatch registró la exclusión por `Environment=Prod`; la lógica también contempla `Criticality=High` y `Maintenance=True`. | ✅ Aprobado |
| **05** | **Instancia ya detenida** | Ejecutar la función de apagado cuando la instancia ya se encuentra `Stopped`. | No se ejecuta una acción redundante. | CloudWatch registró la omisión; la función de apagado procesa solo instancias `running`. | ✅ Aprobado |
| **06** | **Instancia ya encendida** | Ejecutar la función de encendido cuando la instancia ya se encuentra `Running`. | No se ejecuta una acción redundante. | CloudWatch registró **START omitido**; la función de encendido procesa solo instancias `stopped`. | ✅ Aprobado |
| **07** | **Error de permisos** | Ejecutar la función con el permiso necesario de Amazon EC2 denegado. | Se genera un error claro y queda registrado. | CloudWatch registró `AuthFailure / ClientError` y la ejecución finalizó de forma controlada. | ✅ Aprobado |
| **08** | **Ejecución programada (EventBridge)** | Regla habilitada, horario configurado y función Lambda establecida como destino. | La función se ejecuta automáticamente en el horario programado. | **START** y **STOP** fueron comprobados mediante EventBridge, CloudWatch y los estados finales de Amazon EC2. | ✅ Aprobado |
| **09** | **Múltiples instancias** | Dos o más instancias elegibles con estados compatibles con la acción. | Todas las instancias elegibles son procesadas. | CloudWatch registró una ejecución con **dos instancias elegibles** y Amazon EC2 mostró ambas instancias detenidas. | ✅ Aprobado |
| **10** | **Manejo de excepciones** | Provocar un error controlado o utilizar un dato inválido. | El error es capturado y registrado sin terminación abrupta. | `ClientError` capturó el error, registró código y mensaje, y la invocación finalizó con `END` y `REPORT`. | ✅ Aprobado |

## 2. Trazabilidad de evidencias y responsables

| ID | Fecha | Responsable y rol | Evidencia / fuente | Commit / referencia |
|---:|---|---|---|---|
| **01** | 27/07/2026 | Jafet Hernández — Desarrollador Serverless Jr.<br>Adonay Menjívar — Ingeniero Cloud Jr. | Fase 3 Serverless Jr. — Prueba 1<br>Programación y Monitoreo | [`a075a31`](https://github.com/amenjivar835-lgtm/Eco-Scheduler/commit/a075a310a33b8eb91bac50a471a601edf5b01099) |
| **02** | 27/07/2026 | Jafet Hernández — Desarrollador Serverless Jr.<br>Adonay Menjívar — Ingeniero Cloud Jr. | Fase 3 Serverless Jr. — Prueba 2<br>Programación y Monitoreo | [`a075a31`](https://github.com/amenjivar835-lgtm/Eco-Scheduler/commit/a075a310a33b8eb91bac50a471a601edf5b01099) |
| **03** | 27/07/2026 | Jafet Hernández — Desarrollador Serverless Jr. | Fase 3 Serverless Jr. — Prueba 3 | [`95b5a91`](https://github.com/amenjivar835-lgtm/Eco-Scheduler/commit/95b5a911144697e9c510d4f7380fa8fe92d70f68) |
| **04** | 27/07/2026 | Jafet Hernández — Desarrollador Serverless Jr. | Fase 3 Serverless Jr. — Prueba 4 | [`95b5a91`](https://github.com/amenjivar835-lgtm/Eco-Scheduler/commit/95b5a911144697e9c510d4f7380fa8fe92d70f68) |
| **05** | 27/07/2026 | Jafet Hernández — Desarrollador Serverless Jr. | Fase 3 Serverless Jr. — Prueba 5 | [`a075a31`](https://github.com/amenjivar835-lgtm/Eco-Scheduler/commit/a075a310a33b8eb91bac50a471a601edf5b01099) |
| **06** | 27/07/2026 | Jafet Hernández — Desarrollador Serverless Jr. | Fase 3 Serverless Jr. — Prueba 6 | [`a075a31`](https://github.com/amenjivar835-lgtm/Eco-Scheduler/commit/a075a310a33b8eb91bac50a471a601edf5b01099) |
| **07** | 27/07/2026 | Jafet Hernández — Desarrollador Serverless Jr. | Fase 3 Serverless Jr. — Prueba 7 | [`a075a31`](https://github.com/amenjivar835-lgtm/Eco-Scheduler/commit/a075a310a33b8eb91bac50a471a601edf5b01099) |
| **08** | 27/07/2026 | Adonay Menjívar — Ingeniero Cloud Jr.<br>Jafet Hernández — Desarrollador Serverless Jr. | Programación y Monitoreo<br>Fase 3 Serverless Jr. — Prueba 8 | [`8216dbe`](https://github.com/amenjivar835-lgtm/Eco-Scheduler/commit/8216dbe4c50f9d3ec8d0f51cb344d8469fe88661) |
| **09** | 27/07/2026 | Jafet Hernández — Desarrollador Serverless Jr. | Fase 3 Serverless Jr. — Prueba 9 | [`a075a31`](https://github.com/amenjivar835-lgtm/Eco-Scheduler/commit/a075a310a33b8eb91bac50a471a601edf5b01099) |
| **10** | 27/07/2026 | Jafet Hernández — Desarrollador Serverless Jr. | Fase 3 Serverless Jr. — Prueba 10 | [`a075a31`](https://github.com/amenjivar835-lgtm/Eco-Scheduler/commit/a075a310a33b8eb91bac50a471a601edf5b01099) |

> **Resultado final:** 10/10 casos de prueba aprobados (100 %).
