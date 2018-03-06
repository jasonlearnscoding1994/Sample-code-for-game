# Adapted magic8Ball function, from Chapter 3 Automate the Boring Stuff, into a game that takes in a roll value.
import random
playerHealth = 20
enemyHealth = 10
actions = ['attack', 'hit', 'strike']
i = 0

def caseStrip(word):
    action2 = word.lower()
    caseStrip.action3 = action2.rstrip('?.,!@')

def check(word,list):
    check.x = 0
    if word in list:
        print('You move forward to engage the enemy.')
        print('')
        print('Player health is: %d' % playerHealth)
        print('Enemy health is: %d' %enemyHealth)
        check.x += 1
    else:
        print('Invalid actions.')

def check2(word,list):
    check2.y = 0
    if word in list:
        print('You continue to engage the enemy.')
        print('')
        print('Player health is: %d' % newPlayerHealth)
        print('Enemy health is: %d' %newEnemyHealth)
        check2.y += 1
    else:
        print('Invalid actions.')
        
while True:
    print("You encounter an enemy. What will you do?")
    action = input()
    caseStrip(action)
    check(caseStrip.action3,actions)
    if check.x == 1:
        break
    else:
        continue

print("")

def dealDamage(attackRoll):
    if attackRoll == 1:
        return 'Your attack misses.'
    elif attackRoll == 2:
        return "Your blade grazes the enemy."
    elif attackRoll == 3:
        return 'Your blow knocks your enemy back.'
    elif attackRoll == 4:
        return "Your blow shatters your enemy's armour leaving a deep gash."
    elif attackRoll == 5:
        return "Your enemy is severely injured by your powerful blow."

def takeDamage(damageRoll):
    if damageRoll == 1:
        return 'Attack misses.'
    elif damageRoll == 2:
        return "The enemy's blade grazes you."
    elif damageRoll == 3:
        return 'You manage to block but the impact knocks you back.'
    elif damageRoll == 4:
        return 'You tried to block but was too late. Your armor may be strong but the impact of the attack breaks a few of your ribs'
    elif damageRoll == 5:
        return "For a brief moment you felt cold steel. Warm blood gushes out from your deep wound."
    elif damageRoll == 6:
        return "Critical hit. The enemy's sword slids between the gap in your armor, impaling you in your heart. You passed out from shock and to never wake up again."
    
atk = random.randint(1,5)
print(dealDamage(atk))
print("Damage taken by enemy: %d " % atk)
newEnemyHealth = enemyHealth - atk
print("Enemy's health: % d" % newEnemyHealth)
storeEnemy = newEnemyHealth

print("")

dmg = random.randint(1,5)
print(takeDamage(dmg))
print("Damage taken by player: %d " % dmg)
newPlayerHealth = playerHealth - dmg
print("Player's health: % d" % newPlayerHealth)
storePlayer = newPlayerHealth

print("")



##while newPlayerHealth > 0:
##    print ('What is your next course of action?')
##    action = input()
##    caseStrip(action)
##    check2(caseStrip.action3,actions)
##    dealDamage(atk)
##    if newEnemyHealth == 0:
##        print('YOU ARE VICTORIOUS!')
##    
