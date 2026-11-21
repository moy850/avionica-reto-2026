# PROCESADOR DE DATOS DEL VUELO
# PROYECTO DE TELEMETRIA AAIAQ

import csv

# Crear listas vacias
tiempos = []
altitudes = []

# Abrir archivo CSV
archivo = open("flight_log.csv", "r")

lector = csv.reader(archivo)

# Saltar encabezado
next(lector)

# Leer los datos
for fila in lector:

    tiempo = float(fila[0])
    altitud = float(fila[1])

    tiempos.append(tiempo)
    altitudes.append(altitud)

# Cerrar archivo
archivo.close()

# Mostrar resultados
print("PROCESAMIENTO TERMINADO")

print("Cantidad de datos:", len(tiempos))

print("Primera altitud:", altitudes[0])

print("Altitud maxima:", max(altitudes))
