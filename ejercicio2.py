import psutil

# Obtener información sobre el disco
disco = psutil.disk_usage('/')
espacio_disco = disco.total / (1024**3)  # Convertir a gigabytes

# Obtener información sobre la memoria ram
memoria = psutil.virtual_memory()
espacio_memoria = memoria.total / (1024**3)  # Convertir a gigabytes

# Obtener información sobre la CPU
cpu = psutil.cpu_count(logical=False)  # Obtener el número de núcleos físicos de la CPU

# Obtener información sobre las interfaces de red
interfaces_red = psutil.net_if_stats()
cantidad_interfaces = len(interfaces_red)  # Obtener la cantidad de interfaces de red

# Mostrar la información obtenida
print(f"Espacio disponible en disco: {espacio_disco:.2f} GB")
print(f"Espacio disponible en memoria: {espacio_memoria:.2f} GB")
print(f"Cantidad de núcleos físicos de la CPU: {cpu}")
print(f"Cantidad de interfaces de red: {cantidad_interfaces}")
