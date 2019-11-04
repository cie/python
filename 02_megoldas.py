# encoding: utf-8
import pyxel
pyxel.init(160, 120, caption="Japán zászló")

def update():
    # ha épp most nyomtuk le a Q-t
    if pyxel.btnp(pyxel.KEY_Q):
        # lépjen ki
        pyxel.quit()

def draw():
    # letöröljük a képernyőt
    pyxel.cls(0)
    # téglalap: rect(x, y, width, height, color)
    # kör: circ(x, y, r, color)
    # színek: 0=fekete 7=fehér 8=piros

    # ***** megoldás *****
    pyxel.rect(30, 30, 100, 60, 7)
    pyxel.circ(80, 60, 20, 8)
    # ***** vagy: minek is számoljunk a gép helyett? *****
    pyxel.rect(80-100/2, 60-60/2, 100, 60, 7)
    pyxel.circ(80, 60, 20, 8)


pyxel.run(update, draw)
