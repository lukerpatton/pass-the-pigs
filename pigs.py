#this is needed for using random's functions
import random
import time


player_score_total = 0
player_total_turns = 0
end_score = 100

computer_score_total = 0
computer_total_turns = 0
computer_target = 15


def roll_dice():
    roll = random.randint(1,6)
    return roll
    
    
def evaluate_roll(roll):
    if (roll == 1):
        print("You Rolled a 1. Pig Out.")
        print("")
    else:
        print("Dice Roll: " + str(roll))
        print("")
    
    
def player_turn():
    
    # reference global variables
    global player_score_total, player_total_turns
    
    # turn variables
    player_turn_points = 0
    player_total_turns = player_total_turns + 1
    
    # display
    print("Your Turn Number: " + str(player_total_turns))
    print("Your Total Score: " + str(player_score_total))
    print("")
    
    while True:

        choice = input("roll again (r) or bank the points (b) ?")
        
        if choice == "b":
            player_score_total = player_score_total + player_turn_points
            print("")
            print("You've banked " + str(player_turn_points) + " points")
            print("Your total score is now " + str(player_score_total))
            print("")
            break

        elif choice == "r":
            
            # roll dice & display value
            my_roll = roll_dice()
            print("")
            print("You rolled a " + str(my_roll))
            
            if my_roll == 1:
                print("Pig Out!")
                print("")
                break
            else:
                player_turn_points = player_turn_points + my_roll
                print("Your round score is now " + str(player_turn_points))
                print("Your total score is now " + str(player_score_total + player_turn_points))
                print("")
                
        else:
            print("nuh uh try again.")
            print("")

def computer_turn():
    
    # reference global variables
    global computer_score_total, computer_total_turns
    
    # turn variables
    computer_turn_points = 0
    computer_total_turns = computer_total_turns + 1
    
    # display
    print("Computer Turn Number: " + str(computer_total_turns))
    print("Computer Total Score: " + str(computer_score_total))
    print("")
    
    while True:

        if (computer_turn_points < computer_target):
            choice = "r"
            time.sleep(1)
        else:
            choice = "b"
            
        if choice == "b":
            computer_score_total = computer_score_total + computer_turn_points
            print("")
            print("Computer banked " + str(computer_turn_points) + " points")
            print("Computer total score is now " + str(computer_score_total))
            print("")
            break

        elif choice == "r":
            
            # roll dice & display value
            my_roll = roll_dice()
            print("")
            print("Computer rolled a " + str(my_roll))
            
            if my_roll == 1:
                print("Computer Pigged Out!")
                print("")
                break
            else:
                computer_turn_points = computer_turn_points + my_roll
                print("Computer round score is now " + str(computer_turn_points))
                print("Computer total score is now " + str(computer_score_total + computer_turn_points))
                print("")
        else:
            print("nuh yhu try again.")
            print("")


# START - PLAY PIGS
while ((player_score_total < end_score) and (computer_score_total < end_score)):
    player_turn()
    computer_turn()
print("GAME OVER!")

if (player_score_total > computer_score_total):
    print ("CONGRATULATIONS! YOU WIN!")
    print("You won in " + str(player_total_turns) + " turns")
elif (player_score_total < computer_score_total):
    print ("SORRY! YOU LOST!")
    print("You lost in " + str(player_total_turns) + " turns")
else:
    print ("WHOA! Tie Match.")
    print("You tied in " + str(player_total_turns) + " turns")

print("")
print ("Your final score:     " + str(player_score_total))
print ("Computer final score: " + str(computer_score_total))
