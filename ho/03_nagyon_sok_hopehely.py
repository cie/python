import pyxel
import math
import random
pyxel.init(255,255)

def update():
	pass    

def hopehely(x, y, r):
    szin = 15 # fehér
    s = math.sqrt(2) * r / 2
    pyxel.line(x+r, y  , x-r, y  , szin)
    pyxel.line(x  , y-r, x  , y+r, szin)
    pyxel.line(round(x-s),
               round(y-s),
               round(x+s),
               round(y+s), szin)
    pyxel.line(round(x-s),
               round(y+s),
               round(x+s),
               round(y-s), szin)


# Készítettünk egy listát a hópelyhek adataival:
# Minden hópehely egy (x, y, r) rendezett hármas.
hopelyhek = [
    (50, 50, 3),
    (140, 50, 6),
    (60, 80, 10),   # az utolsó vesszőt nem muszáj kitenni
]

def draw():
    pyxel.cls(1) # sötétkék
    # És itt végigmegyünk rajtuk:
    for (x, y, r) in hopelyhek:
        hopehely(x, y + pyxel.frame_count, r)
    # *****
    # a) feladat: Adj hozzá sok hópelyhet!
    # Ha nem szeretnéd kézzel kitalálni a számokat, segíthet a
    # random.randint(a, b) függvény, ami egy a-nál nem kisebb,
    # b-nél kisebb véletlen egész számot ad vissza.

    # b) feladat: amelyik hópehely kiment alul,
    # az jöjjön vissza fölül!
    # Ehhez használhatod a % operátort, ami a maradékos osztás
    # maradékát számolja ki:
    # pl. 2019 % 10 == 9
    
pyxel.run(update, draw)