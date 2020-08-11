def indice_valide(plateau,indice):
	if indice>=0 and indice<plateau["n"]:
		return True
	return False



def case_valide(plateau,i,j):
    if indice_valide(plateau,i) and indice_valide(plateau,j):
        return True
    return False


def get_case(plateau,i,j):
    #print("get case i "+str(i))
    #print("get case j "+str(j))
    assert case_valide(plateau,i,j)
    a=(plateau["n"]*i)
    return plateau["cases"][a+j]


def set_case(plateau,i,j,val):
    #print(plateau)
    #print(i)
    #print(j)
    assert(case_valide(plateau,i,j))
    assert(val==0 or val==1 or val==2)
    a=plateau["n"]*i
    #print(a)
    plateau["cases"][int(a+j)]=val
    return plateau



def creer_plateau(n):
    assert(n==4 or n==6 or n==8)
    cases=[]
    i=0
    while i<(n**2):
        cases.append(0)
        i+=1
    plateau={"n":n,"cases":cases}
    set_case(plateau,(n/2)-1,(n/2)-1,2)
    set_case(plateau,(n/2)-1,(n/2),1)
    set_case(plateau,(n/2),(n/2)-1,1)
    set_case(plateau,(n/2),(n/2),2)
    #print(plateau)
    return plateau



def ligne(n):
    e="*"
    t=0
    q=" "
    while t<n+1:
        q+=e+"       "
        t+=1
    print(q)



def ligne2(plateau,n,k):
    e="*"
    l=0
    q=" "
    while l<n:
        if plateau["cases"][k]==0:
            az=" "
        elif plateau["cases"][k]==1:
            az="N"
        elif plateau["cases"][k]==2:
            az="B"
        else:
            az="erreur"
        q+=e+"   "+az+"   "
        k+=1
        l+=1
    q+=e
    print(q)



def afficher_plateau(plateau):
    e="*"
    i=0
    k=0
    while i<plateau["n"]:
        print((e*8)*plateau["n"])
        j=1
        while j<=3:
            if j==2:
                ligne2(plateau,plateau["n"],k)
            else:
                ligne(plateau["n"])
            j+=1
        k+=plateau["n"]
        i+=1
    print(((e*8)*plateau["n"]))



def test_indice_valide():
    p=creer_plateau(4)
    assert indice_valide(p,0)# doit retourner True car 0 est valide
    assert indice_valide(p,3)# doit retourner True car 3 est valide
    assert not indice_valide(p,-1)# doit retourner False car -1 n'est pas valide
    assert not indice_valide(p,4)# doit retourner False car 4 n'est pas valide
    p= creer_plateau(6)
    assert  indice_valide(p,4)# doit retourner True car on a maintenant 6 cases
    assert  indice_valide(p,5)# doit retourner True car on a maintenant 6 cases
    assert not indice_valide(p,6)# doit retourner False indices de 0 à 5



def test_case_valide():
    p=creer_plateau(4)
    assert case_valide(p,0,2)
    assert not case_valide(p,5,1)
    p= creer_plateau(8)
    assert  case_valide(p,3,3)
    assert not case_valide(p,18,3)




def test_get_case():
    p=creer_plateau(4)
    assert get_case(p,0,0)==0
    assert get_case(p,1,1)==2
    assert get_case(p,1,2)==1
    p=creer_plateau(6)
    assert get_case(p,0,0)==0
    assert get_case(p,2,2)==2
    assert get_case(p,2,3)==1



def test_set_case():
    p = creer_plateau(4)
    assert set_case(p,0,0,1)=={"n":4,"cases": [1, 0, 0, 0, 0, 2, 1, 0, 0, 1, 2, 0, 0, 0, 0, 0]}
    p = creer_plateau(4)
    assert set_case(p,1,2,0)=={"n":4,"cases": [0, 0, 0, 0, 0, 2, 0, 0, 0, 1, 2, 0, 0, 0, 0, 0]}
    p=creer_plateau(6)
    #assert not set_case(p,0,1,5)=={"n":6,"cases":[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1, 0, 0, 0, 0, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0,0,0,0]}
    assert set_case(p,1,2,2)=={"n":6,"cases":[0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 2, 1, 0, 0, 0, 0, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0,0,0,0]}



