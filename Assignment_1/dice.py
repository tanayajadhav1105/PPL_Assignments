import random
l = [1, 2, 3, 4, 5, 6]
while 1 :
    x = input("Enter your choice\na) Press 1 to roll the dice\nb) Press 2 to exit\n")
    if (x == '1') :
        print(random.choice(l))
    else :
        break