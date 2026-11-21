# PROYECTO DE TELEMETRIA AAIAQ
# GENERADOR DE DATOS DEL VUELO

import csv

# 1. CONFIGURACION GENERAL

dt = 0.1
gravedad = 9.81
aceleracion = 60
velocidad_paracaidas = 6

tiempo_rampa = 2.0
tiempo_propulsion = 1.5
tiempo_tierra = 3.0

# Crear lista para guardar los datos
datos = []

# Variables iniciales
tiempo = 0
altitud = 0
velocidad = 0


# 2. FASE 1: COHETE EN LA RAMPA

for i in range(20):

    tiempo = i * dt
    altitud = 0

    datos.append([tiempo, altitud])


# 3. FASE 2: PROPULSION

for i in range(15):

    altitud = altitud + velocidad * dt + 0.5 * aceleracion * dt**2

    velocidad = velocidad + aceleracion * dt

    tiempo = tiempo + dt

    datos.append([tiempo, altitud])


# 4. FASE 3: VUELO BALISTICO

while velocidad > 0:

    altitud = altitud + velocidad * dt - 0.5 * gravedad * dt**2

    velocidad = velocidad - gravedad * dt

    tiempo = tiempo + dt

    datos.append([tiempo, altitud])


# 5. DETECTAR APOGEO

altura_maxima = max(fila[1] for fila in datos)

print("APOGEO DEL COHETE")
print("Altura maxima:", round(altura_maxima, 2), "metros")


# 6. FASE 4: DESCENSO CON PARACAIDAS

velocidad = -velocidad_paracaidas

while altitud > 0:

    altitud = altitud + velocidad * dt

    tiempo = tiempo + dt

    if altitud < 0:
        altitud = 0

    datos.append([tiempo, altitud])


# 7. FASE 5: ATERRIZAJE

for i in range(1, 31):

    tiempo = tiempo + dt

    altitud = 0

    datos.append([tiempo, altitud])


# 8. CREAR ARCHIVO CSV

archivo = open("flight_log.csv", "w", newline="")

escritor = csv.writer(archivo)

# Escribir encabezados
escritor.writerow(["Tiempo", "Altitud"])

# Guardar todos los datos
for fila in datos:

    escritor.writerow(fila)

archivo.close()


# 9. MOSTRAR RESULTADOS

print("SIMULACION TERMINADA")

print("Cantidad de datos:", len(datos))

print("Altitud maxima:", round(altura_maxima, 2), "metros")

print("Tiempo final:", round(tiempo, 2), "segundos")

print("Altitud final:", altitud, "metros")

print("Archivo flight_log.csv creado correctamente")
