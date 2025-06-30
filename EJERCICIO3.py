import tkinter as tk
from tkinter import messagebox
import math



def calcular_logaritmo(valor):

    if valor <= 0:
        raise ValueError("El valor para el logaritmo debe ser un número positivo.")
    return math.log(valor)

def calcular_raiz_cuadrada(valor):

    if valor < 0:
        raise ValueError("El valor para la raíz cuadrada no puede ser negativo.")
    return math.sqrt(valor)



class CalculadoraApp:

    def __init__(self, root):
        self.root = root
        self.root.title("Cálculos Numéricos")
        self.root.geometry("450x250")
        self.root.configure(bg="#eaf2f8") 


        main_frame = tk.Frame(self.root, bg="#eaf2f8", padx=20, pady=20)
        main_frame.pack(expand=True, fill="both")


        tk.Label(main_frame, text="Ingrese un valor numérico:", bg="#eaf2f8", font=("Arial", 12)).pack(pady=(0, 5))
        self.valor_entry = tk.Entry(main_frame, font=("Arial", 14), width=20, justify='center')
        self.valor_entry.pack(pady=5)


        calcular_button = tk.Button(main_frame, text="Calcular", font=("Arial", 12, "bold"), bg="#2874a6", fg="white", command=self.realizar_calculos)
        calcular_button.pack(pady=15)


        self.resultado_label = tk.Label(main_frame, text="", bg="#eaf2f8", font=("Arial", 12, "italic"), justify='left')
        self.resultado_label.pack(pady=10)

    def realizar_calculos(self):

        valor_str = self.valor_entry.get()

        if not valor_str:
            messagebox.showwarning("Entrada Vacía", "Por favor, ingrese un número.")
            return

        try:
            valor = float(valor_str)
            
            
            try:
                resultado_log = calcular_logaritmo(valor)
                log_str = f"Logaritmo Neperiano: {resultado_log:.6f}"
            except ValueError as e:
                log_str = f"Logaritmo Neperiano: {e}"

            
            try:
                resultado_raiz = calcular_raiz_cuadrada(valor)
                raiz_str = f"Raíz Cuadrada: {resultado_raiz:.6f}"
            except ValueError as e:
                raiz_str = f"Raíz Cuadrada: {e}"
            
            
            self.resultado_label.config(text=f"{log_str}\n{raiz_str}")

        except ValueError:
            
            messagebox.showerror("Error de Entrada", "El valor ingresado debe ser numérico.")
            self.resultado_label.config(text="")
        except Exception as e:
            
            messagebox.showerror("Error Inesperado", f"Ocurrió un error: {e}")
            self.resultado_label.config(text="")

def main():

    root = tk.Tk()
    app = CalculadoraApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()

