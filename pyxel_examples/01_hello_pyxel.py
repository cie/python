import pyxel

pyxel.init(160, 120, caption="Hello Pyxel")
pyxel.image(0).load(0, 0, "assets/pyxel_logo_38x16.png")

def update():
    if pyxel.btnp(pyxel.KEY_Q):
        pyxel.quit()

def draw():
    pyxel.cls(0)
    pyxel.text(55, 41, "Hello, Pyxel!", pyxel.frame_count % 16)
    pyxel.blt(61, 66, 0, 0, 0, 38, 16)


pyxel.run(update, draw)
