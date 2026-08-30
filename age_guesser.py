import random

print("My name is computer_bro and I will try to guess your age.")

name = input("What is your name? ")

response = input("Are you between 20 and 30 years of age? (y/n): ").lower()

if response == 'y':
    age = random.randint(20, 30)
else:
    age = random.randint(15, 40)

response = input(f"Are you {age} years old? (y/n): ").lower()

if response == 'y':
    print(f"{name} is {age} years old.")
else:
    print("Rats.")