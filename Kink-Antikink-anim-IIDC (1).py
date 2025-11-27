#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  9 15:29:59 2025

@author: I.I. D. Cortés.
ileon001@alumno.uaemex.mx
Teoría Clasica de Campos a cargo del Dr. J.M. Dávila Dávila.
"""
import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def mostrar_bienvenida():
    print('\nBienvenido al programa para graficar la solución de Sine-Gordon tipo Kink y Anti-kink')
    print("Por favor seleccione el tipo de solución que desea graficar:")
    print("[K] para la función de tipo Kink")
    print("[A] para la función de tipo Anti-Kink")

def y_kink(x, t, l, m, g, v, u0):
    return (4 / l) * np.arctan(np.exp(m * g * (x - v * t - u0)))

def y_anti_kink(x, t, l, m, g, v, u0):
    return (4 / l) * np.arctan(np.exp(-m * g * (x - v * t - u0)))

def obtener_parametros():
    while True:
        l = float(input("Ingrese el valor para lambda λ = "))
        if l != 0:
            break
        print("El valor de lambda debe ser diferente de 0, inténtelo nuevamente")
    
    m = float(input("Ingrese el valor para Mu μ = "))
    
    while True:
        v = float(input("Ingrese el valor para la velocidad V (debe ser menor que 1) = "))
        if v < 1:
            break
        print("El valor de V debe ser menor que 1, inténtelo nuevamente")
    
    g = 1 / math.sqrt(1 - v**2)
    u0 = float(input("Ingrese el valor para U0 u0 = "))
    return l, m, g, v, u0

def graficar_funcion(tipo, x, t_values):
    l, m, g, v, u0 = obtener_parametros()
    
    # Crear la figura y el eje
    fig, ax = plt.subplots()
    ax.set_xlabel("posición [x]")
    ax.set_ylabel("φ(x,t)")
    ax.grid(True)

    if tipo == "K":
        label = "Kink"
        color = 'm'
        title = "Solución tipo Kink (Posición vs φ(x,t))"
    elif tipo == "A":
        label = "Anti-Kink"
        color = 'y'
        title = "Solución tipo Anti-Kink (Posición vs φ(x,t))"
    
    ax.set_title(title)

    # Inicializar la línea
    line, = ax.plot(x, y_kink(x, 0, l, m, g, v, u0) if tipo == "K" else y_anti_kink(x, 0, l, m, g, v, u0), 
                    label=label, color=color, linewidth=2)
    ax.legend()

    # Función de actualización para la animación
    def update(t):
        if tipo == "K":
            y = y_kink(x, t, l, m, g, v, u0)
        else:
            y = y_anti_kink(x, t, l, m, g, v, u0)
        line.set_ydata(y)
        return line,

    # Crear la animación
    anim = FuncAnimation(fig, update, frames=t_values, interval=50, blit=True)

    # Mostrar la animación
    plt.show()

def main():
    x = np.linspace(-10, 10, 500)
    t_values = np.linspace(0, 10, 200)  # Valores de tiempo para la animación
    
    mostrar_bienvenida()
    
    while True:
        opcion = input("Ingrese la opción deseada = ").strip().upper()
        if opcion in ["K", "A"]:
            if opcion == "K":
                print("Usted seleccionó la función tipo Kink")
                print("φ(t,x) = 4/λ arctan(exp(μγ(x - vt - u0)))")
                graficar_funcion("K", x, t_values)
            else:
                print("Usted seleccionó la función tipo Anti-Kink")
                print("φ(x,t) = 4/λ arctan(exp(-μγ(x - vt - u0)))")
                graficar_funcion("A", x, t_values)
            break
        print("Opción no válida. Por favor seleccione [K] para Kink o [A] para Anti-Kink.")
    
    print("Fin del programa.")

if __name__ == "__main__":
    main()
