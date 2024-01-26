def afficher_descriptif_accessoire(nom, prix_ht):
    print("Accessoire:", nom)
    print("PrixHT:", prix_ht)

noms_accessoires = ["Banane", "Abricot", "Pêche", "Fraise", "Framboise"]
prix_ht_accessoires = [1, 2, 3, 1, 2]

for index in range(len(noms_accessoires)):
    afficher_descriptif_accessoire(noms_accessoires[index], prix_ht_accessoires[index])