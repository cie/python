# encoding: utf-8
import pyxel
pyxel.init(160, 120, caption="Pong")


# ***** Oldd meg, hogy a labda a bal oldalon csak akkor pattanjon
# vissza, ha eltalálta az ütőt. *****

# Vezess be egy függvényt (uton_van), aminek a paramétere egy y
# koordináta, és megadja, hogy az a koordináta éppen rajta van-e
# az ütőn (True/False). Használd ezt a függvényt a megoldáshoz.

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


def update():
    labda_update()
    uto_update()

def draw():
    pyxel.cls(0)
    labda_draw()
    uto_draw()


pyxel.run(update, draw)
