# encoding: utf-8
import pyxel
pyxel.init(160, 120, caption="Pong")

class Labda:
    def __init__(self, x, y, sebx, seby):
        self.x = x
        self.y = y
        self.sebx = sebx
        self.seby = seby

    def update(self):
        # ütközés
        if self.x > 160 - 6: self.sebx = -self.sebx
        if self.y > 120 - 6: self.seby = -self.seby
        if self.x < 6:
            if uton_van(self.y):
                sebx = -sebx
        if self.y < 6: self.seby = -self.seby

        # labda mozgatása
        self.x = self.x + self.sebx
        self.y = self.y + self.seby

    def draw(self):
        pyxel.circ(self.x, self.y, 4, 8)

labda = Labda(30, 40, 1, 1)

class Uto:
    def __init__(self, y):
        self.y = y
    def update(self):
        if pyxel.btn(pyxel.KEY_W):
            self.y = self.y - 1
        if pyxel.btn(pyxel.KEY_S):
            self.y = self.y + 1
    def draw(self):
        pyxel.rect(0 self.y - 20/2, 3, 20, 9)
    def rajta_van(self, y):
        return self.y < y < self.y + 20

uto = Uto(60)



def update():
    labda_update()
    uto_update()

def draw():
    pyxel.cls(0)
    labda_draw()
    uto_draw()


pyxel.run(update, draw)
