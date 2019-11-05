# encoding: utf-8
import pyxel
pyxel.init(160, 120, caption="Pong")

# ***** 2.szint 1. feladat.
# Kicsit kezd kusza lenni a program. A labda és az ütő adatai
# szét vannak szórva a fájl elején, közepén és végén, nem látszik
# egyben, hogy mi történik velük.

# Alakítsd át a programot úgy, hogy a labda kezdeti adatai,
# mozgatása és kirajzolása egymás után legyenek, és hasonlóan az
# ütőnek is!

# Ehhez egy új dolgot kell használnod, függvényeket - bár nem
# annyira új: az update és a draw is egy-egy függvény.

# labda
labdax = 30
labday = 40
# ez pedig a sebességét
sebx = 1
seby = 1

# ***** készíts el egy ilyen függvényt *****
def labda_update():
    global labdax, labday, sebx, seby
    # ide helyezd át a labdát mozgató kódokat

# ***** aztán készíts el egy ilyen függvényt is *****
# def labda_draw():


# ütő
utoy = 60

# ***** aztán az ütővel is tégy hasonlóképp *****
def uto_update():
    global utoy
    # ***** ide helyezd át az ütőt mozgató kódot *****

# ***** és készíts el egy ilyen függvényt *****
# def uto_draw():
#


# mit számítsunk minden képkocka előtt
def update():
    # ***** itt ne felejtsd el hívd meg a függvényeidet *****
    # labda_update()
    # uto_update()

    # ***** ezt pedig most már törölheted, nem kell ide *****
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
