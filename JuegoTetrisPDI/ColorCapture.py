#El siguiente código lo que hace es capturar el color amarillo del espacio muestral HSV. Es iportante tener en cuenta que el fondo no 7     #
# puede ser del color capturado y se debe procurar una buena iluminación.                                                                   #
#PASOS                                                                                                                                      #
#1 - Tener una imagen a analizar                                                                                                            #
#2 - Transformar la imagen de BGR a HSV - Linea número 24                                                                                   #
#3 - Delimitar el rango del color que queremos caputrar -linea 15 a la 18                                                                   #
#4 - Mostrar la imagen binarizada o en si desea mostrar solo el color real -Solo imagen binarizada linea 27, mostrar solo color linea 28    #
#############################################################################################################################################
import cv2
import numpy as np                                                                                                  #libreria para el PDI
import win32com.client as comctl
import ArrayColors
from ArrayColors import *


class ColorCapture():
    x=int
    y=int
    captura = cv2.VideoCapture(0)                                                                         #Activa la WEBCAM
    coordenates=[]
    wsh = comctl.Dispatch("WScript.Shell")

    #Definiendo los intervalos colores HSV que se desean capturar, estos se mandan por parametro
    #####################################################################################################
    def __init__(self, color,option):

        self.lowColor1  =   color["lC1"]
        self.highColor1 =   color["hC1"]
        self.lowColor2  =   color["lC2"]
        self.highColor2 =   color["hC2"]
        self.colors     =   color["color"]
        self.option     =   option
        
    #Captura de video
    ####################################################################################################
    def cameraCapture(self):
        while True:                                                                                        #ciclo de ejecucion
            ret, frame = self.captura.read()                                                               #Captura imagen en a1, ret recibe true(lectura de imagen) o false
            if ret == True:                                                                                #SI leyó la imagen entra al condicional
                frameHSV    =   self.changeColorSpace(frame)
                maskColor   =   self.colorcap(frameHSV)
                maskColorIs =   cv2.bitwise_and(frame, frame, mask= maskColor)                             #esta linea de código lo que hace es mostrar el color real del amarillo en vez del blanco, y esto se la monada a la variable
                contours    =   self.definingContours(maskColor)
                self.eliminatingNoiseColor(contours, frame)
                self.ShowImageType(self.option, frame, maskColor, maskColorIs)
            
            if cv2.waitKey(1) & 0xFF == ord('q'):                                                          #Mientras no se presione lq letra 'q' no se termina el programa

                break                                                                                         #Para salir del while   
                
        self.captura.release()                                                                           #Cierra la webcam
        self.bandera = False
        cv2.destroyAllWindows()                                                                            #Destruye todas las ventanas
    
    #Opciones para mostrar pantalla
    ###################################################################################################
    def ShowImageType(self, option, frame, maskColor, maskColorIs):
        if option   ==  1:
            cv2.imshow("Video", frame)                                                                     #Muestra lo que esta capturando la webcam
        elif option ==  2:
            cv2.imshow("Video", frame)
            cv2.imshow("MaskColorBin", maskColor)                                                          #Muestra lo mascara "maskYellow", lo que esta capturando en amarillo lo deja blanco, el resto lo deja negro
        elif option ==  3:
            cv2.imshow("Video", frame)
            cv2.imshow('maskColorIs', maskColorIs)                                                         #Muestra solo el color amarillo
        elif option == 4:
            cv2.imshow("Video", frame)   
            cv2.imshow("MaskColorBin", maskColor)
            cv2.imshow('maskColorIs', maskColorIs)
        
    #Cambiando el espacio de color BGR a HSV
    ###################################################################################################
    def changeColorSpace(self, frame):
        frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)                                                  #Open CV lee normalmente en Blue, Gray and Red, con este comando estamos transformando el espacio de color a HSV (matiz, saturación y brillo)
        return  frameHSV
    
    
    #Capturando el color que  se nos indica por frameHSV con mascaras
    ####################################################################################################
    def colorcap(self, frameHSV):
        maskColor1  =   cv2.inRange(frameHSV, self.lowColor1, self.highColor1)                             #Se crea una mascara que captura el rango bajo medio del amarillo
        maskColor2  =   cv2.inRange(frameHSV, self.lowColor2, self.lowColor2)                              #Se crea una mascara que captura el rango medio alto del amarillo
        maskColor   =   cv2.add(maskColor1,maskColor2)                                                     #Se combinan las anteriores mascaras de modo que pueda detectar el amarillo
        return maskColor
    
    
    #Dibujando Contornos a la imagen
    ####################################################################################################
    def definingContours(self, maskColor):
        contours, _ =  cv2.findContours(maskColor, cv2.RETR_EXTERNAL, 
        cv2.CHAIN_APPROX_SIMPLE)                                                                            #Codigo para capturar  contornos de todas las partes donde se detecto el color amarillo, este codigo arroja dos valores, de los cuales tomaremos el primero 
        #cv2.drawContours(frame,contornos, -1, (0,255,255), 3)                                              #Esta linea de codigo sirve para dibujar los contornos en nuestra captura de video normal. Los parametros son: 
                                                                                                                #Frame: la imagen normal que captura la camara
                                                                                                                #contornos: la captura de los contornos encontrados
                                                                                                                # -1: quiere decir que dibujara todos los contrnos de la misma forma
                                                                                                                # (0,255,255): lo que se dibuje lo hara en color amarillo. Este es el codigo BGR para el amarillo
                                                                                                                # 3: el grosor de la linea que se va a dibujar
        return contours

    #A continuación lo trataremos de eliminar el ruido: los espacios donde se captura tambien amarillo
    ####################################################################################################
    def eliminatingNoiseColor(self, contours, frame):
        wsh = comctl.Dispatch("WScript.Shell")
        for spaces in contours:                                                                             #Vamos a explorar todos los contornos creados con un for
            area = cv2.contourArea(spaces)                                                                  #vamos a capturar el area de cada contorno
            if area>3000:                                                                                   #Si el area es mayor a 3000 entonces se va a dibujar el contorno, de lo contrario no se dibujará
                newContour = cv2.convexHull(spaces)                                                         #Se suaviza el aspecto del contorno, con esto se espera no se tenga tantos picos    
                if self.colors  == "yellow":
                    cv2.drawContours(frame,[newContour], 0, (0,255,255), 3)                                     #se dibujara solo los contornos almacenados en la variable espacios, y 0 para dibujar solo ciertos contornos.  
                elif self.colors  == "blue":
                    cv2.drawContours(frame,[newContour], 0, (255,0,0), 3)
                elif self.colors  == "red":
                    cv2.drawContours(frame,[newContour], 0, (0,0,255), 3)                    
                elif self.colors  == "green":
                    cv2.drawContours(frame,[newContour], 0, (0,255,0), 3) 
                                                        
                #Capturando las coordenadas del punto central del objeto
                #########################################################################################
                M   =   cv2.moments(spaces)                                                                 #Identificamos el punto central del area del objeto a identificar
                if(M["m00"] == 0) : M["m00"] = 1                                                            #para encontrar "x" y "y" hacemos una división, para evitar que la división se haga por 0, se cambia el valor de m["m00"] por 1
                x   =   int(M["m10"]/M["m00"])                                                              #Encontrando el punto x
                y   =   int(M["m01"]/M["m00"])                                                              #Encontrando el punto y
                font =  cv2.FONT_HERSHEY_SIMPLEX                                                            #colocaremos las coordenadas del objeto, conforme se mueve en la imagen y para ello declaramos la fuente del texto
                cv2.circle(frame, (x,y), 7, (0,255,0), 1)                                                   #Se dibuja la figura de circulo en el frame. se manda las coordenadas "x" y "y", con radio 7, dibujandolo de color verde, y grosor 1
                cv2.putText(frame, '{},{}'.format(x,y), (x-50, y-80), 
                            font, 0.75,(0,255,0), 2, cv2.LINE_AA)                                           #Dibujaremos el texto en frame, se mostrara "x" y "y", en la ubicación (x+100, y+100), con la fuente que declaramos, el tamaño 0.75, color verde, grosor 1
                if 200 < x < 400 and 30 < y < 150:
                    print("arriba")
                    cv2.putText(frame, "ARRIBA", (10,30), 0,1,(0,0,255),2 )
                    wsh.SendKeys("{UP}")
                    
                if 200 < x < 400 and 300 < y < 450:
                    print("abajo")
                    cv2.putText(frame, "ABAJO", (10, 30),0, 1, (0, 0, 255), 2)
                    wsh.SendKeys("{DOWN}")
                    
                if 0 < x < 200 and 150 < y < 300:
                    print("izquierda")
                    cv2.putText(frame, "IZQUIERDA", (10, 30),0, 1, (0, 0, 255), 2)
                    wsh.SendKeys("{LEFT}")
                    
                if 400 < x < 600 and 150 < y < 300:
                    cv2.putText(frame, "DERECHA", (10,30), 0,1,(0,0,255),2 )
                    print("derecha")
                    wsh.SendKeys("{RIGHT}")

                self.coordenates.append([x,y])



if __name__ == "__main__":
     capt = ColorCapture(yellow(), 1)
     capt.cameraCapture()
