import random #SS used to choose a random word from the lists of words
import time #SR needed to use time.time() function

#SS symbols used to envrypt
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
MAX_KEY_SIZE = len(SYMBOLS)
score=0

#GA Combined functions that got settings for game created by SS and the timer function created by SR to make the game work together, and created the if statement to check if the user inputted the correct answer or not

#SS lists that correspond to level of difficulty, TA created words that go inside of lists
level_easy = ['elf', 'bell', 'gift', 'ice', 'toys', 'log', 'hope', 'snow', 'cold', 'pie', 'star', 'wish', 'noel', 'joy', 'love', 'coal', 'tree', 'red', 'gold']
level_medium = ['angel', 'green', 'candy', 'merry', 'Dasher', 'candle', 'dancer', 'frosty', 'socks', 'carols', 'jolly', 'ribbon', 'light', 'sleigh', 'Vixen', 'holly', 'cookie', 'santa', 'family', 'Donner', 'winter', 'Cupid', 'Comet', 'parade']
level_hard = ['Rudolph', 'Prancer', 'holiday', 'Blitzen', 'NorthPole', 'PolarBear', 'CandyCane', 'decoration', 'WrappingPaper', 'HotChocolate', 'mistletoe', 'celebrate', 'gingerbread', 'christmas', 'stocking', 'present', 'snowman', 'chocolate', 'ornament', 'reindeer']

#SS This function will ask user to input level of difficulty
def how_difficult(): 
    '''(str)->str
    This function allows the player to enter the level of difficulty of choice.
        Each diffuclty is ranked by the number of letters in the word, starting with Easy (3-4 letters), Medium (5-6 letters) and Hard (7+ letters)
        
>>>how_difficult("easy")
>>>how_difficult("medium")
>>>how_difficult("hard")
    '''    
    while True:
        print("Enter level of difficulty: easy, medium or hard")
        difficulty = input()
        if difficulty in ['easy', 'medium', 'hard']:#SS if user inputs easy medium or hard the input is returned
            return difficulty
        else: #SS if the input is not easy medium or hard the loop restarts until the input is correct
            print("Invalid input")
               
#SS This function chooses a random word from the lists based on difficulty
def word_to_be_encrypted():
    '''This function picks a random word from the list of words regarding the difficulty selected by the player.
        This will be the word the player has to decrypt.
    '''    
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
    '''(int)->str
    This function lets you pick the number that your alphabet will be shifted by. This alphabet includes upper case letters followed by lower case letters.
        Therefore, if the player picks the number 3, the entire alpabet will be shifted to the right by 3 letters, (The letter A will become D, B will become E, G will become J, etc.)
 
>>>encryption_key(9)
>>>encryption_key(32)
>>>encryption_key(46)
    '''
    while True:
        key = int(input("Please enter a number between 1 and 52\n")) #SS Changes the input to type int
        if (key >=1 and key <= MAX_KEY_SIZE): #SS Checking to make sure the key is between 1 and 52
            return key #SS If True so if input is an int between 1 and 52 returns the key
        else:
            print("Invalid input") #SS If false asks the user to try again
            
#SR This function asks the user to input how long they'd like the game to last for
def get_delay():
    '''(int)->str
    This function lets the player pick the lenght of the game. 
        This is a way the player can challenge themselves by decrypting as many words as possible in the shortest time.

>>>get_delay(30) 
>>>get_delay(60)
>>>get_delay(90)
    '''           
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
    ''' This function determines when the game is finised. 
            The lenght of the game is determined by the player and once the time is finished, the game will end.
    '''
    game_end = time.time() + delay
    return game_end

#SS Encrypts the r_word, the word that was chosen randomly
def getTranslatedMessage(r_word, key):
    '''(str)->str
    This function will allow the player to decrypt the next word. The new word will then be displayed for the player to decrypt. 
    '''
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
            print("You are correct! Your score is shown below. Your new word is:") 
            r_word = word_to_be_encrypted()
            score = score+50
            print(score)
            message = getTranslatedMessage(r_word, key)
        else:
            print("Please try again")
    elif time.time() >= game_end:
        print('GAME OVER! Your final score was:')
        print(score)
        break
    else:
        break
