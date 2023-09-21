import os
import random
from juego import *

class juegoarchivo(juego):
    def __init__(self, path_a_mapas):
        archivos_de_mapas = os.listdir(path_a_mapas)
        nombre_archivo = random.choice(archivos_de_mapas)
        path_completo = os.path.join(path_a_mapas, nombre_archivo)
        self.mapa = self.leer_mapa(path_completo)
        juego.__init__(self,self.mapa[0],self.mapa[1],self.mapa[2])


    def leer_mapa(self, path):
        with open(path, 'r') as archivo:
            contenido_mapa = archivo.read().strip().split('\n')
            mapa =  list(map(list,contenido_mapa[1:]))  
            posiciones =tuple(map(int,contenido_mapa[0].split()))         
            return mapa,posiciones[0:2],posiciones[2:]
        








