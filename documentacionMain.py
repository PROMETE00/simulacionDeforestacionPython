import tkinter as tk

class Interfaz:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("DOCUMENTACIÓN")
        
        # Configuración de pantalla
        screen_width = self.ventana.winfo_screenwidth()
        screen_height = self.ventana.winfo_screenheight()
        self.ventana.geometry(f"{screen_width}x{screen_height}")
        
        ancho_panel_izquierdo = 250
        ancho_panel_derecho = screen_width - ancho_panel_izquierdo
        
        # Panel izquierdo
        self.panel_izquierdo = tk.Frame(self.ventana, bg="white", width=ancho_panel_izquierdo, height=screen_height)
        self.panel_izquierdo.place(x=0, y=0)
        
        # Panel derecho
        self.panel_derecho = tk.Frame(self.ventana, bg="brown", width=ancho_panel_derecho, height=screen_height)
        self.panel_derecho.place(x=ancho_panel_izquierdo, y=0)
        
        # Título
        self.tituloPanelDerecho = tk.Label(
            self.panel_derecho, text="DOCUMENTACION", font=("Arial", 30), bg="brown", fg="white"
        )
        self.tituloPanelDerecho.place(x=50, y=40)
        
        # Caja de texto
        self.cajaTexto = tk.Text(self.panel_derecho, height=15, width=70, wrap=tk.WORD, state=tk.DISABLED)
        self.cajaTexto.place(x=50, y=100)
        
        # Botones
        self.crear_botones()

    def crear_botones(self):
        ancho_boton = 25
        alto_boton = 3
        x_boton = 30
        botones = [
            ("Contenido 1", 150, "Este es el contenido 1", "COMPONENTES DEL MODELO MATEMATICO"),
            ("Contenido 2", 250, "Este es el contenido 2", "OBJETIVOS DEL ANALISIS Y RESULTADOS ESPERADOS"),
            ("Contenido 3", 350, "Este es el contenido 3", "MODELO DE REGRESION SIMPLE"),
        ]
        
        for texto, y_pos, contenido, titulo in botones:
            boton = tk.Button(
                self.panel_izquierdo, text=texto, font=("Arial", 24), width=ancho_boton, height=alto_boton,
                command=lambda c=contenido, t=titulo: self.cambiar_contenido(c, t)
            )
            boton.place(x=x_boton, y=y_pos)

    def cambiar_contenido(self, contenido, titulo):
        # Cambiar el contenido de la caja de texto
        self.cajaTexto.config(state=tk.NORMAL)
        self.cajaTexto.delete(1.0, tk.END)
        self.cajaTexto.insert(tk.END, contenido)
        self.cajaTexto.config(state=tk.DISABLED)
        
        # Cambiar el título del panel derecho
        self.tituloPanelDerecho.config(text=titulo)

if __name__ == "__main__":
    ventana = tk.Tk()
    app = Interfaz(ventana)
    ventana.mainloop()
