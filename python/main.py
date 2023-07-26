#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

password = ""
for i in range(nr_letters):
    add = random.choice(letters)
    password += add
for i in range(nr_symbols):
    add = random.choice(symbols)
    password += add
for i in range(nr_numbers):
    add = random.choice(numbers)
    password += add

print("Easy: " + password)


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
#1 = letters, 2 = symbols, 3 = numbers
password2 = ""
total_letters = 0
total_symbols = 0
total_numbers = 0
while total_letters != nr_letters or total_symbols != nr_symbols or total_numbers != nr_numbers:
    choice = random.randint(1, 3)
    if choice == 1:
        if total_letters == nr_letters:
            continue
        else:
            password2 += random.choice(letters)
            total_letters += 1
    elif choice == 2:
        if total_symbols == nr_symbols:
            continue
        else:
            password2 += random.choice(symbols)
            total_symbols += 1
    else:
        if total_numbers == nr_numbers:
            continue
        else:
            password2 += random.choice(numbers)
            total_numbers += 1
print("Advance: " + password2)

#other alternatives for Hard Level: Use the Easy level but instead create a list which means U need to use append. And then shuffle the list
#using random.shuffle, then use the for loop to change the list into a string or you can use the .join function :D