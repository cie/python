# encoding: utf-8
import pyxel
pyxel.init(160, 120, caption="Pong")

# ---- labda -----

labdax = 30
labday = 40
# sebessége
sebx = 1
seby = 1

def labda_update():
    global labdax, labday, sebx, seby
    # ütközés
    if labdax > 160 - 6: sebx = -sebx
    if labday > 120 - 6: seby = -seby
    if labdax < 6:
        # ***** itt ez volt: *****
        # if uton_van(labday):
        # ***** és ez lett: *****
        if bal_uto.rajta_van(labday):
            sebx = -sebx
    if labday < 6: seby = -seby

    # labda mozgatása
    labdax = labdax + sebx
    labday = labday + seby

def labda_draw():
    pyxel.circ(labdax, labday, 4, 8)



# ***** itt volt egy csomó minden, ami már nem kell *****



class Uto:
    def __init__(self):
        self.y = 60
    def update(self):
        if pyxel.btn(pyxel.KEY_W):
            self.y = self.y - 1
        if pyxel.btn(pyxel.KEY_S):
            self.y = self.y + 1
    def draw(self):
        pyxel.rect(0, self.y - 20/2, 3, 20, 9)
    def rajta_van(self, y):
        return self.y-20/2 < y < self.y+20/2

bal_uto = Uto()


def update():
    labda_update()
    # ***** itt ez volt: *****
    # uto_update()
    # ***** és ez lett: *****
    bal_uto.update()

def draw():
    pyxel.cls(0)
    labda_draw()
    # ***** itt ez volt: *****
    # uto_draw()
    # ***** és ez lett: *****
    bal_uto.draw()


pyxel.run(update, draw)
