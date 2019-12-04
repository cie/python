import pyxel
import math
pyxel.init(255,255)

def update():
	pass    

def hopehely(x, y, r):
    szin = 15 # fehér
    s = math.sqrt(2) * r / 2
    pyxel.line(x+r, y  , x-r, y  , szin)
    pyxel.line(x  , y-r, x  , y+r, szin)
    # Itt azért kell kerekíteni, mert törtek jönnek ki, és hogy szimmetrikus legyen:
    pyxel.line(round(x-s),
               round(y-s),
               round(x+s),
               round(y+s), szin)
    pyxel.line(round(x-s),
               round(y+s),
               round(x+s),
               round(y-s), szin)

def draw():
    pyxel.cls(1) # sötétkék
    hopehely(50, 50, 3)
    hopehely(140, 50, 6)
    hopehely(60, 80, 10)
    
    
pyxel.run(update, draw)