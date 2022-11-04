import random
import emoji

def game(comp, you):
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
        elif you == 's':
            return True
        
    



print("Comp Turn: Snake(s) Water(w) or Gun(g) ?")
randNo = random.randint(1,3)
print(randNo)
if randNo == 1:
    comp = 's'
elif randNo ==2:
    comp = 'W' 
elif randNo ==3:
    comp = 'g'

you = input("palyer's Turn: Snake(s) Water(w) or Gun(g) ?")

a = game(comp, you)

print(f"Computer chose {comp}")
print(f"You chose {you}")

if a == None:
    print("The game is tie|")
    # unamused face
    print("\U0001F612")
elif a:
    print("You Win ")
    # grinning face
    print("\U0001F600")
else:
    print("You Lose " )
    # angry face
    print("\N{angry face}")