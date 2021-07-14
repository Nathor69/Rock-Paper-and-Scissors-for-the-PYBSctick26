# main.py -- put your code here!
from random import randint
import time
import pyb
#Here is all of the code.
def jeu():  
    pyb.LED(1).off()
    pyb.LED(2).off()
    pyb.LED(4).off()
    pyb.LED(3).on()
    #The help menu give information about the colour of the LED.
    def help():
        print("""
 _   _        _        
| | | |  ___ | | _ __  
| |_| | / _ \| || '_ \ 
|  _  ||  __/| || |_) |
|_| |_| \___||_|| .__/ 
                |_| """)
        print("\n When the LED is green you have win \n When the LED is red you have lose \n When the LED is blue there is equality \n When the LED is yellow the program runs")
        time.sleep(11)
        pass
    #Here the player chooses rock, paper or scissors.
    def joueur():
        player = input("rock, paper, scissors : \n").lower()
        while player not in ["rock", "paper", "scissors", "help"]:
            player = input("rock, paper, scissors : \n").lower()
        return(player)
    #"The computer" chooses a number between 1 and 3. For 1 = rock for 2 = paper and for 3 = scissors.
    def ordi():
        ordinateur = randint(1,3)
        if ordinateur == 1:
            ordinateur = "rock"
        if ordinateur ==2:
            ordinateur = "paper"
        if ordinateur == 3:
            ordinateur = "scissors"
        return(ordinateur)
    #Here we define the color of the leds if we win, lose or if there is equality.
    def LEDwin():
        pyb.LED(3).off()
        pyb.LED(2).on()
    def LEDlose():
        pyb.LED(3).off()
        pyb.LED(1).on()
    def LEDequal():
        pyb.LED(3).off()
        pyb.LED(4).on()
    #I put the functions into variables because i am lazy. I don't want to rewrite them.
    a = joueur()
    b = ordi()
    if a == "help":
        help()
    #This is where the choice of "the computer" and the player is displayed.
    def choice():
        print ("Player's choice :" ,a, )
        print("Computer's choice :" ,b, )
    choice()
    #Here depending on the choice of the player and "the Computer" the script will say if you have win, lose or if there equality.
    if a == "scissors" and b == "paper":
        print("Well done you win!")
        LEDwin()
    if a == "rock" and b == "scissors":
        print("Well done you win! ")
        LEDwin()
    if a == "paper" and b == "rock":
        print("Well done you win!")
        LEDwin()
    if a == "paper" and b == "scissors":
        print("You have loses :(")
        LEDlose()
    if a == "scissors" and b == "rock":
        print("You have loses :(")
        LEDlose()
    if a == "rock" and b == "paper":
        print("You have loses :(")
        LEDlose()
    if a == "paper" and b == "paper":
        print("equality!")
        LEDequal()
    if a == "rock" and b == "rock":
        print("equality!")
        LEDequal()
    if a == "scissors" and b == "scissors":
        print("equality!")
        LEDequal()
    #We ask to the player if he wants to replay.
    replay = input("Want to replay YES/NO ? \n").lower()
    #We watch if the player wants to replay or quit the game.
    if replay == "YES".lower():
        jeu()
    if replay == "NO".lower():
        print("ok")
        time.sleep(5)
        return
jeu()