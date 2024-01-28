#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the password Generator!")
pw_length = input("How many letters would you like in your password?\n")
symbs = input("How many symbols would you like?\n")
nums = input("How many numbers would you like?\n")
pw = ''

symbs = int(symbs)
nums = int(nums)

for n in range(0, int(pw_length)):
    rdm = random.randint(0,2)
    if(rdm == 1 and symbs > 0):
        pw += pw.join(random.choice(symbols))
        symbs -= 1
    elif(rdm == 2 and nums > 0):
        pw += pw.join(random.choice(numbers))
        nums -=1
    else:
        pw += pw.join(random.choice(letters))

print(f"Here is your password: {pw}")
