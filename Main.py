import random 
#####################
bank = 1000
#define the deck of cards
cards = ["ace"] * 4 + ["jack"] * 4 + ["queen"] * 4 + ["king"] * 4 + list(range(2, 11)) * 4
#define and set all counters to 0
card_counter_player = 0
card_counter_1_player = 0
card_counter_dealer = 0
card_counter_dealer_1 = 0
ace_counter_player = 0
ace_counter_dealer = 0
dealer_check = 0
#set all the card variables to empty
players_cards = ""
dealers_cards = ""
#set all the bust checks to false
bust_check_player = False
bust_check_dealer = False
#####################

def main():
    print("Welcome to BlackJack")
    print("You start with $1000")
    while True:
        Stake()
        deal()
        ace_check()
        card_counter()
        bust_check_player()
        bust_check_dealer()
        player_turn()
        dealer_turn()



def Stake():
    global bank
    global bet
    #tell user their bank balance and ask for their bet
    bet = input(f"Your current balance is ${bank}. What is your bet")
    if bet == int or float:
        bank = bank - bet
    else:
    #make sure it is a valid number
        print("Please enter a valid number")
        Stake()
def deal():
    global players_cards
    global dealers_cards
    random.shuffle(cards)   
    players_cards = (", ".join(str(players_cards) for card in random.sample(cards, 2)))
    dealer_cards = (", ".join(str(dealer_cards) for card in random.sample(cards, 2)))
    print(f"Your cards are {players_cards}")
    print(f"The dealers card is {dealer_cards[0]}")
def ace_check():
    ace_counter_dealer = False
    ace_counter_player = False
    for _ in players_cards:
        if _ == "ace":
            ace_counter_player = True
    for _ in dealers_cards:
        if _ == "ace":
            ace_counter_dealer = True
def card_counter():
    global card_counter_player
    global card_counter_1_player
    global card_counter_dealer
    global card_counter_dealer_1
    #define all the variables as 0
    card_counter_player = 0
    card_counter_1_player = 0
    card_counter_dealer = 0
    card_counter_dealer_1 = 0
    #check if there is an ace in the players hand add 1 to the counter and 11 to the other counter
    for _ in players_cards:
        if ace_counter_player == True:
            card_counter_1_player + 11
            card_counter_player + 1
    #check if there is a str in the players hand and add 10 to the counters
        elif ace_counter_player == False and _ == str:
            card_counter_1_player + 10
            card_counter_player + 10
    #if there is no ace or str add the value of the card to the counter
        else:
            card_counter_player + _
            card_counter_1_player + _
    for _ in ace_counter_dealer:
    #check if there is an ace in the dealers hand add 1 to the counter and 11 to the other counter
        if ace_counter_dealer == True:
            card_counter_dealer_1 + 11
            card_counter_dealer + 1
    #check if there is a str in the dealers hand and add 10 to the counters
        elif ace_counter_dealer == False and _ == str:
            card_counter_dealer_1 + 10
            card_counter_dealer + 10
    #if there is no ace or str add the value of the card to the counter
        else:
            card_counter_dealer + _
            card_counter_dealer_1 + _
def bust_check_player():
    global bust_check_player
    global card_counter_player
    global card_counter_1_player
    #set the bust check to false
    bust_check_player = False
    #check if the player has gone bust
    if card_counter_1_player > 21:
        if card_counter_player > 21:
            print("You have gone bust")
            bust_check_player = True
        else: 
            bust_check_player = False
    else:
        bust_check_player = False

def bust_check_dealer():
    global bust_check_dealer
    global card_counter_dealer
    global card_counter_dealer_1
    #set the bust check to false
    bust_check_dealer = False
    #check if the dealer has gone bust
    if card_counter_dealer_1 > 21:
        if card_counter_dealer > 21:
            print("The dealer has gone bust")
            bust_check_dealer = True
        else:
            bust_check_dealer = False
    else:
        bust_check_dealer = False

def player_turn():
    global players_cards
    global card_counter_player
    global card_counter_1_player
    global bust_check_player
    while True:
        player_choice = input("Do you want to hit or stand? ").lower().strip()
        if player_choice == "hit":
            new_card = random.choice(cards)
            players_cards.append(new_card)
            print(f"You drew a {new_card}. Your cards are now: {', '.join(map(str, players_cards))}")
            card_counter()  # Update the card count
            bust_check_player()  # Check if the player has busted
            if bust_check_player:
                print("You lost this round.")
                break
        elif player_choice == "stand":
            print("You chose to stand.")
            break
        else:
            print("Invalid choice, please choose 'hit' or 'stand'.")
def dealer_turn():
    global dealers_cards
    global card_counter_dealer
    global card_counter_dealer_1
    global dealer_check
    print(f"The dealers cards are {dealers_cards}")
    while dealer_check == 0:
        if card_counter_dealer_1 <= card_counter_1_player:
            if card_counter_dealer_1 < 17:
                new_card = random.choice(cards)
                dealers_cards.append(new_card)
                card_counter()
                print(f"The dealer drew a {new_card}. The dealers cards are now: {', '.join(map(str, dealers_cards))}")
            bust_check_dealer()
        elif card_counter_dealer_1 > card_counter_1_player:
            print("The dealer won this round.")
            break
main()