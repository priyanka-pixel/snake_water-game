import random

def gameWin(comp, you):
    if comp == you:
        return None
    elif comp == 's':
        if you == 'w':
            return False
        elif you == 'g':
            return True
    elif comp == 'w':
        if you == 'g':
            return False
        elif you == 's':
            return True
    elif comp == 'g':
        if you == 's':
            return False
        elif you == 'w':
            return True
print("Comp Turn: Snake(s) water(w) or gun(g")
randNo = random.randint(1,3)
print(randNo)
if randNo == 1:
    comp = 's'
elif randNo == 2:
    comp = 'w'
elif randNo == 3:
    comp = 'g'

you = input("Priyanka Turn: Snake(s) water(w) or gun(g)?" )
print(f'Computer choose {comp}')
print(f'Priyanka choose {you}')
a = gameWin(comp, you)
if a == None:
    print("The game is tie!")
elif a:
    print("You win!")
else:
    print("you Lose!")
