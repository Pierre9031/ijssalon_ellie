def presenteer(dictionary, totaal):
       
    for k, v in dictionary.items():
        print(f"{k} : {v} euro")
    
    print("==========")
    
    print(f"Totaal: {totaal} EUR")
    
mijn_dictionary = {
        "vis": 10,
        "vlees": 25,
        "overig": 15
    } 

totaal = sum(mijn_dictionary.values())

print(presenteer(mijn_dictionary, totaal))
        



    

