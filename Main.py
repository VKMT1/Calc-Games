import random 
#####################
bank = 1000
#####################
Cards = ["ace"*4, 2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,"jack"*4,"queen"*4,"king"*4]
card_counter_player = 0
card_counter_1_player = 0
card_counter_dealer = 0
card_counter_dealer_1 = 0
ace_counter = 0
players_cards = ""
bust_check = False
#####################

def main():
    print("Welcome to BlackJack")
    print("You start with $1000")



def Stake():
    bet = input(f"Your current balance is ${bank}. What is your bet")
    if bet == int or float:
        bank = bank - bet
    else:
        print("Please enter a valid number")
        Stake()
def deal():
    players_cards = random.choice(Cards * 2) 
    dealer_cards = random.choice(Cards * 2)
    print(f"Your cards are {players_cards}")
    print(f"The dealers card is {dealer_cards[0]}")
 #   
def total_card_number():
    card_counter = 0
    card_counter_1_player_ = 0
    ace_counter = 0
    for _ in players_cards:
        if _ == "ace":
                card_counter + 1
                card_counter_1_player + 11
        elif _ == str and not"ace":
            card_counter + 10
            card_counter_1_player + 10
        elif _ == int:
            card_counter + _
            card_counter_1_player + _
    if card_counter_1_player > card_counter:
        ace_counter + 1

def bust_or_not_player():
    if ace_counter > 0:
        if card_counter_1_player > 21:
            if card_counter > 21:
                print("You bust")
                bust_check = True
            else:
                print(f"You have a total of {card_counter}")
        else:
            print(f"You have a total of {card_counter}")
    else:
        if card_counter > 21:
            print("You bust")
            bust_check = True
        else:
            print(f"You have a total of {card_counter}")