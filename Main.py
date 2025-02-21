import random

# Constants for the game
INITIAL_BANK = 1000

def create_deck():
    """Creates and shuffles a new deck for the round."""
    deck = ["ace"] * 4 + ["jack"] * 4 + ["queen"] * 4 + ["king"] * 4 + list(range(2, 11)) * 4
    random.shuffle(deck)
    return deck

def calculate_hand(hand):
    """Calculates the total value of a hand, adjusting aces as needed."""
    total = 0
    ace_count = hand.count("ace")
    for card in hand:
        if isinstance(card, int):
            total += card
        elif card in ["jack", "queen", "king"]:
            total += 10
        else:  # card is an ace
            total += 11
    # Adjust for aces if total is over 21
    while total > 21 and ace_count > 0:
        total -= 10
        ace_count -= 1
    return total

def stake(bank):
    """Asks the player to place a bet and updates the bank accordingly."""
    while True:
        try:
            bet = int(input(f"You have ${bank}. How much would you like to bet? "))
            if 0 < bet <= bank:
                bank -= bet
                return bank, bet
            else:
                print(f"Invalid bet amount. You must bet between $1 and ${bank}.")
        except ValueError:
            print("Please enter a valid number.")

def deal(deck):
    """Deals two cards each to the player and the dealer from the deck."""
    players_cards = [deck.pop(), deck.pop()]
    dealers_cards = [deck.pop(), deck.pop()]
    print(f"Your cards: {', '.join(map(str, players_cards))}")
    print(f"Dealer's visible card: {dealers_cards[0]}")
    return players_cards, dealers_cards

def player_turn(players_cards, deck):
    """Simulates the player's turn. Player chooses 'hit' or 'stand'."""
    bust = False
    while True:
        total = calculate_hand(players_cards)
        print(f"Your current total: {total}")
        if total > 21:
            print("You have gone bust!")
            bust = True
            break
        action = input("Do you want to 'hit' or 'stand'? ").lower()
        if action == "hit":
            card = deck.pop()  # draw next card from the deck
            players_cards.append(card)
            print(f"You drew {card}. Your cards: {', '.join(map(str, players_cards))}")
        elif action == "stand":
            print("You chose to stand.")
            break
    return players_cards, bust

def dealer_turn(dealers_cards, deck):
    """Simulates the dealer's turn, drawing until reaching at least 17."""
    bust = False
    print(f"Dealer's full hand: {', '.join(map(str, dealers_cards))}")
    while calculate_hand(dealers_cards) < 17:
        card = deck.pop()
        dealers_cards.append(card)
        print(f"Dealer drew {card}. Dealer's cards: {', '.join(map(str, dealers_cards))}")
        if calculate_hand(dealers_cards) > 21:
            print("The dealer has gone bust!")
            bust = True
            break
    print(f"Dealer's final total: {calculate_hand(dealers_cards)}")
    return dealers_cards, bust

def evaluate_winner(players_cards, dealers_cards, bet, player_bust, dealer_bust, bank):
    """Compares hands and updates the bank based on the outcome."""
    player_total = calculate_hand(players_cards)
    dealer_total = calculate_hand(dealers_cards)
    
    if player_bust:
        print("You lost your bet.")
    elif dealer_bust or player_total > dealer_total:
        print("You win!")
        bank += bet * 2
    elif player_total == dealer_total:
        print("It's a tie! Your bet is returned.")
        bank += bet
    else:
        print("Dealer wins.")
    return bank

def main():
    bank = INITIAL_BANK
    print("Welcome to BlackJack!")
    print(f"You start with ${bank}")
    
    # Main game loop
    while bank > 0:
        # Create a new deck for the round
        deck = create_deck()
        
        # Reset round-specific flags
        player_bust = False
        dealer_bust = False

        bank, bet = stake(bank)
        players_cards, dealers_cards = deal(deck)
        players_cards, player_bust = player_turn(players_cards, deck)
        if not player_bust:
            dealers_cards, dealer_bust = dealer_turn(dealers_cards, deck)
        bank = evaluate_winner(players_cards, dealers_cards, bet, player_bust, dealer_bust, bank)
        print(f"Your new balance is ${bank}\n")
    
    print("Game over! You're out of money.")

if __name__ == "__main__":
    main()
