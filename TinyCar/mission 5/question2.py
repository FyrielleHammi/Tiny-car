def calculer_prix_ttc(prix_ht):
    tva = 0.2  # Taux de TVA à 20%
    prix_ttc = prix_ht * 1.2
    return prix_ttc

noms_accessoires = ["Banane", "Abricot", "Pêche", "Fraise", "Framboise"]
prix_ht_accessoires = [1, 2, 3, 1, 2]

prix_ttc_accessoires = [1, 2, 3, 1, 2]

for i in range(len(prix_ht_accessoires)):
    prix_ttc = calculer_prix_ttc(prix_ht_accessoires[i])
    prix_ttc_accessoires[i]=prix_ttc

for index in range(len(noms_accessoires)):
    print( noms_accessoires[index])
    print( prix_ht_accessoires[index])
    print( prix_ttc_accessoires[index])
