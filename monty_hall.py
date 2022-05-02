import random

def game(var):
    i = 0
    prob = 0
    while i <= var:
        poss = [1, 2, 3]
        right_door = random.choice(poss)
        choice = random.choice(poss)
        poss.remove(choice)
        comm = random.choice(poss)
        while comm == right_door:
            comm = random.choice(poss)
        poss.remove(comm)
        if poss[0] == right_door:
            prob += 1
        i += 1
    print(prob * 100 / var, "%", sep = "")
    return

game(100)
