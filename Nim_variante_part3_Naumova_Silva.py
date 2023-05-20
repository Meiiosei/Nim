from random import randint
from random import choice
import random
from time import sleep 
from Text import *

# Correspond au tant d'attente (peut être modifer)

haut = "0"
bas = "|"

settings = {
    "nbr_bot": 0,
    "Joueur_1": 'Joueur_1',
    "Joueur_2": 'Joueur_2',
    "nb_manche": 1,
    "affichage": True,
    "mode_de_jeu": True,
    "tab": [7, 5, 3, 1],
    "vitesse" : 2,
    "difficulte" : "facile"
}

tab = [7, 5, 3, 1]
tab_dep = [7, 5, 3, 1]

score = {
    "joueur1": 0,
    "joueur2": 0
}

# Le prochain dictionnaire sert
# à conserver les coups en mémoire lorsque
# c'est l'ordinateur qui joue.

parfait = {
    "indice": 0,
    "nbr": 0
}

p_bot = ['Roberto', 'Robocop', 'T-800',
         'Goldorak', 'Jean-Eude', 'IG-11', 'C3PO',
         'DarkVador',]

# DECLARATION DES FONCTIONS


# Fonctions de PARAMETRAGE


def interface():
    """
    Permet de jouer le jeu à l'aide d'une interface tkinter.

    Args: 
        Aucun 

    Return:
        function : démarrage de l'interface 
    """
    pass


#----------------------------------------------------------------------------------------------------------------------------------


def joueur():
	"""
	Permet de choisir entre :
		- Joueur contre joueur 
		- Ordinateur contre joueur 
		- Ordinateur contre ordinateur

	Args :
		Aucun

	Return :
		Aucun 
	"""
	rep1 = verification_commande("Voulez vous jouer avec un bot ?\n-->")
	if rep1 in rep_favorable:
		rep2 = verification_commande("Est ce qu'un des joueurs humain souhaite jouer ?\n(Si vous répondez non alors 2 bots s'affronteront !)-->")
		if rep2 in rep_favorable:
			settings["Joueur_2"] = random.choice(p_bot)
			settings["nbr_bot"] = 1  # on défini le nombre de bot dans la partie à 1
			pseudo(1)
		else:
			settings["Joueur_1"] = random.choice(p_bot)
			settings["Joueur_2"] = random.choice(p_bot)
            # On fait en sorte que les deux bots n'ai pas le même pseudo
			while settings["Joueur_1"] == settings["Joueur_2"]:
				settings["Joueur_2"] = random.choice(p_bot)
			settings["nbr_bot"] = 2
	else:
		pseudo(2)



#----------------------------------------------------------------------------------------------------------------------------------


def mode_de_jeu():
    """
    Fonction qui change le mode de jeu
    
    arg : mode (dicts) : mode de jeu
    
    return : mode (dicts) : mode de jeu (changé)
    """


    settings["mode_de_jeu"] = False
    print("Bien on change le mode de jeu")
    return settings["mode_de_jeu"]


# ----------------------------------------------------------------------------------------------------------------------------------


def manche():
    """
    Fonction permettant aux joueurs de pouvoirs changer le nombre
    de manche qu'ils vont jouer, par défaut à 1.
    
    Returns : Dictionnaire contenant le nombre de manches à effectué
    """
    nb = verification("Combien de manches désirez-vous donc ?\n-->")
    while nb <= 0 :
        nb = verification("Combien de manches désirez-vous donc ?\n-->")
    settings["nb_manche"] = nb
    affiche_all(f"Bien alors il y aura {nb} manches ! \n\n")


# ----------------------------------------------------------------------------------------------------------------------------------

