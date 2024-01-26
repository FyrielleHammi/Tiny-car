def calculer_prix_ttc(prix_ht):
    tva = 0.2 
    prix_ttc = prix_ht * 1.2
    return prix_ttc

def afficher_elements(noms, prix_ht, prix_ttc):
    for index in range(len(noms)):
        print(noms[index])
        print(prix_ht[index])
        print(prix_ttc[index])
        print()

noms_accessoires = ["Banane", "Abricot", "Pêche", "Fraise", "Framboise"]
prix_ht_accessoires = [1, 2, 3, 1, 2]
prix_ttc_accessoires = []

for i in range(len(prix_ht_accessoires)):
    prix_ttc =(prix_ht_accessoires[i])
    prix_ttc_accessoires(prix_ttc)

def afficher_elements(tb):
    for i in range(len(tb)):
        prix_ttc = calculer_prix_ttc(prix_ht_accessoires[i])
        prix_ttc_accessoires.append(prix_ttc)

        
