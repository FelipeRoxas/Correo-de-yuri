import tkinter as tk
from tkinter import messagebox

#funcion para verificar las credenciales de login
def verificar_login():
    #obtener los calores ingresados
    usuario = entrada_usuario.get()
    contraseña = entrada_contrasena.get()

    #aqui podemos agregar las credenciales correctas (puedes modificar esto)
    usuario_correcto = "admin"
    contraseña_correcta = "1234"

    #comprobar si el usuario y la contraseña son correctas
    if usuario == usuario_correcto and contraseña == contraseña_correcta:
        messagebox.showinfo("Login Existoso", "bienvenido a la pagina principal.")
        abrir_ventana_principal()
        ventana_login.withdraw() #oculta la ventana de login
    else:
        messagebox.showerror("error de login", "usuario o contraseña incorrectos")
#funcion para abrir la ventana principal
def abrir_ventana_principal():
    
    #crear la ventana principal
    ventana_principal = tk.Toplevel(ventana_login)
    ventana_principal.title("pagina princial")
    ventana_principal.geometry("400x300")

    #etiqueta de bienvenida
    etiqueta_bienvenida = tk.label(ventana_principal, text="bienvenido a la pagina principal", font=("Arial",14))
    etiqueta_bienvenida.pack(pady=20)

    #boton para cerrar la ventana principal
    boton_cerrar = tk.Button(ventana_principal, text="cerrar sesion", command=ventana_principal.destroy)
    boton_cerrar.pack(pady=20)

    #crear la ventana de login
    ventana_login = tk.Tk()
    ventana_login.tittle("Login")
    ventana_login.geometry("300x250")

    #etiqueta de titulo
    etiqueta_titulo = tk.label(ventana_login, text="por favor, ingresa tus credenciales", font=("Arial", 12))
    etiqueta_titulo.pack(padi=10)


    #etiqueta y entrada para el usuario
    etiqueta_usuario = tk.Label(ventana_login, text="Usuario:")
    etiqueta_usuario.pack(pady=5)
    entrada_usuario = tk.Entry(ventana_login)
    entrada_usuario.pack(pady=5)

    #etiqueta y entrada para la contraseña
    etiqueta_contraseña = tk.Label(ventana_login, text="contraseña:")
    etiqueta_contraseña.pack(pady=5)
    entrada_contraseña = tk.Entry(ventana_login, show="*")
    entrada_contraseña.pack(pady=5)

    #boton para iniciar sesion
    boton_login = tk.Button (ventana_login, text="iniciar sesion", command=verificar_login)
    boton_login.pack(pady=20)

    #iniciar el bucle principal de la ventana de login
    ventana_login.mainloop()