# main.py -- put your code here!
from random import randint
import time
import pyb
#Ici se trouve tout le code dans une fonction
def jeu():  
    pyb.LED(1).off()
    pyb.LED(2).off()
    pyb.LED(4).off()
    pyb.LED(3).on()
    #Le menu aide donne des indications quand à la couleur de la LED
    def help():
        print("""
 _   _        _        
| | | |  ___ | | _ __  
| |_| | / _ \| || '_ \ 
|  _  ||  __/| || |_) |
|_| |_| \___||_|| .__/ 
                |_| """)
        print("\n Quand la LED est verte c'est que tu as gagné \n Quand la LED est rouge c'est que tu as perdu \n Quand la LED est bleu il y égalité \n Quand la LED est jaune c'est que le programme s'éxécute.")
        time.sleep(11)
        pass
    #Ici l'utilisateur va entrer pierre, feuille ou ciseaux
    def joueur():
        player = input("pierre, feuille, ciseaux : \n").lower()
        while player not in ["pierre", "feuille", "ciseaux", "help"]:
            player = input("pierre, feuille, ciseaux : \n").lower()
        return(player)
    #"L'ordinateur" choisit un nombre entre 1 et 3. Pour 1 = pierre pour 2 = feuille et pour 3 = ciseaux
    def ordi():
        ordinateur = randint(1,3)
        if ordinateur == 1:
            ordinateur = "pierre"
        if ordinateur ==2:
            ordinateur = "feuille"
        if ordinateur == 3:
            ordinateur = "ciseaux"
        return(ordinateur)
    #On va définir l'action des LEDS en fonction de gagné, perdu ou égalité
    def LEDwin():
        pyb.LED(3).off()
        pyb.LED(2).on()
    def LEDlose():
        pyb.LED(3).off()
        pyb.LED(1).on()
    def LEDequal():
        pyb.LED(3).off()
        pyb.LED(4).on()
    #On met les fonctions ordi et joueur dans des variables car 'cest trop long à écrire
    a = joueur()
    b = ordi()
    if a == "help":
        help()
    #C'est la qu'on affiche le choix du robot et du joueur
    def r():
        print ("choix utilisateur :" ,a, )
        print("Choix ordinateur:" ,b, )
    r()
    #Ici en fonction du choix du joueur et du robot le script va dire si vous avez gagné, perdu ou si il ya égalité
    if a == "ciseaux" and b == "feuille":
        print("Bravo vous avez gagner")
        LEDwin()
    if a == "pierre" and b == "ciseaux":
        print("Bravo vous avez gagner")
        LEDwin()
    if a == "feuille" and b == "pierre":
        print("Bravo vous avez gagner")
        LEDwin()
    if a == "feuille" and b == "ciseaux":
        print("Vous avez perdu")
        LEDlose()
    if a == "ciseaux" and b == "pierre":
        print("Vous avez perdu")
        LEDlose()
    if a == "pierre" and b == "feuille":
        print("Vous avez perdu")
        LEDlose()
    if a == "feuille" and b == "feuille":
        print("égalité")
        LEDequal()
    if a == "pierre" and b == "pierre":
        print("égalité")
        LEDequal()
    if a == "ciseaux" and b == "ciseaux":
        print("égalité")
        LEDequal()
    #On demande au joueur si il veut rejouer
    replay = input("Veux tu rejouer? OUI/NON \n").lower()
    #On regarde si l'utilisateur veut quitter ou non si c'est "non" le programme recommence si c'est "oui" le programme se coupe
    if replay == "OUI".lower():
        jeu()
    if replay == "NON".lower():
        print("ok")
        time.sleep(5)
        return
#On appelle la fonction jeu() c'est l'ensemble du programme
jeu()