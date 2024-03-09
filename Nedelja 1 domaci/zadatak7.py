import math

a = int(input("Broj sati koji je Marko proveo na biciklu: "))
def konzumacija_vode():
    return math.floor(a/2)
b = str(konzumacija_vode())
print("Marko je popio"+ b +"litara vode.")