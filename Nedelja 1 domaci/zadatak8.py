import math

p = int(input("Povrsina stolnjaka :"))

def obim_kruga():
    r = math.sqrt(p / math.pi)
    obim = 2* math.pi * r
    return obim
o = str(obim_kruga())
print("Duzina ivice  stolnjaka je "+o+".")