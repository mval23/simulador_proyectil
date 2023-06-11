import tkinter as tk
import numpy as np
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def calcular_distancia(angulo, velocidad, altura):
    # Convertir el ángulo de grados a radianes
    theta = np.radians(angulo)

    # Calcular el tiempo de vuelo
    tiempo_de_vuelo = ((velocidad * np.sin(theta)) + np.sqrt((velocidad * np.sin(theta))**2 + (2 * altura * 9.8))) / 9.8

    # Calcular la distancia horizontal recorrida
    distancia = velocidad * np.cos(theta) * tiempo_de_vuelo

    return distancia


def animar(frame, angulo, velocidad, altura, linea):
    # Convertir el ángulo de grados a radianes
    theta = np.radians(angulo)

    # Calcular el tiempo de vuelo
    tiempo_de_vuelo = ((velocidad * np.sin(theta)) + np.sqrt((velocidad * np.sin(theta))**2 + (2 * altura * 9.8))) / 9.8

    # Calcular los intervalos de tiempo
    t = np.linspace(0, tiempo_de_vuelo, num=100)

    # Calcular las coordenadas x e y
    x = velocidad * np.cos(theta) * t
    y = velocidad * np.sin(theta) * t - 0.5 * 9.8 * t ** 2 + altura

    # Actualizar los datos de la línea
    linea.set_data(x[:frame], y[:frame])

    return linea,


def simular_proyectil(angulo, velocidad, altura):
    # Crear la gráfica
    fig, ax = plt.subplots()
    ax.set_xlim(0, calcular_distancia(angulo, velocidad, altura) * 1.2)
    ax.set_ylim(0, np.max(velocidad ** 2 * np.sin(np.radians(angulo)) ** 2) / (2 * 9.8) + altura * 1.2)
    ax.set_xlabel('Distancia Horizontal (m)')
    ax.set_ylabel('Distancia Vertical (m)')
    ax.set_title('Movimiento del Proyectil')
    ax.grid(True)

    # Crear la línea para el proyectil
    linea, = ax.plot([], [], lw=2)

    # Animar el movimiento del proyectil
    animacion = FuncAnimation(fig, animar, fargs=(angulo, velocidad, altura, linea), frames=100, interval=20, blit=True)

    # Mostrar la gráfica
    plt.show()

    # Calcular la distancia horizontal recorrida
    distancia = calcular_distancia(angulo, velocidad, altura)
    messagebox.showinfo('Resultado', f'El proyectil recorrió una distancia de {distancia:.2f} metros.')


def comenzar_simulacion():
    try:
        angulo = float(angulo_entry.get())
        velocidad = float(velocidad_entry.get())
        altura = float(altura_entry.get())

        simular_proyectil(angulo, velocidad, altura)

    except ValueError:
        messagebox.showerror('Error', 'Entrada inválida. Por favor ingresa valores numéricos.')


# Crear la ventana principal
ventana = tk.Tk()
ventana.title('Simulador de Movimiento del Proyectil')

# Crear la etiqueta y entrada para el ángulo
etiqueta_angulo = tk.Label(ventana, text='Ángulo (grados):')
etiqueta_angulo.grid(row=0, column=0, padx=10, pady=10)
angulo_entry = tk.Entry(ventana)
angulo_entry.grid(row=0, column=1, padx=10, pady=10)

# Crear la etiqueta y entrada para la velocidad
etiqueta_velocidad = tk.Label(ventana, text='Velocidad (m/s):')
etiqueta_velocidad.grid(row=1, column=0, padx=10, pady=10)
velocidad_entry = tk.Entry(ventana)
velocidad_entry.grid(row=1, column=1, padx=10, pady=10)

# Crear la etiqueta y entrada para la altura
etiqueta_altura = tk.Label(ventana, text='Altura (m):')
etiqueta_altura.grid(row=2, column=0, padx=10, pady=10)
altura_entry = tk.Entry(ventana)
altura_entry.grid(row=2, column=1, padx=10, pady=10)

# Crear el botón para simular
boton_simular = tk.Button(ventana, text='Simular', command=comenzar_simulacion)
boton_simular.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Ejecutar el bucle de eventos principal
ventana.mainloop()
