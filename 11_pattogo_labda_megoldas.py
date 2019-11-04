# encoding: utf-8
import pyxel
pyxel.init(160, 120, caption="Pattogó labda")

# ez a két változó tárolja a labda aktuális koordinátáit
labdax = 30
labday = 40
# ***** ez pedig a sebességét
sebx = 1
seby = 1

# mit számítsunk minden képkocka előtt
def update():
    # jeleznünk kell, hogy meg szeretnénk változtatni "kinti"
    # változót
    global labdax, labday, sebx, seby

    # ***** megoldás *****
    # ütközés
    if labdax > 160 - 6: sebx = -sebx
    if labday > 120 - 6: seby = -seby
    if labdax < 6: sebx = -sebx
    if labday < 6: seby = -seby

    # labda mozgatása
    labdax = labdax + sebx
    labday = labday + seby

    
def draw():
    pyxel.cls(0)
    pyxel.circ(labdax, labday, 4, 8)

pyxel.run(update, draw)
