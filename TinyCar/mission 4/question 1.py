noms_accessoires = ["Banane", "Abricot", "Pêche", "Fraise", "Framboise"]

prix_ht_accessoires = [1, 2, 3, 1, 2]

for i in range(len(noms_accessoires)):
    nom = noms_accessoires[i]
    prix_ht = prix_ht_accessoires[i]
    print(f"Nom de l'accessoire : {nom}, Prix HT : {prix_ht} €")