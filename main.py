import time
import sys
import random


# delaying print so characters come out one at a time
def delay_print(s, t):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(t)


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
def clearScreen():
    for emptyLines in range(0, 100):
        print("\n")

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


def beginnings():

    clearScreen()
    print("*CRASH*")

    time.sleep(1.5)

    delay_print("""
You jolt awake, as the sound of thunder rings in the air.
You look around -- it seems as if you’re in a doctor’s office of some sorts.
The lights flicker on and off, and the hallway outside is completely dark.
""", .05)

    while True:
        beginningsOption1 = input("""
What do you do?
1.) Get up
2.) Go back to sleep

""")

        if beginningsOption1 == "1":
            break
        elif beginningsOption1 == "2":
            delay_print("""
You pull the covers back on yourself, and go to sleep.\n""", .05)
            time.sleep(.5)
            delay_print("\n...\n", 1)
            delay_print("\nYou wake back up to the sound of people talking outside the room.",.05)
            time.sleep(.5)
            delay_print('''
            
"Yes, unfortunately. We are diagnosing Mr. Noyes with 
schizophrenia. However, we do believe Bridgeway is the 
best place for him to stay."''',.05)
            time.sleep(2)
            delay_print("\n\nYou hear someone else sobbing through the door.",.05)
            delay_print("""\n\nBut you chuckle quietly. It doesn't matter what they
think -- after all, you're the Grand Wizard.""",.05)
            time.sleep(2)
            print("""
 _____ _                           _ 
/__   \ |__   ___    ___ _ __   __| |
  / /\/ '_ \ / _ \  / _ \ '_ \ / _` |
 / /  | | | |  __/ |  __/ | | | (_| |
 \/   |_| |_|\___|  \___|_| |_|\__,_|
            """)
            input()
            quit()
        else:
            print("That's not a valid option!")
            continue

    delay_print("""

You get up, but you rise too quickly. You stumble, but
catch yourself by holding onto a desk.

You look over on the table. There's a calendar.
Eyes still fuzzy, you're just barely able to make
out the words on the top:
""", .05)
    time.sleep(1)
    delay_print("""
╔╗ ┬─┐┬┌┬┐┌─┐┌─┐┬ ┬┌─┐┬ ┬  ╦ ╦┌─┐┌─┐┌─┐┬┌┬┐┌─┐┬  
╠╩╗├┬┘│ │││ ┬├┤ │││├─┤└┬┘  ╠═╣│ │└─┐├─┘│ │ ├─┤│  
╚═╝┴└─┴─┴┘└─┘└─┘└┴┘┴ ┴ ┴   ╩ ╩└─┘└─┘┴  ┴ ┴ ┴ ┴┴─┘

(Enter)
    """, .01)
    input("")
    delay_print("""

You wonder to yourself why you're there.
Regardless, you feel a rising urge to leave.
(Enter)""", .05)
    input("")

    time.sleep(3)
    print("\n*CRASH*")
    time.sleep(1)
    delay_print("""
Another crack of thunder makes you jump.
You feel unsafe; you pick up a pair of scissors lying on the floor.

""", .05)

    time.sleep(2)
    delay_print("...",1)
    delay_print("""

You cautiously push the door open, and peek outside.
You're located at the end of a hallway, and there's
only one direction to go.
""",.05)

    delay_print("""
You walk out, and cautiously close the door 
behind you, tightly gripping your scissors.""",.05)

    delay_print("\n\nAs you turn the corner, you run into something.", .05)
    delay_print('''\n\n"Hey pal! I'm walkin' over here!"
Whatever you ran into, it has a thick Bostonian accent.''',.05)

    while True:
        beginningsOption2 = input("""
        
How do you respond?
1.) "Who the heck are you?" (enter the tutorial)
2.) Try and stab him. (skip the tutorial)

""")
        if beginningsOption2 == "1":
            delay_print("""
"Ah, nice to meet you, boyo! I'm Cade, the
Tutorial Goblin!"
""",.05)
            delay_print("""
"I gotta say, pal, you got quite a nice place here, but 
enough of the small talk already. Gimme everything you got!"
(Enter)""",.05)
            input()
            print("""
    __   __   __   ____  ____  __________  ___    ____  ______   __________     __________________  ________   __   __   __
   / /  / /  / /  / __ \/ __ \/ ____/ __ \/   |  / __ \/ ____/  /_  __/ __ \   / ____/  _/ ____/ / / /_  __/  / /  / /  / /
  / /  / /  / /  / /_/ / /_/ / __/ / /_/ / /| | / /_/ / __/      / / / / / /  / /_   / // / __/ /_/ / / /    / /  / /  / / 
 /_/  /_/  /_/  / ____/ _, _/ /___/ ____/ ___ |/ _, _/ /___     / / / /_/ /  / __/ _/ // /_/ / __  / / /    /_/  /_/  /_/  
(_)  (_)  (_)  /_/   /_/ |_/_____/_/   /_/  |_/_/ |_/_____/    /_/  \____/  /_/   /___/\____/_/ /_/ /_/    (_)  (_)  (_)   

(Enter)
""")
            input()
            tutorialFightSequence()
        elif beginningsOption2 == "2":
            break
        else:
            print("That's not an option!")
            input("\n(Enter)")

    print("""
    __   __   __   ____  ____  __________  ___    ____  ______   __________     __________________  ________   __   __   __
   / /  / /  / /  / __ \/ __ \/ ____/ __ \/   |  / __ \/ ____/  /_  __/ __ \   / ____/  _/ ____/ / / /_  __/  / /  / /  / /
  / /  / /  / /  / /_/ / /_/ / __/ / /_/ / /| | / /_/ / __/      / / / / / /  / /_   / // / __/ /_/ / / /    / /  / /  / / 
 /_/  /_/  /_/  / ____/ _, _/ /___/ ____/ ___ |/ _, _/ /___     / / / /_/ /  / __/ _/ // /_/ / __  / / /    /_/  /_/  /_/  
(_)  (_)  (_)  /_/   /_/ |_/_____/_/   /_/  |_/_/ |_/_____/    /_/  \____/  /_/   /___/\____/_/ /_/ /_/    (_)  (_)  (_)   

(Enter)
""")

    input("")


