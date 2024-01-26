def calculer_moyenne(liste):
    somme = sum(liste)
    moyenne = somme / len(liste)
    return moyenne

def trouver_minimal(liste):
    return min(liste)

def trouver_maximal(liste):
    return max(liste)

moyenne_prix_ht = calculer_moyenne(prix_ht_accessoires)
prix_ht_minimal = trouver_minimal(prix_ht_accessoires)
prix_ht_maximal = trouver_maximal(prix_ht_accessoires)

print("Moyenne des prix HT:", moyenne_prix_ht)
print("Prix HT minimal:", prix_ht_minimal)
print("Prix HT maximal:", prix_ht_maximal)