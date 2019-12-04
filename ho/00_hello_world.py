import pyxel
import math
# ablak szélessége, magassága, címe
pyxel.init(255,255, caption="Hello")

# Mit csináljunk egy képkocka előtt
def update():
    # kiírjuk alul, hogy Hello 0!, Hello 1! stb. mindig az
    # aktuális képkocka sorszámát
    # ***** a)feladat: módosítsd úgy, hogy Hello World!-öt írjon!
	print("Hello {n}!".format(n = pyxel.frame_count))

# Hogyan rajzolunk ki egy-egy képkockát
def draw():
    # Letöröljük a képernyőt 0-es színnel (fekete)
    pyxel.cls(0)
    # ***** b)feladat: húzz egy vonalat 11-es színnel (neonzöld)
    # Így:
    #pyxel.line(0, 0, 30, 30, 11)
    
# Elindítjuk
pyxel.run(update, draw)