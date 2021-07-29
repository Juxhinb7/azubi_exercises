menue = {
    "fleischgerichte": [
        {'Saltimboca': 18.60},
        {'Supreme vom Maishähnchen': 15.90}
    ],
    "Fischgerichte": [
        {'`Spezialität vom bodensee` Rotaugenfilletin Ei-mantel gebraten mit würziger Tomatensoße': 16.60},
        {'Felchenfillet gedünstet mit Mandelbuttter': 17.90},
        {'Gebratene lachstranche mit Dill-Rieslingsoße': 17.90},
    ],
    "Vegetarisches fürs Buffet": [
        {'Piccata von der yucchini an pikanter Tomatensoße': 10.90},
        {'Portion Tettnanger Stangenspargel (je nach Saison)': 18.90},
        {'Hausgemachte Terrine von ausgesuchten Gemüssen Riesling-Ingwersoße': 11.60},
        {'Rote Paprikaschote mit mediterranem Gemüse gefüllt und mit Schafskäse überbacken': 11.90},
        {'Linguine - Feine Bandnudeln mit Spinat, Champignons und Schafskässe, verfeinert mit Ingwer': 12.30}
    ]
}


for kategorie, foods in menue.items():
    print("\t\t\t----" + kategorie + "----")
    for food in foods:
        print(str(food).replace("{", "").replace("}", "").replace("'", ""))
    print("\n")

bestellt = []

while True:
    wahl = ""
    try:
        wahl = input("Wählen Sie:")
        bestellt.append(wahl)
    except ValueError:
        print("Fehler")
    if wahl == "exit":
        break


preisen = []
for bestelltes_essen in bestellt:
    for categorie in menue.values():
        for item in categorie:
            for menue_essen, preis in item.items():
                if bestelltes_essen == menue_essen:
                    preisen.append(preis)


for e, z in zip(bestellt, preisen):
    print(e, z)

print("Summe:", sum(preisen))
