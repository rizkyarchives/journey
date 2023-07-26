alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def caesar(string, shifts, directions):
    result = ''
    if directions == "decode":
        shifts *= -1
    for letter in string:
        if letter.isalpha():
            index = alphabet.index(letter) + shifts
            while index > 25:
                index -= 26
            while index < 0:
                index += 26
            result += alphabet[index]
        else:
            result += letter
    return result

logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
print(logo)
running = True
while running:
    error_testing = True
    while error_testing:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        if direction == "encode" or direction == "decode":
            error_testing = False
        else:
            print("Invalid Choice!")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    print(f"{direction}d: " + caesar(text, shift, direction))
    keep_running = input("Wanna continue? 'yes' or 'no': ")
    if keep_running == 'no':
        running = False
        print("Bye.")
    print("\n\n")