def firstFightSequenceHealth():
    # don't do drugs kids

    healthDashes = 20
    cadeHealthDashes = 16  # i literally cannot figure out why it will not let me get 20 dashes

    # code for parker health dashes
    parkerDashConvert = int(parker.maxHealth / healthDashes)  # divide total health into dashes
    parkerCurrentDashes = int(parker.health / parkerDashConvert)  # convert current health to dashes
    parkerRemainingHealth = healthDashes - parkerCurrentDashes  # calculate empty space in bar

    parkerHealthDisplay = '-' * parkerCurrentDashes  # health display
    parkerRemainingDisplay = ' ' * parkerRemainingHealth
    parkerHealthPercent = str(int((parker.health / parker.maxHealth) * 100)) + "%"  # percentage

    parkerHealthBar = "|" + parkerHealthDisplay + parkerRemainingDisplay + "|"

    # code for cade
    cadeDashConvert = int(cade.maxHealth / cadeHealthDashes)  # divide total health into dashes
    cadeCurrentDashes = int(cade.health / cadeDashConvert)  # convert current health to dashes
    cadeRemainingHealth = cadeHealthDashes - cadeCurrentDashes  # calculate empty space in bar

    cadeHealthDisplay = '-' * cadeCurrentDashes  # health display
    cadeRemainingDisplay = ' ' * cadeRemainingHealth
    cadeHealthPercent = str(int((cade.health / cade.maxHealth) * 100)) + "%"  # percentage

    cadeHealthBar = "|" + cadeHealthDisplay + cadeRemainingDisplay + "|"

    # oh my god this is disgusting
    print(f"""
                       Cade | {cade.monster.title()}
                             {cade.health} / {cade.maxHealth}
             {cadeHealthPercent} {cadeHealthBar}





Parker | {parker.monster.title()}
{parker.health} / {parker.maxHealth}
{parkerHealthBar} {parkerHealthPercent}""")


