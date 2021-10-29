#python3.10.0
#-*-coding:Latin-1 -*

"""déterminer si une année est une année bissextile"""

#Demander a l utilisateur de saisir une annee
# on verifie que l Annee saisie est bien un entier
# on verifie que l annee saisie est composee de 4 chiffres
# on verifie si l annee est bissextile

annee_saisie=""
annee_saisie_int=0

while len(annee_saisie) is not 4:

    annee_saisie = input("Veuillez saisir une annee: ")
    annee_saisie_int= int (annee_saisie)

    if len(annee_saisie) is not 4:
        print("L'annee saisie n a pas 4 chiffre")


if annee_saisie_int %4 ==0 :
    print("c'est une annee bissextile")
else:
    if annee_saisie_int%100 == 0 :
        
        if annee_saisie_int%400 ==0:
            print("c'est une annee bissextile")
        else:
            print("c'est une annee bissextile")
    else:
        print("c'est une annee bissextile")

#CONCLUSION:
#PENSER PLUS SIMPLEMENT ET PLUS EFFICACEMENT SOIT REDUIRE AU MIEUX LE NBRE DE 
#LIGNE DE CODE




    



