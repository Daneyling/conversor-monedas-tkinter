import tkinter as tk
from tkinter import ttk, messagebox

# Tasas de cambio ejemplo
exchange_rates = {
    "USD": {"USD": 1.0, "EUR": 0.89, "GBP": 0.78, "JPY": 156.3, "MXN": 18.2, "NIO": 36.5},
    "EUR": {"USD": 1.12, "EUR": 1.0, "GBP": 0.88, "JPY": 174.3, "MXN": 20.3, "NIO": 40.2},
    "GBP": {"USD": 1.28, "EUR": 1.14, "GBP": 1.0, "JPY": 198.4, "MXN": 23.1, "NIO": 46.3},
    "JPY": {"USD": 0.0064, "EUR": 0.0057, "GBP": 0.0050, "JPY": 1.0, "MXN": 0.12, "NIO": 0.23},
    "MXN": {"USD": 0.055, "EUR": 0.049, "GBP": 0.043, "JPY": 8.3, "MXN": 1.0, "NIO": 2.0},
    "NIO": {"USD": 0.027, "EUR": 0.025, "GBP": 0.022, "JPY": 4.4, "MXN": 0.5, "NIO": 1.0}
}

# Colores vivos y modernos
BG_COLOR = "#CBA6F7"        # Fondo lila brillante
BTN_COLOR = "#FF4F81"       # Fucsia elegante
TEXT_COLOR = "#2D2D2D"      # Gris oscuro
ENTRY_BG = "#FAFAFA"        # Fondo entradas
BTN_TEXT = "#FFFFFF"        # Texto botón

# Función de conversión
def convert_currency():
    try:
        amount = float(entry_amount.get())
        from_currency = combo_from.get()
        to_currency = combo_to.get()
        rate = exchange_rates[from_currency][to_currency]
        result = round(amount * rate, 2)
        entry_result.config(state='normal')
        entry_result.delete(0, tk.END)
        entry_result.insert(0, str(result))
        entry_result.config(state='readonly')
    except ValueError:
        messagebox.showerror("Error", "Por favor ingresa una cantidad válida.")
    except KeyError:
        messagebox.showerror("Error", "Conversión no disponible.")

# Crear ventana
root = tk.Tk()
root.title("Conversor de Monedas Daneyling y Miguel")
root.geometry("400x430")
root.configure(bg=BG_COLOR)

monedas = ["USD", "EUR", "GBP", "JPY", "MXN", "NIO"]

# Etiquetas
def crear_etiqueta(texto):
    return tk.Label(root, text=texto, bg=BG_COLOR, fg=TEXT_COLOR, font=("Arial", 14, "bold"))

crear_etiqueta("De moneda:").pack(pady=(15, 0))
combo_from = ttk.Combobox(root, values=monedas, state="readonly", font=("Arial", 12))
combo_from.pack(pady=5)
combo_from.set("USD")

crear_etiqueta("A moneda:").pack(pady=(15, 0))
combo_to = ttk.Combobox(root, values=monedas, state="readonly", font=("Arial", 12))
combo_to.pack(pady=5)
combo_to.set("EUR")

crear_etiqueta("Cantidad:").pack(pady=(15, 0))
entry_amount = tk.Entry(root, font=("Arial", 16), bg=ENTRY_BG, justify="center")
entry_amount.pack(pady=5, ipadx=10, ipady=5)

convert_btn = tk.Button(root, text="Convertir", font=("Arial", 13, "bold"),
                        bg=BTN_COLOR, fg=BTN_TEXT, padx=10, pady=5,
                        activebackground="#E43D6F", command=convert_currency)
convert_btn.pack(pady=20)

crear_etiqueta("Resultado:").pack()
entry_result = tk.Entry(root, font=("Arial", 16), bg=ENTRY_BG, justify="center", state="readonly")
entry_result.pack(pady=5, ipadx=10, ipady=5)

# Ejecutar ventana
root.mainloop()