import time
from battles import *
import pygame
# from view2 import *

'''Music commented out because some IDEs have trouble loading the music. Works in Thonny and other IDEs.'''
'''No GUI for text was a design choice. Running the text in the terminal gives it 
more of a retro text-adventure feel'''

#initialize pygame module
pygame.init()

# load and play music track
pygame.mixer.music.load('grieve.mp3')
pygame.mixer.music.play(-1)


def slow_print(dialogue):
    for char in dialogue:
        print(char, end='')
        time.sleep(.00001)


# TODO: Create a GUI that enacts this in its own window
def main():

    # reads and prints script line by line
    with open('scene_1.txt', 'r', encoding='utf-8') as scene_1:
        for line in scene_1:

            # if the next line is empty, wait for the player to press return
            if line.isspace():
                print(line, end='')

            # When the program reads this line, play battle music and start combat
            elif line == "<INTRO BATTLE!>\n":
                pygame.mixer.music.fadeout(5)
                pygame.mixer.music.unload()
                pygame.mixer.music.load('Distort3.mp3')
                pygame.mixer.music.play(-1)

                rove_combat(alex, rove)

                # if the player loses the battle, end the program
                if game_over:
                    break

                # at the end of combat, have the battle music fade out then play overworld track
                pygame.mixer.music.fadeout(5)
                pygame.mixer.music.unload()
                pygame.mixer.music.load('grieve.mp3')
                pygame.mixer.music.play(-1)

            # When the program reads this line, play battle music and start combat
            elif line == "<READY? GO!>\n":
                pygame.mixer.music.fadeout(5)
                pygame.mixer.music.unload()
                pygame.mixer.music.load('gone_feral_take_2.mp3')
                pygame.mixer.music.play(-1)

                cultist_combat(alex, cultist)

                #if the player loses battle, end the program
                if game_over:
                    break

                # at the end of combat, have the battle music fade out then play overworld track
                pygame.mixer.music.fadeout(5)
                pygame.mixer.music.unload()
                pygame.mixer.music.load('grieve.mp3')
                pygame.mixer.music.play(-1)

            # base case, print the line and wait for input
            else:
                slow_print(line)
                input()


if __name__ == "__main__":
    main()
