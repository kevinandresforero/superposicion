import numpy as np
from scipy.signal import convolve
import math

class SuperposicionMAS:
  """
  Clase para calcular la amplitud y frecuencia dominante de la onda superpuesta de dos MAS de diferentes frecuencias.

  Atributos:
    db1: Nivel de potencia en decibeles del primer MAS.
    db2: Nivel de potencia en decibeles del segundo MAS.
    w1: Frecuencia angular del primer MAS.
    w2: Frecuencia angular del segundo MAS.
    phi1: Angulo de desfase del primer MAS.
    phi2: Angulo de desfase del segundo MAS.

  Métodos:
    calcular_superposicion(): Calcula la onda superpuesta de los dos MAS.
    get_amplitud_frecuencia_dominante(): Obtiene la amplitud y la frecuencia dominante de la onda superpuesta.
  """

  def __init__(self, db1, db2, w1, w2, phi1=0, phi2=0):
    """
    Constructor de la clase.

    Args:
      db1: Nivel de potencia en decibeles del primer MAS.
      db2: Nivel de potencia en decibeles del segundo MAS.
      w1: Frecuencia angular del primer MAS.
      w2: Frecuencia angular del segundo MAS.
      phi1: Angulo de desfase del primer MAS (opcional, por defecto 0).
      phi2: Angulo de desfase del segundo MAS (opcional, por defecto 0).
    """
    self.db1 = db1
    self.db2 = db2
    self.w1 = w1
    self.w2 = w2
    self.phi1 = phi1
    self.phi2 = phi2

  def db_to_amp(self, db):
    """
    Convierte un valor en decibeles a amplitud.
    
    Args:
        db (float): Valor en decibeles.
    
    Returns:
        float: Amplitud correspondiente.
    """
    amp = 10 ** (db / 20)
    return amp

  def amp_to_db(self, amp):
    """
    Convierte un valor de amplitud a decibeles.
    
    Args:
        amp (float): Valor de amplitud.
    
    Returns:
        float: Valor en decibeles correspondiente.
    """
    if amp == 0:
        return -math.inf
    else:
        db = 20 * math.log10(amp)
        return db

  def calcular_superposicion(self):
    """
    Calcula la onda superpuesta de los dos MAS.

    Returns:
      numpy.ndarray: Onda superpuesta.
    """
    # Convertir decibeles a amplitudes
    A1 = self.db_to_amp(self.db1)
    A2 = self.db_to_amp(self.db2)

    # Calcular las funciones
    t = np.linspace(0, 10, 1000)  # Rango de tiempo
    y1 = A1 * np.sin(self.w1 * t + self.phi1)
    y2 = A2 * np.sin(self.w2 * t + self.phi2)
    x = y1 + y2

    return x

  def get_db_frecuencia_dominante(self, signal):
    """
    Obtiene la amplitud y la frecuencia dominante de la señal de ruido.

    Args:
        signal (np.ndarray): Señal de ruido (array de NumPy).

    Returns:
        tuple: Amplitud y frecuencia dominante de la señal.
    """

    sampling_rate = 1000

    # Calcula la transformada de Fourier de la señal
    fourier_transform = np.fft.fft(signal)

    # Obtiene las frecuencias correspondientes a los coeficientes de Fourier
    frequencies = np.fft.fftfreq(len(signal), 1 / sampling_rate)

    # Calcula la amplitud de cada componente de frecuencia
    amplitudes = np.abs(fourier_transform)

    # Encuentra el índice de la componente de frecuencia con la máxima amplitud
    max_amplitude_idx = np.argmax(amplitudes)

    # Obtiene la amplitud y la frecuencia dominante
    amplitude = amplitudes[max_amplitude_idx]
    frequency = np.abs(frequencies[max_amplitude_idx])

    # Return both amplitude and frequency in a tuple
    return self.amp_to_db(amplitude), frequency

'''
#   ejemplo de uso de la clase

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
print("Frecuencia dominante:", frecuencia_dominante)'''


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