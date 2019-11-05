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
    if labdax < 6: sebx = -sebx
    if labday < 6: seby = -seby

    # labda mozgatása
    labdax = labdax + sebx
    labday = labday + seby

def labda_draw():
    pyxel.circ(labdax, labday, 4, 8)


# Ez az ütő-dolog még így is elég kusza. Itt tartottunk vele:
#
# # ----- ütő -----
# utoy = 60
# def uto_update():
#     global utoy
#     if pyxel.btn(pyxel.KEY_W):
#         utoy = utoy - 1
#     if pyxel.btn(pyxel.KEY_S):
#         utoy = utoy + 1
# def uto_draw():
#     pyxel.rect(0, utoy - 20/2, 3, 20, 9)
# 
# # ----- ütő2 -----
# uto2y = 60
# def uto2_update():
#     global uto2y
#     if pyxel.btn(pyxel.KEY_I):
#         uto2y = uto2y - 1
#     if pyxel.btn(pyxel.KEY_K):
#         uto2y = uto2y + 1
# def uto2_draw():
#     pyxel.rect(160-3, uto2y - 20/2, 3, 20, 9)
# 
# A két ütő nagyon hasonló, csak kicsit térnek el. Ugyanolyan
# FAJTA DOLGOK.

# Van egy nagyon KLASSZ funkció a pythonban, ami pont a "dolgok"
# kezelésére van kitalálva, különösen ha egy "fajta" dologból több
# is kell. Ez a class (osztály). Szó szerint azt jelenti, hogy
# dolgoknak egy fajtája.

# Az 1. szinten megtanultuk a változókat, amik adatokat tárolnak.
# A 2. szinten megtanultuk a függvényeket, amik műveleteket tudnak
# csoportosítani.
# Az osztály együtt kezeli az összetartozó adatokat és műveleteket.

# Így néz ki egy ütő-osztály:

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
        

# * a class szó csinál egy osztályt. Az osztályok neveit
# megegyezés szerint nagybetűvel kezdjük
# * az __init__ egy speciális művelet, a "dolog" létrehozására
# való, beállítja a kezdeti adatait
# * az összes műveletnek van egy 'self' paramétere - ami a "dolog"
# saját maga. Ebbe van betéve minden adat.
# * az up és a down adatokat most vezettük be: az, hogy melyik
# billentyűkkel lehet mozgatni az ütőt

# Ebből egy ütő létrehozása így történik (x, y, up, down):
uto = Uto(0, 60, pyxel.KEY_W, pyxel.KEY_S)
# Egy másik pedig így:
uto2 = Uto(160-3, 60, pyxel.KEY_I, pyxel.KEY_K)


def update():
    labda_update()
    # a metódusok meghívása pedig így történik
    uto.update()
    uto2.update()

def draw():
    pyxel.cls(0)
    labda_draw()
    # és így
    uto.draw()
    uto2.draw()

# ***** A feladat: Készítsd el a Labda osztályt

pyxel.run(update, draw)
