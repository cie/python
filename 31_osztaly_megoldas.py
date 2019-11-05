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
        if self.x > 160 - 6: self.sebx = -self.sebx
        if self.y > 120 - 6: self.seby = -self.seby
        if self.x < 6: self.sebx = -self.sebx
        if self.y < 6: self.seby = -self.seby

        # labda mozgatása
        self.x = self.x + self.sebx
        self.y = self.y + self.seby

    def draw(self):
        pyxel.circ(self.x, self.y, 4, 8)

labda = Labda(30, 40, 1, 1)

class Uto:
    def __init__(self, x, y, up, down):
        self.x = x
        self.y = y
        self.up = up
        self.down = down
    def update(self):
        if pyxel.btn(self.up):
            self.y = self.y - 1
        if pyxel.btn(self.down):
            self.y = self.y + 1
    def draw(self):
        pyxel.rect(self.x, self.y - 20/2, 3, 20, 9)
        
uto = Uto(0, 60, pyxel.KEY_W, pyxel.KEY_S)
uto2 = Uto(160-3, 60, pyxel.KEY_I, pyxel.KEY_K)

def update():
    labda.update()
    uto.update()
    uto2.update()

def draw():
    pyxel.cls(0)
    labda.draw()
    uto.draw()
    uto2.draw()

pyxel.run(update, draw)
