money = 0

while(True):
    if(money == 10):
        print ("You have won the game!")
        break
    else:    
        user_choice = input("[1] Mow Lawn with teeth [2] Check Stats [Q] Quit")
    
        if(user_choice == "Q"):
            break
        elif(user_choice == "1"):
            money += 1
            print (f"You have earned $1! Total money: ${money}")
        elif(user_choice == "2"):
            print (f"Current money: ${money}")
    