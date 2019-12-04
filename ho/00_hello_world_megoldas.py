import pyxel
import math
pyxel.init(255,255, caption="Hello")

def update():
    # Hello World!
	print("Hello {n}!".format(n = "World"))
    # vagy csak simán:
	print("Hello Wolrd!")

def draw():
    pyxel.cls(0)
    pyxel.line(0, 0, 30, 30, 11)
    
# Elindítjuk
pyxel.run(update, draw)