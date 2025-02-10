DEBUG = False
DEBUG1 = True



import sys
import os
sys.path.append(os.path.abspath("../../"))
DEBUG and print("--------------------")
DEBUG and print(sys.path)
DEBUG and print("--------------------")


import copy
import random
from datastructures.bag import Bag
from projects.project1.card import Card, Suit, Face

game_on = True


def main():
    one_deck_list = [Card(face, suit) for suit in Suit for face in Face]
    


    ######################################################
    DEBUG and print(f"One deck has {len(one_deck_list)} cards")
    DEBUG and print("".join(str(card) for card in one_deck_list))
    ######################################################



    deck_count = random.choice([2, 4, 6, 8])
    multi_deck_list = [card for _ in range(deck_count) for card in copy.deepcopy(one_deck_list)]
    print("------------1")
    print(type(multi_deck_list))
    print("------------1")


    ######################################################
    DEBUG1 and print(f"{deck_count} decks have {len(multi_deck_list)} cards")
    DEBUG and print("".join(str(card) for card in multi_deck_list))
    ######################################################



    deck_bag = Bag(*multi_deck_list) #unpack list and plug them in individually
    dealer_bag = []
    player_bag = []


    ######################################################
    DEBUG and print("------------1")
    DEBUG and print(deck_bag.distinct_items())
    DEBUG and print(len(deck_bag.distinct_items()))
    DEBUG and print("------------2")
    DEBUG and print(deck_bag.generate_all())
    DEBUG1 and print(len(deck_bag.generate_all()))
    DEBUG and print("------------3")
    ######################################################

    def get_card():
        new_card = random.sample(list(deck_bag.generate_all()), 1)
        print(type(new_card))
        deck_bag.take(new_card)
        return new_card
            
    
    two_cards = random.sample(list(deck_bag.generate_all()), 2)
    DEBUG and print(type(two_cards))
    for item in two_cards:
        DEBUG and print("before taking:", deck_bag.count(item))
        deck_bag.take(item)
        DEBUG and print("after taking:", deck_bag.count(item))
        player_bag.append(item)
    
    one_card = random.sample(list(deck_bag.generate_all()), 1)
    for item in one_card:
        DEBUG and print("before taking:", deck_bag.count(item))
        deck_bag.take(item)
        DEBUG and print("after taking:", deck_bag.count(item))
        dealer_bag.append(item)

    DEBUG and print(type(player_bag))
    DEBUG and print(type(dealer_bag))

    DEBUG1 and print(len(deck_bag.generate_all())," after taking cards.")
    deck_bag.dictionary
    print("Initial deal:")
    print(f"Player's Hand: {"".join(str(card) for card in player_bag)} with a face value of: {sum(card.face.face_value() for card in player_bag)}")
    print(f"Dealer's Hand: {"".join(str(card) for card in dealer_bag)} with a face value of: {sum(card.face.face_value() for card in dealer_bag)}")
    print(" ")

    restart = False

    while True:

        if restart:
            initialize_game()


        print(f"Player's Hand: {"".join(str(card) for card in player_bag)} with a face value of: {sum(card.face.face_value() for card in player_bag)}")
        answer = input("Would you like to (H)it or (S)tay?")

        if answer == "H":
            one_card = random.sample(list(deck_bag.generate_all()), 1)
            for item in one_card:
                deck_bag.take(item)
                DEBUG1 and print(len(deck_bag.generate_all())," after taking cards.")
                player_bag.append(item)
            print(f"Player's Hand: {"".join(str(card) for card in player_bag)} with a face value of: {sum(card.face.face_value() for card in player_bag)}")

            if sum(card.face.face_value() for card in player_bag) > 21:
                print("Dealer won!")

        elif answer == "S":
            while sum(card.face.face_value() for card in dealer_bag) < 17:
                one_card = random.sample(list(deck_bag.generate_all()), 1)
                for item in one_card:
                    deck_bag.take(item)
                    DEBUG1 and print(len(deck_bag.generate_all())," after taking cards.")
                    dealer_bag.append(item)
                print(f"Dealer's Hand: {"".join(str(card) for card in dealer_bag)} with a face value of: {sum(card.face.face_value() for card in dealer_bag)}\n")
            if sum(card.face.face_value() for card in dealer_bag) > 21:
                print("Player won!")
            
            elif sum(card.face.face_value() for card in dealer_bag) == 21:
                pass

        elif answer == "R":
            restart = True
            
        else:
            return False

if __name__ == '__main__':
    main()
    