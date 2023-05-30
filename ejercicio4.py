import requests
import csv
from collections import Counter
import re

# URL del endpoint
url = "https://dummyjson.com/quotes"

# Realizar una solicitud GET a la URL
response = requests.get(url)

# Obtener los datos JSON de la respuesta
data = response.json()

# Extraer las citas del JSON
quotes = data["quotes"]

# Extraer los textos de las citas
textos = [quote["quote"] for quote in quotes]

# Unir todos los textos en un solo texto completo
texto_completo = " ".join(textos)

# Eliminar caracteres no alfanuméricos y convertir a minúsculas
texto_completo = re.sub(r'[^\w\s]', '', texto_completo).lower()

# Palabras a excluir
excluir = ['a', 'an', 'the', 'and', 'or', 'but', 'is', 'are', 'was', 'were', 'in', 'on', 'at', 'to']

# Dividir el texto en palabras
palabras = texto_completo.split()

# Contar la frecuencia de cada palabra
contador = Counter(palabras)

# Obtener el ranking de palabras más frecuentes
ranking = contador.most_common()

# Filtrar el ranking excluyendo palabras específicas
ranking_filtrado = [(palabra, frecuencia) for palabra, frecuencia in ranking if palabra not in excluir]

# Obtener las diez palabras más repetidas
top_ten = ranking_filtrado[:10]

# Mostrar el top ten de palabras más repetidas
print("Top Ten de palabras más repetidas")
for palabra, frecuencia in top_ten:
    print(f"Palabra: {palabra} - Cantidad de veces que aparece: {frecuencia}")
