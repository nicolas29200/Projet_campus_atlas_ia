-- Chiffre d'affaire total
SELECT sum(prix*qte) as chiffre_affaire FROM ventes;

-- Chiffre d'affaire et vente par produit
select produit, sum(prix*qte) as ca, sum(qte) as quantite_vendue from ventes
group by produit;

-- Chiffre d'affaire et vente par région
select region, sum(prix*qte) as ca, sum(qte) as quantite_vendue from ventes
group by region;