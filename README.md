
'''#   ejemplo de uso de la clase

#from superposicion_mas import SuperposicionMAS

# Parámetros
db1 = 60  # Nivel de potencia en decibeles del primer MAS
db2 = 80  # Nivel de potencia en decibeles del segundo MAS
w1 = 100  # Frecuencia angular del primer MAS
w2 = 200  # Frecuencia angular del segundo MAS
phi1 = 0  # Angulo de desfase del primer MAS (opcional, por defecto 0)
phi2 = 0  # Angulo de desfase del segundo MAS (opcional, por defecto 0)

# Crear instancia de la clase
superposicion = SuperposicionMAS(db1, db2, w1, w2, phi1, phi2)

# Calcular la onda superpuesta
t = np.linspace(0, 10, 1000)  # Rango de tiempo
x = superposicion.calcular_superposicion()

# Obtener amplitud y frecuencia dominante
amplitud, frecuencia_dominante = superposicion.get_db_frecuencia_dominante(x)

print("dB:", amplitud)
print("Frecuencia dominante:", frecuencia_dominante)
'''

#   graficar superposición
'''import matplotlib.pyplot as plt
# Visualizar la onda superpuesta
plt.plot(t, x)
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.title("Onda superpuesta")
plt.grid(True)
plt.show()
'''
