taille = int(input("Entrez le nombre d'accessoires : "))

noms_accessoires = []
prix_ht_accessoires = []

for i in range(taille):
    nom = input(f"Entrez le nom de l'accessoire {i + 1} : ")
    prix = int(input(f"Entrez le prix HT de {nom} : "))
    noms_accessoires.append(nom)
    prix_ht_accessoires.append(prix)

print("Noms et prix HT des accessoires :")
total = 0
prix_min = int("inf")
accessoire_min = ""
prix_max = int("-inf")
accessoire_max = ""

for i in range(len(noms_accessoires)):
    nom = noms_accessoires[i]
    prix_ht = prix_ht_accessoires[i]
    total += prix_ht
    print(f"Nom de l'accessoire : {nom}, Prix HT : {prix_ht} €")

    if prix_ht < prix_min:
        prix_min = prix_ht
        accessoire_min = nom

        if prix_ht > prix_max:
        prix_max = prix_ht
        accessoire_max = nom

print(f"Somme totale des achats : {total} €")

print(f"Accessoire au prix maximum : {accessoire_max} ({prix_max} €)")

prix_moyen = total / taille
print(f"Prix moyen : {prix_moyen} €")