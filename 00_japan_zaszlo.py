# A #-tel kezdődő sorok megjegyzések (kommentek).
# encoding: utf-8  (ez az ékezetes betűkért kell)

# ***** 0. szint, 0. feladat: rajzolj egy japán zászlót az ablak
# közepére (fehér téglalap, piros kör) *****

# betöltjük a pyxel könyvtárat
import pyxel

# megnyitjuk az ablakot: szélesség, magasság, cím
pyxel.init(160, 120, caption="Japán zászló")

# mi történjen minden képkocka előtt
def update():
    # ha épp most nyomtuk le a Q-t
    if pyxel.btnp(pyxel.KEY_Q):
        # lépjen ki
        pyxel.quit()

# mit rajzoljunk minden képkockában
def draw():
    # letöröljük a képernyőt
    pyxel.cls(0)
    # ***** ide írd a kódot *****
    # segítség:
    # téglalap: pyxel.rect(x, y, width, height, color)
    # kör: pyxel.circ(x, y, r, color)
    # színek: 0=fekete 7=fehér 8=piros
    # ablak szélessége 160, magassága 120
    # origó a bal felső sarok(!), x jobbra, y lefelé(!)


# elindítjuk a játékot
pyxel.run(update, draw)