def test_creer_plateau():
    assert creer_plateau(4)=={"n":4,"cases": [0, 0, 0, 0, 0, 2, 1, 0, 0, 1, 2, 0, 0, 0, 0, 0]}
    assert creer_plateau(6)=={"n":6,"cases":[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1, 0, 0, 0, 0, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0,0,0,0]}


#########################################################################################################################################
#########################################################################################################################################
#########################################################################################################################################




def pion_adverse(joueur):
    assert(joueur==1) or (joueur==2)
    if joueur==1:
        return 2
    return 1




def prise_possible_direction(plateau,i,j,vertical,horizontal,joueur):


    k=i+vertical             #k c'est la ligne de la case juste après la case choisit, dans la direction donné
    l=j+horizontal           #l c'est la colonne de la case juste après la case chosit, dans la direction donné
    #print("k "+str(k))
    #print("l"+str(l))
    if not case_valide(plateau,k,l):
        return False

    t=0                                     #on initialise un "t" qui va compter le nombre de cases qui sont compris entre deux case avec les memes valeurs
    while (get_case(plateau,k,l)!=joueur) :  #tant que je n'arriva pas a une case de la meme valeur que la mienne


        #if k<=0 or l<=0 or (k>=(plateau["n"])) or (l>=(plateau["n"])):      # si en cherchant une autre case avec la meme valeur que la mienne dans la direction donnée et que je sort du plateau alors                                                # cette direction n'est pas possible donc la fonction renvoie False

        if (get_case(plateau,k,l)==0):                                      # si en cherchant une autre case avec la meme valeur que la mienne dans la direction donnée et que je tombe
            return False                                                    # sur un 0 alors la fonction affiche false

        t=t+1                                                               #Pendant ma recherche j'incrémente le t qui va compter le nombre de case que je vais manger
        k=k+vertical                            #je change de case verticalement
        l=l+horizontal                      #je change de case horizontalement
##        print("k"+str(k))
##        print("l"+str(L))
        #if k<=0 or l<=0 or (k>=(plateau["n"])) or (l>=(plateau["n"])):  #si la case juste après n'est pas une case valide alors la fonction retourne false
        if not case_valide(plateau,k,l):
            return False
    if t>0:
        return True                                                         # si j'attérit à une autre case avec la meme valeur que la mienne sans sortir du plateau et sans avoir de 0 entre
    else:                                                                   # et que je mange au moins une case alors la fonction renvoie True sinon elle renvoie False
        return False






def mouvement_valide(plateau,i,j,joueur):
    a=1
    b=0
    c=-1
##
##    if get_case(plateau,i,j)==0:                                           # pour que ça soit un mouvement valide il faut deja que la case ou je pose mon pion soit

    if prise_possible_direction(plateau,i,j,c,c,joueur):               # une case "vide"
            #print("1")
        return True                                                    #on teste avec les 8 directions possible si au moins une fonctionne alors
    if prise_possible_direction(plateau,i,j,c,b,joueur):               #la fonction renverra True
            #print("2")
        return True
    if prise_possible_direction(plateau,i,j,a,c,joueur):
            #print("3")
        return True
    if prise_possible_direction(plateau,i,j,b,c,joueur):
            #print("4")
        return True
    if prise_possible_direction(plateau,i,j,b,a,joueur):
            #print("5")
        return True
    if prise_possible_direction(plateau,i,j,c,a,joueur):
            #print("6")
        return True
    if prise_possible_direction(plateau,i,j,a,b,joueur):
            #print("7")
        return True
    if prise_possible_direction(plateau,i,j,a,a,joueur):
            #print("8")
        return True

    return False                                                # si aucune de ces directions n'a fonctionner alors la fonction renvoir False






def mouvement_direction(plateau,i,j,vertical,horizontal,joueur):

    if mouvement_valide(plateau,i,j,joueur):                #si le mouvement est valide alors on place a la case donné le numero du joueur et
        set_case(plateau,i,j,joueur)

        k=i+vertical
        l=j+horizontal

        while get_case(plateau,k,l)!=joueur:               #et a chaque case que l'on aura "mange" on mets la valeur du joueur
