noms_accessoires = ["Banane", "Abricot", "Pêche", "Fraise", "Framboise"]

prix_ht_accessoires = []

for i in noms_accessoires:
    prix = int(input("Entrez le prix HT de {i} : "))
    prix_ht_accessoires.append(prix)

print("Noms et prix HT des accessoires :")
for i in range(len(noms_accessoires)):
    nom = noms_accessoires[i]
    prix_ht = prix_ht_accessoires[i]
    print("Nom de l'accessoire : {nom}, Prix HT : {prix_ht} €")

    