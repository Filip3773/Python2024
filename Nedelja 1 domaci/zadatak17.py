cena_knjige =int(input("Cena knjige:"))
popust = int(input("popust na knjigu:"))
b = str(cena_knjige-((cena_knjige/100)*popust))
print("Cena knjige je "+b+" .")