##            val1=get_case(plateau,k,l)
##            val2=pion_adverse(val1)
            set_case(plateau,k,l,joueur)

            k=k+vertical
            l=l+horizontal
                                                           #on fait cela pour toute les cases jusqu'à tombé à la case dans lequel il y aura notre numéro

        return plateau
    return plateau






def mouvement(plateau,i,j,joueur):

    if prise_possible_direction(plateau,i,j,-1,-1,joueur):       # si la prise_possible_direction est possible pour un sens donné alors le plateau va changé

        mouvement_direction(plateau,i,j,-1,-1,joueur)            # et ce changement ce fait pour tout les sens ou c'est possible

    if prise_possible_direction(plateau,i,j,-1,0,joueur):

        mouvement_direction(plateau,i,j,-1,0,joueur)

    if prise_possible_direction(plateau,i,j,1,-1,joueur):

        mouvement_direction(plateau,i,j,1,-1,joueur)

    if prise_possible_direction(plateau,i,j,0,-1,joueur):

        mouvement_direction(plateau,i,j,0,-1,joueur)

    if prise_possible_direction(plateau,i,j,0,1,joueur):

        mouvement_direction(plateau,i,j,0,1,joueur)

    if prise_possible_direction(plateau,i,j,-1,1,joueur):

        mouvement_direction(plateau,i,j,-1,1,joueur)

    if prise_possible_direction(plateau,i,j,1,0,joueur):

        mouvement_direction(plateau,i,j,1,0,joueur)

    if prise_possible_direction(plateau,i,j,1,1,joueur):

        mouvement_direction(plateau,i,j,1,1,joueur)


    return plateau





def joueur_peut_jouer(plateau,joueur):
    i=0                                                 #on initialise un i qui va faire changé les lignes
    while i<plateau["n"]:                               #on fait tout cela pour parcourir toutes les cases du tableau #on va parcourir toutes les lignes

        j=0                                             # et toutes les colonnes
        while j<plateau["n"]:
            #print("i "+str(i))
            #print("j "+str(j))

            if mouvement_valide(plateau,i,j,joueur):            # si pour un couple (i,j) donc une case le mouvement est possible alors la fonction renverra True
                return True

            j=j+1


        i=i+1
    return False                                            # si en parcourant toutes les cases aucune ne permet de faire un mouvement alors la fonction renverra False






def fin_de_partie(plateau):

    if joueur_peut_jouer(plateau,1) or joueur_peut_jouer(plateau,2):     #si l'un des deux joueurs peut jouer alors la fonction renverra False

        return False ##ou 0

    return True                                                             #si aucun des deux peut jouer alors la fonction renverra True donc que la partie est fini






def gagnant(plateau):
    somme1=0                                                   # on crée une variable qui va compter le nombre de 1 dans le plateau
    somme2=0                                                    # on creé une  variable qui va compter le nombre de 2 dans le plateau

    i=0                                                         #le i va nous permettre de parcourir le tableau du dico plateau
    while i<len(plateau["cases"]):                              #tant que je ne parcours pas tout le tableau

        if plateau["cases"][i]==1:                              #si il y a un 1 alors la variable qui compte le nombre de 1 s'incrémente
            somme1+=1

        if plateau["cases"][i]==2:                              #de meme pour 2
            somme2+=1

        i=i+1

    if somme1<somme2:                                         #s'il y a plus de 2 que de 1 alors la fonction retournera 2
        return 2
    elif somme2<somme1:                                         # s'il y a plus de 1 que de 2 alors la fonction retournera 1
        return 1
    else:                                                       # si il n'y a pas plus de 1 que de 2 ni plus de 2 que de 1 alors il y a autant de 1 que de 2
        return 0                                                # donc la fonction reverra 0 pour dire "égalité"






