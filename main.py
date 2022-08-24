import random
from tkinter import N
import gamechar

player_units = []
ai_unit = []


def main():
    
    print("Welcome to The Battle Game")
    setup3p = 1
    while (setup3p <= 3):
        print("Player ", setup3p)
        char_type = input("Enter Character Type [ w / t ]: ").lower()
        char_name_num = str(random.randint(1,99))
        char_input = str(input("Enter Character Name: ")).upper()
        char_name = (char_input) + (char_name_num)
        if setup3p == 1:
            char1 = gamechar.GameCharacter(char_type, char_name) 
        elif setup3p == 2:
            char2 = gamechar.GameCharacter(char_type, char_name)
        elif setup3p == 3:
            char3 = gamechar.GameCharacter(char_type, char_name)
        setup3p = setup3p + 1
        
            
    print(char1)
    print(char2)
    print(char3)
    print(".")

    setup3ai = 1
    while (setup3ai <= 3):
        #print("AI ", setup3ai)
        ai_list = ['w', 't']
        ai_choice = random.choice(ai_list)
        ai_name1 = random.randint(1, 99)
        ai_name = "AI" + str(ai_name1)
        if setup3ai == 1:
            ai1 = gamechar.GameCharacter(ai_choice, ai_name) 
        elif setup3ai == 2:
            ai2 = gamechar.GameCharacter(ai_choice, ai_name)
        elif setup3ai == 3:
            ai3 = gamechar.GameCharacter(ai_choice, ai_name)
        setup3ai = setup3ai + 1

    print(ai1)
    print(ai2)
    print(ai3)
    print(".")

    rounds = 1
    while (rounds < 10):
        
        if rounds % 2 == 1:
            char1.attack(ai1)
            print(char1.get_type() + " " + char1.get_name() + " inflicted " + char1.get_damage() + " on " + str(ai1.type) + str(ai1.name))
            print(char1)
            print(char2)
            print(char3)
            print(ai1)
            print(ai2)
            print(ai3)
            print(".")
            

        else:
            ai1.attack(char1)
            print(ai1.get_type() + " " + ai1.get_name() + " inflicted " + ai1.get_damage() + " on " + str(char1.type) + str(char1.name))
            print(char1)
            print(char2)
            print(char3)
            print(ai1)
            print(ai2)
            print(ai3)
            print(".")
          
        rounds += 1  
        

    







main()
