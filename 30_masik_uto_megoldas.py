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

# ----- ütő2 -----
uto2y = 60
def uto2_update():
    global uto2y
    if pyxel.btn(pyxel.KEY_I):
        uto2y = uto2y - 1
    if pyxel.btn(pyxel.KEY_K):
        uto2y = uto2y + 1
def uto2_draw():
    pyxel.rect(160-3, uto2y - 20/2, 3, 20, 9)



def update():
    labda_update()
    uto_update()
    uto2_update()

def draw():
    pyxel.cls(0)
    labda_draw()
    uto_draw()
    uto2_draw()


pyxel.run(update, draw)
