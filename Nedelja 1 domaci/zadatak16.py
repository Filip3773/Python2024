a = 1
br_km=int(input("Broj kilometara koji je taksi presao:"))
def cena_po_km():
    return a + (br_km*0.5) 
b = str(cena_po_km())
print("Duzni ste taksisti "+b+" eura.")