import pygame #SR importing the module for pygame

pygame.init() #SR initializing the module

#SR creating screen for the game
screen_width=600
screen_height=500
screen = pygame.display.set_mode((screen_width,screen_height))

#SR setting a name for the game
pygame.display.set_caption('Caesar Cypher')

#SR setting colour for the screen
background_colour = (101,195,113)

#SR creates the colour black that will be used for the alphabet list
Alphabet_colour= (0,0,0)

#SR creates the colour red that will be used for the typed text
text_display_colour= (196,63,63)

#SR setting the font for the different texts that will be displayed
Alphabetlist_font = pygame.font.SysFont("Ariel", 60)
text_display_font = pygame.font.SysFont("didot.tte", 40)

#SR setting the font of the game code that will be displayed
Game_font = pygame.font.SysFont("Ariel", 30)

#SR variable for the text input that will be inputted by the user
user_input_text = " " 

#SR makes the game loop true
running = True

#SR Game loop
while running:
    #SR searches for events that will happen on the computer
    for event in pygame.event.get():
        #SR If the window is closed, the loop ends
        if event.type == pygame.QUIT:
            running = False
        #SR gives value to the keys on the keybpard being pressed
        if event.type == pygame.KEYDOWN:
            #SR Removes a letter from the string if the backspace is pressed
            if event.key == pygame.K_BACKSPACE:
                user_input_text = user_input_text[:-1]
            #SR gives the unicode value to all the other keys and and will add them to the string when pressed
            else:
                user_input_text += event.unicode
        
    #SR sets the colour of the background
    screen.fill(background_colour)
    
    #SR Creates the variable for the list of alphabets with the desired colour black that will be displayed
    Alphabetlist_1 = Alphabetlist_font.render('A B C D E F G H I J K L M', True, Alphabet_colour)
    Alphabetlist_2 = Alphabetlist_font.render('N O P Q R S T U V W X Y Z', True, Alphabet_colour)
    Alphabetlist_3 = Alphabetlist_font.render('a b c d e f g h i j k l m', True, Alphabet_colour)
    Alphabetlist_4 = Alphabetlist_font.render('n o p q r s t u v w x y z', True, Alphabet_colour)
  
    #SR Displays the alphabet listvariable  on the window at the desired locations
    screen.blit(Alphabetlist_1, (50,100))
    screen.blit(Alphabetlist_2, (40,140))
    screen.blit(Alphabetlist_3, (90,180))
    screen.blit(Alphabetlist_4, (75,220))
    
    #SR Creates the variable for the users text input with the desired colour black that will be displayed
    text_display = text_display_font.render( user_input_text, True, text_display_colour)
    
    #SR Displays the variable for the text at the desired location
    screen.blit(text_display, (150,400))
    
    #SR keeps the screen updated
    pygame.display.flip()

#SR Closes the program
pygame.quit()
