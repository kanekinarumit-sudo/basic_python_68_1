"""
#
# Functions
#
"""

def myFullname (firstNmame= "Unknown", lastName="Forger"):
    return firstNmame + " " + lastName

print(myFullname("Tanjiro", "Kamado"))  # Corrected 'priynt' to 'print'
print(myFullname(firstNmame="Loid"))  # Using default parameters
print(myFullname())
print(myFullname(lastName="Smith"))  # Using default parameters
print(myFullname("Anna" ,"Forger"))  # Providing both parameters
print(myFullname("Yor" ,"Forger")) 
print(myFullname("Bond" ,"Forger")) 


def redPotion(hp):
    return hp + 50
def bluePotion(mp):
    return mp + 30

current_hp = 70
print("Current HP:" , current_hp)  # Corrected 'pritnt' to 'print'
current_hp = redPotion(current_hp)
print("After using Red Potion, HP:", current_hp)