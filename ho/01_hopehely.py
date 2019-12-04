import pyxel
import math
pyxel.init(255,255)

# Feladat: készíts hópelyheket!
# Lehessen megadni a középpontjuk koordinátáit és a sugarukat.
# A hópehely négy egyforma hosszú vonalból álljon,
# függőleges, vízszintes és két 45 fokos.

# Mit csináljunk két képkocka között
def update():
	pass  # Semmit :)
    # (De muszáj ideírni, hogy a bekezdés meglegyen.)

def hopehely(x, y, r):
    # Ide írd a hópelyhet kirajzoló kódot!
    #
    # Ami segíthet:
    #
    # - vonalrajzolás:
    #pyxel.line(x1, y1, x2, y2, szín)
    # - gyökvonás:
    #math.sqrt(2)
    # - legközelebbi egészhez kerekítés:
    #round(0.6)

# Hogyan rajzolunk ki egy-egy képkockát
def draw():
    # Letöröljük a képernyőt 1-es színnel (sötétkék)
    pyxel.cls(1)
    # Itt hívjuk meg a hopehely függvényt, háromszor:
    hopehely(50, 50, 3)
    hopehely(140, 50, 6)
    hopehely(60, 80, 10)
    
    
pyxel.run(update, draw)
