import pyxel


class App:
    def __init__(self):
        pyxel.init(160, 120, caption="Hello Pyxel")
        pyxel.image(0).load(0, 0, "assets/pyxel_logo_38x16.png")
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

    def draw(self):
        pyxel.cls(0)
        pyxel.rect(30, 30, 100, 60, 12)
        #Draw a rectangle of width w, height h and color col from (x, y)
        pyxel.circ(80, 60, 20, 1)



App()