def firstFightSequence():
    firstFightTurn = 0

    while cade.health > 0 and parker.health > 0:

        # player turn
        if firstFightTurn == "parker":
            clearScreen()
            firstFightSequenceHealth()
            print(f"""
        ┌─────────────────────────┐
        │ 1.) Attack  3.) Item    │
        │                         │
        │ 2.) Defend  4.) Escape  │
        └─────────────────────────┘
            """)
            delay_print("What will you do? ", .01)

            firstFightOption = input("")

            # menu logic
            # attacks
            if firstFightOption == "1":
                clearScreen()
                firstFightSequenceHealth()
                print(f"""
        ┌─────────────────────────┐
        │ 1.) Stab   2.) Back     │
        └─────────────────────────┘
                """)

                firstAttackOption = input("\nWhat will you do? ")
                if firstAttackOption == "1":
                    firstAttackRoll = random.randint(0, 100)
                    if firstAttackRoll > 80:
                        delay_print("\nCritical Hit!\nYou hit the enemy right in the throat.\n", .01)
                        delay_print("20 dmg.", .01)
                        cade.takeDamage(20)
                        input()
                    elif firstAttackRoll > 20:
                        delay_print("\nYou stab the enemy.\n", .01)
                        delay_print("10 dmg.", .01)
                        cade.takeDamage(10)
                        input()
                    else:
                        delay_print("\nA swing and a miss!\n", .01)
                        delay_print("0 dmg.", .01)
                        input()

                elif firstAttackOption == "2":
                    continue
                else:
                    print("That's not a valid option!")
                    print("(Enter)")
                    input("")
                    continue

            # defense
            elif firstFightOption == "2":
                clearScreen()
                firstFightSequenceHealth()
                print(f"""
        ┌─────────────────────────┐
        │ 1.) Parry  2.) Back     │
        └─────────────────────────┘
        """)

                firstDefenseOption = input("\nWhat will you do? ")
                if firstDefenseOption == "1":
                    firstDefenseRoll = random.randint(0, 100)
                    if firstDefenseRoll > 65:
                        delay_print("\nYou parry the enemy's attack, and manage to swipe at him.\n5 dmg.\n", .01)
                        input()
                        continue
                    else:
                        delay_print(
                            "\nYou try to parry the enemy's attack, but he kicks you in the nuts.\nYou take 5 dmg.\n",
                            .01)
                        parker.takeDamage(5)

                elif firstDefenseOption == "2":
                    continue
                else:
                    print("That's not a valid option!")
                    print("(Enter)")
                    input("")
                    continue

            # bag
            elif firstFightOption == "3":
                clearScreen()
                firstFightSequenceHealth()
                print(f"""        
        ┌─────────────────────────┐
        │ Your bag is empty.      │
        │ (enter)                 │
        └─────────────────────────┘
                """)
                input()
                continue

            # escape
            elif firstFightOption == "4":
                clearScreen()
                firstFightSequenceHealth()
                print(f"""        
        ┌─────────────────────────┐
        │ You can't escape!       │
        │ (enter)                 │
        └─────────────────────────┘    
            """)

                input()
                continue

            else:
                delay_print("That's not an option!", .01)
                input()
                continue

        # cade turn
        elif firstFightTurn == "cade":
            botFirstAttackRoll = random.randint(0, 100)
            if botFirstAttackRoll > 90:
                delay_print("\nYou get slashed by the enemy!\n15 dmg.", .01)
                parker.takeDamage(15)
                input()
            elif botFirstAttackRoll > 50:
                delay_print("\nThe enemy swipes at you with their claws.\n5 dmg.", .01)
                parker.takeDamage(5)
                input()
            else:
                delay_print("\nYou sidestep the enemy as he swings at you.\n0 dmg.", .01)
                input()

        if firstFightTurn == "parker":
            firstFightTurn = "cade"
        else:
            firstFightTurn = "parker"


