import plotly.express as px
import pandas as pd

données = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vSC4KusfFzvOsr8WJRgozzsCxrELW4G4PopUkiDbvrrV2lg0S19-zeryp02MC9WYSVBuzGCUtn8ucZW/pub?output=csv')

# Chiffre d'affaire
données["ca"]=données["prix"]*données["qte"]

# Moyenne chiffre d'affaires et volume de ventes par produit
print(données[["produit","ca","qte"]].groupby("produit").mean())

# Médiane chiffre d'affaires et volume de ventes par produit
print(données[["produit","ca","qte"]].groupby("produit").median())

# Ecart-type volume de ventes par produit
print(données[["produit","qte"]].groupby("produit").std())

# Variance volume de ventes par produit
print(données[["produit","qte"]].groupby("produit").var())

# Regroupement des différentes mesures dans le même dataframe
stats = données.groupby("produit").agg(
    ca_moyen=("ca", "mean"),
    ca_median=("ca", "median"),
    volume_moyen=("qte", "mean"),
    volume_median=("qte", "median"),
    volume_ecart_type=("qte", "std"),
    volume_variance=("qte", "var")
)
print(stats)

# Quantité vendue par produit
ventes_produit = données.groupby("produit")["qte"].sum().reset_index()

# CA par produit
ca_produit = données.groupby("produit")["ca"].sum().reset_index()


# Graphe camenbert de la quantité vendue par région
figure = px.pie(données, values='qte', names='region', title='quantité vendue par région')

figure.write_html('ventes-par-region.html')

print('ventes-par-région.html généré avec succès !')


# Graphe en barre du ca par produit

figure = px.bar(
    ca_produit,
    x="produit",
    y="ca",
    title="Chiffre d'affaires par produit",
    text_auto=True
)
figure.write_html("ca-par-produit.html")


# Graphe en barre du nombre de ventes par produit

figure = px.bar(
    ventes_produit,
    x="produit",
    y="qte",
    title="Ventes par produit",
    text_auto=True
)
figure.write_html("ventes-par-produit.html")