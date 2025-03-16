'''
Ce programme permet de calculer le nombre d'années nécessaires pour 
utiliser un capital en fonction d'un prélèvement mensuel constant.
Dans le cas présent : 
    * capital de départ = 400.000 (cap_dep)
    * taux d'intérêt = 2 % (taux_ann)
    * prélèvement mensuel = 1.200 (prel_mens)
'''

"""
    fonction pour formater les nombre avec un point pour les séparateurs de milliers et une virgule pour les décimales
"""
def format_number(number):
     # Formatage des nombres avec une virgule pour séparer les milliers et un point pour séparer les décimales = configuration anglo saxonne dans ce cas 2 décimales
    formatted_number = "{:,.2f}".format(number)
    # Remlacement du point par la virgule et de la virgule par le point 
    formatted_number = formatted_number.replace(",", "X").replace(".", ",").replace("X", ".")
    return formatted_number

cap_dep = 400000
taux_ann = 0.030
prel_mens = 1500
annees = 0
interets_total= 0

while cap_dep > 0 :
   
    annees +=1
    for mois in range (1,13):
        cap_dep -= prel_mens
        if cap_dep <= 0 : 
            break
        
    
    interets_annuels = cap_dep * taux_ann
    print(f"Année {annees} les intérêts annuels sont de : {format_number(round(interets_annuels, 2))} euros")
    
    cap_dep += interets_annuels
    
    interets_total += interets_annuels

print("========================================================")
print(f"Intérets totaux cumulés : {format_number(round(interets_total, 2))} euros")
print("")
print(f"Nombre d'années avant épuisement complet du capital : {annees}")
print("===============================================================")