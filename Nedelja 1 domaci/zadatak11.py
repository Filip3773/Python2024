import math
x1=int(input("x1 koridinata:"))
y1=int(input("y1 koridinata:"))
x2=int(input("x2 koridinata:"))
y2=int(input("y2 koridinata:"))

def euklidsko_rastojanje():
    return  math.sqrt((x2-x1)**2 + (y2-y1)**2)

print(euklidsko_rastojanje())