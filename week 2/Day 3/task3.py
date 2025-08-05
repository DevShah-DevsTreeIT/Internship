choices = ["rock","paper","scissor"]
while True:
    
    player1_choice = input("please choose any one from: rock,paper,scissor: ").lower()
    player2_choice = input("please choose any one from: rock,paper,scissor: ").lower()
    
    
    print(f"Player 1 choose: {player1_choice}")
    print(f"Player 2 choose: {player2_choice}")
    
    
    if player1_choice == player2_choice:
        print("It's a Tie")
    
    elif player1_choice == "rock" and player2_choice== "scissor" or player1_choice== "scissor" and player2_choice== "paper" or player1_choice== "paper" and player2_choice== "rock":
        print("player 1 wins")
        
    elif player2_choice== "rock" and player1_choice== "scissor" or player2_choice== "scissor" and player1_choice== "paper" or player2_choice== "paper" and player1_choice== "rock":
        print("player 2 wins")
    else:
        if player1_choice not in choices or player2_choice not in choices:
            print("Invalid input! Please choose from: rock, paper, scissors")

    choice  = input("Want to  restart Y or N: ").lower()
    if choice == "y":
        continue
    else:
        break
