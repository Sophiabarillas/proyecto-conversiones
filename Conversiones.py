import tkinter as tk
from tkinter import ttk, messagebox

# Funciones de conversión
def convertir_longitud(valor, tipo):
    try:
        valor = float(valor)
        if tipo == "Metros a Kilómetros":
            return f"{valor / 1000:.3f} km"
        elif tipo == "Pulgadas a Metros":
            return f"{valor * 0.0254:.3f} m"
    except ValueError:
        messagebox.showerror("Error", "Ingrese un número válido")

def convertir_masa(valor, tipo):
    try:
        valor = float(valor)
        if tipo == "Kilogramos a Gramos":
            return f"{valor * 1000:.2f} g"
        elif tipo == "Libras a Kilogramos":
            return f"{valor * 0.453592:.2f} kg"
    except ValueError:
        messagebox.showerror("Error", "Ingrese un número válido")

def convertir_tiempo(valor, tipo):
    try:
        valor = float(valor)
        if tipo == "Segundos a Minutos":
            return f"{valor / 60:.2f} min"
        elif tipo == "Horas a Días":
            return f"{valor / 24:.2f} días"
    except ValueError:
        messagebox.showerror("Error", "Ingrese un número válido")

# Función para crear ventana de conversión
def crear_ventana(titulo, opciones, funcion_conversion):
    ventana = tk.Toplevel()
    ventana.title(titulo)
    ventana.geometry("300x200")

    tk.Label(ventana, text="Seleccione conversión:").pack(pady=5)
    tipo_conversion = ttk.Combobox(ventana, values=opciones, state="readonly")
    tipo_conversion.pack()

    tk.Label(ventana, text="Ingrese valor:").pack(pady=5)
    entrada = tk.Entry(ventana)
    entrada.pack()

    resultado = tk.StringVar()
    tk.Label(ventana, textvariable=resultado).pack(pady=10)

    def ejecutar_conversion():
        res = funcion_conversion(entrada.get(), tipo_conversion.get())
        if res:
            resultado.set(f"Resultado: {res}")

    tk.Button(ventana, text="Convertir", bg="#d8855f", command=ejecutar_conversion).pack()

# Ventana principal
ventana_principal = tk.Tk()
ventana_principal.title("Conversor Universal")
ventana_principal.geometry("250x200")

tk.Label(ventana_principal, text="Escoja su opción", bg="#e74479", font=("Times New Roman", 17)).pack(fill="x", pady=10)

tk.Button(ventana_principal, text="Longitud", bg="#5f72d8", fg="black", command=lambda: 
    crear_ventana("Conversión de Longitud", ["Metros a Kilómetros", "Pulgadas a Metros"], convertir_longitud)
).pack(pady=5)

tk.Button(ventana_principal, text="Masa", bg="#895fd8", fg="black", command=lambda: 
    crear_ventana("Conversión de Masa", ["Kilogramos a Gramos", "Libras a Kilogramos"], convertir_masa)
).pack(pady=5)

tk.Button(ventana_principal, text="Tiempo", bg="#5f99d8", fg="black", command=lambda: 
    crear_ventana("Conversión de Tiempo", ["Segundos a Minutos", "Horas a Días"], convertir_tiempo)
).pack(pady=5)

ventana_principal.mainloop()