#question 8
##p=creer_plateau(4)
##w=prise_possible_direction(p,1,3,0,-1,2)
##print(w)
##s=prise_possible_direction(p,1,3,0,-1,1)
##print(s)
##o=prise_possible_direction(p,1,3,-1,-1,2)
##print(o)
##t=prise_possible_direction(p,1,0,0,1,1)
##print(t)


#QUESTION 9
##p=creer_plateau(4)
##w=mouvement_valide(p,1,3,2)
##print(w)

#question 10
##p=creer_plateau(4)
##print(p)
##w=mouvement_direction(p,0,3,-1,1,2)
##print(w)
##p=creer_plateau(4)
##print(p)
##w=mouvement_direction(p,1,3,0,-1,2)
##print(w)

#QUESTION 11
##p=creer_plateau(4)
##print(p)
##mouvement(p,1,3,2)
##print(p)

#QUESTION12
##p=creer_plateau(4)
##w=joueur_peut_jouer(p,1)
##print(w)
##set_case(p,1,1,1)
##set_case(p,2,2,1)
##w=joueur_peut_jouer(p,1)
##print(w)

#question 13
##p=creer_plateau(4)
##w=fin_de_partie(p)
##print(w)
##set_case(p,1,1,1)
##set_case(p,2,2,1)
##w=fin_de_partie(p)
##print(w)

#question14
##p=creer_plateau(4)
##set_case(p,1,1,1)
##set_case(p,2,2,1)
##w=gagnant(p)
##print(w)



def test_pion_adverse():
    assert pion_adverse(1)==2
    assert pion_adverse(2)==1





def test_prise_possible_direction():
    p=creer_plateau(4)
    assert prise_possible_direction(p,1,3,0,-1,2)
    assert not prise_possible_direction(p,1,3,0,-1,1)
    p=creer_plateau(6)
    assert prise_possible_direction(p,4,3,-1,0,1)
    assert not prise_possible_direction(p,4,3,-1,0,2)





def test_mouvement_valide():
    p=creer_plateau(4)
    assert mouvement_valide(p,1,3,2)
    assert not mouvement_valide(p,0,0,1)
    p=creer_plateau(6)
    assert not mouvement_valide(p,1,1,1)
    assert mouvement_valide(p,3,1,2)




def test_mouvement_direction():
    p=creer_plateau(4)
    assert mouvement_direction(p,0,3,-1,1,2)=={'cases': [0, 0, 0, 0, 0, 2, 1, 0, 0, 1, 2, 0, 0, 0, 0, 0], 'n': 4}
    assert mouvement_direction(p,1,3,0,-1,2)=={'n': 4,'cases': [0, 0, 0, 0, 0, 2, 2, 2, 0, 1, 2, 0, 0, 0, 0, 0]}
    p=creer_plateau(6)
    assert mouvement_direction(p,0,0,1,1,1)=={"n":6,"cases":[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1, 0, 0, 0, 0, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0,0,0,0]}
    assert mouvement_direction(p,2,1,0,1,1)=={"n":6,"cases":[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0,0,0,0]}



def test_mouvement():
    p=creer_plateau(4)
    assert mouvement(p,1,3,2)=={'n': 4, 'cases': [0, 0, 0, 0, 0, 2, 2, 2, 0, 1, 2, 0, 0, 0, 0, 0]}
    p=creer_plateau(4)
    assert mouvement(p,0,3,2)=={'n': 4, 'cases': [0, 0, 0, 0, 0, 2, 1, 0, 0, 1, 2, 0, 0, 0, 0, 0]}
    p=creer_plateau(6)
    assert mouvement(p,1,2,1)=={"n":6,"cases":[0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0,0,0,0]}
    p=creer_plateau(6)
    assert mouvement(p,0,0,1)=={"n":6,"cases":[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1, 0, 0, 0, 0, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0,0,0,0]}




def test_joueur_peut_jouer():
    p=creer_plateau(4)
    assert joueur_peut_jouer(p,2)
    set_case(p,1,1,1)
    set_case(p,2,2,1)
    assert not joueur_peut_jouer(p,2)
    p=creer_plateau(6)
    assert joueur_peut_jouer(p,1)
    set_case(p,2,3,2)
    set_case(p,3,2,2)
    assert not joueur_peut_jouer(p,1)





