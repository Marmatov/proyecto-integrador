import os
import random
from juego import *
from functools import reduce

class juegoarchivo(juego):
    def __init__(self, path_a_mapas):
        archivos_de_mapas = os.listdir(path_a_mapas)
        nombre_archivo = random.choice(archivos_de_mapas)
        path_completo = os.path.join(path_a_mapas, nombre_archivo)
        self.mapa = self.leer_mapa(path_completo)
        juego.__init__(self,self.mapa[0],self.mapa[1],self.mapa[2])


    def leer_mapa(self, path):
        with open(path, 'r') as archivo:
            contenido_mapa = archivo.readlines()
            red= reduce(lambda x,y:x+y,contenido_mapa).split("\n")
            mapa =  list(map(list,red[1:]))  
            posiciones =tuple(map(int,red[0].split()))         
            return mapa ,posiciones[0:2],posiciones[2:]
         