def tutorialFightSequence():
    clearScreen()

    # first tutorial - introduce health
    firstFightSequenceHealth()
    delay_print("""
"Whatcha got here, boyo, are the health bars!"
"Top right, you got my health, and bottom left, you got yours."
(enter)""", .01)
    input()

    # second tutorial - introduce menu
    delay_print('''
"Let's get the battle menu in here real quick."
(enter)''', .01)
    input()

    # third tutorial - introduce input and attack menu
    clearScreen()
    firstFightSequenceHealth()
    print(f"""
            ┌─────────────────────────┐
            │ 1.) Attack  3.) Item    │
            │                         │
            │ 2.) Defend  4.) Escape  │
            └─────────────────────────┘
                """)
    delay_print('''"Right here, boyo, is the battle menu. You can
do all sortsa stuff. Go ahead! Try whalin' on me."
(enter)''', .01)
    input()

    while True:
        clearScreen()
        firstFightSequenceHealth()
        print(f"""
                ┌─────────────────────────┐
                │ 1.) Attack  3.) Item    │
                │                         │
                │ 2.) Defend  4.) Escape  │
                └─────────────────────────┘
                    """)
        delay_print("To enter the attack menu, press 1 and hit enter. ", .01)
        tutorialInput3 = input("")

        if tutorialInput3 != "1":
            delay_print('"Come on pal, use the right number!"', .01)
            input("\n(Enter)")
        else:
            break

    # fourth tutorial - introduce attack menu and do damage
    clearScreen()
    firstFightSequenceHealth()
    print(f"""
            ┌─────────────────────────┐
            │ 1.) Stab   2.) Back     │
            └─────────────────────────┘
                    """)
    delay_print('''"Good job boyo! You got to the attack menu -- now
go ahead, clock me!"
(enter)''', .01)
    input()

    while True:
        clearScreen()
        firstFightSequenceHealth()
        print(f"""
                ┌─────────────────────────┐
                │ 1.) Stab   2.) Back     │
                └─────────────────────────┘
    """)
        tutorialInput4 = input("What do you want to do? ")
        if tutorialInput4 == "1":
            delay_print("""You stab the goblin.
10 dmg.""", .01)
            cade.takeDamage(10)
            delay_print('\n\n"Whoo! Real nice."', .01)
            input("\n(Enter)")
            break
        elif tutorialInput4 == "2":
            delay_print('"Ah, come on now, boyo! You can' + "'" + "t back out now!", .01)
            input("\n(Enter)")
            continue
        else:
            delay_print("You at least gotta choose the right number!", .01)
            input("\n(Enter)")
            continue

    # fifth tutorial - introduce turns
    clearScreen()
    firstFightSequenceHealth()
    delay_print('''
"After your turn, it's obviously my turn.
It wouldn't be fair if all you did was swing at me, right boyo?"
(enter)''', .01)
    input()

    clearScreen()
    firstFightSequenceHealth()
    delay_print("""
The enemy brings out a bright orange and blue dart gun.
You are shot with it.
You take 1 dmg from laughing too hard.
(enter)""", .01)
    parker.takeDamage(1)
    input()

    # sixth tutorial - introduce defense
    clearScreen()
    firstFightSequenceHealth()
    delay_print('''
"Well, pal, you got the hang of navigating menus.
Now, lemme show you what everything else does."''', .01)
    input()

    clearScreen()
    firstFightSequenceHealth()
    print(f"""
            ┌─────────────────────────┐
            │ 1.) Attack  3.) Item    │
            │                         │
            │ 2.) Defend  4.) Escape  │
            └─────────────────────────┘
                    """)
    delay_print('''
"Now, boyo, defense is a gamble.
If you manage to pull off a defense action, you'll
get some damage in, and it'll skip the enemy's turn."
(enter)''', .01)
    input()

    while True:
        clearScreen()
        firstFightSequenceHealth()
        print(f"""
                ┌─────────────────────────┐
                │ 1.) Attack  3.) Item    │
                │                         │
                │ 2.) Defend  4.) Escape  │
                └─────────────────────────┘
                        """)
        tutorialInput6 = input("What would you like to do? ")
        if tutorialInput6 == "1":
            delay_print('"Come on, pal! We just went through attacking!"', .01)
            input("\n(Enter)")
            continue
        elif tutorialInput6 == "2":
            break
        else:
            delay_print('"Come on, pal... you' + "'" + 're getting on my nerves!"', .01)
            input("\n(Enter)")
            continue

    while True:
        clearScreen()
        firstFightSequenceHealth()
        print("""
                ┌─────────────────────────┐
                │ 1.) Parry  2.) Back     │
                └─────────────────────────┘
                """)
        tutorialInput6point5 = input("What would you like to do? ")
        if tutorialInput6point5 == "1":
            delay_print("\nThe goblin rushes at you at a leisurely pace.", .01)
            delay_print("\nYou kick him while he's wide open.\n", .01)
            delay_print("5 dmg.", .01)
            cade.takeDamage(5)
            delay_print('\n"Real nice! Now, my turn gets skipped."', .01)
            input("\n(Enter)")
            break
        else:
            delay_print("You should have the hang of this by now, boyo!", .01)
            input("\n(Enter)")
            continue

    # last tutorial - rest of the menus
    clearScreen()
    firstFightSequenceHealth()
    print(f"""
                ┌─────────────────────────┐
                │ 1.) Attack  3.) Item    │
                │                         │
                │ 2.) Defend  4.) Escape  │
                └─────────────────────────┘""")
    delay_print("""
"Alright, boyo, I'll tell you what the other options do.
When you get some items, you'll be able to use 'em through the "Item" menu.
If you're in a reeeal sticky situation, you might be able to dip using "Escape"."
(Enter)
""", .01)
    input()

    clearScreen()
    firstFightSequenceHealth()
    print(f"""
                ┌─────────────────────────┐
                │ 1.) Attack  3.) Item    │
                │                         │
                │ 2.) Defend  4.) Escape  │
                └─────────────────────────┘""")
    delay_print("""I feel like ya got the hang of this. How 'bout we try this again,
but this time, I'll be real angry. Like, super angry. 
(Enter)""", .01)
    input()

    # send to real battle
    delay_print("""
    Somehow, you feel completely rejuvinated. (You have been healed to max health.)
    """, .01)
    input()
    cade.restoreToFull()
    parker.restoreToFull()

    firstFightSequence()


def mainMenu():

    clearScreen()
    delay_print("Welcome to The Grand Quest!", .01)
    delay_print("\nWhat would you like to do?", .01)

    while True:
        mainMenuOption = input("""
1.) Start Game
2.) Load Game
3.) READ BEFORE PLAYING
4.) Quit

""")

        if mainMenuOption == "1":
            beginnings()
        elif mainMenuOption == "2":
            while True:
                delay_print("""
Where would you like to load to?
1.) Act I: Where Am I?
2.) Act II: Unavailable
Q.) Return to main menu
""",.01)
                loadOption = input("")
                if loadOption == "1":
                    beginnings()
                elif loadOption == "2":
                    print("That's not available right now.")
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
 (Enter)""",.03)
            input()
            delay_print("""
If you're using an online compiler such as OnlineGDB or Programiz,
you may want to set your browser size to around 70% or even lower.

Ignoring these options may mean that ASCII art will be distorted.

Other than that, thanks for playing!
(Enter)
""",.03)
            input()
            continue
        elif mainMenuOption == "4":
            quit()
        else:
            print("That's not a valid option!")


mainMenu()

input()

print("end")
