# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 14:45:19 2021

@author: admin
"""

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

#SR setting the font of the alphabet that will be displayed
Alphabetlist_font = pygame.font.SysFont("Ariel", 60)

#SR setting the font of the game code that will be displayed
Game_font = pygame.font.SysFont("Ariel", 30)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill(background_colour)
    
    #SR Creates the list of alphabets with the desired colour black  
    Alphabetlist_1= Alphabetlist_font.render('A B C D E F G H I J K L M', True, Alphabet_colour)
    Alphabetlist_2= Alphabetlist_font.render('N O P Q R S T U V W X Y Z', True, Alphabet_colour)
    Alphabetlist_3= Alphabetlist_font.render('a b c d e f g h i j k l m', True, Alphabet_colour)
    Alphabetlist_4= Alphabetlist_font.render('n o p q r s t u v w x y z', True, Alphabet_colour)
  
    #SR Displays the alphabet list on the window at the desired locations
    screen.blit(Alphabetlist_1, (50,100))
    screen.blit(Alphabetlist_2, (40,140))
    screen.blit(Alphabetlist_3, (90,180))
    screen.blit(Alphabetlist_4, (75,220))
    
    #Game= Game_font.render(, True, Alphabet_colour)
    
    pygame.display.flip()


pygame.quit()