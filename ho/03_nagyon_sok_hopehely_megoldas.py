import pyxel
import math
import random
pyxel.init(255,255)

def update():
	pass    

def hopehely(x, y, r):
    szin = 15 # fehér
    s = math.sqrt(2) * r / 2
    pyxel.line(x+r, y  , x-r, y  , szin)
    pyxel.line(x  , y-r, x  , y+r, szin)
    pyxel.line(round(x-s),
               round(y-s),
               round(x+s),
               round(y+s), szin)
    pyxel.line(round(x-s),
               round(y+s),
               round(x+s),
               round(y-s), szin)

# sok random hópehely
hopelyhek = [
    (random.randint(0, 255), random.randint(0, 255), random.randint(2, 8)),
    (random.randint(0, 255), random.randint(0, 255), random.randint(2, 8)),
    (random.randint(0, 255), random.randint(0, 255), random.randint(2, 8)),
    (random.randint(0, 255), random.randint(0, 255), random.randint(2, 8)),
    (random.randint(0, 255), random.randint(0, 255), random.randint(2, 8)),
    (random.randint(0, 255), random.randint(0, 255), random.randint(2, 8)),
    (random.randint(0, 255), random.randint(0, 255), random.randint(2, 8)),
    (random.randint(0, 255), random.randint(0, 255), random.randint(2, 8)),
]

def draw():
    pyxel.cls(1) # sötétkék
    for (x, y, r) in hopelyhek:
        hopehely(x, (y + pyxel.frame_count) % 255, r)
    
pyxel.run(update, draw)