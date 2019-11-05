# encoding: utf-8
import pyxel
pyxel.init(160, 120, caption="Pong")

class Labda:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.sebx = 1
        self.seby = 1

    def update(self):
        # ütközés
        if self.x > 160 - 6:
            # ***** jobb ütővel való ütközés ellenőrzése *****
            if jobb_uto.rajta_van(self.y):
                self.sebx = -self.sebx
        if self.y > 120 - 6: self.seby = -self.seby
        if self.x < 6:
            if bal_uto.rajta_van(self.y):
                self.sebx = -self.sebx
        if self.y < 6: self.seby = -self.seby

        # labda mozgatása
        self.x = self.x + self.sebx
        self.y = self.y + self.seby

    def draw(self):
        pyxel.circ(self.x, self.y, 4, 8)

labda = Labda(80, 60)

class Uto:
    # **** bevezettünk 3 új konstrutor-paraméteret *****
    def __init__(self, x, up, down):
        self.y = 60 
        self.x = x
        self.up = up
        self.down = down
    def update(self):
        # ***** a self-ben elmentett adatot használjuk
        if pyxel.btn(self.up):
            self.y = self.y - 1
        # ***** itt is:
        if pyxel.btn(self.down):
            self.y = self.y + 1
    def draw(self):
        # ***** itt pedig az x-et
        pyxel.rect(self.x, self.y - 20/2, 3, 20, 9)
    def rajta_van(self, y):
        return self.y-20/2 < y < self.y+20/2

# ***** és így létre tudjuk hozni a kétféle ütőt
bal_uto = Uto(0, pyxel.KEY_W, pyxel.KEY_S)
jobb_uto = Uto(160-3, pyxel.KEY_I, pyxel.KEY_K)



def update():
    labda.update()
    bal_uto.update()
    # ***** update-elni kell az új ütőt is ***** 
    jobb_uto.update()

def draw():
    pyxel.cls(0)
    labda.draw()
    bal_uto.draw()
    # ***** és ki is kell rajzolni ***** 
    jobb_uto.draw()


pyxel.run(update, draw)
