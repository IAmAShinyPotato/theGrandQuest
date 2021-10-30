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


parker = Characters('Parker', "human", 100, 100)
cade = Characters('Cade', "goblin", 50, 100)


# main game code?
def clearScreen():
    print("""
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    """)


def intro():
    delay_print("You find yourself at CAC in the deep night...\n", .1)
    delay_print("But as the arbiter of truth, the harbinger of light...\n", .1)
    delay_print("\nYou will bring peace upon this land.\n", .2)
    delay_print("You are... ", .1)
    time.sleep(3)
    delay_print("P A R K E R.", .25)

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
    delay_print("""
    

    

You awaken in a musty hospital room.
The lights flicker; the faint hum of a broken TV electrifies the still air.
(Enter)""", .05)
    input("")
    delay_print("""

You get up too quickly. You stumble over, grabbing a table for some support.
Looking over on the table, you notice a small calendar.
Vision still fuzzy, you struggle to make out the words:
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

A low rumble reverberates through the halls outside the room.
Fearful for your life, you grab a pair of scissors lying on the ground.

You leave the room, wandering out into the hall.

(Enter)
    """, .05)
    input("")

    delay_print("""

As you turn the corner, you run right into something.
It stumbles back, regains composure, and hisses at you.    
    """, .05)

    print("""
    __   __   __   ____  ____  __________  ___    ____  ______   __________     __________________  ________   __   __   __
   / /  / /  / /  / __ \/ __ \/ ____/ __ \/   |  / __ \/ ____/  /_  __/ __ \   / ____/  _/ ____/ / / /_  __/  / /  / /  / /
  / /  / /  / /  / /_/ / /_/ / __/ / /_/ / /| | / /_/ / __/      / / / / / /  / /_   / // / __/ /_/ / / /    / /  / /  / / 
 /_/  /_/  /_/  / ____/ _, _/ /___/ ____/ ___ |/ _, _/ /___     / / / /_/ /  / __/ _/ // /_/ / __  / / /    /_/  /_/  /_/  
(_)  (_)  (_)  /_/   /_/ |_/_____/_/   /_/  |_/_/ |_/_____/    /_/  \____/  /_/   /___/\____/_/ /_/ /_/    (_)  (_)  (_)   

(Enter)
""")

    input("")


def firstFightSequence():
    firstFightTurn = 0

    while cade.health > 0:

        # player turn
        if firstFightTurn == "parker":
            clearScreen()
            print(f"""
                              Cade
                          {cade.health} / {cade.maxHealth}
        
        
        Parker
        {parker.health} / {parker.maxHealth}
        ┌─────────────────────────┐
        │ 1.) Attack  3.) Item    │
        │                         │
        │ 2.) Defend  4.) Escape  │
        └─────────────────────────┘
            """)
            delay_print("What will you do? ", .05)

            firstFightOption = input("")

            # menu logic
            # attacks
            if firstFightOption == "1":
                clearScreen()
                print(f"""
                              Cade
                          {cade.health} / {cade.maxHealth}
        
        
        Parker
        {parker.health} / {parker.maxHealth}
        ┌─────────────────────────┐
        │ 1.) Stab   2.) Back     │
        └─────────────────────────┘
                """)

                firstAttackOption = input("\nWhat will you do? ")
                if firstAttackOption == "1":
                    firstAttackRoll = random.randint(0, 100)
                    if firstAttackRoll > 80:
                        delay_print("\nCritical Hit!\nYou hit the enemy right in the throat.\n", .05)
                        delay_print("20 dmg.", .05)
                        cade.takeDamage(20)
                        input()
                    elif firstAttackRoll > 20:
                        delay_print("\nYou stab the enemy.\n", .05)
                        delay_print("10 dmg.", .05)
                        cade.takeDamage(10)
                        input()
                    else:
                        delay_print("\nA swing and a miss!\n", .05)
                        delay_print("0 dmg.", .05)
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
                print(f"""
                              Cade
                          {cade.health} / {cade.maxHealth}
        
        
        Parker
        {parker.health} / {parker.maxHealth}
        ┌─────────────────────────┐
        │ 1.) Parry  2.) Back     │
        └─────────────────────────┘
        """)

                firstDefenseOption = input("\nWhat will you do? ")
                if firstDefenseOption == "1":
                    firstDefenseRoll = random.randint(0,100)
                    if firstDefenseRoll > 65:
                        delay_print("\nYou parry the enemy's attack, and manage to swipe at him.\n5 dmg.\n", .05)
                        input()
                        continue
                    else:
                        delay_print("\nYou try to parry the enemy's attack, but he kicks you in the nuts.\nYou take 5 dmg.\n", .05)
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
                print(f"""
                              Cade
                          {cade.health} / {cade.maxHealth}
        
        
        Parker
        {parker.health} / {parker.maxHealth}        
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

                print(f"""
                              Cade
                          {cade.health} / {cade.maxHealth}
        
        
        Parker
        {parker.health} / {parker.maxHealth}        
        ┌─────────────────────────┐
        │ You can't escape!       │
        │ (enter)                 │
        └─────────────────────────┘    
            """)

                input()
                continue

        # cade turn
        elif firstFightTurn == "cade":
            botFirstAttackRoll = random.randint(0,100)
            if botFirstAttackRoll > 90:
                delay_print("\nYou get slashed by the enemy!\n15 dmg.", .05)
                parker.takeDamage(15)
                input()
            elif botFirstAttackRoll > 50:
                delay_print("\nThe enemy swipes at you with their claws.\n5 dmg.", .05)
                parker.takeDamage(5)
                input()
            else:
                delay_print("\nYou sidestep the enemy as he swings at you.\n0 dmg.", .05)
                input()

        if firstFightTurn == "parker":
            firstFightTurn = "cade"
        else:
            firstFightTurn = "parker"


input()


def theGame():
    firstFightSequence()


theGame()

print("end")
