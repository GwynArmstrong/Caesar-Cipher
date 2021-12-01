import random #SS used to choose a random word from the lists of words

#SS symbols used to envrypt
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
MAX_KEY_SIZE = len(SYMBOLS)

#SS lists that correspond to level of difficulty, 
level_easy = ['sun', 'fire', 'rain']#Tony will add the list of words
level_medium = ['sun', 'fire', 'rain']
level_hard = ['sun', 'fire', 'rain']


#SS This function will ask user to input level of difficulty
def how_difficult(): 
    while True:
        print("Enter level of difficulty: easy, medium or hard")
        difficulty = input()
        if difficulty in ['easy', 'medium', 'hard']:#SS if user inputs easy medium or hard the input is returned
            return difficulty
        else: #SS if the input is not easy medium or hard the loop restarts until the input is correct
            print("Invalid input")
            
        
#SS This function chooses a random word from the lists based on difficulty
def word_to_be_encrypted():
    if difficulty == 'easy': #SS If the how_difficult function returns easy
        r_word = random.choice(level_easy) #SS chooses a random word from level_easy
        return r_word
    elif difficulty == 'medium': #SS If the how_difficult function returns medium
        r_word = random.choice(level_medium) #SS chooses a random word from level_medium
        return r_word
    else:#SS If the how_difficult function returns hard
        r_word = random.choice(level_hard) #SS chooses a random word from level_hard
        return r_word
    
#SS This function asks user to input a key to encrypt the message
def encryption_key():
    while True:
        key = int(input("Please enter a number between 1 and 52\n")) #SS Changes the input to type int
        if (key >=1 and key <= MAX_KEY_SIZE): #SS Checking to make sure the key is between 1 and 52
            return key #SS If True so if input is an int between 1 and 52 returns the key
        else:
            print("Invalid input") #SS If false asks the user to try again

#SS Encrypts the r_word, the word that was chosen randomly
def getTranslatedMessage(r_word, key):
    new_word="" #SS empty string to add the encrypted symbols    
    for symbol in r_word: 
        symbolIndex = SYMBOLS.find(symbol)
        if symbolIndex == -1: #SS Symbol not found in SYMBOLS.
        #SS Just add this symbol without any change.
            new_word += symbol #SS adds symbols to new word which is an empty string
            
        else:
            #SS ncrypt or dercypt.
            symbolIndex += key

        if symbolIndex >= len(SYMBOLS):
            symbolIndex -= len(SYMBOLS)
        elif symbolIndex <0:
            symbolIndex += len(SYMBOLS)
        
        new_word += SYMBOLS[symbolIndex] #SS changes the new_word not r_word
        
    return new_word


difficulty = how_difficult()
r_word = word_to_be_encrypted()
key = encryption_key()
message = getTranslatedMessage(r_word, key)
print(message) #SS prints the result of the encryption
