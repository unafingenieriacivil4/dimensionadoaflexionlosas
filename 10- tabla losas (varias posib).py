import tkinter as tk

def encontrar_valores_mas_cercanos(matriz, valor_objetivo, n=3):
    # Lista para almacenar los valores cercanos
    valores_cercanos = []

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            valor_actual = matriz[i][j]
            # Solo considerar valores que son mayores o iguales al valor objetivo
            if valor_actual >= valor_objetivo:
                diferencia = abs(valor_actual - valor_objetivo)
                # Agregar el valor y su posición a la lista
                valores_cercanos.append((diferencia, valor_actual, i, j))

    # Ordenar la lista por la diferencia y seleccionar los n más cercanos
    valores_cercanos.sort(key=lambda x: x[0])
    return valores_cercanos[:n]

def buscar_valor():
    try:
        valor_objetivo = float(entry.get())
        valores_cercanos = encontrar_valores_mas_cercanos(matriz, valor_objetivo)

        # Formatear el resultado
        resultados = []
        for diferencia, valor, fila, columna in valores_cercanos:
            resultados.append("Asreal=" f"{valor} cm² (ϕ {columnas[columna]} cada {filas[fila]})")
        
        # Usar '\n' para mostrar los resultados uno debajo del otro
        resultado_text.set("\n".join(resultados) if resultados else "No hay valores disponibles que cumplan con el criterio.")
    except ValueError:
        resultado_text.set("Por favor, ingresa un número válido.")

# Definir la matriz de 18 filas y 6 columnas
matriz = [
    [4.04, 7.18, 11.22, 16.16, 28.73, 44.87],
    [3.53, 6.28, 9.82, 14.14, 25.14, 39.26],
    [3.14, 5.59, 8.73, 12.57, 22.34, 34.90],
    [2.83, 5.03, 7.85, 11.31, 20.11, 31.41],
    [2.57, 4.57, 7.14, 10.28, 18.28, 28.55],
    [2.36, 4.19, 6.54, 9.42, 16.76, 26.17],
    [2.17, 3.87, 6.04, 8.70, 15.47, 24.16],
    [2.02, 3.59, 5.61, 8.08, 14.36, 22.44],
    [1.89, 3.35, 5.24, 7.54, 13.41, 20.94],
    [1.77 ,3.14 ,4.91 ,7.07 ,12.57 ,19.64],
    [1.66 ,2.96 ,4.62 ,6.65 ,11.83 ,18.18],
    [1.57 ,2.79 ,4.36 ,6.28 ,11.17 ,17.16],
    [1.49 ,2.65 ,4.13 ,5.95 ,10.58 ,16.54],
    [1.41 ,2.51 ,3.93 ,5.65 ,10.05 ,15.72],
    [1.34 ,2.39 ,3.74 ,5.38 ,9.57 ,14.95],
    [1.28 ,2.28 ,3.56 ,5.13 ,9.13 ,14.26],
    [1.23 ,2.18 ,3.41 ,4.91 ,8.73 ,13.63],
    [1.18 ,2.09 ,3.27 ,4.70 ,8.36 ,13.07],
    [1.13 ,2.01 ,3.14 ,4.52 ,8.04 ,12.57],
] # Asegúrate de que tienes exactamente las filas necesarias (18 filas)

# Definir los diámetros de barra y las separaciones
columnas = ["6 mm", "8 mm", "10 mm", "12 mm", "16 mm", "20 mm"] # Diámetros de barra (6 columnas)
filas = ["7 cm", "8 cm", "9 cm", "10 cm", "11 cm", "12 cm", "13 cm",
         "14 cm", "15 cm", "16 cm", "17 cm", "18 cm", "19 cm",
         "20 cm", "21 cm", "22 cm", "23 cm", "24 cm",
         "25 cm"] # Separaciones (18 filas)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Dimensionado de acero a flexión")

# Crear y colocar los widgets
label = tk.Label(ventana,text="Introduce el área necesaria por flexión: As [cm²]")
label.pack(pady=10)

entry = tk.Entry(ventana)
entry.pack(pady=5)

boton_buscar = tk.Button(ventana,text="Dimensionar",command=buscar_valor)
boton_buscar.pack(pady=20)

# Etiqueta para mostrar el resultado
resultado_text = tk.StringVar() # Variable para almacenar el texto del resultado
resultado_label = tk.Label(ventana,textvariable=resultado_text)
resultado_label.pack(pady=10)

# Iniciar el bucle principal de la interfaz gráfica
ventana.mainloop()