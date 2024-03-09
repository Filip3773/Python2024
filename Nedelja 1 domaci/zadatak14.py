def procena_cene_stana(velicina, lokacija, parking):
    cena_kvadrata = 1200
    fiksno_ucesce = 1000

  
    if lokacija == 1:
        faktor_lokacije = 3
    elif lokacija == 2:
        faktor_lokacije = 2
    else:
        faktor_lokacije = 1

  
    cena = velicina * cena_kvadrata + faktor_lokacije * 5 * cena_kvadrata + parking * 10 * cena_kvadrata + fiksno_ucesce

    return cena


velicina_stana = float(input("Unesite veličinu stana (u m^2): "))
lokacija_stana = int(input("Unesite lokaciju stana (1 za zonu 1, 2 za zonu 2, 3 za zonu 3): "))
parking_stana = int(input("Da li stan ima parking? (1 za da, 0 za ne): "))

cena_stana = procena_cene_stana(velicina_stana, lokacija_stana, parking_stana)
print("Procijenjena cijena stana je:", cena_stana, "eura.")
