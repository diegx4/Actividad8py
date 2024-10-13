import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Registro de Datos")
        
        #Fondo
        self.fondo = Image.open(r"C:\Users\1150070020\Downloads\FND.jpeg")
        self.fondo = self.fondo.resize((800, 600), Image.LANCZOS)
        self.fondo_img = ImageTk.PhotoImage(self.fondo)
        self.label_fondo = tk.Label(root, image=self.fondo_img)
        self.label_fondo.place(x=0, y=0, relwidth=1, relheight=1) 

        # Etiquetas y campos de entrada
        self.label_nombre = tk.Label(root, text="Nombre:", bg='lightblue')
        self.label_nombre.pack(pady=5)

        self.entry_nombre = tk.Entry(root)
        self.entry_nombre.pack(pady=5)

        self.label_apellido = tk.Label(root, text="Apellido:", bg='lightblue')
        self.label_apellido.pack(pady=5)

        self.entry_apellido = tk.Entry(root)
        self.entry_apellido.pack(pady=5)

        self.label_telefono = tk.Label(root, text="Teléfono:", bg='lightblue')
        self.label_telefono.pack(pady=5)

        self.entry_telefono = tk.Entry(root)
        self.entry_telefono.pack(pady=5)

        self.label_edad = tk.Label(root, text="Edad:", bg='lightblue')
        self.label_edad.pack(pady=5)

        self.entry_edad = tk.Entry(root)
        self.entry_edad.pack(pady=5)

        self.label_estatura = tk.Label(root, text="Estatura:", bg='lightblue')
        self.label_estatura.pack(pady=5)

        self.entry_estatura = tk.Entry(root)
        self.entry_estatura.pack(pady=5)

        self.radio_var = tk.StringVar(value="Hombre")  # Valor por defecto
        self.radio_hombre = tk.Radiobutton(root, text="Hombre", variable=self.radio_var, value="Hombre", bg='lightblue')
        self.radio_hombre.pack(pady=5)

        self.radio_mujer = tk.Radiobutton(root, text="Mujer", variable=self.radio_var, value="Mujer", bg='lightblue')
        self.radio_mujer.pack(pady=5)

        # Botón para guardar los datos
        self.button_guardar = tk.Button(root, text="Guardar", command=self.guardar)
        self.button_guardar.pack(pady=20)

    def guardar(self):
        # Obtener datos
        nombre = self.entry_nombre.get()
        apellido = self.entry_apellido.get()
        telefono = self.entry_telefono.get()
        edad = self.entry_edad.get()
        estatura = self.entry_estatura.get()
        genero = self.radio_var.get()

        # Validar campos
        if not all([nombre, apellido, telefono, edad, estatura]):
            messagebox.showwarning("Advertencia", "Por favor, complete todos los campos.")
            return

        # Guardar en la base de datos
        try:
            connection = mysql.connector.connect(
                host='localhost',
                database='dats',
                user='root',
                password='gsmn71acD*'
            )
            cursor = connection.cursor()
            query = "INSERT INTO personas (Nombre, Apellido, Telefono, Edad, Estatura, Genero) VALUES (%s, %s, %s, %s, %s, %s)"
            cursor.execute(query, (nombre, apellido, telefono, edad, estatura, genero))
            connection.commit()
            messagebox.showinfo("Éxito", "Datos guardados correctamente.")
            self.limpiar_campos()
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Ocurrió un error al guardar los datos: {err}")
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    def limpiar_campos(self):
        self.entry_nombre.delete(0, tk.END)
        self.entry_apellido.delete(0, tk.END)
        self.entry_telefono.delete(0, tk.END)
        self.entry_edad.delete(0, tk.END)
        self.entry_estatura.delete(0, tk.END)
        self.radio_var.set("Hombre")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.geometry("300x500") 
    root.mainloop()