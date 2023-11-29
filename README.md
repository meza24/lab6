# RealTimeDataManager - README

## Descripción de los módulos

### RealTimeDataManager
Esta sección del código incluye la definición de la clase RealTimeDataManager, que simula la producción de información en tiempo real y avisa a los suscriptores cuando hay modificaciones en los datos. Además, brinda funcionalidades para preparar y crear esta información inicial.

### EventManager
Dentro del archivo llamado `eventos.py`, se encuentra la clase `EventManager`, la cual simplifica el proceso de suscripción y notificación de eventos a los suscriptores.

## Funcionamiento y Ejemplos

El fragmento de código suministrado simula la generación de información en tiempo real de forma aleatoria, como datos de temperatura y humedad. A cada intervalo de 3 segundos, se actualizan estos datos y se notifica a los suscriptores a través del `EventManager` cuando se producen cambios en los mismos.

### Ejemplo de uso:

```python
# Crear una instancia de RealTimeDataManager
real_time_data_manager = RealTimeDataManager()

# Función de callback para imprimir los datos actualizados
def print_updated_data(data):
    print(f"Datos en tiempo real actualizados: {data}") 

# Suscribir el callback a los eventos de actualización de datos
real_time_data_manager.event_manager.subscribe("datos_actualizados", print_updated_data)

# Iniciar las actualizaciones en tiempo real en segundo plano 
import threading
update_thread = threading.Thread(target=real_time_data_manager.start_real_time_updates)
update_thread.start()

# El programa se ejecuta en segundo plano. Para finalizar, presione Ctrl + C en la terminal.
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("\nPrograma terminado.")
