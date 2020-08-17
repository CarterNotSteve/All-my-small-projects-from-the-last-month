from random import randint

ball = False 
out = False

while not out:
    print("Ball, hide")
    move = input(">>> ")
    
    if move.capitalize() == "Ball":
        print("You grab for a ball", end=" ")
        ballgrab = randint(1,100)
        if ballgrab % 2 == 0:
             ball = True
             print("and you clench it in your hand")
        else:
            print("but you miss")
            
        hit = randint(1,100)
        if hit % 3 == 0:
            print("You got hit.")
            out = True
            
    elif move.capitalize() == "Hide":
        print("where to hide? [1-10]")
        hideslot = input("$ ")
        try:
            if randint(1, 100) % int(hideslot) == 0:
                print("you were hit")
                out = not out
                
        except ValueError:
            print("input a valid number")
                    