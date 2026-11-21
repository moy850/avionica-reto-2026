# PROYECTO DE TELEMETRIA AAIAQ
# PROCESAMIENTO DE DATOS DEL VUELO

import csv
import matplotlib.pyplot as plt

# PASO 1: LEER LOS DATOS

tiempos = []
altitudes = []

archivo = open("flight_log.csv", "r")
lector = csv.reader(archivo)

next(lector)

for fila in lector:

    tiempo = float(fila[0])
    altitud = float(fila[1])

    tiempos.append(tiempo)
    altitudes.append(altitud)

archivo.close()

print("Datos leidos correctamente")


# PASO 2: FILTRAR LOS DATOS

altitudes_filtradas = []

for i in range(len(altitudes)):

    if i < 4:
        promedio = sum(altitudes[0:i+1]) / (i+1)

    else:
        promedio = sum(altitudes[i-4:i+1]) / 5

    altitudes_filtradas.append(promedio)

print("Filtrado terminado")


# PASO 3: CALCULAR LA VELOCIDAD

velocidades = []

for i in range(1, len(altitudes_filtradas)):

    cambio_altura = altitudes_filtradas[i] - altitudes_filtradas[i-1]

    cambio_tiempo = tiempos[i] - tiempos[i-1]

    velocidad = cambio_altura / cambio_tiempo

    velocidades.append(velocidad)

print("Velocidad calculada")


# PASO 4: DETECTAR EL DESPEGUE

for i in range(len(velocidades)):

    if velocidades[i] > 5:

        tiempo_despegue = tiempos[i+1]

        print("Despegue detectado:", tiempo_despegue, "segundos")

        break


# PASO 5: DETECTAR EL APOGEO

altura_maxima = max(altitudes_filtradas)

posicion = altitudes_filtradas.index(altura_maxima)

tiempo_apogeo = tiempos[posicion]

print("Altura maxima:", round(altura_maxima, 2), "metros")

print("Tiempo del apogeo:", tiempo_apogeo, "segundos")


# PASO 6: DETECTAR EL ATERRIZAJE

for i in range(posicion, len(altitudes_filtradas)):

    if altitudes_filtradas[i] <= 0.1:

        tiempo_aterrizaje = tiempos[i]

        print("Aterrizaje detectado:", tiempo_aterrizaje, "segundos")

        break


# PASO 7: MOSTRAR RESULTADOS

print("PROCESAMIENTO TERMINADO")

print("Cantidad de datos:", len(tiempos))

# PASO 8: COMPARAR GRAFICAS

plt.figure(figsize=(10, 5))

# Graficar datos originales
plt.plot(tiempos, altitudes, label="Altitud original")

# Graficar datos filtrados
plt.plot(tiempos, altitudes_filtradas, label="Altitud filtrada")

# Agregar titulos
plt.xlabel("Tiempo en segundos")
plt.ylabel("Altitud en metros")

plt.title("Comparacion de altitud")

# Mostrar leyenda y cuadricula
plt.legend()
plt.grid()

# Guardar grafica
plt.savefig("comparacion_graficas.png")

# Mostrar grafica
plt.show()

print("Grafica creada correctamente")

# PASO 9: GRAFICA DE VELOCIDAD

# Crear la grafica
plt.figure(figsize=(10, 5))

# Dibujar la velocidad
plt.plot(tiempos[1:], velocidades)

# Agregar titulos
plt.xlabel("Tiempo en segundos")
plt.ylabel("Velocidad en m/s")

plt.title("Velocidad vertical del cohete")

# Mostrar cuadricula
plt.grid()

# Guardar la imagen
plt.savefig("velocidad_cohete.png")

# Mostrar grafica
plt.show()

print("Grafica de velocidad creada correctamente")

# PASO 10: GRAFICA DE EVENTOS

# Crear la grafica
plt.figure(figsize=(10, 5))

# Dibujar la altitud
plt.plot(tiempos, altitudes_filtradas, label="Altitud")

# Marcar el despegue
plt.axvline(tiempo_despegue, color="green", label="Despegue")

# Marcar el apogeo
plt.axvline(tiempo_apogeo, color="red", label="Apogeo")

# Marcar el aterrizaje
plt.axvline(tiempo_aterrizaje, color="orange", label="Aterrizaje")

# Agregar titulos
plt.xlabel("Tiempo en segundos")
plt.ylabel("Altitud en metros")
plt.title("Eventos principales del vuelo")

# Mostrar leyenda y cuadricula
plt.legend()
plt.grid()

# Guardar grafica
plt.savefig("eventos_vuelo.png")

# Mostrar grafica
plt.show()

print("Grafica de eventos creada correctamente")
