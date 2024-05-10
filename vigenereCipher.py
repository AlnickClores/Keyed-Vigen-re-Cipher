from vigenereCipherLibray import * 

# main program
print("Keyed Vigenere Table")
print("1. Cipher \n2. Decipher")
mode = int(input("Enter the mode: "))

if mode == 1:
    nameOfVigenereTable = input("Enter the name of your Vigenere Table: ")
    keyword = input(f"Enter the keyword of your {nameOfVigenereTable} Vigenere Table: ")
    cipherMode(nameOfVigenereTable, keyword)
elif mode == 2:
    nameOfVigenereTable = input("Enter the name of your Vigenere Table: ")
    keyword = input(f"Enter the keyword of your {nameOfVigenereTable} Vigenere Table: ")
    decipherMode(nameOfVigenereTable, keyword)
else:
    print("Enter proper mode choice.")
