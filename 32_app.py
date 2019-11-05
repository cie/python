# encoding: utf-8
import pyxel
pyxel.init(160, 120, caption="Pong")

# Szeretnénk elkezdeni számolni a pontokat. A pontszám egy olyan adat, ami az
# egész játékra tartozik (nem a labdára és nem az ütőkre).  Van két függvényünk
# is (update és draw) ami az egész játékra tartozik, és három változó is, ami
# az egész játékra tartozik (hehe, a labda, a bal_uto és a jobb_uto).
# Jó lenne ezeket is összecsomagolni egy osztályba.

# **** Feladat: készíts egy osztályt a játék egészére tartozó változókból és
# függvényekből! Legyen a neve App.

class Labda:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.sebx = 1
        self.seby = 1

    def update(self):
        # ütközés
        if self.x > 160 - 6:
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
    def __init__(self, x, up, down):
        self.y = 60 
        self.x = x
        self.up = up
        self.down = down
    def update(self):
        if pyxel.btn(self.up):
            self.y = self.y - 1
        if pyxel.btn(self.down):
            self.y = self.y + 1
    def draw(self):
        pyxel.rect(self.x, self.y - 20/2, 3, 20, 9)
    def rajta_van(self, y):
        return self.y < y < self.y + 20

bal_uto = Uto(0, pyxel.KEY_W, pyxel.KEY_S)
jobb_uto = Uto(160-3, pyxel.KEY_I, pyxel.KEY_K)



def update():
    labda.update()
    bal_uto.update()
    jobb_uto.update()

def draw():
    pyxel.cls(0)
    labda.draw()
    bal_uto.draw()
    jobb_uto.draw()


pyxel.run(update, draw)