def test_fin_de_partie():
    p=creer_plateau(4)
    assert not fin_de_partie(p)
    set_case(p,1,1,1)
    set_case(p,2,2,1)
    assert fin_de_partie(p)
    p=creer_plateau(6)
    assert not fin_de_partie(p)
    set_case(p,2,3,2)
    set_case(p,3,2,2)
    #print(p)
    assert fin_de_partie(p)




def test_gagnant():
    p=creer_plateau(4)
    assert not gagnant(p)
    set_case(p,1,1,1)
    set_case(p,2,2,1)
    assert gagnant(p)
    p=creer_plateau(8)
    assert not gagnant(p)
    set_case(p,3,3,1)
    set_case(p,4,4,1)                          # Normalement quand il n'y a que des 1 dans le plateau tu ni place de 1 n'y placé de 2 parce que pour pouvoir les placé
    assert gagnant(p)                          #il faut deja qu'il puisse manger au moins une case


##test_pion_adverse()
##test_prise_possible_direction()
##test_mouvement_valide()
##test_mouvement_direction()
##test_mouvement()
##test_joueur_peut_jouer()
##test_fin_de_partie()
##test_gagnant()

#question 15
##w=creer_partie(6)
##print(w)

#question 16
##p={"joueur":1,"plateau":creer_plateau(4)}
##print(saisie_valide(p, "M"))  # retourne True
##print(saisie_valide(p, "b1")) # retourne True
##print(saisie_valide(p, "b4")) # return False
##partie={"joueur":1,"plateau":creer_plateau(4)}
##w=saisie_valide(partie,"b")
##print(w)
#question17
##p=creer_partie(4)
##tour_jeu(p)
##print(p)

#QUESTION18
##n=saisir_action(None)
##print(n)

from os import system
import os
import json




def creer_partie(n):
    assert(n==4 or n==6 or n==8)                                       #SI LA TAILLE N'EST NI DE 4 NI DE 6 NI DE 8 LA FONCTION LEVE UNE ERREUR
    partie={"joueur":1,"plateau":creer_plateau(n)}                     #CREER LE DICO PARTIE
    return partie


def saisie_valide(partie,s):
    if s=="M":                       # SI LE "s" est égale à M alors la fonction renvoie True
        return True
    l=["a","b","c","d","e","f","g","h"] # un tableau avec toutes les lettres possible aux max
    c=[1,2,3,4,5,6,7,8]                 # un tableau avec tous les chiffres possible aux max
    lignes=[]                             #on fait des tableaux vide
    colonnes=[]
    i=0
##    print(s[0])
##    print(s[1])
    while i<partie["plateau"]["n"]:      #temps que l'on atteint pas la taille du plateau
        lignes.append(l[i])              # on complete les tableaux lignes et colonnes avec les lettres autorisé en fonction du tableau
        colonnes.append(c[i])
        i=i+1
    if ord(s[0])<=ord(lignes[len(lignes)-1]) and ord(s[0])>=ord(lignes[0])and ord(str(s[1]))>=ord(str(colonnes[0])) and ord(str(s[1]))<=ord(str(colonnes[len(colonnes)-1])):
        a=0
        while s[0]!=lignes[a]:        #si la lettre et les chiffres donnés en parametre est dans le code ascii entre les min et les max du tableau alors
            a=a+1                       #on transforme la lettre en chiffre
##        print(a)

        if mouvement_valide(partie["plateau"],a,int(s[1])-1,partie["joueur"]): # et si cette case et une case valide alors la fonction retourne true
            return True

    return False



def effacer_terminal():
    system('cls')

def tour_jeu(partie):
    effacer_terminal()
    afficher_plateau(partie["plateau"])

    if joueur_peut_jouer(partie["plateau"],partie["joueur"]):

        s=input("saisie un mouvement")
        while not saisie_valide(partie,s):          #TANT QUE LA SAISIE N4EST PAS BONNE ON REDEMMANDE
            s=input("saisie un mouvement")
        if s=="M":                                  # SI C4EST "M"  ON RETOURNE FALSE
            return False
        else:
            l=["a","b","c","d","e","f","g","h"]
            c=[1,2,3,4,5,6,7,8]
            lignes=[]
            colonnes=[]
            i=0

            while i<partie["plateau"]["n"]:
                lignes.append(l[i])
                colonnes.append(c[i])
                i=i+1
