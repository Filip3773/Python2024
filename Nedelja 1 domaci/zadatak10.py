import math
k1 = (input("Uneti kordinate prve tacke(leve ivice)-napraviti razmak izmdeju x i y: ").split())
k2 = (input("Uneti kordinate druge tacke").split())

x1 = (int(k1[0]))
y1 = (int(k1[1]))
x2 = (int(k2[0]))
y2 = int(k2[1])

def hipotenuza():
    d = math.sqrt((x2-x1)**2  +(y2-y1)**2)
    return d

def povrsina():
    p = math.sqrt((x2-x1)**2) * math.sqrt((y2-y1)**2)
    return p
#Mogao sam isto da stavim abs(x2-x1) ali sam se kanso setio
def obim():
     o = 2*(math.sqrt((x2-x1)**2)) + 2*(math.sqrt((y2-y1)**2))
     return o

o = str(obim())
p= str(povrsina())
print("Povrsina zida je "+p+" a obim "+o+" .")

