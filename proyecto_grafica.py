from tkinter import *
import tkinter.messagebox as tkmb
import random
import os
from PIL import ImageTk, Image

tkmb.showinfo("Explicación", "Bienvenido al juego de adivina el numero, tendras que adivinar un numero del 1 al 100, mediante vayas digitando numeros se te irán dando pistas, se te informará si tu numero es menor o mayor al numero por adivinar. Suerte")

root = Tk()

root.title("Adivina el numero")


intentos = 1

numero_maquina = random.randint(1,100)

marco = LabelFrame(root,
                   text="Digite un numero del 1 al 100",
                   padx=50,
                   pady=50)
marco.pack(padx=25, pady=10)

numero_usuario = Entry(marco,width=30)
numero_usuario.insert(0,"Escriba un numero...")
numero_usuario.bind("<Button-1>", lambda x : numero_usuario.delete(0, END))
numero_usuario.pack()

root.eval('tk::PlaceWindow . center')

root.resizable(False, False)

ruta_raiz = os.path.dirname(__file__)
ruta_boton = os.path.join(ruta_raiz, "boton")

boton = ImageTk.PhotoImage(Image.open(os.path.join(ruta_boton, "button.png")).resize((80,40)))

def verificar_numero():
    global intentos
    try:
        numero = int(numero_usuario.get())
        
        if numero < numero_maquina:
            tkmb.showinfo("Pista", f"El numero es mas alto. Digite un numero mayor que {numero}")
            intentos += 1
        elif numero > numero_maquina:
            tkmb.showinfo("Pista", f"El numero es mas bajo. Digite un numero menor que {numero}")
            intentos += 1
        else:
            tkmb.showinfo("Felicidades", f"Has adivinado el numero en {intentos} intentos")
            root.destroy()
    except:
        tkmb.showerror("¡Error!", "Valor no válido.")
        intentos += 1

boton_enviar = Button(root, image=boton , border=0 ,command=verificar_numero).pack()


root.mainloop()
