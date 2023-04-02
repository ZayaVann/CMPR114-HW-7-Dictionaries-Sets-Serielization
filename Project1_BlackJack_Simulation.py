##################################################################################################################################################
# Program: m7 homework #7 Dictionaries/Sets/Serialization: 1. Blackjack Simulation
# Programmer: Isaiah Vann
# Class: CMPR 114 Spring 2023
# Instructor: Professor Durendal Huynh
# Date: 3/28/23
##################################################################################################################################################

# Previously in this chapter you saw the card_dealer.py program that simulates cards being
# dealt from a deck. Enhance the program so it simulates a simplified version of the game of
# Blackjack between two virtual players. The cards have the following values:
# Numeric cards are assigned the value they have printed on them. For example, the value
# of the 2 of spades is 2, and the value of the 5 of diamonds is 5.
# Jacks, queens, and kings are valued at 10.
# Aces are valued at 1 or 11, depending on the player’s choice.
# The program should deal cards to each player until one player’s hand is worth more than
# 21 points. When that happens, the other player is the winner. (It is possible that both players’
# hands will simultaneously exceed 21 points, in which case neither player wins.) The
# program should repeat until all the cards have been dealt from the deck.
# If a player is dealt an ace, the program should decide the value of the card according to the
# following rule: The ace will be worth 11 points, unless that makes the player’s hand exceed
# 21 points. In that case, the ace will be worth 1 point.

import random

def main():
    # Creating players
    player_hand = 0
    dealer_hand = 0

    # Create a deck of cards.
    deck = create_deck()

    # Creating rules
    blackjack = 21
    soft17 = 17
    othercards = ''
    draw_count = 0

    # Options
    hit = 'h'

    # Get the number of cards to deal.
    num_cards = 1

    # Deal the cards.
# To Player
    print('Card dealt to Player.')
    value_dealt, player_card_1 = deal_cards(deck, num_cards) # Recording value of 1st card
    player_hand = value_dealt
    print(f'The Player wields a value of: {player_hand}.')
    draw_count += 1
    print()

# To Dealer
    print('Card dealt to Dealer.')
    value_dealt, dealer_card_1 = deal_cards(deck, num_cards) # Recording value of 1st card
    dealer_hand = value_dealt
    print(f'The Dealer wields a value of: {dealer_hand}.')
    print()

# Dealing 2nd card Player Again
    print('Card dealt to Player.')
    value_dealt, player_card_2 = deal_cards(deck, num_cards) # Recording value of 2nd card
    player_hand += value_dealt
    print(f'The Player after 2nd card dealt has a hand value of {player_hand}.')
    draw_count += 1
    print()

