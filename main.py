from act1 import *


# init class for all mobs
class Characters:
    def __init__(self, name, monster, health, maxHealth):
        self.name = name
        self.monster = monster
        self.health = health
        self.maxHealth = maxHealth

    def takeDamage(self, atkDamage):
        self.health -= atkDamage

    def heal(self, healing):
        self.health += healing

    def restoreToFull(self):
        self.health = self.maxHealth


parker = Characters('Parker', "human", 100, 100)
cade = Characters('Cade', "goblin", 50, 50)


# main game code

def intro():
    delay_print("You find yourself at CAC in the deep night...\n", .05)
    delay_print("But as the arbiter of truth, the harbinger of light...\n", .05)
    delay_print("\nYou will bring peace upon this land.\n", .05)
    delay_print("You are... ", .1)
    time.sleep(3)
    delay_print("P A R K E R.", .2)

    delay_print("""
                                   ,     :     ,
                              '.    ;    :    ;    ,`
                          '-.   '.   ;   :   ;   ,`   ,-`
                       "-.   '-.  '.  ;  :  ;  ,`  ,-`   ,-"
                          "-.   '-. '. ; : ; ,` ,-`   ,-"
                     '"--.   '"-.  '-.'  '  `.-`  ,-"`   ,--"`
                          '"--.  '"-.   ...   ,-"`  ,--"`
                               '"--.  .:::::.  ,--"`
                    ------------------:::::::------------------
 _____ _   _  _____   _____ ______  ___   _   _______   _____ _   _ _____ _____ _____ 
|_   _| | | ||  ___| |  __ \| ___ \/ _ \ | \ | |  _  \ |  _  | | | |  ___/  ___|_   _|
  | | | |_| || |__   | |  \/| |_/ / /_\ \|  \| | | | | | | | | | | | |__ \ `--.  | |  
  | | |  _  ||  __|  | | __ |    /|  _  || . ` | | | | | | | | | | |  __| `--. \ | |  
  | | | | | || |___  | |_\ \| |\ \| | | || |\  | |/ /  \ \/' / |_| | |___/\__/ / | |  
  \_/ \_| |_/\____/   \____/\_| \_\_| |_/\_| \_/___/    \_/\_\ ___/\____/\____/  \_/    

    """, .001)

    input("Press enter to continue.")


def mainMenu():
    clearScreen()
    delay_print("Welcome to The Grand Quest!", .01)
    delay_print("\n\nWhat would you like to do?", .01)

    while True:
        mainMenuOption = input("""

1.) Start Game
2.) Load Game
3.) READ BEFORE PLAYING
4.) Watch intro sequence
5.) Quit

""")

        if mainMenuOption == "1":
            beginnings()
        elif mainMenuOption == "2":
            while True:
                delay_print("""
Where would you like to load to?
================================
1.) Act I, Scene 1: Where Am I?
2.) Act I, Scene 2: Cade's Tutorial
3.) Act I, Scene 3: Goblin Fight?!
4.) Act II: Unavailable
Q.) Return to main menu
""", .01)
                loadOption = input("")
                if loadOption == "1":
                    beginnings()
                elif loadOption == "2":
                    tutorialFightSequence()
                elif loadOption == "3":
                    firstFightSequence()
                elif loadOption == "4":
                    print("That's currently unavailable.")
                    continue
                elif loadOption == "Q":
                    break
                else:
                    print("That's not a valid option!")
                    continue
            continue
        elif mainMenuOption == "3":
            delay_print("""
This game is best played with a short and wide aspect ratio.
This means that your window should be set like this:
┌───────────────┐
│               │
│               │
└───────────────┘
and not like this:
 ┌───┐
 │   │
 │   │
 │   │
 │   │
 └───┘
 Generally, you will want it to be as wide as possible.
 Ignoring these options may cause distortions of ASCII art.
 
 Other than that, thanks for playing!
 (Enter)""", .02)
            input()
            continue
        elif mainMenuOption == "4":
            intro()
        elif mainMenuOption == "5":
            quit()
        else:
            print("That's not a valid option!")


if __name__ == "__main__":
    mainMenu()

print("end")
