# Classic-Fields
Gráfica para Kink y Antikink
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

print('  ')
print("Bienvenido al programa para graficar la solución de Sine-Gordon tipo Kink y Anti-kink")
print("Por favor seleccione el tipo de solución que desea graficar:")
print("[K] para la función de tipo Kink")
print("[A] para la función de tipo Anti-Kink")

# Variables globales para almacenar los valores de las funciones
phi_valoresK = None
phi_valoresA = None
x = np.linspace(-10, 10, 500)  # Rango de x común para ambas funciones

# Definir la función Kink
def y_kink(x, t, l, m, g, v, u0):
    return (4 / l) * np.arctan(np.exp(m * g * (x - v * t - u0)))

# Definir la función Anti-Kink
def y_anti_kink(x, t, l, m, g, v, u0):
    return (4 / l) * np.arctan(np.exp(-m * g * (x - v * t - u0)))

# Función para graficar Kink o Anti-Kink
def graficar_funcion(tipo):
    while True:
        l = float(input("Ingrese el valor para lambda λ = "))
        if l == 0:
            print("El valor de lambda debe ser diferente de 0, inténtelo nuevamente")
        else:
            break
    
    m = float(input("Ingrese el valor para Mu μ = "))
    g = float(input("Ingrese el valor para Gamma γ = "))
    v = float(input("Ingrese el valor para la velocidad V = "))
    u0 = float(input("Ingrese el valor para U0 u0 = "))
    t_fijo = 0.0
    
    if tipo == "K":
        phi_valores = y_kink(x, t_fijo, l, m, g, v, u0)
        label = "Kink"
        color = 'm'
        title = "Solución tipo Kink (Posición vs φ(x,t))"
    elif tipo == "A":
        phi_valores = y_anti_kink(x, t_fijo, l, m, g, v, u0)
        label = "Anti-Kink"
        color = 'y'
        title = "Solución tipo Anti-Kink (Posición vs φ(x,t))"
    
    # Graficar
    plt.plot(x, phi_valores, label=label, color=color, linewidth=2)
    plt.xlabel("posición [x]")
    plt.ylabel("φ(x,t)")
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.show()
    
    return phi_valores

# Bucle principal
while True:
    a = input("Ingrese la opción deseada = ").strip().upper()  # Convertir a mayúsculas y eliminar espacios
    if a == "K":
        print("Usted seleccionó la función tipo Kink")
        print("φ(t,x) = 4/λ arctan(exp(μγ(x - vt - u0)))")
        phi_valoresK = graficar_funcion("K")
        break  # Salir del bucle si la opción es válida
    
    elif a == "A":
        print("Usted seleccionó la función tipo Anti-Kink")
        print("φ(x,t) = 4/λ arctan(exp(-μγ(x - vt - u0)))")
        phi_valoresA = graficar_funcion("A")
        break  # Salir del bucle si la opción es válida
    
    else:
        print("Opción no válida. Por favor seleccione [K] para Kink o [A] para Anti-Kink.")

# Preguntar si desea graficar otra función
while True:
    k = input("¿Desea graficar otra función? ([S] para sí y [N] para no): ").strip().upper()
    if k == "S":
        a = input("Ingrese la opción deseada ([K] para Kink o [A] para Anti-Kink) = ").strip().upper()
        if a == "K":
            print("Usted seleccionó la función tipo Kink")
            print("φ(t,x) = 4/λ arctan(exp(μγ(x - vt - u0)))")
            phi_valoresK = graficar_funcion("K")
        elif a == "A":
            print("Usted seleccionó la función tipo Anti-Kink")
            print("φ(x,t) = 4/λ arctan(exp(-μγ(x - vt - u0)))")
            phi_valoresA = graficar_funcion("A")
        else:
            print("Opción no válida. Por favor seleccione [K] para Kink o [A] para Anti-Kink.")
    elif k == "N":
        break  # Salir del bucle si el usuario no quiere graficar otra función
    else:
        print("Por favor ingrese una opción válida, con las letras [S] y [N].")

# Preguntar si desea graficar ambas funciones en una sola imagen
while True:
    d = input("¿Desea graficar ambas funciones en una sola imagen? ([S] para sí y [N] para no): ").strip().upper()
    if d == "S":
        if phi_valoresK is not None and phi_valoresA is not None:
            # Graficar ambas funciones
            plt.plot(x, phi_valoresK, label="Kink", color='m', linewidth=2)  # Kink en magenta
            plt.plot(x, phi_valoresA, label="Anti-Kink", color='y', linewidth=2)  # Anti-Kink en amarillo
            plt.xlabel("posición [x]")
            plt.ylabel("φ(x,t)")
            plt.title("Soluciones de tipo Kink y Anti-Kink (Posición vs φ(x,t))")
            plt.legend()
            plt.grid(True)
            plt.show()
            
            print("Fin del programa.")
        else:
            print("No se han calculado ambas funciones. Ejecute primero las opciones [K] y [A].")
        break  # Salir del bucle después de graficar
    
    elif d == "N":
        print("Fin del programa.")
        break  # Salir del bucle si el usuario no quiere graficar
    
    else:
        print("Por favor ingrese una opción válida, con las letras [S] y [N].")
