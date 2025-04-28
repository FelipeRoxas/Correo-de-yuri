import tkinter as tk

#crear la ventana principal
ventana = tk.Tk()

#establecer el titulo de la ventana
ventana.title("MI primera ventana con Tkinter")

#establecer tamaño de la ventana
ventana.geometry("300x200")

#etiqueta de texto en la ventana
etiqueta = tk.Label(ventana, text="Hola, Tkinter")
etiqueta.pack(pady=20)

#Boton para cerrar la ventana
boton = tk.Button(ventana, text="cerrar", command=ventana.quit)
boton.pack(pady=20)

#iniciar el bucle principal de la interfaz grafica
ventana.mainloop()