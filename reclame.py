def aanbieding_1(smaak="aardbei", prijs=4, korting=0.1):
    
    uitvoer = f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak van {smaak}, van {prijs} voor 3,60 euro"
    return uitvoer

print(aanbieding_1())

def inkomsten_totaal():
    mijn_lijst = [220, 430, 125, 160, 205, 90, 345]
    totaal=sum(mijn_lijst)
    btw=0.09
    bedrag=totaal*btw
    return(f"Het totaal van alle inkomsten van deze week is {totaal} euro waarover {bedrag} euro btw betaald dient te worden betaald.")

print (inkomsten_totaal())

def laag_en_hoog():
    mijn_lijst = [220, 430, 125, 160, 205, 90, 345]
    hoogste=max(mijn_lijst)
    laagste=min(mijn_lijst)
    return hoogste, laagste

print(laag_en_hoog())

def gemiddelde ():
    mijn_lijst = [220, 430, 125, 160, 205, 90, 345]
    totaal=sum(mijn_lijst)
    aantal=len(mijn_lijst)
    gemiddelde=totaal/aantal
    return f"De gemiddelde inkomsten deze week zijn {gemiddelde} euro"

print(gemiddelde())

def meervoudig (invoer_lijst):
    invoer_lijst=[10,5,3,2,1,2,9]
    hoogste=max(invoer_lijst)
    laagste=min(invoer_lijst)
    return hoogste, laagste
    
print(meervoudig())

# opgave 12, eerste deel
from algemene_functies import algemene_functies2 

def combinatie(invoer_lijst2):
    
    korte_lijst = laag_en_hoog(invoer_lijst2)
    
    
    