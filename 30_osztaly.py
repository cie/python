# encoding: utf-8
import pyxel
pyxel.init(160, 120, caption="Pong")

# Gratulálok! Elérted a 3. szintet!

# Nemsokára elkészítjük a második ütőt, de előbb valami fontos
# dolgot be kell vezessünk.

# Az 1. szinten megtanultuk a változókat, amik adatokat tárolnak.
# A 2. szinten megtanultuk a függvényeket, amik műveleteket tudnak
# A 3. szinten megtanuljuk az osztályokat, amik az összetartozó
# adatokat és műveleteket együtt kezelik!

# Itt vannak a labdával kapcsolatos változóink és függvényeink:

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
        if uton_van(labday):
            sebx = -sebx
    if labday < 6: seby = -seby

    # labda mozgatása
    labdax = labdax + sebx
    labday = labday + seby

def labda_draw():
    pyxel.circ(labdax, labday, 4, 8)

# És itt vannak az ütővel kapcsolatos változóink és függvényeink:

# ----- ütő -----
utoy = 60
def uto_update():
    global utoy
    if pyxel.btn(pyxel.KEY_W):
        utoy = utoy - 1
    if pyxel.btn(pyxel.KEY_S):
        utoy = utoy + 1
def uto_draw():
    pyxel.rect(0, utoy - 20/2, 3, 20, 9)

def uton_van(y):
    return utoy < y < utoy + 20

# A labda is egy fajta "dolog", és az ütő is egy fajta "dolog",
# sőt, ütőből nemsokára két darab is lesz, két "dolog" ugyanabból
# a fajtából.
# Az osztály (class) a dolgoknak egy fajtáját jelenti, az objektum
# (object) pedig egy konkrét dolgot.  Lesz két osztályunk (Labda
# és Ütő), és három objektumunk (a labda, a bal ütő és a jobb
# ütő).

# Az ütő-osztály így néz ki:

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
        return self.y < y < self.y + 20

# * a class szó csinál egy osztályt. Az osztályok neveit
# megegyezés szerint nagybetűvel kezdjük
# * a class-ban vannak függvények - ezek az osztály "metódusai".
# * az __init__ egy speciális metódus, a "dolog" létrehozására
# való, beállítja a kezdeti adatait (ez az ún. konstruktor)
# * az összes metódusnak van egy 'self' paramétere - ami a "dolog"
# saját maga. Ebbe van betéve minden adat (itt csak az y) a '.'
# operátorral.

# Ebből egy objektum (egy konkrét ütő) létrehozása így történik:
bal_uto = Uto()
# És a metódusainak meghívása így történik:
# bal_uto.draw()
# bal_uto.update()
# bal_uto.rajta_van(20)


# ***** Feladat: üzemeld be az új bal_uto objektumot, és töröld ki
# a régi, ütővel kapcsolatos műveleteket! *****


def update():
    labda_update()
    uto_update()

def draw():
    pyxel.cls(0)
    labda_draw()
    uto_draw()


pyxel.run(update, draw)
