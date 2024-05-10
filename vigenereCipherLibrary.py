import string

# function to generate the Vigenere Table
def generateVigenereTable(name_of_table, keyword):
    alphabet = string.ascii_lowercase
    filtered_alphabet = ''.join(filter(lambda x: x not in name_of_table, alphabet))
    table = []
    
    table_row = name_of_table + filtered_alphabet
    for i in range(26):
        table.append(table_row)
        table_row = table_row[1:] + table_row[0]
    
    return table

def printVigenereTable(table, nameOfVigenereTable):
    print()
    print(f"Generated '{nameOfVigenereTable}' Vigenere Table:")
    for row in table:
        print(' '.join(row))

#function to generate the ciphered text
def generateCipherText(table, secretMessage, keystream):
    cipherText = ''
    for i in range(len(secretMessage)):
        if secretMessage[i] == ' ':
            cipherText += ' '
        else:
            keystream_char = keystream[i % len(keystream)]
            row_index = 0
            col_index = 0

            while table[row_index][0] != keystream_char:
                row_index += 1
                
            while table[0][col_index] != secretMessage[i]:
                col_index += 1
            cipherText += table[row_index][col_index]
            
    return cipherText
    
#function to generate secret message from ciphered text
def generateSecretMessage(table, cipherText, keystream):
    generatedSecretMessage = ''
    for i in range(len(cipherText)):
        if cipherText[i] == ' ':
            generatedSecretMessage += ' '
        else:
            keystream_char = keystream[i % len(keystream)]
            row_index = 0
            while table[row_index][0] != keystream_char:
                row_index += 1
            col_index = table[row_index].index(cipherText[i])
            generatedSecretMessage += table[0][col_index]
            
    return generatedSecretMessage

# Function to handle ciphering
def cipherMode(nameOfVigenereTable, keyword):
    secretMessage = input("Enter your secret message or cipher text: ")

    secretMessage = ''.join(secretMessage.split())
    keywordLength = len(keyword)
    messageLength = len(secretMessage)

    keystream = (keyword * (messageLength // keywordLength)) + keyword[:messageLength % keywordLength]
    table = generateVigenereTable(nameOfVigenereTable, keyword)

    printVigenereTable(table, nameOfVigenereTable)
    cipherText = generateCipherText(table, secretMessage, keystream)
    
    print("\nKeystream:", keystream)
    print("Cipher Text:", cipherText)

# Function to handle deciphering
def decipherMode(nameOfVigenereTable, keyword):
    cipheredText = input("Enter the cipher text: ")

    cipheredText = ''.join(cipheredText.split())
    keywordLength = len(keyword)
    messageLength = len(cipheredText)

    keystream = (keyword * (messageLength // keywordLength)) + keyword[:messageLength % keywordLength]
    table = generateVigenereTable(nameOfVigenereTable, keyword)

    printVigenereTable(table, nameOfVigenereTable)
    generatedSecretMessage = generateSecretMessage(table, cipheredText, keystream)
    
    print("\nKeystream:", keystream)
    print("Cipher Text:", cipheredText)
    print("Secret Message:", generatedSecretMessage)
