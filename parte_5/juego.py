import os
import readchar

class juego():
    def __init__(self,mapa,inicio,final):
        self.mapa = mapa
        self.inicio = inicio
        self.final = final

    def mainloop(self):
            py,px = self.inicio
            while (py,px) != self.final:
                self.mapa[py][px] = "P"
                self.terminal()
                k = readchar.readkey()
                if k == readchar.key.UP:
                    if(py-1)>=0:
                        if self.mapa[py-1][px]!="#":
                            self.mapa[py][px]= "."
                            py-=1
                elif k == readchar.key.DOWN:
                    if(py+1)<len(self.mapa):
                        if self.mapa[py+1][px]!="#":
                            self.mapa[py][px]= "."
                            py+=1
                elif k == readchar.key.RIGHT:
                    if(px+1)<=len(self.mapa[0]):
                        if self.mapa[py][px+1]!="#":
                            self.mapa[py][px]= "."
                            px+=1
                elif k == readchar.key.LEFT:
                    if(px-1)>=0:
                        if self.mapa[py][px-1]!="#":
                            self.mapa[py][px]= "."
                            px-=1

    def terminal(self):
        os.system('cls' if os.name=='nt' else 'clear')
        for fila in self.mapa :
            print(" ".join(fila))

