def nova_c(pocetna_c):
   
    nova_c = pocetna_c * 1.10
    nova_c = nova_c * 0.90
    return nova_c
pocetna_c = float(input("Unesite početnu cenu konzole: "))
nova = nova_c(pocetna_c)
print("Nova cena nakon promjena je:", nova)

