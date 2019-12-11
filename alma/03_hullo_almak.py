import pyxel
import random

# Itt most almák potyognak.
# ***** Feladat: csináld meg, hogy ha egy almát elkap
# az ember, tűnjön el, és a pont nőjön 1-gyel.

pyxel.init(150,150)
pyxel.image(0).load(0, 0, "assets/ember.png")
pyxel.image(1).load(0, 0, "assets/alma.png")
    
class Ember:
    def __init__(self):
        self.x = 0
        self.y = pyxel.height - 16
    def update(self):
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.x += 1.1
        if pyxel.btn(pyxel.KEY_LEFT):
            self.x -= 1.1
    def draw(self):
        if pyxel.btn(pyxel.KEY_RIGHT) or pyxel.btn(pyxel.KEY_LEFT):
        	u = 1 + int(pyxel.frame_count / 4) % 2
        else:
            u = 0
        w = -16 if pyxel.btn(pyxel.KEY_LEFT) else 16
        pyxel.blt(self.x, self.y, 0, u*16, 0, w, 16, 12)
        
ember = Ember()

class Alma:
    def __init__(self):
        self.x = random.randint(0, pyxel.width - 16)
        self.y = -16
    def update(self):
        self.y += 1
    def draw(self):
        pyxel.blt(self.x, self.y, 1, 2*16, 0, 16, 16, 12)

almak = []

pont = 0
    
def update():
    ember.update()
    if random.randint(0,70) == 0:
        almak.append(Alma())
    for a in almak: a.update()
    
def draw():
    pyxel.cls(15)
    for a in almak: a.draw()
    ember.draw()
    pyxel.text(8, 5, str(pont), 8)
    
pyxel.run(update, draw)

