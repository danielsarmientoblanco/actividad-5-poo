import tkinter as tk

from tkinter import messagebox, scrolledtext


class Programador:

    def __init__(self, nombre, apellidos):

        self.nombre = nombre

        self.apellidos = apellidos


    def __str__(self):

        return f"{self.nombre} {self.apellidos}"


class EquipoMaraton:

    MAX_INTEGRANTES = 3


    def __init__(self, nombre_equipo, universidad, lenguaje):

        self.nombre_equipo = nombre_equipo

        self.universidad = universidad

        self.lenguaje = lenguaje

        self.programadores = []


    def esta_lleno(self):

        return len(self.programadores) >= self.MAX_INTEGRANTES


    def anadir_programador(self, programador):

        if self.esta_lleno():

            raise Exception("El equipo está completo. No se pueden añadir más integrantes.")

        self.programadores.append(programador)


    @staticmethod

    def validar_campo(campo):

        if any(char.isdigit() for char in campo):

            raise ValueError("El campo no puede contener dígitos.")

        if len(campo) > 20:

            raise ValueError("La longitud no debe ser superior a 20 caracteres.")

        if not campo:

            raise ValueError("El campo no puede estar vacío.")


class EquipoApp:

    def __init__(self, root):

        self.root = root

        self.root.title("Gestión de Equipos de Maratón")

        self.root.geometry("600x550")

        self.root.configure(bg="#f0f8ff")

        self.equipo = None


        self.frame_equipo = tk.LabelFrame(root, text="Datos del Equipo", padx=15, pady=10, bg="#f0f8ff", font=("Arial", 12, "bold"))

        self.frame_equipo.pack(pady=10, padx=10, fill="x")


        self.frame_programador = tk.LabelFrame(root, text="Añadir Integrante", padx=15, pady=10, bg="#f0f8ff", font=("Arial", 12, "bold"))

        self.frame_programador.pack(pady=10, padx=10, fill="x")


        self.frame_info = tk.LabelFrame(root, text="Información del Equipo", padx=15, pady=10, bg="#f0f8ff", font=("Arial", 12, "bold"))

        self.frame_info.pack(pady=10, padx=10, fill="both", expand=True)


        tk.Label(self.frame_equipo, text="Nombre del Equipo:", bg="#f0f8ff").grid(row=0, column=0, sticky="w", pady=2)

        self.nombre_equipo_entry = tk.Entry(self.frame_equipo, width=40)

        self.nombre_equipo_entry.grid(row=0, column=1, pady=2, padx=5)


        tk.Label(self.frame_equipo, text="Universidad:", bg="#f0f8ff").grid(row=1, column=0, sticky="w", pady=2)

        self.universidad_entry = tk.Entry(self.frame_equipo, width=40)

        self.universidad_entry.grid(row=1, column=1, pady=2, padx=5)


        tk.Label(self.frame_equipo, text="Lenguaje de Prog.:", bg="#f0f8ff").grid(row=2, column=0, sticky="w", pady=2)

        self.lenguaje_entry = tk.Entry(self.frame_equipo, width=40)

        self.lenguaje_entry.grid(row=2, column=1, pady=2, padx=5)


        self.btn_crear_equipo = tk.Button(self.frame_equipo, text="Crear Equipo", command=self.crear_equipo, bg="#4682b4", fg="white")

        self.btn_crear_equipo.grid(row=3, column=0, columnspan=2, pady=10)


        tk.Label(self.frame_programador, text="Nombre:", bg="#f0f8ff").grid(row=0, column=0, sticky="w", pady=2)

        self.nombre_prog_entry = tk.Entry(self.frame_programador, width=40)

        self.nombre_prog_entry.grid(row=0, column=1, pady=2, padx=5)


        tk.Label(self.frame_programador, text="Apellidos:", bg="#f0f8ff").grid(row=1, column=0, sticky="w", pady=2)

        self.apellidos_prog_entry = tk.Entry(self.frame_programador, width=40)

        self.apellidos_prog_entry.grid(row=1, column=1, pady=2, padx=5)


        self.btn_anadir_prog = tk.Button(self.frame_programador, text="Añadir Integrante", command=self.anadir_programador, bg="#32cd32", fg="white")

        self.btn_anadir_prog.grid(row=2, column=0, columnspan=2, pady=10)


        self.info_text = scrolledtext.ScrolledText(self.frame_info, wrap=tk.WORD, height=10, state="disabled")

        self.info_text.pack(fill="both", expand=True)

        

        self.configurar_estado_widgets("programador", "disabled")


    def configurar_estado_widgets(self, seccion, estado):

        if seccion == "equipo":

            for child in self.frame_equipo.winfo_children():

                child.configure(state=estado)

        elif seccion == "programador":

            for child in self.frame_programador.winfo_children():

                child.configure(state=estado)


    def actualizar_info_texto(self):

        self.info_text.config(state="normal")

        self.info_text.delete(1.0, tk.END)

        if self.equipo:

            info = (f"Equipo: {self.equipo.nombre_equipo}\n"

                    f"Universidad: {self.equipo.universidad}\n"

                    f"Lenguaje: {self.equipo.lenguaje}\n"

                    f"----------------------------------\n"

                    f"Integrantes ({len(self.equipo.programadores)}/{self.equipo.MAX_INTEGRANTES}):\n")

            for i, prog in enumerate(self.equipo.programadores):

                info += f" {i+1}. {prog}\n"

            self.info_text.insert(tk.END, info)

        self.info_text.config(state="disabled")


    def crear_equipo(self):

        try:

            nombre = self.nombre_equipo_entry.get()

            universidad = self.universidad_entry.get()

            lenguaje = self.lenguaje_entry.get()

            

            EquipoMaraton.validar_campo(nombre)

            EquipoMaraton.validar_campo(universidad)

            EquipoMaraton.validar_campo(lenguaje)


            self.equipo = EquipoMaraton(nombre, universidad, lenguaje)

            messagebox.showinfo("Éxito", "Equipo creado correctamente. Ahora añada los integrantes.")

            

            self.configurar_estado_widgets("equipo", "disabled")

            self.configurar_estado_widgets("programador", "normal")

            self.actualizar_info_texto()


        except ValueError as e:

            messagebox.showerror("Error de Validación", str(e))

        except Exception as e:

            messagebox.showerror("Error", f"Ocurrió un error inesperado: {e}")


    def anadir_programador(self):

        if not self.equipo:

            messagebox.showerror("Error", "Primero debe crear un equipo.")

            return

        

        try:

            nombre = self.nombre_prog_entry.get()

            apellidos = self.apellidos_prog_entry.get()


            EquipoMaraton.validar_campo(nombre)

            EquipoMaraton.validar_campo(apellidos)


            programador = Programador(nombre, apellidos)

            self.equipo.anadir_programador(programador)


            self.nombre_prog_entry.delete(0, tk.END)

            self.apellidos_prog_entry.delete(0, tk.END)

            self.actualizar_info_texto()


            if self.equipo.esta_lleno():

                messagebox.showinfo("Equipo Completo", "Se han añadido todos los integrantes al equipo.")

                self.configurar_estado_widgets("programador", "disabled")


        except ValueError as e:

            messagebox.showerror("Error de Validación", str(e))

        except Exception as e:

            messagebox.showerror("Error", str(e))


def main():

    root = tk.Tk()

    app = EquipoApp(root)

    root.mainloop()


if __name__ == "__main__":

    main()
