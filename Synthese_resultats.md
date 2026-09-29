# Synthèse des résultats – Analyse des ventes

## 1. Analyse SQL

Les requêtes SQL sont disponibles dans le fichier `requetes_ventes.sql`

### a. Chiffre d'affaire total

Requête :

```sql
-- Chiffre d'affaire total
SELECT sum(prix*qte) as chiffre_affaire FROM ventes;
```

Le chiffre d'affaire de la PME est de 44 825€

### b. Ventes par produit

Requête :
```sql
-- Chiffre d'affaire et vente par produit
select produit, sum(prix*qte) as ca, sum(qte) as quantite_vendue from ventes
group by produit;

```
| Produit | CA (€) | Quantité vendue |
|---------|-------:|----------------:|
| **Produit A** | 17 500 | 1 750 |
| **Produit B** | 15 825 | 1 055 |
| **Produit C** | 11 500 |   575 |

Le produit le moins vendu et avec le plus petit CA est le produit C. 
Le produit le plus vendu et avec le plus gros CA est le produit A.


### c. Ventes par région

```sql
-- Chiffre d'affaire et vente par région
select region, sum(prix*qte) as ca, sum(qte) as quantite_vendue from ventes
group by region;
```

| Région | CA (€) | Quantité vendue |
|--------|-------:|----------------:|
| **Sud** | 24 100 | 1 775 |
| **Nord** | 20 725 | 1 605 |

Le CA de la région Sud est plus élevé que celui de la région nord, c'est également dans le Sud que la plus grande quantité de produit a été vendue.

## 2. Exploration du jeu de données avec Pandas

Tableau récapitulatif consolidé (valeurs arrondies à 2 décimales) :

| Produit | CA moyen (€) | CA médian (€) | Volume moyen | Volume médian | Écart-type volume | Variance volume |
|---------|-------------:|--------------:|-------------:|--------------:|------------------:|----------------:|
| **Produit A** | 1 250,00 | 1 225,0 | 125,00 | 122,5 | 38,08 | 1 450,00 |
| **Produit B** | 1 217,31 | 1 200,0 |  81,15 |  80,0 | 21,23 |  450,64 |
| **Produit C** |   958,33 |   900,0 |  47,92 |  45,0 | 17,90 |  320,27 |


- **Chiffre d'affaires** : le **Produit A** est en tête (CA moyen = 1 250 €), suivi de près par le **Produit B** (≈ 1 217 €). Le **Produit C** est en retrait (≈ 958 €).
- **Volume** : le **Produit A** est également en tête avec 125 unités en moyenne devant le produit B (81 unités en moyenne) et le produit C (48 unités en moyenne)
- La moyenne est supérieure à la médiane pour tous les produits, le prix étant fixe, des transactions à fort volume tirent la moyenne vers le haut.

Pour la dispersion des volumes on a :

| Produit | Écart-type | Coefficient de variation | Régularité des ventes |
|---------|-----------:|--------------------------:|-----------------------|
| Produit A | 38,08 | ≈ 30,5 % | Moyenne |
| Produit B | 21,23 | ≈ 26,2 % | **La plus régulière** |
| Produit C | 17,90 | ≈ 37,3 % | **La plus variable** (en relatif) |

NB: coefficient de variation : Ecart-type / Moyenne

Bien que l'écart type du **Produit C** soit le plus faible, si on prend en compte la moyenne respective du volume pour les produits, on se rend compte que c'est le **Produit B** qui a les ventes les plus stables et le **Produit C** qui a les ventes les plus variables.

## 3. Produit le plus et le moins vendu (python natif)

Volume total d'unités vendues par produit :

| Produit | Unités vendues |
|---------|---------------:|
| **Produit A** | **1 750** |
| Produit B | 1 055 |
| **Produit C** | **575** |

- Le produit le plus vendu est le **Produit A** 1 750 unités.
- Le produit le moins vendu est le **Produit C** 575 unités.
- Le Produit A représente à lui seul plus de la moitié du volume total tandis que le Produit C en représente moins de 20%.

## 4. Conclusions

- Le CA total est de 44 825 € pour 3 380 unités vendues, réparties sur 3 produits et 2 régions.
- Le produit A est le plus vendu : il représente environ 52 % des unités vendues et 39 % du chiffre d'affaires.
- Le produit B réalise également de bonnes ventes : il représente environ 35 % du CA et ses ventes sont les plus régulières.
- Le produit C est celui qui se vend le moins : il représente environ 26 % du CA et ses ventes relatives sont aussi les plus variables
- La région Sud réalise davantage de ventes que le Nord : son CA est supérieur d'environ 16 % et son volume de ventes de 11 %. 