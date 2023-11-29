import time # Para generar un retardo
import random # Para generar datos aleatorios
from eventos import EventManager # Importar la clase EventManager

'''
Clase que genera datos en tiempo real y notifica a los suscriptores cuando los datos han cambiado. 
'''
class RealTimeDataManager:

    # Inicializar los datos en tiempo real y el EventManager 
    def __init__(self):
        self.data = {"temperatura": 25.0, "humedad": 60.0} # Datos en tiempo real
        self.event_manager = EventManager() # EventManager para notificar a los suscriptores

    # Método para iniciar las actualizaciones en tiempo real en segundo plano 
    def start_real_time_updates(self):

        # Generar datos en tiempo real y notificar a los suscriptores cuando los datos han cambiado 
        while True:
            time.sleep(3) # Retardo de 3 segundos 
            self.generate_real_time_data() # Generar datos en tiempo real 

            # Notificar a los suscriptores que los datos han cambiado
            self.event_manager.notify("datos_actualizados", self.data.copy())

    # Método para generar datos en tiempo real 
    def generate_real_time_data(self):
        '''
        Aqui se generan datos aleatorios para simular datos en tiempo real. 
        '''
        self.data["temperatura"] += random.uniform(-1.0, 1.0) # Incrementar o decrementar la temperatura en un valor aleatorio entre -1.0 y 1.0
        self.data["humedad"] += random.uniform(-2.0, 2.0) # Incrementar o decrementar la humedad en un valor aleatorio entre -2.0 y 2.0

# Crear una instancia de RealTimeDataManager
real_time_data_manager = RealTimeDataManager()

# Callback para imprimir los datos actualizados
def print_updated_data(data):
    print(f"Datos en tiempo real actualizados: {data}") 

# Suscribir el callback a los eventos de actualización de datos
real_time_data_manager.event_manager.subscribe("datos_actualizados", print_updated_data)

# Iniciar las actualizaciones en tiempo real en segundo plano 
import threading # Para crear hilos
update_thread = threading.Thread(target=real_time_data_manager.start_real_time_updates) # Crear un hilo para iniciar las actualizaciones en tiempo real
update_thread.start() # Iniciar el hilo 

'''
El programa se ejecuta en segundo plano. Para terminar el programa, presione Ctrl + C en la terminal. 
'''
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("\nPrograma terminado.")