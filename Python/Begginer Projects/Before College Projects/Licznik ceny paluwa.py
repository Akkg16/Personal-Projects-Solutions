from ast import Break, Return




while True:
    try:
        cena_paliwa = float(input("Jaka jest obecna cena za litr paliwa? :"))
    except ValueError:
        print("This is not a number")
        continue
    try:
        spalanie_min = float(input("Jakie przewidujesz minimalne spalanie podczas swojej jazdy? "))
    except ValueError:
        print("This is not a number")
        continue
    try: 
        spalanie_max = float(input("Jakie przewidujesz maksymalne spalanie podczas swojej jazdy? "))
    except ValueError:
        print("This is not a number.")
        continue
    try:
        ile_hajsu = float(input("Ile masz zamiar zapłacić? "))
    except ValueError:
        print("This is not a number")
        continue        
    else:
        break
spalanie = (spalanie_max + spalanie_min)/2
cena_paliwa = float(cena_paliwa)
spalanie = float(spalanie)
ile_hajsu = float(ile_hajsu)
litry = (ile_hajsu/cena_paliwa)
x = (100*litry)/spalanie
x = round(x)
as_string = str(x)
ile_hajsu_as_string = str(ile_hajsu)
print("Za cenę " + ile_hajsu_as_string + "zł możesz przejechać około " + as_string + "km")
input()