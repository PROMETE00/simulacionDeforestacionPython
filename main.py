import tkinter as tk
from documentacionMain import Interfaz

def main():
    ventana = tk.Tk()
    app = Interfaz(ventana)  # Instanciamos la interfaz desde el archivo `interfaz.py`
    ventana.mainloop()

if __name__ == "__main__":
    main()
