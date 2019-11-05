# encoding: utf-8
import pyxel
pyxel.init(160, 120, caption="Pong")

# **** Számold a pontokat! ****
# Legyen az app osztálynak egy-egy mezője, ami a jobb ill. bal
# játékos pontját tárolja.
# Legyen az app osztálynak egy-egy metódusa, ami a jobb ill. bal
# játékos pontszerzését kezeli le.
# Egy pont után induljon a labda újra középről, a nyert játékos
# irányába.
# Írd ki a pontokat!

class Labda:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.sebx = 1
        self.seby = 1

    def update(self):
        # ütközés
        if self.x > 160 - 6:
            if app.jobb_uto.rajta_van(self.y):
                self.sebx = -self.sebx
            else:
                app.bal_nyert()
        if self.y > 120 - 6: self.seby = -self.seby
        if self.x < 6:
            if app.bal_uto.rajta_van(self.y):
                self.sebx = -self.sebx
            else:
                app.jobb_nyert()
        if self.y < 6: self.seby = -self.seby

        # labda mozgatása
        self.x = self.x + self.sebx
        self.y = self.y + self.seby

    def draw(self):
        pyxel.circ(self.x, self.y, 4, 8)


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
        return self.y-20/2 < y < self.y+20/2


class App:
    def __init__(self):
        self.labda = Labda(80, 60)
        self.bal_uto = Uto(0, pyxel.KEY_W, pyxel.KEY_S)
        self.jobb_uto = Uto(160-3, pyxel.KEY_I, pyxel.KEY_K)
        self.bal_pont = 0
        self.jobb_pont = 0

    def update(self):
        self.labda.update()
        self.bal_uto.update()
        self.jobb_uto.update()

    def draw(self):
        pyxel.cls(0)
        pyxel.text(20, 0, str(self.bal_pont), 12)
        pyxel.text(160-20, 0, str(self.jobb_pont), 12)
        self.labda.draw()
        self.bal_uto.draw()
        self.jobb_uto.draw()

    def bal_nyert(self):
        self.bal_pont = self.bal_pont + 1
        self.labda.x = 80
        self.labda.y = 60
        self.labda.sebx = -1

    def jobb_nyert(self):
        self.jobb_pont = self.jobb_pont + 1
        self.labda.x = 80
        self.labda.y = 60
        self.labda.sebx = 1

app = App()

pyxel.run(app.update, app.draw)
