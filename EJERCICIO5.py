import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext

def leer_archivo_texto(ruta_archivo):
    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
            contenido = archivo.read()
            return contenido
    except FileNotFoundError:
        raise Exception(f"El archivo no se encontró en la ruta:\n{ruta_archivo}")
    except Exception as e:
        raise Exception(f"No se pudo leer el archivo.\nError: {e}")

class LectorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lector de Archivos de Texto")
        self.root.geometry("700x500")
        self.root.configure(bg="#2c3e50")

        top_frame = tk.Frame(self.root, bg="#2c3e50", pady=10)
        top_frame.pack(fill="x")

        btn_seleccionar = tk.Button(top_frame, text="Seleccionar Archivo (.txt)", 
                                    font=("Arial", 12, "bold"), bg="#3498db", fg="white", 
                                    command=self.seleccionar_y_leer_archivo)
        btn_seleccionar.pack(side="left", padx=10)
        
        self.ruta_label = tk.Label(top_frame, text="Ningún archivo seleccionado", 
                                   font=("Arial", 10, "italic"), bg="#2c3e50", fg="white")
        self.ruta_label.pack(side="left", padx=10)

        self.texto_contenido = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, 
                                                         font=("Courier New", 11), 
                                                         state="disabled", bg="#ecf0f1")
        self.texto_contenido.pack(pady=10, padx=10, fill="both", expand=True)

    def seleccionar_y_leer_archivo(self):
        ruta_archivo = filedialog.askopenfilename(
            title="Seleccione un archivo de texto",
            filetypes=(("Archivos de Texto", "*.txt"), ("Todos los archivos", "*.*"))
        )

        if not ruta_archivo:
            return

        self.ruta_label.config(text=ruta_archivo)
        
        self.texto_contenido.config(state="normal")
        self.texto_contenido.delete(1.0, tk.END)

        try:
            contenido = leer_archivo_texto(ruta_archivo)
            self.texto_contenido.insert(tk.END, contenido)
        except Exception as e:
            messagebox.showerror("Error de Lectura", str(e))
        finally:
            self.texto_contenido.config(state="disabled")

def main():
    root = tk.Tk()
    app = LectorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
