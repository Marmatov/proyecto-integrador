import os
import readchar


mapa="""..###################
....#.#.#.....#.....#
###.#.#.###.###.#.#.#
#.............#.#.#.#
#.#.#.###########.###
#.#.#.#.......#.....#
#.###.#.###.###.###.#
#.#.#.#.#.#...#.#...#
#.#.#.###.###.#####.#
#...#...#.....#.....#
#.###.#.#.#########.#
#.#####.#####.#####.#
#.#.........#...#...#
#.###.###.###.#####.#
#.#...#.......#.....#
#.#########.###.#####
#.........#.......#.#
#.###.#.#.#.#.#.###.#
#...#.#.#.#.#.#.....#
###################.#"""

inicio=(0,0)
final=(19,19)
def cmatriz(mapa):
    return list(map(list,mapa.split("\n")))

def terminal(terreno):
    os.system('cls' if os.name=='nt' else 'clear')
    for fila in terreno:
        print(" ".join(fila))

def mainloop (mapa,inicio,final):
    py,px=inicio
    while (py,px) != final:
        mapa[py][px] = "P"
        terminal(mapa)
        k = readchar.readkey()
        if k == readchar.key.UP:
            if(py-1)>=0:
                if mapa[py-1][px]!="#":
                    mapa[py][px]= "."
                    py-=1
        elif k == readchar.key.DOWN:
            if(py+1)<len(mapa):
                if mapa[py+1][px]!="#":
                    mapa[py][px]= "."
                    py+=1
        elif k == readchar.key.RIGHT:
            if(px+1)<=len(mapa[0]):
                if mapa[py][px+1]!="#":
                    mapa[py][px]= "."
                    px+=1
        elif k == readchar.key.LEFT:
            if(px-1)>=0:
                if mapa[py][px-1]!="#":
                    mapa[py][px]= "."
                    px-=1
    

mainloop(cmatriz(mapa), inicio,final)

