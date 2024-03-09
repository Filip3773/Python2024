d = int(input("Duzina terena u metrima: "))
s = int(input("Sirina terena u metrima: "))
r = int(input("Rastojanje ograde terena u metrima: "))

def duzina_ograde():
    return (d+r)*(s+r)

d = str(duzina_ograde())
print("Duzina ograde je " +d+".")
