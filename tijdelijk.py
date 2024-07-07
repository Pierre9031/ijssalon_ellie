prijzen = {
    "aardbei" : "3",
    "vanille" : "4",
    "chocolade" : "5"
}
aanbieding = 3 * 0.8
reclame_tekst = (f"Vandaag in de aanbieding: vanille-ijs, 1 liter - slechts € {aanbieding}")
print (reclame_tekst)
reclame_tekst2=reclame_tekst[:62]
print(reclame_tekst2)
print (f"Vandaag in de aanbieding: vanille-ijs, 1 liter - slechts € {aanbieding}".upper())
reclame_tekst3=reclame_tekst2.upper()
print(reclame_tekst3)
list = ["vandaag", "in", "de", "aanbieding", "vanille-ijs", "1", "liter", "-", "slechts", "€", "2.40"]
reclame_tekst4 = list
print(reclame_tekst4[0:11])
for el in reclame_tekst4:
    print(el.lower())
for el in reclame_tekst4:
    if len(el) > 4:
        elup = el[0].upper() + el[1:]
        print(elup)    
    else:
        print (el)