def allumettes():
    """Permet de changer le nombre d'allumettes dans la partie 

    Args:
        tab_dep (tableau): Contient le nombre l'allumettes par défaut.

    Returns:
        tableau (tab): Un tableau fais à partir de tab_dep mais qui lui sera 
                    modifié au cours de la partie. 
    """
    rep = verification_commande("Voulez vous changez le nombre d'allumettes ? (Etant par défaut de 7-5-3-1)\n-->")
    if rep in rep_favorable:
        for i in range(1, 5):
            var = "ligne", i
            var = verification(f"Ligne {i} ~ Combien d'allumettes souhaitez vous mettre ? \n-->")
            while var <= 0 :
                var = verification(f"Ligne {i} ~ Combien d'allumettes souhaitez vous mettre ? \n-->")
            tab[i - 1] = int(var)
        return tab
    else:
        return tab

# ----------------------------------------------------------------------------------------------------------------------------------


def verif_tri(tab):
    """
    Vérifie si les allumettes sont dans l'ordre

	Args :
		Aucun
    Returns:
        Bool: False si pas dans l'ordre décroissant (du plus petit au plus grand)
    """
    if tab == []:
        return False
    dep = tab[0]    # On commence par toujours prendre la première valeur
    for i in range(len(tab)):
        if tab[i] <= dep:
            dep = tab[i]    # Ensuite on remplace la première valeur par
                            # la suivante et ainsi de suite
        else:
            return False
    return True

# ----------------------------------------------------------------------------------------------------------------------------------


def tri():
    """Fonction qui, si les allumettes sont dans le désordre, propose de 
    les rangés, et le fais si la réponse du joueur est favorable. 
    
    Args :
    	Aucun

    Return :
    	(list) : Tableau des allumettes 
    """
    if verif_tri(tab) == False:
        rep = verification_commande("Vos allumettes ne sont pas dans l'ordre\nVoulez vous les rangés ? -->")
        if rep in rep_favorable:
            tab.sort(reverse=True)
        else:
            print("Bien on ne range pas les alumettes ")
        return tab

# ----------------------------------------------------------------------------------------------------------------------------------


def mode_affichage():
    """
    Fonction qui permet de changer la manière dont les allumettes sont affichées 
    """

    settings["affichage"] = False
    print("Bien on change l'affichage ! ")

# ----------------------------------------------------------------------------------------------------------------------------------

def vitesse() :
    """
    Fonction qui change la durée d'attente.
    """

    rep = verification("Quelle est la nouvelle durée d'attente ? : ")
    while rep < 0 :
        rep = verification("Quelle est la nouvelle durée d'attente ? : ")
    settings["vitesse"] = rep 
    
def difficulte ():
    """Permet de changer la difficulté.

    Returns:
        _type_: _description_
    """
    if settings["difficulte"] == "facile":
        settings["difficulte"] ="difficile"
    elif settings["difficulte"] == "difficile":
        settings["difficulte"] = "facile"
    print (f"Bien le mode de jeu à été changer en mode {settings['difficulte']} ! ")
# ----------------------------------------------------------------------------------------------------------------------------------

def pseudo(nbr):
    """
    Permet de définir un pseudonyme.

    Args :
        nbr (int) : Nombre de joueur.

    Return :
        (dicts) --> name : contient le pseudo des joueurs
    """
    for i in range(nbr):
        if i == 0:
            player = "Joueur_1"
        elif i == 1:
            player = "Joueur_2"
        rep = verification_commande(f"{player}, voulez vous changez de pseudonyme ? ( O = Oui / N = Non)\n-->")		
        if rep in rep_favorable:
            nouveau_pseudo = input("Alors comment désirez-vous être appelé ?\n--->")
            if nouveau_pseudo == "exit":
                fonction_exit()
            elif nouveau_pseudo == "help":
                affiche_all(commande['aide'])
            elif nouveau_pseudo == "rules":
                affiche_all(commande['rules'])
                sleep(3)
                nouveau_pseudo = input("Alors comment désirez-vous être appelé ?\n--->")
            else:
                settings[player] = nouveau_pseudo
                print(f"Bien vous serez donc désormais appelé {nouveau_pseudo} !")
        else:
            print("Bien, nous ne changerons pas votre pseudonyme !\n")

        return settings

# Fonctions de STRATEGIE GAGNANTE

