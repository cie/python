import pyxel

pyxel.init(150,150)
pyxel.image(0).load(0, 0, "assets/ember.png")


# Ez itt egy ún. osztály.
# Egy osztály egy valamilyen fajta dolog (itt egy ember)
# adatait kezeli. Ehhez különféle műveleteket, ún.
# metódusokat kell benne definiálni.

class Ember:
    # Az __init__ egy speciális metódus,
    # ez állítja be a kezdeti adatokat.
    def __init__(self):
        self.x = 0
        self.y = 50
        
    # ez egy másik metódus    
    def mozgat(self):
        # ha le van nyomva a jobbra gomb
        if pyxel.btn(pyxel.KEY_RIGHT):
            # növeljük az x értékét
            self.x += 1.1
            
    # ez pedig egy harmadik metódus
    def rajzol(self):
        if pyxel.btn(pyxel.KEY_RIGHT):
        	i = 1 + int(pyxel.frame_count / 4) % 2
        else:
            i = 0
        pyxel.blt(self.x, self.y, 0, i*16, 0, 16, 16, 12)
        
        
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
# Trükk: ahhoz, hogy a blt() megtükrözzön egy képet, a szélességet
# egyszerűen az ellentettjére (negatívra) kell állítani.
    
pyxel.run(update, draw)

