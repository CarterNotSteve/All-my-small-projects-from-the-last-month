import time

print("Type out 'The quick brown fox jumped over the lazy dog'")
incorrect = True
while incorrect:
    times1 = time.localtime()
    time1 = time.strftime("%H:%M:%S", times1)
    print(time1)
    phrase = input(">>> ")
    if phrase.capitalize() == "The quick brown fox jumped over the lazy dog":
        print("correct")
        incorrect = False
    else:
        print("False")
        
times2 = time.localtime()
times3 = times2 - times1
time3 = time.strftime("%H:%M:%S")
print("you took "+time3)