##            print(lignes)
##            print(colonnes)
            a=0
            t=0
            while s[0]!=lignes[t]:                   #PAREIL QUE LA FONCTION PRECEDENTE
                a=a+1
                t=t+1
            i=a
            j=int(s[1])-1
            mouvement(partie["plateau"],i,j,partie["joueur"]) #LA ON FAIT LE MOUVEMENT

        return True


def saisir_action(partie):
    print("Quelle action souhaitez-vous réaliser ?")
    choix=int(input())
    if partie is None:                               #SI IL N'Y A PAS DE PARTIE ALORS LES CHOIX SONT COMPRIS ENTRE 0 ET 2 INCLUS
        while choix<0 or choix>2:
            print("Quelle action souhaitez-vous réaliser ?")

            choix=int(input())
        return choix
    else:

        while choix<0 or choix>4:         #SI IL Y UNE PARTIE ALORS LES CHOIX SONT COMPRIS ENTRE 0 ET 4 INCLUS
            print("Quelle action souhaitez-vous réaliser ?")
            choix=int(input())
        return choix





def jouer(partie):
    print("joueur 1 joue")
##    tour_jeu(partie)
    while not fin_de_partie(partie["plateau"]):   #TANT QUE C'est possible de jouer

        a=tour_jeu(partie)                                    #on joue
        partie["joueur"]=pion_adverse(partie["joueur"])       #le joueur change
        print("joueur"+str(partie["joueur"])+"joue")
##        print(partie)
##        tour_jeu(partie)
        if not a:                                                 #si un des deux joueur appui sur M pendant le jeu ( avant que ca ce finnisse)
            return False                                          #la fonction retourne false


    tour_jeu(partie)                         # pour poser le dernier pion
    return True


def saisir_taille_plateau():
    a=int(input("Saisie un nombre entre 4,6 et 8"))           #on saisie la taille du plateau
    while a!=4 and a!=6 and a!=8:                           # tant qu'il n 'est ni egale à 4 ni à 6 ni à 8 on redemande
        a=int(input("Saisie un nombre entre 4,6 et 8"))

    return a

def sauvegarder_partie(partie):
    with open('sauvegarde_partie.json','w') as fp:          #comme write
        json.dump(partie,fp)                                    #trouver sur internet




def charger_partie():
    if os.path.exists("sauvegarde_partie.json"):
        with open('sauvegarde_partie.json','r') as fp:
            partie=json.load(fp)                              #trouver sur internet
        b=creer_partie(partie["plateau"]["n"])

    else:
        a=saisir_taille_plateau()
        b=creer_partie(a)



    return b






##def othello():
##	PERMET DE JOUER A OTHELLO
##	ON PEUT SAUVEGARDER UNE PARTIE
##	CONTINUER UNE PARTIE
##	CHARGER UNE NOUVELLE PARTIE
##	QUITTER LA PARTIE




def othello():
	p=creer_partie(saisir_taille_plateau())
	if not jouer(charger_partie()):
		if saisir_action(partie)or saisir_action(None)==0:
			return
		if saisir_action(partie)or saisir_action(None)==1:
			charger_partie()
			jouer()
		if saisir_action(partie)or saisir_action(None)==2:
			charger_partie()
			jouer()
		if saisir_action(partie)==3:
			sauvegarde_partie(partie)
			jouer()
		if saisir_action(partie)==4:
			jouer()






def test_creer_partie():
    assert creer_partie(4)=={'plateau': {'cases': [0, 0, 0, 0, 0, 2, 1, 0, 0, 1, 2, 0, 0, 0, 0, 0], 'n': 4}, 'joueur': 1}
    assert creer_partie(6)=={'plateau': {'cases': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1, 0, 0, 0, 0, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 'n': 6}, 'joueur': 1}


