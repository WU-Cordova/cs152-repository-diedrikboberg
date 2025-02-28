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

    #restart = False
    continue_game = True
    while continue_game:

        one_deck_list = [Card(face, suit) for suit in Suit for face in Face]
        


        ######################################################
        DEBUG and print(f"One deck has {len(one_deck_list)} cards")
        DEBUG and print("".join(str(card) for card in one_deck_list))
        ######################################################



        deck_count = random.choice([2, 4, 6, 8])
        multi_deck_list = [card for _ in range(deck_count) for card in copy.deepcopy(one_deck_list)]
        DEBUG and print("------------1")
        DEBUG and print(type(multi_deck_list))
        DEBUG and print("------------1")


        ######################################################
        DEBUG and print(f"{deck_count} decks have {len(multi_deck_list)} cards")
        DEBUG and print("".join(str(card) for card in multi_deck_list))
        ######################################################



        deck_bag = Bag(*multi_deck_list) #unpack list and plug them in individually
        dealer_bag = []
        player_bag = []

        def value_player_hand():
            total_value = 0
            ace_present = False
            

            for card in player_bag:
                total_value += card.face.face_value()
                if str(card) == "[A❤️]" or str(card) == "[A♠️]" or str(card) == "[A♣️]" or str(card) == "[A♦️]":
                    #print("Ace in hand.")
                    #print(card)
                    ace_present = True
            
            if total_value > 21 and ace_present:
                total_value = total_value - 10
                
            #value_player_hand = sum(card.face.face_value() for card in player_bag)
            
            return total_value

            
            #return value_player_hand

        def value_dealer_hand():
            value_dealer_hand = sum(card.face.face_value() for card in dealer_bag)
            return value_dealer_hand

        ######################################################
        DEBUG and print("------------1")
        DEBUG and print(deck_bag.distinct_items())
        DEBUG and print(len(deck_bag.distinct_items()))
        DEBUG and print("------------2")
        DEBUG and print(deck_bag.get_full_bag())
        DEBUG and print(len(deck_bag.get_full_bag()))
        DEBUG and print("------------3")
        ######################################################

        def get_card():
            new_card = random.sample(list(deck_bag.get_full_bag()), 1)
            print(type(new_card))
            deck_bag.take(new_card)
            return new_card
        
        def dealer_picks():
            while value_dealer_hand() < 17:

                one_card = random.sample(list(deck_bag.get_full_bag()), 1)
                for item in one_card:
                    deck_bag.take(item)
                    DEBUG and print(len(deck_bag.get_full_bag())," after taking cards.")
                    dealer_bag.append(item)
            print(f"Dealer's Hand: {"".join(str(card) for card in dealer_bag)} with a face value of: {value_dealer_hand()}")
                
        
        two_cards = random.sample(list(deck_bag.get_full_bag()), 2)
        DEBUG and print(type(two_cards))
        for item in two_cards:
            DEBUG and print("before taking:", deck_bag.count(item))
            deck_bag.take(item)
            DEBUG and print("after taking:", deck_bag.count(item))
            player_bag.append(item)
        
        one_card = random.sample(list(deck_bag.get_full_bag()), 1)
        for item in one_card:
            DEBUG and print("before taking:", deck_bag.count(item))
            deck_bag.take(item)
            DEBUG and print("after taking:", deck_bag.count(item))
            dealer_bag.append(item)

        DEBUG and print(type(player_bag))
        DEBUG and print(type(dealer_bag))

        DEBUG and print(len(deck_bag.get_full_bag())," after taking cards.")
        deck_bag.dictionary
        print("Initial deal:")
        print(f"Player's Hand: {"".join(str(card) for card in player_bag)} with a face value of: {value_player_hand()}")
        print(f"Dealer's Hand: {"".join(str(card) for card in dealer_bag)} with a face value of: {value_dealer_hand()}")
        print(" ")

    
        #if restart:
        #    initialize_game()


        print(f"Player's Hand: {"".join(str(card) for card in player_bag)} with a face value of: {value_player_hand()}")
        answer = input("Would you like to (H)it or (S)tay?")
        still_on = True

        while still_on:
            
            if answer == "H":
                one_card = random.sample(list(deck_bag.get_full_bag()), 1)
                for item in one_card:
                    deck_bag.take(item)
                    DEBUG and print(len(deck_bag.get_full_bag())," after taking cards.")
                    player_bag.append(item)
                print(f"Player's Hand: {"".join(str(card) for card in player_bag)} with a face value of: {value_player_hand()}")
            
                if value_player_hand() > 21:

                    print("Dealer won!")
                    
                    rematch = input("Play again? (Y)es or (N)o.")

                    if rematch == "Y":
                        #continue
                        still_on = False
                

                    elif rematch == "N":
                        continue_game = False
                
                elif value_player_hand() == 21:
                    dealer_picks()
                    if value_dealer_hand() == 21:
                        print("It's a tie.")

                        rematch = input("Play again? (Y)es or (N)o.")

                        if rematch == "Y":
                            #continue
                            still_on = False

                        elif rematch == "N":
                            continue_game = False
                
                    else:   
                        print("Player won!")
                    
                        rematch = input("Play again? (Y)es or (N)o.")

                        if rematch == "Y":
                            #continue
                            still_on = False

                        elif rematch == "N":
                            continue_game = False
                
                else:
                    answer = input("Would you like to (H)it or (S)tay?")
                    
                
            


            if answer == "S":
                
                dealer_picks()
                print("dealer has picked.")
                if value_dealer_hand() > 21:
                    print("Player won!")
                    
                    rematch = input("Play again? (Y)es or (N)o.")

                    if rematch == "Y":
                        #continue
                        still_on = False

                    elif rematch == "N":
                        continue_game = False
                
                elif value_dealer_hand() == 21:
                    if value_player_hand() != 21:
                        print("Dealer won!")
                    
                        rematch = input("Play again? (Y)es or (N)o.")

                        if rematch == "Y":
                            #continue
                            still_on = False

                        elif rematch == "N":
                            continue_game = False

                elif value_dealer_hand() < 21:
        
                    if 21 - value_player_hand()  > 21 - value_dealer_hand():
                        print("Dealer won!")
                        
                        rematch = input("Play again? (Y)es or (N)o.")

                        if rematch == "Y":
                            #continue
                            still_on = False

                        elif rematch == "N":
                            continue_game = False

                    elif 21 - value_player_hand()  < 21 - value_dealer_hand():
                        print("Player won!")
                        
                        rematch = input("Play again? (Y)es or (N)o.")

                        if rematch == "Y":
                            #continue
                            still_on = False

                        elif rematch == "N":
                            continue_game = False
                    
                elif value_dealer_hand == value_player_hand():
                    print("It's a tie.")

                    rematch = input("Play again? (Y)es or (N)o.")

                    if rematch == "Y":
                        #continue
                        still_on = False

                    elif rematch == "N":
                        continue_game = False

                else:
                    print(value_dealer_hand)
                    print(value_player_hand)
                        

if __name__ == '__main__':
    main()
    