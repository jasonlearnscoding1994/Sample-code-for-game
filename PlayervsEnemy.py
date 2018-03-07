# Example from Chapter 3, adapted magic8Ball function into a game that takes in a roll value.
# This game involves a player encounter with an enemy and is given the option to attack or run.
# The game ends when either the player or enemy's health drops to or below zero.

import random # This imports the random class from a library.

playerHealth = 20 # Starting health for player.
enemyHealth = 17 # Starting health for enemy.

actions = ['attack', 'hit', 'strike', 'run', 'escape', 'bounce'] # Lmited list of action words the player can use to initiate/terminate the program.

def caseStrip(word): # This function is used to convert all letters from uppercase to lowercase and to remove all punctuations.
    action2 = word.lower() # Uppercase to lowercase.
    caseStrip.action3 = action2.rstrip('?.,!@') # Remove punctuations.

def check(word,list): # This function is used to check whether an action word is associated with "attacking" or "running".
    check.x = 0
    check.y = 0
    if word in list[0:2]: # Check list index from "attack" to "strike"
        print('You move forward to engage the enemy.')
        print('')
        print('~~~~~~START~~~~~~')
        print('Player health: %d' % playerHealth)
        print('Enemy health: %d' %enemyHealth)
        print('~~~~~~~~~~~~~~~~~')
        check.x += 1 # If the words are found, mark it as "correct"
    elif word in list[3:5]: # If not, check list index from "run" to "bounce"
        print('You ran away.')
        check.y += 1 # If the words are found, mark it as "correct"
    else: # If not, say invalid action.
        print('Invalid actions.')

def check2(word,list): # This function is used to recheck whether an action word is associated with "attacking" or "running" later on in the encounter.
    check.z = 0
    if word in list[0:2]:
        print('You continue to engage the enemy.')
        print('')
    elif word in list[3:5]:
        print('You ran away.')
        check.z += 1
    else:
        print('Invalid actions.')

while True: # Loop asks whether an action input has been entered.
    print("You encounter an enemy. Will you attack or run?")
    action = input() # Ask for player input.
    caseStrip(action) # Use function caseStrip to change uppercase to lowercase and remove all punctuations.
    check(caseStrip.action3,actions) # Use function check to compare player input to list of action words.
    if check.x == 1: # If correct "attack" input is entered, break loop.
        break
    elif check.y == 1: # If not, check whether correct "run" input is entered, if so break loop.
        break
    else:
        continue # If not, asks user for inputs again.

print("")

def dealDamage(attackRoll): # Function is used to contain damage numbers dealt by player and expressions.
    if attackRoll == 1:
        return 'Your attack slightly dazes your enemy.'
    elif attackRoll == 2:
        return "Your blade grazes the enemy."
    elif attackRoll == 3:
        return 'Your blow knocks your enemy back.'
    elif attackRoll == 4:
        return "Your blow shatters your enemy's armour leaving a deep gash."
    elif attackRoll == 5:
        return "SCHLING! Your enemy is severely injured by your powerful blow."

def takeDamage(damageRoll): # Function is used to contain damage numbers dealt by enemy and expressions.
    if damageRoll == 1:
        return 'The enemy\'s blade grazes you.'
    elif damageRoll == 2:
        return "The enemy's blade grazes you."
    elif damageRoll == 3:
        return 'You manage to block but the impact knocks you back.'
    elif damageRoll == 4:
        return 'You tried to block but was too late. The impact of the attack breaks a few of your ribs.'
    elif damageRoll == 5:
        return "For a brief moment you felt cold steel. Warm blood gushes out from your deep wound."
    elif damageRoll == 6:
        return "Critical hit. The enemy's sword slids between the gap in your armor impaling you."


while True: # Loop is used to deal damage to player and enemy using a randomly generated number.
    if check.y == 1: # Check if correct "run" action has been entered. If so, break loop.
        break
    else: # If not, run damage calculation.
        dmg = random.randint(1,6) # Damage taken is taken from randomly generated number from 1 to 5.
        print(takeDamage(dmg))
        print("Damage taken by player: %d " % dmg)
        newPlayerHealth = playerHealth - dmg
        print("Player's health: % d" % newPlayerHealth)
        print('')
        atk = random.randint(1,5) # Damage dealt is taken from randomly generated number from 1 to 5
        print(dealDamage(atk))
        print('Damage taken by enemy: %d' % atk)
        newEnemyHealth = enemyHealth - atk
        print('Enemy\'s health: % d' % newEnemyHealth)
        print('')
        print('Player health is: %d' % newPlayerHealth)
        print('Enemy health is: %d' %newEnemyHealth)
        print('')
        if newPlayerHealth > 0 and newEnemyHealth <= 0: # Check to see if player health is more than zero and whether enemy health has dropped below zero, if so, display win text and break loop. Good Game.
            print('YOU WIN.')
            break
        elif newPlayerHealth > 0: # If player health more than zero only, then ask player what to do.
            enemyHealth = newEnemyHealth
            playerHealth = newPlayerHealth
            print ('What is your next course of action? Attack or run?')
            action = input()
            caseStrip(action)
            check2(caseStrip.action3,actions)
            if check.z == 1: # If correct "run" action is received, break loop.
                break
            else: # If not, run loop again.
                continue
        else: # If player health is less than or equal to zero, print you died and break loop. Game Over.
            print('YOU DIED.')
            break
