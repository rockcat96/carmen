
all_tools = [{"tool":"teeth", "profit":1, "cost":0},
             {"tool":"rusty scissors", "profit":5, "cost":5},
             {"tool":"old-timey push lawnmower", "profit":50, "cost":25},
             {"tool":"fancy battery-powered lawnmower", "profit":100, "cost":250},
             {"tool":"a team of starving students", "profit":250, "cost":500}]

player_stats = {"total_money":0, "current_tool":0, "game_round":0}

## create a function for mowing the lawn
def mow_lawn():
    tool = all_tools[player_stats["current_tool"]]
    
    print(f"You got hired to mow the lawn. You used {tool['tool']} and made ${tool['profit']}.")
    player_stats['total_money'] += tool['profit']
    print(f"You currently have saved ${player_stats['total_money']}.")
    player_stats["game_round"] += 1
    
    if((player_stats['total_money'] >= 5 and player_stats['current_tool'] == 0) or (player_stats['total_money'] >= 25 and player_stats['current_tool'] == 1) or (player_stats['total_money'] >= 250 and player_stats['current_tool'] == 2) or (player_stats['total_money'] >= 500 and player_stats['current_tool'] == 3)):
        print(f"You are now eligible to upgrade your current tool to {all_tools[player_stats['current_tool'] + 1]['tool']}. You can upgrade your tool tomorrow by choosing 'Upgrade Tool'.")
        
     

##create a function for checking total money 

def check_stats():
    tool = all_tools[player_stats["current_tool"]]
    upgraded_tool = all_tools[player_stats["current_tool"] + 1]
    
    print(f"You currently have ${player_stats['total_money']} and are using {tool['tool']} to mow the lawn.")
    
    if(upgraded_tool["cost"] <= player_stats["total_money"]):
        print(f"You are now eligible to upgrade your current tool to {upgraded_tool['tool']}. You can upgrade your tool by choosing 'Upgrade Tool'.")
        return 0
    
    print(f"You are ${upgraded_tool['cost'] - player_stats['total_money']} away from the next tool upgrade.")

## create a function for upgrading tools 

def upgrade_tool():
    tool = all_tools[player_stats["current_tool"]]
    upgraded_tool = all_tools[player_stats["current_tool"] + 1]
    
    if(player_stats["current_tool"] == len(all_tools)-1 or upgraded_tool == None):
        print("You have the best tool of the game. No more upgrades available.")
        return 0
        
    
    if(player_stats['total_money'] < upgraded_tool["cost"] ):
        print(f"You don't have enough money to upgrade you tool. You still need ${upgraded_tool['cost'] - player_stats['total_money']}")
        return 0
        
    player_stats["total_money"] -= upgraded_tool["cost"]
    player_stats["current_tool"]+=1
    print(f"Your upgrade is complete and your updated saving is ${player_stats['total_money']}.You can now use {upgraded_tool['tool']} and make ${upgraded_tool['profit']} everytime you mow lawn.")
    
       

## welcome loop
while(player_stats["game_round"] == 0):
    print("Welcome to the landscape game")
    user_name = input("What's your name? ")
    print(f"Hey {user_name}! Congrats on opening up your own landscaping business! You can make money by cutting lawns. To start you can use your teeth to cut lawn. As you make more money, you can upgrade your tool to make money more efficiently. Alright, enough talking, time to get working {user_name}.")
    player_stats["game_round"] += 1
    

## loop for user input and checking win status 
while(player_stats["game_round"] > 0):
    print(f"Start your day {player_stats['game_round']} by choosing the following choices:")
    user_choice = input("[A] Mow Lawn [B] Check Stats [C] Upgrade Tool [Q] Quit ").lower()
    
    if(user_choice == "a"):
        mow_lawn()
    
    if(user_choice == "b"):
        check_stats()
        
    if(user_choice == "c"):
        upgrade_tool()
    
    if(user_choice == "q"):
        print("You quit the game. Thanks for playing.")
        player_stats["game_round"] = -1
        break
    
    if(player_stats['total_money'] >= 1000 and player_stats['current_tool'] == 4):
        print(f"Congrats! You won the game! It took you {player_stats['game_round']} turns to beat the game.")
        break
   
