import math

def distanca(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def povrsina_t(x1, y1, x2, y2, x3, y3):
    a = distanca(x1, y1, x2, y2)
    b = distanca(x2, y2, x3, y3)
    c = distanca(x3, y3, x1, y1)
    s = (a + b + c) / 2  # poluobim
    povrsina = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return povrsina

# Unos koordinata tačaka trougla
x1, y1 = map(float, input("Unesite koordinate prve tačke (x1 y1): ").split())
x2, y2 = map(float, input("Unesite koordinate druge tačke (x2 y2): ").split())
x3, y3 = map(float, input("Unesite koordinate treće tačke (x3 y3): ").split())

# Izračunavanje površine trougla
povrsina_t = povrsina_t(x1, y1, x2, y2, x3, y3)

print("Površina trougla je:", povrsina_t)
