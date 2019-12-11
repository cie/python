import pyxel

pyxel.init(150,150)

# Most egy másik képet töltünk be.
pyxel.image(0).load(0, 0, "assets/ember.png")
# Ezen is 16x16-os egységek vannak. Az 0-dik egy álló ember
# az 1-2-dik a sétáló ember animációja.
    
# két képkocka között
def update():
    pass # nem csinálunk semmit
    
# egy-egy képkockánál
def draw():
    # töröljük a képernyőt 15-ös színnel
    pyxel.cls(15)
    
    pyxel.blt(20, 50, 0, 0, 0, 3*16, 16)
    
    # ***** Feladat: rajzold meg a sétáló embert animálva,
    # a kék háttér nélkül.
    
pyxel.run(update, draw)

