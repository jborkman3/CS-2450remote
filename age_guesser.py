import random

print("My name is computer_bro and I will try to guess your age.")

name = input("What is your name? ")

response = input("Are you between 20 and 30 years of age? (y/n): ").lower()

if response == 'y':
    age = random.randint(20, 30)
else:
    valid_ages = [a for a in range(15, 19) if a < 20 or a for a in range(31, 40) if a > 30]
    age = random.choice(valid_ages)

response = input(f"Are you {age} years old? (y/n): ").lower()

if response == 'y':
    print(f"{name} is {age} years old.")
else:
    print("Rats.")