#se importa la biblioteca de  tkinter
import tkinter as tk
from math import sqrt


#se crea la ventana principal
ventana = tk.Tk()
ventana.title("proyecto python")
ventana.geometry('2000x2000')
ventana.configure(background='pale goldenrod')

#se crea un cuadrado color blanco en la ventana principal
canvas = tk.Canvas(ventana, width=800, height=600, bg='white')
canvas.pack()

#se crea el titulo en la ventana principal
texto = tk.Label(ventana, text="PROYECTO PYTHON", font=("AGENCY FB", 90),fg="navy")
texto.pack()
texto.place(x=330, y=40)
def calcular_raiz():
    numero = float(entry1())
    resultado = sqrt(numero)
    label.config(text="Resultado: {:.2f}".format(resultado))

    label_instrucciones = tk.Label(raiz, text="Ingresa un número:")
    label_instrucciones.pack()

    entry1 = tk.Entry(ventana)
    entry1.pack()
    
    
    boton_calcular = tk.Button(ventana, text="Calcular", command=calcular_raiz)
    boton_calcular.pack()

    label = tk.Label(ventana, text="Resultado:")
    label.pack()
# se crea la función para abrir la ventana de raíz cuadrada
def abrir_la_raiz():
    raiz = tk.Toplevel()
    raiz.title("raiz cuadrada")
    raiz.geometry('380x300')
    raiz.configure(background='pale goldenrod')

#dentro de la funcion se crea el titulo de la ventana raiz
    titulo_raiz1 = tk.Label(raiz, text="raiz cuadrada", font=("arial black", 18), fg="navy", bg="pale goldenrod")
    titulo_raiz1.pack()
    
#Dentro de la funcion se crea un cuadro blanco en la ventana raiz
    canvas = tk.Canvas(raiz, width=250, height=230, bg='white')
    canvas.pack()
    # se crea el cuadro de texto donde se ingresa el número
    entry2 = tk.Entry(raiz)
    entry2.pack()
    entry2.place(x=180 ,y=80)
    
    
    texto_numero = tk.Label(raiz, text="Numero:")
    texto_numero.pack()
    texto_numero.place(x=110, y=80)
    # se crea la función para calcular la raíz cuadrada
    def calcular_raiz():

        numero = float(entry2.get())
        resultado = sqrt(numero)
        label2.config(text="Resultado: {:.2f}".format(resultado))
        entry2.delete(0, tk.END) 
    # se crea el botón para calcular la raíz cuadrada
    boton_calcular = tk.Button(raiz, text="Calcular", command=calcular_raiz)
    boton_calcular.pack()
    boton_calcular.place(x=110,y=110)
    # se crea el label para mostrar el resultado
    label2 = tk.Label(raiz, text="Resultado:")
    label2.pack()
    label2.place(x=180, y=110)
# se crea el botón que abre la ventana principal de raiz cuadrada
    boton = tk.Button(ventana, text="Raiz Cuadrada", font=("agency fb", 20), command=abrir_la_raiz)
    boton.pack()
    boton.place(x=600, y=230)

    

#se crea la accion de crear la ventana llamada potencias
def abrir_la_potencia():
    potencias = tk.Toplevel()
    potencias.title("potencias")
    potencias.geometry('380x300')
    potencias.configure(background='pale goldenrod')
    
   #se crea el titulo en la ventana potencias
    titulo_potencias = tk.Label(potencias, text="Elevar Potencias", font=("arial black", 18), fg="navy", bg="pale goldenrod")
    titulo_potencias.pack()
    
    #se crea un cuadro blanco en la ventana potencias
    canvas = tk.Canvas(potencias,width=250, height=230,bg='WHITE')
    canvas.pack()
    
    #se crea el cuadro de texto donde se escribe la base
    barra_potencia = tk.Entry(potencias)
    barra_potencia.pack()
    barra_potencia.place(x=150, y=80)
    
    #se creo el texto que dice base
    texto_base = tk.Label(potencias, text="Base:")
    texto_base.pack()
    texto_base.place(x=110, y=80)
    
#se crea la barra dode se ingresa el exponente
    barra_potencia1 = tk.Entry(potencias)
    barra_potencia1.pack()
    barra_potencia1.place(x=150, y=120)
    #texto que indica que alli se ingresa el exponente
    texto_exponente = tk.Label(potencias, text="Exponente:")
    texto_exponente.pack()
    texto_exponente.place(x=80, y=120)
    
#se crea la funcion de calcular potencias
    def calcular_potencia():
        
      #la formula para calcular las potencias
        base = int(barra_potencia.get())
        exponente = int(barra_potencia1.get())
        resultado = base ** exponente
        texto_resultado.config(text=f"Resultado: {resultado}")
        
#la accion que hace que se borren los numeros de las barras de texto donde se ponen la base y el exponente
        barra_potencia.delete(0, tk.END)
        barra_potencia1.delete(0, tk.END)
        
   #se crea el boton calcular que le manda una señal a la terminal de que este boton ejecute la accion calcular_potencias
    boton_calcular = tk.Button(potencias, text="calcular", command=calcular_potencia)
    boton_calcular.pack()
    boton_calcular.place(x=170, y=150)
    
#abajo del boton calcular aparece la palabra resultado y la respuesta de la potencia que quieres elevar
    texto_resultado = tk.Label(potencias, text="",bg="white")
    texto_resultado.pack()
    texto_resultado.place(x=150, y=180)
    
#se crea el boton que abre la ventana principal de raiz cuadrada
boton = tk.Button(ventana, text="Raiz Cuadrada", font=("agency fb", 20), command=abrir_la_raiz)
boton.pack()
boton.place(x=600, y=230)

#se crea el boton de abrir la ventana potencias
boton1 = tk.Button(ventana, text="Elevar Potencias", font=("agency fb", 20), command=abrir_la_potencia)
boton1.pack()
boton1.place(x=590, y=300)



#se crea un bucle para que sempre se mantenga abierta las ventanas creadas

ventana.mainloop()
