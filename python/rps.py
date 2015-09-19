import random;
# get the user input
list = ['rock', 'paper', 'scissors', 'lizard', 'spock']
valid = False
while valid == False :
    player_choice = input("Enter your choice of rock, paper, scissors, lizard or spock: ").lower()
    if(player_choice in list):
        valid = True
print ("Your Choice = ", player_choice) # show the player choice is inputting correctly

#Computer Choice
computer_choice = random.randint (0,4)
# print (computer_choice)
if (computer_choice == 0):
    computer = "rock"
elif (computer_choice == 1):
    computer = "paper"
elif (computer_choice == 2):
    computer = "scissors"
elif (computer_choice == 3):
    computer = "spock"
elif (computer_choice == 4):
    computer = "lizard"

print ("Computer Choice = ", computer) # used to debug code and show random choice

# decide the outcome
if (player_choice == computer):
	print("It's a Draw!")

elif (player_choice == "rock"):
	if (computer == "paper" or computer == "spock"):
		print("The Computer wins!");
	elif(computer == "lizard" or computer == "scissors"):
		print("You win!");

elif (player_choice == "paper"):
	if (computer == "scissors" or computer == "lizard"):
		print("The Computer wins!");
	elif (computer == "rock" or computer == "spock"):
		print("You win!")

elif (player_choice == "scissors"):
	if (computer == "rock" or computer == "spock"):
		print("The Computer wins!");
	elif (computer == "paper" or computer == "lizard"):
		print("You win!");

elif (player_choice == "spock"):
	if (computer == "paper" or computer == "lizard"):
		print("The Computer wins!");
	elif (computer == "rock" or computer == "lizard"):
		print("You win!");

elif (player_choice == "lizard"):
	if (computer == "scissors" or computer == "rock"):
		print("The Computer wins!");
	elif (computer == "paper" or computer == "spock"):
		print("You win!");
