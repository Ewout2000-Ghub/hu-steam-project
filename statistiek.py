def gemiddelde(lst, key = None):
    totaal = 0

    if key: # Als er een key is meegegeven als parameter
        for item in lst: # Loop door de lijst
            totaal += item[key] # Voeg bij het totaal elk item met de benoemde key toe
    else:
        for item in lst:
            totaal += item

    gemiddelde = totaal / len(lst) # Bereken het gemiddelde door het totaal te delen door het aantal items in de lijst

    return gemiddelde # Geef het gemiddelde terug


def modus(lst):
    modus_lijst = {} # Maak een set aan

    for item in lst: # Ga door alle items in lst
        if item in modus_lijst: # Als het item al in de set modus_lijst zit
            modus_lijst[item] += 1 # Voeg dan 1 aan de value toe
        else:
            modus_lijst[item] = 0 # Voeg het item aan de set toe

    meest_voorkomend = None
    for item in modus_lijst.items(): # Ga door alle items in modus_lijst
        if meest_voorkomend is None:
            meest_voorkomend = item
        else:
            if item[1] > meest_voorkomend[1]: # Als de value van het item groter is dan de voorgaande opgeslagen value
                meest_voorkomend = item # Zet dan het nieuwe item als meest_voorkomend

    return meest_voorkomend[0]


def mediaan(lst):
    return len(lst) // 2 + 1 # Lengte van de lijst delen door 2, de floor ervan + 1