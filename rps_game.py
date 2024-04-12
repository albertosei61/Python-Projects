import random
#create a rock paper scissors, game
#function accepts user input in str
#Create a list of strings list_hands = ["rock", "paper", "scissors"]
#play = input("Enter your hand")
#If play is in list of string:
    #opp_hand = random pick of any string in the list
#print f"Opponent picks: {opp_hand}

 


def rock_paper_scissors():
    list_hands = ["rock", "paper", "scissors"]

    play = input("Play your hand: rock, paper, or scissors: ").strip().lower()
    if play in list_hands:
        opp_hand = random.choice(list_hands)
        if (play, opp_hand) in [("rock", "scissors"), ("scissors", "paper"), ("paper", "rock")]:
            print(f"You won to {opp_hand}")
        elif play == opp_hand:
            print(f"The opponent chose: {opp_hand} \nIt's a draw")
        else:
            print(f"You lost to {opp_hand}")
            
rock_paper_scissors()


















