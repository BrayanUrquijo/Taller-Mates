from tkinter import *
from tkinter import ttk
# import messagebox
import random

# Se crea la ventana
ventana = Tk()

# Imagen de icono
ventana.iconbitmap("Logo.ico")

# Caracteristicas
ventana.title("Ahorcado with Functions")
ventana.geometry("1000x700")
ventana.resizable(0,0)
ventana.config(bg="White")

# Imagenes

fondo_univalle = PhotoImage(file="logo_uv.png")
fondo_univalle = fondo_univalle.subsample(5, 5)
fondo_univalle1 = Label(ventana, image=fondo_univalle)
fondo_univalle1.config(bg="White")
fondo_univalle1.place(x=763, y=10)

fondo_ladrillo = PhotoImage(file="fondo_ladrillo.png")
fondo_ladrillo = fondo_ladrillo.subsample(-1, 2)
fondo_ladrillo1 = Label(ventana, image=fondo_ladrillo)
fondo_ladrillo1.config(bg="Black")
fondo_ladrillo1.place(x=0, y=560)

fondo_cielo = PhotoImage(file="fondo_cielo.png")
fondo_cielo = fondo_cielo.subsample(1, 1)
fondo_cielo1 = Label(ventana, image=fondo_cielo)
fondo_cielo1.config(bg="Black")
fondo_cielo1.place(x=-150, y=-37)

linea_frame = Frame(ventana, width=10, height=700)
linea_frame.config(bg="Black")
linea_frame.place(x=750, y=0)

linea_frame1 = Frame(ventana, width=750, height=10)
linea_frame1.config(bg="Black")
linea_frame1.place(x=0, y=550)

# Nombre del juego y de los integrantes

nombre_juego = Label(ventana, text="Ahorcado", font=("ITALIC", 25))
nombre_juego.config(bg="White", fg="Black")
nombre_juego.place(x=810, y=250)

nombre_juego1 = Label(ventana, text="With", font=("ITALIC", 25))
nombre_juego1.config(bg="White", fg="Black")
nombre_juego1.place(x=845, y=300)

nombre_juego2 = Label(ventana, text="Functions", font=("ITALIC", 25))
nombre_juego2.config(bg="White", fg="Black")
nombre_juego2.place(x=810, y=350)

integrantes = Label(ventana, text="Integrantes:", font=("ITALIC", 25))
integrantes.config(bg="White", fg="Red")
integrantes.place(x=800, y=450)

integrantes1 = Label(ventana, text="Juan Stevan Cruz", font=("ITALIC", 17))
integrantes1.config(bg="White", fg="Black")
integrantes1.place(x=790, y=500)

integrantes2 = Label(ventana, text="Brayan Urquijo", font=("ITALIC", 17))
integrantes2.config(bg="White", fg="Black")
integrantes2.place(x=800, y=550)

integrantes3 = Label(ventana, text="Jhoan Fabrizio H", font=("ITALIC", 17))
integrantes3.config(bg="White", fg="Black")
integrantes3.place(x=790, y=600)

#Personaje ahorcado

ahorcado = PhotoImage(file="Ahorcado.png")
ahorcado = ahorcado.subsample(3, 3)
ahorcado1 = Label(ventana, image=ahorcado)
ahorcado1.config(bg="white", border=5, relief="groove")
ahorcado1.place(x=50, y=25)

# Boton para cerrar
def cerrar():
    ventana.destroy()

boton_cerrar = Button(ventana, text="Cerrar", font=("ITALIC", 20), command=cerrar)
boton_cerrar.config(bg="Red", fg="White", border="5", relief="groove")
boton_cerrar.place(x=825, y=635)

# Entry para la palabra
palabra_resultado = Entry(ventana, font=("ITALIC", 20))
palabra_resultado.config(width=30, border=5, relief="groove", bg="Red", fg="White")
palabra_resultado.config(justify="center")
palabra_resultado.place(x=10, y=480)

boton_validar = Button(ventana, text="Validar", font=("ITALIC", 20))
boton_validar.config(width=5, bg="Red", fg="White", border=5, relief="groove")
boton_validar.place(x=500, y=470)

# funcion pregunta

def cargar_preguntas_respuestas(nombre_archivo):
    """
    Carga las preguntas y respuestas desde un archivo de texto.
    """
    preguntas_respuestas = []
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                pregunta, *respuestas = map(str.strip, linea.strip().split(","))
                respuestas = [respuesta.replace("[", "").replace("]", "").replace("'", "").replace('"', '') for respuesta in respuestas]
                preguntas_respuestas.append((pregunta, respuestas))
    except FileNotFoundError:
        print(f"El archivo '{nombre_archivo}' no existe.")
    return preguntas_respuestas

def hacer_pregunta(pregunta, respuestas):
    """
    Presenta una pregunta y muestra las respuestas mezcladas.
    """
    print(f"Pregunta: {pregunta}\n")
    respuestas_mezcladas = random.sample(respuestas, len(respuestas))
  
    for i, respuesta in enumerate(respuestas_mezcladas, start=1):
        print(f"{i}. {respuesta}")
    
    while True:
        try:
            respuesta_usuario = int(input("Elige la respuesta correcta entre (1, 2 o 3): ")) - 1
            if 0 <= respuesta_usuario < len(respuestas_mezcladas):
                break
            else:
                print("Ingresa un número válido (1, 2 o 3).")
        except ValueError:
            print("Ingresa un número válido que sea (1, 2 o 3).")
    
    return respuestas[respuesta_usuario]

def main():
    archivo_preg = "preguntas.txt"
    preguntas_respuestas = cargar_preguntas_respuestas(archivo_preg)
    if preguntas_respuestas:
        for pregunta, respuestas in preguntas_respuestas:
            respuesta_usuario = hacer_pregunta(pregunta, respuestas)
            if respuesta_usuario == respuestas[0]:
                print("¡Correcto!\n")
            else:
                print(f"Respuesta incorrecta. La respuesta correcta era: {respuestas[0]}\n")

if __name__ == "__main__":
    def palabra_pregu():
        if letra.get() == True :
            main()


# Se mantiene la ventana abierta
ventana.mainloop()
