# encoding: utf-8
import pyxel
pyxel.init(160, 120, caption="Pattogó labda")

# ***** 1. szint 1. feladat (azaz ezzel együtt már három volt:)
# Pattogjon a labda az ablak széleinél.
#
# Ehhez szükség lesz új változókra: vezess be két új változót
# a labda x és y irányú sebességének tárolására. Aztán változtasd
# meg a sebességet, ha kimenne a szélén.
# *****

# ez a két változó tárolja a labda aktuális koordinátáit
labdax = 30
labday = 40

# mit számítsunk minden képkocka előtt
def update():
    # jeleznünk kell, hogy meg szeretnénk változtatni "kinti"
    # változót
    global labdax, labday

    # ***** ide írd a kódot *****
    # segítség
    # if valami_igaz:
    #    csinálj_valamit

    # labda mozgatása (***** ezt meg kell változtatnod)
    labdax = labdax + 1
    labday = labday + 1

    
def draw():
    pyxel.cls(0)
    pyxel.circ(labdax, labday, 4, 8)

pyxel.run(update, draw)
