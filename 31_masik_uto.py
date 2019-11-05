# encoding: utf-8
import pyxel
pyxel.init(160, 120, caption="Pong")

# ***** Bónuszpálya: a Labda osztályt megkapod ingyen :) ****
# Íme:

class Labda:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.sebx = 1
        self.seby = 1

    def update(self):
        # ütközés
        if self.x > 160 - 6: self.sebx = -self.sebx
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

# Figyeld csak meg, hogy a Labda osztály __init__ metódusának van
# még két paramétere. Ezek ún. konstruktor-paraméterek. Ezek
# értékét akkor lehet megadni, amikor létrehozzuk az objektumot -
# és ott meg is adjuk (Labda(80,60)).  Ezeket leggyakrabban csak
# lementjük a self-be a nem túl izgalmas self.x = x; self.y = y
# típusú sorokkal.


# ***** A feladatod: létre kell hoznod a jobb ütőt.
# Ez kicsit máshogy kell működjön:
# * Egyrészt - mily meglepő - a jobb oldalon kell legyen.
# * Másrészt az I és K billentyűkkel kell vezérelni.
#
# Vezess be az Uto-ben is konstruktor-paramétereket, hogy a fent
# leírt eltéréseket az egyes objektumoknál meg tudd adni!
# Három konstruktor-paramétert vezess be:
# * x - az ütő x-pozíciója
# * up - melyik billentyű mozgatja fel
# * down - melyik billentyű mozgatja le
# Mentsd le ezeket a self-be, ahogy a Labda osztálynál van,
# és használd a self-ben lévő értéket a metódusokban.

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
    labda.update()
    bal_uto.update()

def draw():
    pyxel.cls(0)
    labda.draw()
    bal_uto.draw()


pyxel.run(update, draw)
