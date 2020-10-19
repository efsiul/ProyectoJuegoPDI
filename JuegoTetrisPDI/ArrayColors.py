import numpy as np


def yellow():
    lC1 =    np.array([25, 15, 0], np.uint8)                                                                #Definimos un array con los valores de matiz mas bajo para el amarillo 15, 100 para saturación y 255 para brillo
    hC1 =    np.array([30, 255, 255], np.uint8)                                                             #Definimos un array con los valores de matiz medio bajo para el amarillo 25, 255 para saturación y 255 para brillo  
    lC2 =    np.array([31, 15, 0], np.uint8)                                                                #Definimos un array con los valores de matiz medio alto para el amarillo 26, 100 para saturación y 255 para brillo
    hC2 =    np.array([35, 255, 255], np.uint8)                                                             #Definimos un array con los valores de matiz mas bajo para el amarillo 35, 100 para saturación y 255 para brillo
    yellow=  {"lC1":lC1, "hC1":hC1, "lC2":lC2,"hC2": hC2, "color":"yellow"}    
    return yellow
        
def blue():
    lC1 =    np.array([100, 100, 0], np.uint8)                                                               #Definimos un array con los valores de matiz mas bajo para el azul 15, 100 para saturación y 255 para brillo
    hC1 =    np.array([113, 255, 255], np.uint8)                                                             #Definimos un array con los valores de matiz medio bajo para el azul 25, 255 para saturación y 255 para brillo  
    lC2 =    np.array([114, 100, 0], np.uint8)                                                               #Definimos un array con los valores de matiz medio alto para el azul 26, 100 para saturación y 255 para brillo
    hC2 =    np.array([127, 255, 255], np.uint8)                                                             #Definimos un array con los valores de matiz mas bajo para el azul 35, 100 para saturación y 255 para brillo
    blue=    {"lC1":lC1, "hC1":hC1, "lC2":lC2,"hC2": hC2, "color":"blue"}  
    return blue       

def red():
    lC1 =    np.array([0, 100, 20], np.uint8)                                                                #Definimos un array con los valores de matiz mas bajo para el rojo 15, 100 para saturación y 255 para brillo
    hC1 =    np.array([8, 255, 255], np.uint8)                                                               #Definimos un array con los valores de matiz medio bajo para el rojo 25, 255 para saturación y 255 para brillo  
    lC2 =    np.array([175, 100, 20], np.uint8)                                                              #Definimos un array con los valores de matiz medio alto para el rojo 26, 100 para saturación y 255 para brillo
    hC2 =    np.array([179, 255, 255], np.uint8)                                                             #Definimos un array con los valores de matiz mas bajo para el rojo 35, 100 para saturación y 255 para brillo
    red=     {"lC1":lC1, "hC1":hC1, "lC2":lC2,"hC2": hC2, "color": "red"}    
    return red       
    
def green():
    lC1 =    np.array([55, 0, 0], np.uint8)                                                                 #Definimos un array con los valores de matiz mas bajo para el verde 15, 100 para saturación y 255 para brillo
    hC1 =    np.array([62, 255, 255], np.uint8)                                                             #Definimos un array con los valores de matiz medio bajo para el verde 25, 255 para saturación y 255 para brillo  
    lC2 =    np.array([63, 0, 0], np.uint8)                                                                 #Definimos un array con los valores de matiz medio alto para el verde 26, 100 para saturación y 255 para brillo
    hC2 =    np.array([70, 255, 255], np.uint8)                                                             #Definimos un array con los valores de matiz mas bajo para el verde 35, 100 para saturación y 255 para brillo
    green=     {"lC1":lC1, "hC1":hC1, "lC2":lC2,"hC2": hC2, "color":"green"}    
    return green 