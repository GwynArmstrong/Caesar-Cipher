import random #SS used to choose a random word from the lists of words
import time #SR needed to use time.time() function

#SS symbols used to envrypt
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
MAX_KEY_SIZE = len(SYMBOLS)

#SS lists that correspond to level of difficulty, TA created words that go inside of lists
level_easy = ['elf', 'bell', 'gift', 'ice', 'toys', 'log', 'hope', 'snow', 'cold', 'pie', 'star', 'wish', 'noel', 'joy', 'love', 'coal', 'tree', 'red', 'gold']
level_medium = ['angel', 'green', 'candy', 'merry', 'dasher', 'candle', 'dancer', 'frosty', 'socks', 'carols', 'jolly', 'ribbon', 'light', 'sleigh', 'vixon', 'holly', 'cookie', 'santa', 'family', 'donner', 'winter', 'cupid', 'comet', 'parade']
level_hard = ['rudolph', 'prancer', 'holiday', 'blitzen', 'northpole', 'polarbear', 'candycane', 'decoration', 'wrappingpaper', 'hotchocolate', 'mistletoe', 'celebrate', 'gingerbread', 'christmas', 'stocking', 'present', 'snowman', 'chocolate', 'ornament', 'reindeer']

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
            
#SR This function asks the user to input how long they'd like the game to last for
def get_delay():
    while True:
        delay = int(input("Game Time: 30, 60, 90 seconds?\n"))#input time
        if delay == int(30):
            return delay #If the input is valid
        elif delay == int(60):
            return delay # If the input is valid
        elif delay == int(90):
            return int(delay)#If the input is valid
        else:
            print("Invalid input")#If invalid input asks user to try again 
         
#GA Find the total time of the game using the delay found above 
def gameTime(delay):
    game_end = time.time() + delay
    return game_end

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
delay = get_delay()
game_end = gameTime(delay)
message = getTranslatedMessage(r_word, key)

#SR
while True:
    if time.time() < game_end:
        #GA This if statement checks if the user has inputted the correct solution
        #if they have it gives them another word, if not they must try again
        print(message) #SS Prints the result of the encryption
        guess = input("Enter what you think the decrypted word is (your key of incryption is " + str(key) + "):\n")
        if guess == r_word:
            print("You are correct")
            r_word = word_to_be_encrypted()
            message = getTranslatedMessage(r_word, key)
        else:
            print("Please try again")
    elif time.time() >= game_end:
        print('GAME OVER')
        break
    else:
        break
