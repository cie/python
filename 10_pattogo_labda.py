# encoding: utf-8

# Gratulálok! Eljutottál az 1. szintre (pythonban mindent 0-val kezdünk számozni, ezért van ilyen furcsán :)

# ***** 1. szint, 0. feladat: Ez a program most egy álló labdát rajzol ki. Oldd meg, hogy a labda mozogjon valahogy (pl. a függőlegeshez képest 45 fokban egyenletesen haladjon)

import pyxel
pyxel.init(160, 120, caption="Japán zászló")

# ez a két változó tárolja a labda aktuális koordinátáit
labdax = 30
labday = 40

# mit számítsunk minden képkocka előtt
def update():
    # ha épp most nyomtuk le a Q-t, lépjen ki
    if pyxel.btnp(pyxel.KEY_Q):
        pyxel.quit()

    # jeleznünk kell, hogy meg szeretnénk változtatnki "kinti" változót
    # (olyat, amit nem itt, az update függvényben hoztunk létre)
    global labdax, labday
    # ***** ide írd a kódot, ami a labda két koordinátáját változtatja *****

    
# mit rajzoljunk minden képkockában
def draw():
    # letöröljük a képernyőt (0=fekete)
    pyxel.cls(0)
    # kirajzoljuk a labdát
    # pyxel.circ(x, y, r, szín)
    pyxel.circ(labdax, labday, 4, 8)

pyxel.run(update, draw)
