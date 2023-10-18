import random
turns = ["rock","paper","scisorrs"]
human_turn = input("Enter rock, scissors or paper:")
computer_turn = random.choice(turns)


print("human:" + human_turn +"vs." + "computer:" + computer_turn)
print(f"human: {human_turn}  vs. computer: {computer_turn}")
if human_turn == computer_turn: 
    print("It's a draw!")

elif human_turn == "rock" and computer_turn == "scissors":
    print("Human win!")

elif human_turn == "paper" and computer_turn == "rock":
    print("Human win!")

elif human_turn == "scissors" and computer_turn == "paper":
    print("Human win!")
else:
    print("computer wins!")