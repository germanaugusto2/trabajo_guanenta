#---------------------------------
# Desktop app No. 2- Temperatura
#---------------------------------

# se importa la libreria tkinter con todas sus funciones
from tkinter import *
from tkinter import messagebox

#-------------------------
# funciones de la app
#-------------------------

# abrir toplevel centigrados
def abrir_toplevel_estudiante():
    global toplevel_estudiante
    toplevel_estudiante = Toplevel()
    toplevel_estudiante.title("Estudiante")
    toplevel_estudiante.resizable(False, False)
    toplevel_estudiante.geometry("300x200")
    toplevel_estudiante.config(bg="white")

    # logo de la app

    # etiqueta para valor en centigrados
    lb_c = Label(toplevel_estudiante, text = "estudiante")
    lb_c.config(bg="white", fg="blue", font=("Helvetica", 18))
    lb_c.place(x=130, y=40)

    # caja de texto para valor en centigrados
    entry_c = Entry(toplevel_estudiante, textvariable=toplevel_estudiante)
    entry_c.config(bg="white", fg="blue", font=("Times New Roman", 18), width=6)
    entry_c.focus_set()
    entry_c.place(x=210,y=60)

   # boton para convertir


# aceptar
def aceptar():
    global cent
    cent = int(c.get())
    toplevel_estudiante.destroy()

# convertir

# borrar
def borrar():
    messagebox.showinfo("Guanenta", "Los datos serán borrados")
    c.set("")
    t_resultados.delete("1.0","end")

# salir
def salir():
    messagebox.showinfo("Guanenta", "La app se va a cerrar")
    ventana_principal.destroy()

#-----------------------------
# ventana principal de la app
#-----------------------------

# se declara una variable llamada ventana_principal, que adquiere las caracteristicas de un objeto Tk()
ventana_principal = Tk()

# titulo de la ventana
ventana_principal.title("Guanenta")

# tamaño de la ventana
ventana_principal.geometry("500x500")

# deshabilitar boton de maximizar
ventana_principal.resizable(False, False)

# color de fondo de la ventana
ventana_principal.config(bg="white")

#--------------------------------
# variables globales
#--------------------------------
c = StringVar()
kf = StringVar()
global logo

#--------------------------------
# frame entrada datos
#--------------------------------
frame_entrada = Frame(ventana_principal)
frame_entrada.config(bg="white", width=480, height=180)
frame_entrada.place(x=10, y=10)

# logo de la app
logo = PhotoImage(file="ing/escudo_colegio.png")
lb_logo = Label(frame_entrada, image=logo, bg="white")
lb_logo.place(x=70,y=40)

# titulo de la app
titulo = Label(frame_entrada, text="Guanenta")
titulo.config(bg = "white",fg="blue", font=("Helvetica", 20))
titulo.place(x=240,y=10)

bt_centigrados = Button(frame_entrada, text="Ingresar dato estudiante", command=abrir_toplevel_estudiante)
bt_centigrados.place(x=240, y=60)


def abrir_toplevel_estudiante():
    global toplevel_corporal
    toplevel_corporal = Toplevel()
    toplevel_corporal("Estudiante")
    toplevel_corporal.resizable(False, False)
    toplevel_corporal.geometry("300x200")
    toplevel_corporal.config(bg="white")
lb_c = Label(toplevel_corporal, text = "masa corporal")
lb_c.config(bg="white", fg="blue", font=("Helvetica", 18))
lb_c.place(x=130, y=40)

entry_c = Entry(toplevel_estudiante, textvariable=toplevel_corporal)
entry_c.config(bg="white", fg="blue", font=("Times New Roman", 18), width=6)
entry_c.focus_set()
entry_c.place(x=210,y=60)
  

    # etiqueta para valor en centigrados
   # boton para convertir


# aceptar
def aceptar():
    global cent
    cent = int(c.get())
    toplevel_corporal.destroy()


# radiobutton para kelvi



#--------------------------------
# frame operaciones
#--------------------------------
frame_operaciones = Frame(ventana_principal)
frame_operaciones.config(bg="white", width=480, height=100)
frame_operaciones.place(x=10, y=200)

# boton para convertir



# boton para borrar
bt_borrar = Button(frame_operaciones, text="Borrar", command=borrar)
bt_borrar.place(x=190, y=35, width=100, height=30)

# boton para salir
bt_salir = Button(frame_operaciones,text="Salir", command=salir)
bt_salir.place(x=335, y=35, width=100, height=30)

#--------------------------------
# frame resultados
#--------------------------------
frame_resultados = Frame(ventana_principal)
frame_resultados.config(bg="white", width=480, height=180)
frame_resultados.place(x=10, y=310)

# area de texto para los resultados
t_resultados = Text(frame_resultados)
t_resultados.config(bg="black", fg="green yellow", font=("Courier", 18))
t_resultados.place(x=10,y=10,width=460,height=160)

# run
# se ejecuta el metodo mainloop() de la clase Tk() a través de la instancia ventana_principal. Este metodo despliega la ventana en pantalla y queda a la espera de lo que el usuario haga (click en un boton, escribir, etc).  Cada acción del usuario se conoce como un evento.  El método mainloop() es un bucle infinito.
ventana_principal.mainloop()