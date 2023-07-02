import random 

print("Welcome to the Password Generator")

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_-+=<>.,/?{}[]`~'

number = int(input("\nEnter the number of passwords variations needed: "))

length = int(input("Enter the password length: "))

print('\nHere are your passwords: ')

for x in range(number):
    passwords = ''
    for y in range(length):
        passwords += random.choice(chars)
    print(passwords)

