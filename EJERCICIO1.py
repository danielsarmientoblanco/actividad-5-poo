import tkinter as tk
from tkinter import scrolledtext

class SimuladorExcepcionesApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simulador de Manejo de Excepciones")
        self.root.geometry("500x450")
        self.root.configure(bg="#f0f0f0")

        main_frame = tk.Frame(self.root, bg="#f0f0f0", padx=15, pady=15)
        main_frame.pack(expand=True, fill="both")

        button_frame = tk.Frame(main_frame, bg="#f0f0f0")
        button_frame.pack(pady=10)

        btn_excepcion1 = tk.Button(button_frame, text="Lanzar ZeroDivisionError", 
                                   font=("Arial", 11, "bold"), bg="#e74c3c", fg="white",
                                   command=self.simular_primer_bloque)
        btn_excepcion1.pack(side="left", padx=10)

        btn_excepcion2 = tk.Button(button_frame, text="Lanzar AttributeError", 
                                   font=("Arial", 11, "bold"), bg="#9b59b6", fg="white",
                                   command=self.simular_segundo_bloque)
        btn_excepcion2.pack(side="left", padx=10)

        self.consola_output = scrolledtext.ScrolledText(main_frame, wrap=tk.WORD, 
                                                        font=("Courier New", 11), 
                                                        height=15, bg="#2c3e50", fg="white")
        self.consola_output.pack(pady=10, fill="both", expand=True)

    def log_message(self, message):
        self.consola_output.insert(tk.END, message + "\n")
        self.consola_output.see(tk.END)

    def simular_primer_bloque(self):
        self.consola_output.delete(1.0, tk.END)
        self.log_message("--- Iniciando Simulación 1 ---")
        
        try:
            self.log_message("Ingresando al primer try")
            cociente = 10000 / 0
            self.log_message("Después de la división")
        except ZeroDivisionError:
            self.log_message("División por cero")
        finally:
            self.log_message("Ingresando al primer finally")
        
        self.log_message("--- Simulación 1 Finalizada ---\n")

    def simular_segundo_bloque(self):
        self.consola_output.delete(1.0, tk.END)
        self.log_message("--- Iniciando Simulación 2 ---")

        try:
            self.log_message("Ingresando al segundo try")
            objeto = None
            objeto.to_string() 
            self.log_message("Imprimiendo objeto")
        except ZeroDivisionError:
            self.log_message("División por cero")
        except Exception as e:
            self.log_message("Ocurrió una excepción")
            self.log_message(f"(Tipo de excepción: {type(e).__name__})")
        finally:
            self.log_message("Ingresando al segundo finally")
        
        self.log_message("--- Simulación 2 Finalizada ---\n")

def main():
    root = tk.Tk()
    app = SimuladorExcepcionesApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