# Dealing 2nd card Dealer Again
    print('Card dealt to Dealer.')
    value_dealt, dealer_card_2 = deal_cards(deck, num_cards) # Recording value of 2nd card
    dealer_hand += value_dealt
    print('The Dealer reveals their face down card.')
    print(f'There hand value is now at: {dealer_hand}.')
    print()

    # Calculating in accordance to the rules of Blackjack
    while dealer_hand < soft17:
        value_dealt, othercards = deal_cards(deck, num_cards)
        dealer_hand += value_dealt

        # Dealer Lose Condition
        if dealer_hand > blackjack:
            print(f'Dealer has {value_dealt}.')
            print('Dealer has gone Bust!')
            print('Player Won!')
            print('Game Over.')
            quit()
        elif dealer_hand == blackjack:
            print(f'Dealer has {value_dealt}.')
            print('Dealer has Blackjack!')
            print('Player Lost.')
            print('Game Over.')
            quit()
    print()

    # Player Choices
    print(f'Player has {player_hand}.')
    print(f'Dealer has {dealer_hand}.')
    player_option = input('Choose h to Hit or any input to Stand: ')
    if player_option == hit:
        while player_hand < soft17:
            value_dealt, othercards = deal_cards(deck, num_cards)
            player_hand += value_dealt 
        print(f'Player has {player_hand}.')

    else: # Dealer Draws
        value_dealt, othercards = deal_cards(deck, num_cards)
        dealer_hand += value_dealt
   
    # Ultimate Win Condition for Player
    if draw_count == 7 and player_hand <= 21:
        print('\nThe Player has drawn 7 cards without going bust!')
        print('Player Won!')
        print('Game Over.')

    # Player Bust Condition:
    elif player_hand > blackjack:
        print('\nThe Player has gone bust.')
        print('Player Lost.')
        print('Game Over.')

    # Player Bust Condition:
    elif dealer_hand > blackjack:
        print('\nThe Dealer has gone bust!')
        print('Player Won!')
        print('Game Over.')

        # Blackjack Condition 1 for Dealer:
    elif dealer_hand == blackjack:
        print('\nThe dealer has Blackjack!')
        print('Player Lost.')
        print('Game Over.')

        # Blackjack Condition 2 for Dealer:
    elif dealer_card_1 == 'Ace of Spades' or dealer_card_1 == 'Ace of Hearts' or dealer_card_1 == 'Ace of Clubs' or dealer_card_1 == 'Ace of Diamons':
        if dealer_hand == 10:
            print('\nThe dealer has Blackjack!')
            print('Player Lost.')
            print('Game Over.')
    elif dealer_card_2 == 'Ace of Spades' or dealer_card_2 == 'Ace of Hearts' or dealer_card_2 == 'Ace of Clubs' or dealer_card_2 == 'Ace of Diamons':
        if dealer_hand == 10:
            print('\nThe dealer has Blackjack!')
            print('Player Lost.')
            print('Game Over.')
        
        # Blackjack Condition 1 for Player:
    elif player_hand == blackjack:
        print('\nThe Player has Blackjack!')
        print('Player Won!')
        print('Game Over.')

        # Blackjack Condition 2 for Player:
    elif player_card_1 == 'Ace of Spades' or player_card_1 == 'Ace of Hearts' or player_card_1 == 'Ace of Clubs' or player_card_1 == 'Ace of Diamons':
        if dealer_hand == 10:
            print('\nThe dealer has Blackjack!')
            print('Player Lost.')
            print('Game Over.')
    elif player_card_2 == 'Ace of Spades' or player_card_2 == 'Ace of Hearts' or player_card_2 == 'Ace of Clubs' or player_card_2 == 'Ace of Diamons':
        if dealer_hand == 10:
            print('\nThe dealer has Blackjack!')
            print('Player Lost.')
            print('Game Over.')

    # Push Condition (Draw)
    elif dealer_hand == blackjack and player_hand == blackjack:
        print('\nPush.')
        print('Game Over.')

    # Regular Rules:
    # Player Win Condition:
    elif player_hand > dealer_hand:
        print('\nPlayer has more than Dealer.')
        print('Player Won!')
        print('Game Over.')

    # Dealer Win Condition:
    elif player_hand < dealer_hand:
        print('\nPlayer has less than Dealer.')
        print('Player Lost.')
        print('Game Over.')

# The create_deck function returns a dictionary
# rerpesenting a deck of cards.

def create_deck():
    # Create a dictionary with each card and its value
    # stored as key-value pairs.
    deck = {'Ace of Spades': 1, '2 of Spades': 2, '3 of Spades': 3,
            '4 of Spades': 4, '5 of Spades': 5, '6 of Spades': 6,
            '7 of Spades': 7, '8 of Spades': 8, '9 of Spades': 9,
            '10 of Spades': 10, 'Jack of Spades': 10, 
            'Queen of Spades': 10, 'King of Spades': 10,
            
            'Ace of Hearts': 1, '2 of Hearts': 2, '3 of Hearts': 3,
            '4 of Hearts': 4, '5 of Hearts': 5, '6 of Hearts': 6,
            '7 of Hearts': 7, '8 of Hearts': 8, '9 of Hearts': 9,
            '10 of Hearts': 10, 'Jack of Hearts': 10, 
            'Queen of Hearts': 10, 'King of Hearts': 10,
            
            'Ace of Clubs': 1, '2 of Clubs': 2, '3 of Clubs': 3,
            '4 of Clubs': 4, '5 of Clubs': 5, '6 of Clubs': 6,
            '7 of Clubs': 7, '8 of Clubs': 8, '9 of Clubs': 9,
            '10 of Clubs': 10, 'Jack of Clubs': 10, 
            'Queen of Clubs': 10, 'King of Clubs': 10,
            
            'Ace of Diamonds': 1, '2 of Diamonds': 2, '3 of Diamonds': 3,
            '4 of Diamonds': 4, '5 of Diamonds': 5, '6 of Diamonds': 6,
            '7 of Diamonds': 7, '8 of Diamonds': 8, '9 of Diamonds': 9,
            '10 of Diamonds': 10, 'Jack of Diamonds': 10, 
            'Queen of Diamonds': 10, 'King of Diamonds': 10,}
    
    # Return the deck.
    return (deck)

# The deal_cards function deals a sepcified number of cards
# from the deck.

def deal_cards(deck, number):
    # Initialize an accumulator for the hand value.
    hand_value = 0

    # Make sure the number of cards to deal is not
    # greater than the number of cards in the deck.
    if number > len(deck):
        number = len(deck)
    
    # Deal the cards and accumulate their values.
    for count in range(number):
        card = random.choice(list(deck))
        print(card)
        hand_value += deck[card]

    # Returning Hand Value to main
    return (hand_value, card)

# Call the main function
if __name__ == '__main__':
    main()