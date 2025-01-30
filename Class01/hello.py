
Lucky_num = 20

gussed_num = int(input("Enter a number between 0 & 50:"))

if gussed_num == Lucky_num:
    print("You Gussed correct !!!")
elif gussed_num > Lucky_num:
    print("Please try again with decreasing your guess number")
elif gussed_num < Lucky_num:
    print("Please try again with increasing your guess number")

# import random

# # Generate a random number between 0 and 50
# Lucky_num = random.randint(0, 50)



LIMIT = 10

first = 0 
while first < LIMIT:
    first += 1

    second = 0
    while second < LIMIT:
        second += 1
    print(first, '*', second, '=', first * second)
