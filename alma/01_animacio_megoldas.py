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
    
    i = 1 + int(pyxel.frame_count / 4) % 2
    #   ^ ez azért kell, mert az 1-dik (nem a 0-dik) kockánál kezdünk
    #                 ^ az aktuális képkocka sorszáma
    #                             ^ azért osztunk le, hogy ne legyen túl gyors
    #                                  ^ csak 2 kockából áll az animáció, ezért 
    #                                    2-es maradékot veszünk
    
    pyxel.blt(20, 50, 0, i*16, 0, 16, 16, 12)
    #                      ^ 16 széles egy képkocka
    #                                     ^ a kék színt kihagyjuk
    
pyxel.run(update, draw)

