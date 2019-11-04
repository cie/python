# encoding: utf-8
import pyxel
pyxel.init(160, 120, caption="Pattogó labda")


# Gratulálok! Ezennel eljutottál a 2. szintre!

# Lehet, hogy már sejtetted: a "Pong" játékot fogjuk elkészíteni.
# Ezért most a pattogó labda mellé készítünk egy ütőt is (később
# majd még egyet)


# ez a két változó tárolja a labda aktuális koordinátáit
labdax = 30
labday = 40
# ez pedig a sebességét
sebx = 1
seby = 1

# ***** vegyél fel egy változót az ütő y koordinátájához *****

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
    # ***** mozgasd az ütőt fel, ha a W le van nyomva *****
    # ***** mozgasd az ütőt le, ha a S le van nyomva *****
    # if pyxel.btn(pyxel.KEY_W):

    
def draw():
    pyxel.cls(0)
    pyxel.circ(labdax, labday, 4, 8)

    # ***** és rajzold meg az ütőt *****
    # pyxel.rect(x, y, width, height, color)

pyxel.run(update, draw)
