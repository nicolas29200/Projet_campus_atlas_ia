import csv



fichier_csv = 'ventes.csv'
volume_produit = {}

with open(fichier_csv, newline='', encoding='utf-8') as f:
    
    # Lecture du fichier CSV
    données = csv.DictReader(f, delimiter=',', quotechar='"')

    # Parcours des lignes du csv
    for ligne in données:
        
        produit = ligne["produit"]
        qte = int(ligne["qte"])

        #Initialise le produit avec une quantité 0 dans le dictionnaire
        if produit not in volume_produit:
            volume_produit[produit] = 0
            
        # Ajout du volume de chaque ligne au produit correspondant
        volume_produit[produit] += qte

# Affichage des ventes par produit
print(volume_produit)

# Produit le plus vendu
produit_plus_vendu = max(volume_produit, key=volume_produit.get)
# Produit le moins vendu
produit_moins_vendu = min(volume_produit, key=volume_produit.get)

print("Produit le plus vendu :", produit_plus_vendu,
      "-", volume_produit[produit_plus_vendu], "unités")

print("Produit le moins vendu :", produit_moins_vendu,
      "-", volume_produit[produit_moins_vendu], "unités")