def int_to_bin(nbr):
	"""
	Transforme un entier en base 10 en binaire

	Args :
		nbr(int) : Valeur d'un entier en base 10.

	Return :
		(str) : Valeur en binaire.

	"""
	if nbr == 0:
		return '0'
	elif nbr == 1:
		return '1'
	else:
		return int_to_bin(nbr // 2) + str(nbr % 2)


def bin_to_int(bit):
	"""
	Transforme une valeur en base 2 en valeur base 10 soit un nombre entier.

	Args :
		bit(str) : Valeur binaire.

	Return :
		(int) : La valeur en base 10 correspondant.
	"""
	n = 0
	tour = 0
	for i in range(len(bit) - 1, -1, -1):
		if bit[i] == '1':
			n = n + 2**tour
		tour = tour + 1
	return n


def tab_int_to_tab_bin(tableau):
	"""
	Transforme un tableau de valeur entière (en base 10)
	en tableau de valeur binaire correspondante.

	Args :
		tableau(list) : tableau d'entiers positifs

	Return :
		(list) : tableau de valeur en binaire (chaine de caractères).
  
	"""
	return [int_to_bin(tableau[i]) for i in range(len(tableau))]


def xor(ch1, ch2):
	"""
	Permet de comparer deux représenatations binaire 
	avec la méthode du "ou exclusif" aussi appelé XOR.

	Exemple de XOR : 

	A    B    A XOR B
	0    0      0
	0    1      1
	1    0      1
	1    1      0
	
	Le xor ne "réagi" que lorsque les valeurs sont différentes.

	Args :
		ch1(str) : Première valeur binaire.
		ch2(str) : Seconde valeur binaire.
	
	Return :
		(str) : Résultat du xor entre les deux valeur binaire.
	"""

	if len(ch1) < len(ch2):
		ch1 = '0'*(len(ch2) - len(ch1)) + ch1
	else:
		ch2 = '0'*(len(ch1) - len(ch2)) + ch2

	resultat = ''
	for i in range(len(ch1)):
		if ch1[i] == ch2[i]:
			resultat = resultat + '0'
		else:
			resultat = resultat + '1'

	return resultat


def somme_xor(tableau):
	""" 
	Fais le xor de tout les éléments binaire d'un tableau.

	Args :
		tableau(list) : tableau de valeaurs binaires.

	Return :
		(str) : Résultat du xor final.
	"""
	val1 = tableau[0]
	resultat = ''
	for i in range(len(tableau) - 1):
		resultat = xor(val1, tableau[i+1])
		val1 = resultat
	return resultat


def type_config(tableau):
	"""
	Permet de savoir si un tableau de valeur en binaire 
	est dit 'Pair' ou bien 'Impair'

	Args :
		tableau(list) : Valeurs binaire 

	Return :
		(bool) : Pair = True ; Impair = False 
	"""
	verification = somme_xor(tableau)
	result = 0

	for i in range(len(verification)):

		result = result + int(verification[i])
	return result == 0


def ligne_a_modifier(tableau):
	"""
	Permet de Donner la première occurence de la valeur la plus élévé 
	des valeurs bianires présente dans un tableau.

	Args :
	
		tableau(list) : Tableau de valeur binaire 

	Return : 
		(int) : indice de la valeur recherchée 
	"""
	verif = 0
	indice = 0
	for i in range(len(tableau)):
		if verif < bin_to_int(tableau[i]):
			verif = bin_to_int(tableau[i])
			indice = i

	return indice


def coup_parfait(tableau):
    """
    Donne un couple contenant l'indice de la ligne à 
    modifier et le nombre d'allumettes à enlever.

    Args :
        tableau(list) : tableau contenant des valeurs binaire

    Return :
        (int) --> indice : Indice de la ligne à prélever 
        (int) --> nbr : Nombre d'allumettes à prélever 
    """
    # On commence par vérifié si le tableau contient bien que 
    # des chaines de caractère, si ce n'est pas le cas on le 
    # transforme : 
    
    for i in range(len(tableau)):
        if type(tableau[i]) == str:
            continue
        else:
            tableau = tab_int_to_tab_bin(tableau)

    # Ensuite on choisi la ligne où l'on prend les allumettes
    indice = ligne_a_modifier(tableau)
    # Puis une fois la ligne choisie on décide du nombre d'allumettes à prendre
    valeur_gardé = bin_to_int(xor(tableau[indice], somme_xor(tableau)))
    
    # On vérifie que l'on ne doit pas gardé plus d'allumettes qu'il y en a 
    # Ce qui causera le fait de prendre un nombre négatif d'allumettes
    if valeur_gardé > bin_to_int(tableau[indice]):
        # Si c'est le cas on recommence à parcourir le tableau pour que
        # le bot choisisse la bonne stratégie : 
        for i in range(len(tableau)):
            valeur_gardé = bin_to_int(xor(tableau[i], somme_xor(tableau)))
            if valeur_gardé < bin_to_int(tableau[i]):
                indice = i
                nbr = bin_to_int(tableau[indice]) - valeur_gardé
                
    else:
        nbr = bin_to_int(tableau[indice]) - valeur_gardé
        
    # Je préfère garder ce test sous le coude au cas ou quelque chose n'irait pas 
    # Mais il m'étais surtout utile lors des tests de la stratégie gagnante.
    if nbr == 0 or nbr > bin_to_int(tableau[indice]) or indice > len(tableau):
        print("Quelque chose ne vas pas ")
    return indice, nbr

def minimum ():
    pass

def coup_miseret(tableau):
    """Permet de jouer un coup parfait en mode misère

    Args:
        tableau (list): Situation des allumettes
    """
    pass

def ordi_parfait(tableau):
    """
    Permet de jouer un coup parfait ou de jouer
    un coup aléatoire selon la situation.

    Args:
        tableau (list): Situation des allumettes

    Returns:
        tuple (int): Le coup qui est joué.
    """
    for i in range(len(tableau)):
        if type(tableau[i]) == str:
            pass
        else:
            tableau = tab_int_to_tab_bin(tableau)
    if type_config(tableau) == True or settings["difficulte"] == "facile":
        ordi_alea()
    if settings ["mode_de_jeu"] == False :
        parfait["indice"] = coup_misere(tableau)[0]
        parfait["nbr"] = coup_misere(tableau)[1]
    else:
        parfait["indice"] = coup_parfait(tableau)[0]
        parfait["nbr"] = coup_parfait(tableau)[1]
    return parfait["indice"], parfait["nbr"]
    

def ordi_alea():
    """
    Permet de faire jouer un coup aléatoire à une entité
    non joueur.

    Args:
        Aucun

    Return :
        None --> On passe tout par un dictionnaire 
    """

    ligne = randint(0, 3)
    while tab[ligne] == 0:
        ligne = randint(0, 3)

    nbr = randint(1, tab[ligne])
    while nbr > tab[ligne]:
        nbr = randint(1, tab[ligne])
        
    parfait["indice"] = ligne
    parfait["nbr"] = nbr

# Fonctions de JEU BASIQUE 


def coup_possible(nb_dispo, nb_joueur):
    """
    Permet de savoir si un coup est faisable ou non.
    
    Args :
        nb_dispo (int) : Nombre d'allumette(s) disponible 
        nb_joueur (int) : Nombre d'allumette(s) voulu 
    Return :
        Bool : True si le coup est possible, False si non. None si une mauvaise
        entrée de l'utilisateur.
    """
    if type(nb_dispo) == str or type(nb_joueur) == str:
        return None
    else:
        return (nb_dispo - nb_joueur) >= 0


def joue(ligne, nombre):
    """
    Joue le coup s'il est faisable, et change l'état de la partie.
    Args :
        ligne (int): le numéro de la ligne que l'on souhaite prendre
        nombre (int): le nombre d'allumettes prisent
    Return :
        None : si le coup n'est pas faisable
        tab (tableau): le tableau d'allumettes modifié si le coup est faisable
    """
    if coup_possible(tab[ligne], nombre) == True:
        tab[ligne] = tab[ligne] - nombre
        return tab
    return None


def tour_a_tour(t):
    """
    Petite fonction très simple permettant de determiné
    quel joueur doit jouer
    Args:
        t (int): incrémente de 1 a chaque tour, permet de faire
        du tour a tour
    Returns:
        dicts : le pseudo du joueur qui doit jouer.
    """
    if t % 2 == 0:
        return settings["Joueur_1"]
    return settings["Joueur_2"]


def gagner(tab):
    """
    Fonction permettant de savoir si un joueur a gagner ou pas
    Args :
        tab(tableau) : tableau du nombre d'allumettes disponible
    Return :
        Bool : True si le joueur a gagné, False si non.
    """
    somme = 0
    for i in range(len(tab)):
        somme = somme + tab[i]
    if somme == 0:
        return True
    return False


def verification(question):
    """Fonction permettant de forcer l'input d'un joueur pour qu'il soit valide

    Args:
        reponse (str): réponse du input à vérifier
        question (str): Question qui a été posé

    Returns:
        reponse (str): la réponse valide.
    """
    reponse = input(question)
    if reponse == "exit":
        fonction_exit()
    elif reponse == "help":
        affiche_all(commande['aide'])
        sleep(settings["vitesse"])
        reponse = input(question)
        reponse = verification(question)
    elif reponse == "rules":
        affiche_all(commande['rules'])
        sleep(settings["vitesse"])
        reponse = input(question)
        reponse = verification(question)
    try:
        reponse = int(reponse)
    except:
        while not reponse.isdigit() or reponse == "²":
            reponse = input(question)
            if reponse == "exit":
                fonction_exit()
            elif reponse == "help":
                affiche_all(commande['aide'])
                sleep(settings["vitesse"])
                reponse = input(question)
                reponse = verification(question)
            elif reponse == "rules":
                affiche_all(commande['rules'])
                sleep(settings["vitesse"])
                reponse = input(question)
                reponse = verification(question)
    return int(reponse)


def verification_commande(question):
    """Fonction qui vérifie les commandes pour les input

    Args:
        question (str): Question qui a été posé

    Returns:
        reponse (str): la réponse.
    """
    reponse = input(question)
    if reponse == "exit":
        fonction_exit()
    elif reponse == "help":
        affiche_all(commande['aide'])
        sleep(settings["vitesse"])
        reponse = input(question)
        reponse = verification_commande(question)
    elif reponse == "rules":
        affiche_all(commande['rules'])
        sleep(settings["vitesse"])
        reponse = input(question)
        reponse = verification_commande(question)
    return reponse
    
def fonction_exit():
    """
    Fonction qui permet au joueur, à tout moment
    dans le jeu de quitter la partie.

    """
    affiche_all("\n---------- LE JEU VA S'ARRETER !----------  ")
    exit()
    
def humain(demande):
    """Fonction d'interface avec l'utilisateur, qui lui permet d'entrer
    un nombre d'allumettes ou la ligne qu'il a choisi.

    Args:
        demande (str): Type de input voulu (pour les allumetets ou les lignes)

    Returns:
        valeur (int): La valeur valide choisi par l'utilisateur 
    """

    if demande == "ligne":
        reponse = verification("Sur quelle ligne souhaitez vous prendre des allumettes ?\n-->")
    elif demande == 'allumette':
        reponse = verification("Combien d'allumettes voulez-vous en prendre ?\n-->")
    reponse = int(reponse)
    if demande == "ligne":
        while reponse <= 0 or reponse > len(tab):
            affiche_all(error["infaisable"])
            reponse = verification("Sur quelle ligne souhaitez vous prendre des allumettes ?\n-->")
        while tab[reponse - 1] == 0:
            affiche_all(error["infaisable"])
            reponse = verification("Sur quelle ligne souhaitez vous prendre des allumettes ?\n-->")
        reponse = reponse - 1
    if demande == 'allumette':
        reponse = int(reponse)
    return reponse

# -----------------------------------------------------------------------------------------------


def jeu():
    t = 0
    
    if settings["nbr_bot"] == 0:

        affiche()

        while not gagner(tab) == True :
            ligne = humain('ligne')
            affiche_all(f"Vous pouvez prendre jusqu'a : {tab[ligne]} allumette(s)")
            coup = humain('allumette')
            while coup > tab[ligne] or coup <= 0:
                affiche_all(error["infaisable"])
                coup = humain('allumette')

            joue(ligne, coup)

            while joue == None:
                affiche_all(error["infaisable"])
                ligne = humain('ligne')
                colonne = humain('allumette')
                joue(ligne, colonne)
            affiche()
            t += 1    # Compte les tours, permet de passé d'un joueur a l'autre,
                    # et de pouvoir dire combien de tour sont passés
                    
                    
    elif settings["nbr_bot"] == 1:
        
        affiche()
        while not gagner(tab) == True :
            
            if tour_a_tour(t) == settings["Joueur_1"] :
                ligne = humain('ligne')
                affiche_all(f"Vous pouvez prendre jusqu'a : {tab[ligne]} allumette(s)")
                coup = humain('allumette')
                
                while coup > tab[ligne] or coup <= 0:

                    affiche_all(error["infaisable"])
                    coup = humain('allumette')
                    joue(ligne, coup)
                
                while joue == None:

                    affiche_all(error["infaisable"])
                    ligne = humain('ligne')
                    colonne = humain('allumette')
                    joue(ligne, colonne)
                joue(ligne, coup)
            else:
                ordi_parfait(tab)
                ligne = parfait["indice"]
                coup = parfait["nbr"]
                joue(ligne, coup)
                print(f"{tour_a_tour(t)} à pris {coup} allumettes sur ligne {ligne + 1} !")

            affiche()
            t = t + 1

    elif settings["nbr_bot"] == 2:

        affiche()

        while not gagner(tab) == True:
            ordi_parfait(tab)
            ligne = parfait["indice"]
            coup = parfait["nbr"]
            joue(ligne, coup)
            print (f"{tour_a_tour(t)} à pris {coup} allumettes sur la ligne {ligne + 1} !")
            sleep(settings["vitesse"])
            affiche()
            t += 1


    if settings["mode_de_jeu"] == True :
        affiche_win(tour_a_tour(t+1))
        return tour_a_tour(t+1)
    elif settings["mode_de_jeu"] == False:
        affiche_win(tour_a_tour(t))
        return tour_a_tour(t)

# PARTIE INITIALISATION

def initialisation():
    """Fonction initialisant tout les paramètres du jeu, c'est 
    une fonction de démarrage. 
    
    Elle ne renvoit rien et ne peux être testé.
    """
    reponse = 'o'
    while reponse in rep_favorable :
        print(f"-------------[Paramètres]------------",
              f"\n1 - Nombre de robot : {settings['nbr_bot']}",
              f"\n2 - Nom du joueur 1 : {settings['Joueur_1']}",
              f"\n3 - Nom du joueur 2 : {settings['Joueur_2']}",
              f"\n4 - Nombre de manche : {settings['nb_manche']}",
              f"\n5 - Mode d'affiche : {settings['affichage']}",
              f"\n6 - Mode de jeu : {settings['mode_de_jeu']}",
              f"\n7 - Nombre d'allumettes : {settings['tab']}",
              f"\n8 - Vitesse de jeu : {settings['vitesse']}",
              f"\n9 - Difficulté : {settings['difficulte']}"
              "\n-------------------------------------")
        reponse = verification_commande("Voulez vous changer l'un de ces paramètres ?\n-->")
        if reponse in rep_favorable :
            changement = verification("Veuillez alors inscrire le nombre correspondant au paramètre correspondant : ")
            
            if changement == 1 :
                joueur()
                
            elif changement == 2:
                if settings["nbr_bot"] == 2 :
                    print("Désolé, mais vous ne pouvez modifier le pseudo d'un bot !")
                else:
                    pseudo(1)
                    
            elif changement == 3:
                if settings["nbr_bot"] > 0:
                    print ("Désolé, mais vous ne pouvez modifier le pseudo d'un bot !")
                else :
                    pseudo(2)
                    
            elif changement == 4:
                manche()
                
            elif changement == 5:
                mode_affichage()
                
            elif changement == 6:
                mode_de_jeu()
                
            elif changement == 7:
                allumettes()
                settings["tab"] = tab
                tri()
                
            elif changement == 8:
                vitesse()
            
            elif changement == 9:
                difficulte()
    r = input("Voulez vous voir les règles du jeu avant de commencer ?\n-->")

    if r in rep_favorable:
        affiche_all(commande["rules"])
        sleep(3)

    affiche_all(demarrage)


# PARTIE AFFICHAGE

def score_fin(score):
    """Fonction qui regarde le gagnant de toutes les manches
    qui écrit un message en fonctions des résultats, prend également 
    en compte les cas d'égalité.
    
    Ne renvoit rien et ne peut etre testé.

    Args:
        score (dict): dictionnaire contenant le score de chaque joueur.
    """
    print (f"Joueur qui a débuté : {settings['Joueur_1']}")
    if score["joueur1"] > score["joueur2"]:
        affiche_all(
            f"Bravo, {settings['Joueur_1']} est le grand vainqueur ! Il a remporté {score['joueur1']} manches !")
    elif score["joueur1"] < score["joueur2"]:
        affiche_all(
            f"Bravo, {settings['Joueur_2']} est le grand vainqueur ! Il a remporté {score['joueur2']} manches !")
    elif score["joueur1"] == score["joueur2"]:
        affiche_all(
            f"Wow que d'émotions ! C'est donc une égalité parfaite ! Avec {score['joueur2']} partout !")

# -----------------------------------------------------------------------------------------------


def affiche():
    """
    Fonction d'affichage qui permet d'afficher le nombre d'allumettes 
    restante dans le jeux.
    
    Args :
        event (str) : type d'affichage des allumettes 
    """

    if settings["affichage"] == False:
        print()
        for i in range(len(tab)):
            print('\033[1m' + f'Il reste {tab[i]} allumette(s) dans la ligne {i+ 1 }' + '\033[0m')
        print()

    elif settings["affichage"] == True:
        for i in range(len(tab)):
            print ("ligne n°", i+1, " :",  end= " ")
            for x in range(tab[i]):
                print(haut, end=' ')
            print()
            print(" " * len("ligne n° 1 : "), end=' ')
            for x in range(tab[i]):
                print (bas, end=' ')
            print()
            print()
        print()
        for i in range(len(tab)):
            print('\033[1m' + f'Il reste {tab[i]} allumette(s) dans la ligne {i+ 1 }' + '\033[0m')
        print()
    

# -----------------------------------------------------------------------------------------------


def affiche_all(arg):
    """Fonction d'affichage qui permet d'afficher ce que l'on veut comme message,
    permet de centralisé les print à un seul endroit du programme.
    Args:
        arg (tout type): Ce que l'on veut afficher 
    Returns:
        Rien
    """
    print(arg)

# -----------------------------------------------------------------------------------------------


def affiche_win(name):
    """Fonction qui permet d'afficher le gagnant de chaque manche 

    Args:
        win (str): type de mode de jeu de la partie. 
        t (int) :  permet de connaitre le pseudo du joueur gagnant 
    """
    print("-------------------------------------------------------\n"
              f"Félicitation {name}, vous remportez la manche!!\n"
            "-------------------------------------------------------")

# PROGRAMME PRINCIPAL

if __name__ == "__main__":
    
    initialisation()  # paramétrage du jeu
    tab_dep = [tab[i] for i in range(len(tab))]  # Mise en place (sécurisé)
                                                 # des allumettes

    for i in range(settings['nb_manche']):  # Tourne en fonction du nombre de manche
        affiche_all(f"\n---------------------Manche n° {i + 1} ---------------------\n")
        if jeu() == settings["Joueur_1"]:                 # |
            score["joueur1"] = score["joueur1"] + 1                                
        else:                                         
            score["joueur2"] = score["joueur2"] + 1   

        # Réinitialise les paramètres de la partie.
        sleep(settings["vitesse"])
        tab = [tab_dep[i] for i in range(len(tab_dep))]
        t = 0

    score_fin(score)  # Permet d'écrire le résultat du gagnant !

