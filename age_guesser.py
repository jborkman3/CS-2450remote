import random 

print("My name is computer_bro and I will try to guess your age.")

name = input("what is yourname?")

guessed = False
while not guessed:
    age = random.randint(15, 40)
    response = input(f"Are you {age} years old? (y/n): ")
    if response == 'y':
        print(f"{name} is {age} years old. ")
        guessed = True
    else:
        print("Rats. ")