def test_saisie_valide():
    partie=creer_partie(4)
    assert saisie_valide(partie,"M")  # ECRIRE M #SI LE JOUEUR ECRIT M LA SAISIE EST BONNE
    assert saisie_valide(partie,"b1") # ECRIRE b1 #SI LE JOEUR ECRIT
    assert not saisie_valide(partie,"a1")  #ECRIRE a1
    partie=creer_partie(6)
    assert saisie_valide(partie,"M")   #ECRIRE M
    assert saisie_valide(partie,"c2")   #ECRIRE c2
    assert not saisie_valide(partie,"f1")  #ECRIRE f1

def test_tour_jeu():

    p=creer_partie(6)
    assert not tour_jeu(p)=={'plateau': {'cases': [0, 0, 0, 0, 0, 2, 1, 0, 0, 1, 2, 0, 0, 0, 0, 0], 'n': 4}, 'joueur': 1} #LE JOUEUR 1 N'A PAS ENCORE JOUER
    set_case(p["plateau"],2,1,1)  #LE JOUEUR 1 JOUE
    assert tour_jeu(p)          #TOUR JEU RENVOIE TRUE
    p=creer_partie(4)
    assert not tour_jeu(p)
    set_case(p["partie"],1,0,1) #PAREIL
    assert tour_jeu(p)

def test_saisir_action():

    assert saisir_action(None)==0            #ECRIRE 0          #SI IL N4 Y AUCUNE PARTIE ON PEUT ECRIRE 0
    assert not saisir_action(None)==3           #ECRIRE 3      SI IL N Y AUCUNE PARTIE ON NE PEUT PAS ECRIRE 3
    p=creer_partie(4)
    assert saisir_action(p)==2
    assert not saisir_action(p)==5

def test_jouer():
##    partie=creer_partie(4)
##    assert not jouer(partie)
##    partie["plateau"]= {'n': 4, 'cases': [1, 1, 1, 1, 1, 2, 1, 2,2, 1, 2, 2, 1, 2, 1,2 ]}
##    assert jouer(partie)
    partie=creer_partie(6)
    assert not jouer(partie) #TESTE AVEC M
    partie["plateau"]={'cases': [1, 2, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1,1 ,2, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2], 'n': 6}
    assert jouer(partie)    #TESTE AVEC a1 PAR EXEMPLE


def test_saisir_taille_plateau():
    assert saisir_taille_plateau()==4        #ecire 4 4 AFFCIHE TRUE
    assert not saisir_taille_plateau()==10    #ECRIRE 10 SI L'UTILISATEUR ECRIT 10 LA QUESTION EST REPOSE

def partie_existe():
    if os.path.exists("sauvegarde_partie.json"):     #une fonction pour voir si il y a un fichier avec le meme nom qui existe
        return True
    return False

def test_sauvegarder_partie():
    p=creer_partie(4)
    sauvegarder_partie(p)
    assert partie_existe()

def test_charger_partie():
    p=creer_partie(4)
    assert charger_partie()=={'plateau': {'n': 4, 'cases': [0, 0, 0, 0, 0, 2, 1, 0, 0, 1, 2, 0, 0, 0, 0, 0]}, 'joueur': 1}
    sauvegarder_partie(p)
    assert charger_partie()=={'plateau': {'n': 4, 'cases': [0, 0, 0, 0, 0, 2, 1, 0, 0, 1, 2, 0, 0, 0, 0, 0]}, 'joueur': 1}


def othello():
    partie=charger_partie()
    while not jouer(partie):
        if not saisir_action(partie)==0:
            return
        if not saisir_action(partie)==1:
            return (gagnant(partie["plateau"]))
        if not saisir_action(partie)==2:
            charger_partie()
            jouer(partie)
        if not saisir_action(partie)==3:
            sauvegarder_partie(partie)
            jouer(partie)
        if not saisir_action(partie)==4:
            charger_partie()
            jouer(partie)



'''
test_creer_partie()
test_saisie_valide()
test_tour_jeu()
test_saisir_action()
test_jouer()
test_sauvegarder_partie()
test_charger_partie()
'''

othello()
