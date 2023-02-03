game = {"equipment": 0, "money": 0}

# Player possible equipment
equipments = [
    { "name": "Teeth", "price": 0, "money": 1}, 
    { "name": "Rusty Scissors","price": 5, "money": 5 },
    { "name": "Old-timey push lawnmower", "price": 25, "money": 50 },
    { "name": "Fancy battery-powered lawnmower", "price": 250, "money": 100 },
    { "name": "Team of starving students", "price": 500, "money": 250 }
]


# Game Options 

def cut_grass():
    equipment = equipments[game["equipment"]]
    print(f"You cut the grass with {equipment['name']} and make ${equipment['money']}!")
    game["money"] += equipment["money"]
    
def check_stats():
    equipment = equipments[game["equipment"]]
    print(f"You have ${game['money']} and are using {equipment['name']}.")
    
def upgrading():
    if (game["equipment"] >= len(equipments) - 1):
        print('You have all the equipments')
    next_equipment = equipments[game["equipment"] + 1]
    if (next_equipment == None):
        print("You have all the equipments.")
        return 0
    if (game["money"] < next_equipment["price"]):
        print(f"Not enough money, need ${next_equipment['price']} for {next_equipment['name']}")
        return 0
    game["money"] -= next_equipment["price"]
    print(f"You upgraded to {next_equipment['name']}!")    
    game["equipment"] += 1

    
def win_check():
    if(game["equipment"] == 4 and game["money"] >= 1000):
        print("You have won the game!")
        return True
    return False

print ("The Lawn-Mowing Game! Get all the upgrades and $1000 to win!")

while (True):
    
    user_choice = input(f"[1] Cut Grass [2] Check Stats [3] Upgrade [Q] Quit")
    
    if (user_choice == "1"):
        cut_grass()
        
    if (user_choice == "2"):
        check_stats()
        
    if (user_choice == "3"):
        upgrading()
        
    if (user_choice == "Q"):
        print("You quit the game")
        break
    if (win_check()):
        break