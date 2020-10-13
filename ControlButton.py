from numpy.lib.function_base import append
from ColorCapture import *
from ArrrayColors import *
import numpy as np
from sys import int_info
from numpy.core.numeric import count_nonzero     



class ControlButton():
    capt=ColorCapture
    arriba=bool;
    abajo=bool;
    
    def __init__(self, coordenadas):
        self.coord=coordenadas
        self.arriba= False
        self.abajo= False
        
    def button(self):    
        while(210<=capt.x & capt.x>=418 & 0<=capt.y & capt.y>=153):
            self.arriba=True
            print("arriba")
        
    

if __name__ == "__main__":
    #capt=ColorCapture(yellow(),3)
    #capt.cameraCapture()
    #coord=capt.coordenates
    
    ceros=np.zeros((3,4))
    