# encoding: utf-8
import pyxel
pyxel.init(160, 120, caption="Pattogó labda")

# ez a két változó tárolja a labda aktuális koordinátáit
labdax = 30
labday = 40
# ez pedig a sebességét
sebx = 1
seby = 1

# ütő
utoy = 60

# mit számítsunk minden képkocka előtt
def update():
    # jeleznünk kell, hogy meg szeretnénk változtatni "kinti"
    # változót
    global labdax, labday, sebx, seby

    # ütközés
    if labdax > 160 - 6: sebx = -sebx
    if labday > 120 - 6: seby = -seby
    if labdax < 6: sebx = -sebx
    if labday < 6: seby = -seby

    # labda mozgatása
    labdax = labdax + sebx
    labday = labday + seby

    # ütő mozgatása
    global utoy
    if pyxel.btn(pyxel.KEY_W):
        utoy = utoy - 1
    if pyxel.btn(pyxel.KEY_S):
        utoy = utoy + 1

    
def draw():
    pyxel.cls(0)

    # labda
    pyxel.circ(labdax, labday, 4, 8)

    # ütő
    pyxel.rect(0, utoy - 20/2, 3, 20, 9)

pyxel.run(update, draw)
