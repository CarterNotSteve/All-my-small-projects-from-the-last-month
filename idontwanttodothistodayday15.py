from random import randint

class monster():
    def __init__(health, attack, name):
        monster.health = health
        monster.atk = attack
        monster.name = name
        
        
mon1 = monster(20, randint(1,10), "Smelborp")
mon2 = monster(20, randint(1,10), "Brachistochrone")


protag = monster(50, randint(1, 100), "name")
alive = True
roundnum = 1

protag.name = input("Name: ")


while alive:
    protag.atk  = randint(1,20)
    if protag.health <= 0:
        print("You died")
        alive = False
        
    move = input("Dodge or attack")
    capmv = move.capitalize()
    
    if capmv == "Dodge":
        mv2 = input("Guess: ")
        if roundnum == 1:
            atk2 = mon1.atk - mv2
            if atk2 < 0:
                atk2 = atk2 - (atk2 * 2)
                
            if atk2 % 2 == 0:
                print("Critical!")
                atk2 = atk2 * 2
        protag.health = protag.health - atk 2
                