from   tkinter   import *
from   tkinter   import ttk
from   functools import partial
from   tkinter   import messagebox
from   tkinter   import PhotoImage 
import time
import random

#Programa Funcion============================================================================
def creacion_matriciana(fi,co):
    matriz = [None] * co
    for n in range (co):
        matriz[n] = [None] * fi

    return(matriz)

#===========================================================================================

def vector_imagenes():
    vector_img = []
    vector_img.append(PhotoImage(file = 'chori.png'         ))
    vector_img.append(PhotoImage(file = 'milanga.png'       ))
    vector_img.append(PhotoImage(file = 'fideos.png'        ))
    vector_img.append(PhotoImage(file = 'empanadas.png'     ))
    vector_img.append(PhotoImage(file = 'mate.png'          ))
    vector_img.append(PhotoImage(file = 'alfajor.png'       ))
    vector_img.append(PhotoImage(file = 'hamburguesa.png'   ))
    vector_img.append(PhotoImage(file = 'pebete.png'        ))
    vector_img.append(PhotoImage(file = 'chocotorta.png'    ))
    vector_img.append(PhotoImage(file = 'asado.png'         ))
    vector_img.append(PhotoImage(file = 'guiso_lentejas.png'))
    vector_img.append(PhotoImage(file = 'pizza.png'         ))
    vector_img.append(PhotoImage(file = 'ravioles.png'      ))
    vector_img.append(PhotoImage(file = 'facturas.png'      ))
    vector_img.append(PhotoImage(file = 'pastel_papa.png'   ))
    vector_img.append(PhotoImage(file = 'miga.png'          ))
    vector_img.append(PhotoImage(file = 'tapa.png'          ))
    
    return(vector_img)

#===========================================================================================

def boton_click(n, z, cont):
    if(cont[0] < 1):
        
        cont[0] += 1

        cont[1]  = n 

        cont[2]  = z

        cont[3] += 1

        print(cont[0])
        
        matriz_btn[cont[1]][cont[2]]= Label(image= vector_img[matriz_num[cont[1]][cont[2]]])
        matriz_btn[cont[1]][cont[2]].place(x = (150*(cont[1]))+50, y = (150*(cont[2]))+50, height = 150, width = 150)
        
    else:
        matriz_btn[n][z] = Label(image = vector_img[matriz_num[n][z]])
        
        matriz_btn[n][z].place(x = (150*n)+50, y = (150*z)+50, height = 150, width = 150)
        app.update()
        time.sleep(.5)
        
        if(matriz_num[cont[1]][cont[2]] == matriz_num[n][z]):

            cont[4] += 1
            
            matriz_btn[cont[1]][cont[2]] = Label(image = vector_img[matriz_num[cont[1]][cont[2]]])
        
            matriz_btn[cont[1]][cont[2]].place(x = (150*(cont[1]))+50, y = (150*(cont[2]))+50, height = 150, width = 150)
            app.update()
        
            matriz_btn[n][z] = Label(image = vector_img[matriz_num[n][z]])
        
            matriz_btn[n][z].place(x = (150*n)+50, y = (150*z)+50, height = 150, width = 150)
        
            app.update()
        
            cont[0] = 0
            
        else:
            
             matriz_btn[cont[1]][cont[2]]= Button(image = vector_img[16], command=partial(boton_click,cont[1],cont[2], cont))
             
             matriz_btn[cont[1]][cont[2]].place(x = (150*(cont[1]))+50, y = (150*(cont[2]))+50, height = 150, width = 150)
        
             app.update()
        
             matriz_btn[n][z]= Button(image = vector_img[16], command=partial(boton_click,n, z, cont))
             
             matriz_btn[n][z].place(x = (150*n)+50, y = (150*z)+50, height = 150, width = 150)
        
             app.update()

             cont[0] = 0
             cont[1] = 0
             cont[2] = 0
        
    app.update()

    if(cont[4] == 16):
        messagebox.showinfo(title='Felicidades', message='Completaste el juego en ' + str(cont[3]) + ' clicks\n La cantidad optima de clicks es de 32')
    
#===========================================================================================
    
def cargar_matriz_num(matriz_num):
    for n in range(16):
        for z in range(2):
            px = random.randint(0, 3)
            py = random.randint(0, 7)
            while(matriz_num[py][px] != None):
                px = random.randint(0, 3)
                py = random.randint(0, 7)
            matriz_num[py][px]= n
            
#===========================================================================================
            
def cargamiento_botones(matriz_btn, matriz_num, vector_img, cont):

    for i in range(8):
        for j in range(4):
            
            matriz_btn[i][j] = Label(image = vector_img[matriz_num[i][j]])

            matriz_btn[i][j].place(x = (150*i)+50, y = (150*j)+50, height = 150, width = 150)
            app.update()

    time.sleep(3)

    for n in range(8):
        for z in range(4):
            matriz_btn[n][z]= Button(image = vector_img[16], command=partial(boton_click,n, z, cont))

            matriz_btn[n][z].place(x = (150*n)+50, y = (150*z)+50, height = 150, width = 150)
            
            app.update()


#Programa Principal==========================================================================
app = Tk ()
app.title("Test de Memoria")
app.geometry ("1300x800"   )

#Componentes=================================================================================
fi   = int(4)
co   = int(8)
cont = [0, 0, 0, 0, 0]
matriz_num = creacion_matriciana(fi,co)

matriz_btn = creacion_matriciana(fi,co)

vector_img = vector_imagenes()

cargar_matriz_num(matriz_num)

cargamiento_botones(matriz_btn, matriz_num, vector_img, cont)

#============================================================================================
app.mainloop()
