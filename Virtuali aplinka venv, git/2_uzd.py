import calendar

metai_nuo = int(input("Įveskite metus nuo: "))
metai_iki = int(input("Įveskite metus iki: "))

def keliamieji_metai(metai_nuo, metai_iki):
    for metai in range(metai_nuo, metai_iki):
        if calendar.isleap(metai):
            print(metai)

keliamieji_metai(metai_nuo, metai_iki)
input("Spauskite 'Enter'")

# Leistų vartotojui įvesti metus nuo ir metus iki
# Atspausdintų visus keliamuosius metus pagal duotą rėžį
# Paleidžiamasis failas turi turėti norimą ikoną