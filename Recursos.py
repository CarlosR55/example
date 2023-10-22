import psutil
import tkinter as tk

# Crear una ventana
window = tk.Tk()
window.title("Uso de recursos de la PC")

# Crear etiquetas para mostrar la información
total_label = tk.Label(window, text="Memoria total:")
available_label = tk.Label(window, text="Memoria disponible:")
used_label = tk.Label(window, text="Memoria utilizada:")
mem_percent_label = tk.Label(window, text="Porcentaje de memoria utilizada:")
cpu_percent_label = tk.Label(window, text="Porcentaje de uso de CPU:")

# Añadir las etiquetas a la ventana
total_label.pack()
available_label.pack()
used_label.pack()
mem_percent_label.pack()
cpu_percent_label.pack()

# Función para actualizar la información de uso de recursos de la PC
def update_info():
    # Obtener información sobre la memoria virtual
    mem = psutil.virtual_memory()

    # Obtener la cantidad total de memoria RAM en bytes
    total = mem.total

    # Obtener la cantidad de memoria RAM disponible en bytes
    available = mem.available

    # Obtener la cantidad de memoria RAM utilizada en bytes
    used = mem.used

    # Obtener el porcentaje de memoria RAM utilizada
    mem_percent = mem.percent

    # Obtener el porcentaje de uso de CPU
    cpu_percent = psutil.cpu_percent()

    # Convertir la cantidad de memoria RAM utilizada a megabytes
    used_mb = used / (1024 * 1024)

    # Actualizar las etiquetas con la información actualizada
    total_label.config(text=f"Memoria total: {total / (1024 * 1024):.2f} MB")
    available_label.config(text=f"Memoria disponible: {available / (1024 * 1024):.2f} MB")
    used_label.config(text=f"Memoria utilizada: {used} bytes ({used_mb:.2f} MB)")
    mem_percent_label.config(text=f"Porcentaje de memoria utilizada: {mem_percent}%")
    cpu_percent_label.config(text=f"Porcentaje de uso de CPU: {cpu_percent}%")

    # Programar la función para que se ejecute de nuevo después de 1000 milisegundos (1 segundo)
    window.after(1000, update_info)

# Iniciar la actualización de la información de uso de recursos de la PC
update_info()

# Iniciar el bucle principal de la ventana
window.mainloop()
