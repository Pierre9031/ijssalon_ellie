def decoreer(tekst=""):
    lengte=len(tekst) + 4
    print()
    print(lengte * "*")
    print(f"* {tekst} *")
    print()
    
def fooi_pp(b, p):
    try:
        bedrag_pp=b/p
    except:
        bedrag_pp="??"
        
    return f"Het bedrag per persoon is {bedrag_pp} EUR"

b= int(input("Welk bedrag zit er in de pot?"))
p= int(input ("Over hoeveel mensen moet de pot worden verdeeld?"))

print(fooi_pp(b,p))

    
