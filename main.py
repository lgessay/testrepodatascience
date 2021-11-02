#afficher nom age
def afficher_info(nom, age, taille=0):
    print()

    print("Vous vous appelez " + nom + ". Vous avez " + str(age) + " ans")
    # print(f"Vous vous appelez {nom}. Vous avez {age} ans")
    print("L'an prochain vous aurez " + str(age + 1) + " ans.")
    # print("L'an prochain vous aurez %s ans." % (age + 1))

    if age == 1 or age == 2:
        print("Vous etes un bebe")
    elif age < 10:
        print("Vous etes enfant")
    elif 12 <= age < 17:
        print("Vous etes adolescent")
    elif age == 17:
        print("Vous etes presque majeur")
    elif age == 18:
        print("Vous etes tout juste majeur")
    elif age >= 60:
        print("Vous etes senior")
    elif age >= 18:
        print("Vous etes majeur")
    else:
        print("Vous etes mineur")

    # afficher taille
    if not taille == 0:
        print("Votre taille : " + str(taille) + " m")

def demander_age(nom_personne):
    age_int = 0
    while age_int == 0:
        age_str = input(nom_personne + ",quel est votre age ?")
        try:
            age_int = int(age_str)
        except ValueError:
            print("ERREUR : vous devez entrer un nombre pour l'age")
    return age_int


def demander_nom():
    nom_str = ""
    while nom_str == "":
        nom_str = input("Quel est ton nom ?")
    return nom_str


"""
#demander nom
nom1 = demander_nom()
nom2 = demander_nom()

#demander age
age1 = demander_age(nom1)
age2 = demander_age(nom2)


#afficher resultat

afficher_info(nom1, age1)
afficher_info(nom2, age2)

# print("ERREUR : vous devez entrer un nombre pour l'age")
"""

NB_PERSONNES = 1

# la boucle for
for i in range(0, NB_PERSONNES):
    nom = "personne" + str(i+1)
    age = demander_age(nom)
    afficher_info(nom, age)

