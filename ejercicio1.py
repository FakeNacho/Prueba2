import subprocess
from datetime import datetime, timedelta

# Obtener la hora actual
hora_actual = datetime.now().strftime("%H:%M")

# Calcular la hora de inicio restando una hora a la hora actual
hora_inicio = (datetime.strptime(hora_actual, "%H:%M") - timedelta(hours=1)).strftime("%H:%M")

# Si la hora de inicio es mayor que la hora actual, restar un día a la hora de inicio
if hora_inicio > hora_actual:
    hora_inicio = (datetime.strptime(hora_inicio, "%H:%M") - timedelta(days=1)).strftime("%H:%M")

# Construir el comando para buscar los registros en el archivo de registro de autenticación
comando_grep = f"grep 'Failed password' /var/log/auth.log | grep '{hora_inicio}\|{hora_actual}' | wc -l"

# Ejecutar el comando en la línea de comandos y capturar la salida
resultado = subprocess.run(comando_grep, shell=True, capture_output=True, text=True)

# Obtener el resultado como una cadena de texto
intentos_fallidos_str = resultado.stdout.strip()

# Convertir la cadena de texto a un entero
intentos_fallidos = int(intentos_fallidos_str)

# Mostrar la cantidad de intentos fallidos de inicio de sesión
print("Cantidad de intentos fallidos de inicio de sesión: ", intentos_fallidos)
