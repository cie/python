# encoding: utf-8
import pyxel
pyxel.init(160, 120, caption="Szálló labda")

# ez a két változó tárolja a labda aktuális koordinátáit
labdax = 30
labday = 40

# mit számítsunk minden képkocka előtt
def update():
    # ha épp most nyomtuk le a Q-t, lépjen ki
    if pyxel.btnp(pyxel.KEY_Q):
        pyxel.quit()

    # jeleznünk kell, hogy meg szeretnénk változtatni "kinti"
    # változót
    global labdax, labday

    # ***** megoldás *****
    labdax = labdax + 1
    labday = labday + 1

    
# mit rajzoljunk minden képkockában
def draw():
    # letöröljük a képernyőt (0=fekete)
    pyxel.cls(0)
    # kirajzoljuk a labdát
    # pyxel.circ(x, y, r, szín)
    pyxel.circ(labdax, labday, 4, 8)

pyxel.run(update, draw)
