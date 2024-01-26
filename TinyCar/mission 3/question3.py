# Nombre maximum de tentatives autorisées pour le code secret
tentatives_max = 3

for tentative in range(tentatives_max):
    code_secret = input("Entrez le code secret pour accéder à l'application : ")
    if code_secret == "Padawan":
        # Demande du nombre de produits à traiter
        while True:
            try:
                n = int(input("Entrez le nombre de produits à traiter : "))
                break
            except ValueError:
                print("Veuillez entrer un nombre valide.")

        for _ in range(n):
            marque = input("Entrez la marque de la voiture : ")
            modèle = input("Entrez le modèle de la voiture : ")

            prixHT = float(input("Entrez le prix HT de la voiture : "))

            # Demande à l'utilisateur de spécifier s'il a une carte de fidélité
            while True:
                print("Choisissez une option :")
                print("1 - Sans carte de fidélité")
                print("2 - Avec carte gold")
                print("3 - Avec carte platinium")
                
                choix_carte = input("Votre choix : ")

                if choix_carte in ["1", "2", "3"]:
                    break
                else:
                    print("Choix invalide. Veuillez choisir 1, 2 ou 3.")

            # Demande du taux de TVA en fonction de la réponse de l'utilisateur
            if choix_carte == "3":
                tauxTVA = 5  # Carte platinium : TVA à 5%
            else:
                tauxTVA = 20  # Par défaut : TVA à 20%

            # Appliquer des réductions en fonction de la carte de fidélité
            if choix_carte == "2":
                type_produit = input("Le produit est-il électrique ? (Oui/Non) : ").lower()
                if type_produit == "oui":
                    taux_reduction = 30  # Carte gold + produit électrique : 30% de réduction
                else:
                    taux_reduction = 20  # Carte gold : 20% de réduction
            elif choix_carte == "3":
                taux_reduction = 15  # Carte platinium : 15% de réduction
            else:
                taux_reduction = 0  # Sans carte de fidélité : pas de réduction

            prixTTC = prixHT * (1 + (tauxTVA / 100))

            # Appliquer la réduction
            if taux_reduction > 0:
                reduction = prixTTC * (taux_reduction / 100)
                prixTTC -= reduction

            print(f"Le prix total TTC de la voiture {marque} {modèle} est de {prixTTC} euros.")
    else:
        tentatives_restantes = tentatives_max - (tentative + 1)
        if tentatives_restantes > 0:
            print(f"Code secret incorrect. Il vous reste {tentatives_restantes} tentative(s).")
        else:
            print("Nombre maximal de tentatives atteint. Accès refusé.")
            exit()


# Saluer l'utilisateur
print("Merci d'avoir utilisé l'application. Au revoir !")