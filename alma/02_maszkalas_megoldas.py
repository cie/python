import pyxel

pyxel.init(150,150)
pyxel.image(0).load(0, 0, "assets/ember.png")


class Ember:
    def __init__(self):
        self.x = 0
        self.y = 50
        
    def mozgat(self):
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.x += 1.1
        if pyxel.btn(pyxel.KEY_LEFT): # ha balra
            self.x -= 1.1 # csökkentjük
            
    def rajzol(self):
        if pyxel.btn(pyxel.KEY_RIGHT) or pyxel.btn(pyxel.KEY_LEFT): # akkor is, ha balra
        	i = 1 + int(pyxel.frame_count / 4) % 2
        else:
            i = 0
        w = -16 if pyxel.btn(pyxel.KEY_LEFT) else 16
        pyxel.blt(self.x, self.y, 0, i*16, 0, w , 16, 12)
        
        
# Itt hozunk létre egy konkrét embert.        
ember = Ember()
# Bevett szokás, hogy az osztály neve nagybetűs, a
# konkrét objektum (vagy példány) neve pedig kisbetűs.


def update():
    # két képkocka között meghívjuk a mozgat() metódust
    ember.mozgat()
    
def draw():
    pyxel.cls(15)
    # miután töröltük a képernyőt, meghívjuk a rajzol() metódust
    ember.rajzol()

# ***** Feladat: Az ember jobbra tud sétálni, de csináld
# meg, hogy balra is tudjon.
    
pyxel.run(update, draw)

