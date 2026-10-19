import random
emogi = { 'r':'ROCK','p':'PAPER','s':'sicer' }
choices = ('r','p','s')
user_choice = input('choice rock(r),paper(p),sesor(s): ')
if user_choice not in choices:
    print("choice invalide!")
computer_choice = random.choice(choices)
print('your choice',emogi[user_choice])
print('computer choice',emogi[computer_choice])
if user_choice==computer_choice:
    print('draw')
elif((user_choice=='r' and computer_choice=='s') or
    (user_choice=='s' and computer_choice=='p') or
    (user_choice=='p' and computer_choice=='r')):
    print('you win the game')
else:
    print('you lose the game')

    
     


