import math


x1_hrast = int(input("x kordinata hrasta"))
y1_hrast = int(input("y kordinata hrasta"))

x2_kuca = int(input("x kordinata kuce"))
y2_kuca = int(input("x kordinata kuce"))

x_blago = x2_kuca + 2
y_blago = y2_kuca - 3


d_vazdusno = math.sqrt((x_blago - x1_hrast)**2 + (y_blago - y1_hrast)**2)


d_hrast_kuca = math.sqrt((x2_kuca - x1_hrast)**2 + (y2_kuca - y1_hrast)**2)
d_kuca_blago = math.sqrt((x_blago - x2_kuca)**2 + (y_blago - y2_kuca)**2)
d_obilazak = d_hrast_kuca + d_kuca_blago

# Ispis rezultata
print("Koordinate blaga su:", (x_blago, y_blago))
print("Vazdušno rastojanje od hrasta do blaga je:", d_vazdusno)
print("Rastojanje od hrasta do blaga uz obilazak kuće je:", d_obilazak)
