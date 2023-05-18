#---------------------------------
# Desktop app No. 2- Temperatura
#---------------------------------

# se importa la libreria tkinter con todas sus funciones
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

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
    lb_c = Label(toplevel_estudiante, text = "estudiante")
    lb_c.config(bg="white", fg="blue", font=("Helvetica", 18))
    lb_c.place(x=100, y=30)

 

    # caja de texto para valor en centigrados
    entry_c = Entry(toplevel_estudiante, textvariable=toplevel_estudiante)
    entry_c.config(bg="white", fg="blue", font=("Times New Roman", 18), width=6)
    entry_c.focus_set()
    entry_c.place(x=210,y=60)

   # boton para convertir
def abrir_toplevel_masCorporal():
    global toplevel_masCorporal
    toplevel_masCorporal = Toplevel()
    toplevel_masCorporal.title("masCorporal")
    toplevel_masCorporal.resizable(False, False)
    toplevel_masCorporal.geometry("300x200")
    toplevel_masCorporal.config(bg="white")
    lb_c = Label(toplevel_masCorporal, text = "masCorporal")
    lb_c.config(bg="white", fg="blue", font=("Helvetica", 18))
    lb_c.place(x=130, y=40)

    # caja de texto para valor en centigrados
    entry_c = Entry(toplevel_masCorporal, textvariable=toplevel_masCorporal)
    entry_c.config(bg="white", fg="blue", font=("Times New Roman", 18), width=6)
    entry_c.focus_set()
    entry_c.place(x=210,y=60)

# logo de la app

# etiqueta para valor en centigrados


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
    toplevel_masCorporal.delete("1.0","end")

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
lb_logo.place(x=20,y=20)

# titulo de la app
titulo = Label(frame_entrada, text="German A.Ordoñez.G")
titulo.config(bg = "white",fg="blue", font=("Helvetica", 20))
titulo.place(x=240,y=10)

bt_est = Button(frame_entrada, text="Ingresar dato estudiante", command=abrir_toplevel_estudiante)
bt_est.place(x=240, y=60)
bt_corp = Button(frame_entrada, text="masCorporal", command=abrir_toplevel_masCorporal)
bt_corp.place(x=240, y=90)


  

    # etiqueta para valor en centigrados
lb_c = Label(frame_entrada, text = "Nombre ")
lb_c.config(bg="white", fg="blue", font=("Helvetica", 18))
lb_c.place(x=100, y=140)
entry_c = Entry(frame_entrada, textvariable=c)
entry_c.config(bg="white", fg="blue", font=("Times New Roman", 18), width=10)
entry_c.focus_set()
entry_c.place(x=200,y=130)
combo = ttk.Combobox(state="reandonly",values=["6-5","6-6","6-7","6-8","7-4","7-5","8-4","8-5","8-6","9-4","9-5","9-6","10-1","10-2","10-3","10-4","10-5","10-6","10-7"])
combo.place(x=110,y=130)


   # boton para convertir


# aceptar
def aceptar():
    global cent
    cent = int(c.get())
    toplevel_masCorporal.destroy()


# radiobutton para kelvi



#--------------------------------
# frame operaciones
#--------------------------------
frame_operaciones = Frame(ventana_principal)
frame_operaciones.config(bg="white", width=480, height=100)
frame_operaciones.place(x=10, y=200)

# boton para convertir



# boton para borrar

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

# run
# se ejecuta el metodo mainloop() de la clase Tk() a través de la instancia ventana_principal. Este metodo despliega la ventana en pantalla y queda a la espera de lo que el usuario haga (click en un boton, escribir, etc).  Cada acción del usuario se conoce como un evento.  El método mainloop() es un bucle infinito.
ventana_principal.mainloop()