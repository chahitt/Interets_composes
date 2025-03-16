'''
Ce programme permet de calculer le nombre d'années nécessaires pour 
utiliser un capital en fonction d'un prélèvement mensuel constant
et d'un prélèvement unique pendant la durée de l'opération 
Dans le cas présent : capital de départ = 400.000taux d'intérêt = 2 % prélèvement mensuel = 1.200 et prélèvement après 3 ans et demi = 25.000
'''
def format_number(number):
     # Formatage des nombres avec une virgule pour séparer les milliers et un point pour séparer les décimales = configuration anglo saxonne dans ce cas 2 décimales
    formatted_number = "{:,.2f}".format(number)
    # Remlacement du point par la virgule et de la virgule par le point 
    formatted_number = formatted_number.replace(",", "X").replace(".", ",").replace("X", ".")
    return formatted_number

cap_dep = 400000
taux_ann = 0.02
prel_mens = 1200
annees = 0
interet_total= 0
retrait_partiel = 25000

while cap_dep>0 :
    annees +=1
    for mois in range (1,13):
        if annees == 3 and mois == 6: 
            cap_dep -= retrait_partiel
        cap_dep-=prel_mens
        if cap_dep <= 0 : 
            break
    interets_annuels = cap_dep * taux_ann
    cap_dep += interets_annuels
    interet_total += interets_annuels
    
print(f"Nombre d'années avant épuisement complet du capital : {annees}")
print(f"Intérets totaux accumulés : {interet_total:.2f} euros")

print("========================================================")
print(f"Intérets totaux cumulés : {format_number(round(interet_total, 2))} euros")
print("")
print(f"Nombre d'années avant épuisement complet du capital : {annees}")
print("===============================================================")