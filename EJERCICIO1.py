import tkinter as tk
from tkinter import messagebox

class Vendedor:
    def __init__(self, nombre, apellidos):
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = 0

    def get_info(self):

        return (f"Nombre del vendedor = {self.nombre}\n"
                f"Apellidos del vendedor = {self.apellidos}\n"
                f"Edad del vendedor = {self.edad}")

    def verificar_edad(self, edad):

        if not 0 <= edad < 120:
            raise ValueError("La edad no puede ser negativa ni mayor a 120.")
        
        if edad < 18:
            raise ValueError("El vendedor debe ser mayor de 18 años.")
        
        self.edad = edad

class VendedorApp:

    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Vendedores")
        self.root.geometry("480x300")
        self.root.configure(bg="#f0f0f0")

        main_frame = tk.Frame(self.root, bg="#f0f0f0", padx=20, pady=20)
        main_frame.pack(expand=True, fill="both")

        
        tk.Label(main_frame, text="Nombre del Vendedor:", bg="#f0f0f0", font=("Arial", 12)).grid(row=0, column=0, sticky="w", pady=5)
        self.nombre_entry = tk.Entry(main_frame, font=("Arial", 12), width=30)
        self.nombre_entry.grid(row=0, column=1, pady=5, padx=10) 

        
        tk.Label(main_frame, text="Apellidos del Vendedor:", bg="#f0f0f0", font=("Arial", 12)).grid(row=1, column=0, sticky="w", pady=5)
        self.apellidos_entry = tk.Entry(main_frame, font=("Arial", 12), width=30)
        self.apellidos_entry.grid(row=1, column=1, pady=5, padx=10) 

        
        tk.Label(main_frame, text="Edad del Vendedor:", bg="#f0f0f0", font=("Arial", 12)).grid(row=2, column=0, sticky="w", pady=5)
        self.edad_entry = tk.Entry(main_frame, font=("Arial", 12), width=30)
        self.edad_entry.grid(row=2, column=1, pady=5, padx=10)

        
        verificar_button = tk.Button(main_frame, text="Verificar y Guardar", font=("Arial", 12, "bold"), bg="#4CAF50", fg="white", command=self.procesar_vendedor)
        verificar_button.grid(row=3, column=0, columnspan=2, pady=20)

    def procesar_vendedor(self):

        nombre = self.nombre_entry.get()
        apellidos = self.apellidos_entry.get()
        edad_str = self.edad_entry.get()

        if not nombre or not apellidos or not edad_str:
            messagebox.showerror("Error de Entrada", "Todos los campos son obligatorios.")
            return

        try:
            edad = int(edad_str)
            vendedor = Vendedor(nombre, apellidos)
            vendedor.verificar_edad(edad)
            info = vendedor.get_info()
            messagebox.showinfo("Vendedor Registrado", info)

        except ValueError as e:
            messagebox.showerror("Error de Validación", f"Error en los datos ingresados:\n{e}")
        except Exception as e:
            messagebox.showerror("Error Inesperado", f"Ocurrió un error: {e}")

def main():

    root = tk.Tk()
    app = VendedorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
