from cgitb import handler
import random

values = {
    "Two" : 2,
    "Three" : 3,
    "Four" : 4,
    "Five" : 5,
    "Six" : 6,
    "Seven" : 7,
    "Eight" : 8,
    "Nine" : 9,
    "Ten" : 10,
    "Jack" : 11,
    "Queen" : 12,
    "King" : 13,
    "Ace" : 14
}

suits = ('Hearts', 'Clubs', 'Spades', 'Diamonds')

ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')



class Card():
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
        
    def __str__(self):
        return self.rank + " of " + self.suit



class Deck():
    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                created_card = Card(suit,rank)
                self.all_cards.append(created_card)
    
    def shuffle(self):
        random.shuffle(self.all_cards)
        print("Deck was shuffled!")
    
    def deal_a_card(self):
        if len(self.all_cards) >= 1:
            card_dealt = self.all_cards.pop()
            print ("You drew the " + str(card_dealt))
            return card_dealt
        else:
            print("no cards remaining")
            return None

    def no_of_cards(self):
        print(str(len(self.all_cards)) + " Cards remaining.")
    
    def deal_first_hand(self):
        first_card_dealt = self.all_cards.pop()
        second_card_dealt = self.all_cards.pop()
        return [first_card_dealt, second_card_dealt]


class Player():
    def __init__(self, name, id, hand) -> None:
        self.id = id
        self.hand = hand
        self.hand_str = 0
        self.name = name

    def calculate_hand_str(self):
        hand_value = 0
        for card in self.hand:
            hand_value += card.value
        self.hand_str = hand_value

    def show_hand(self):
        temp_hand = []
        for card in self.hand:
            temp_hand.append(str(card))
        final_hand = (',').join(temp_hand)
        return final_hand
    
    def draw_a_card(self, deck):
        return deck.deal_a_card()


def should_i_deal_a_card():
    answer = input("Do you want another card? [Y][n] ") or "Y"
    return answer

print("Welcome to BlackJack.")


def begin_game():
    start_game = input("Want to play? [Y][n] ") or "Y"

    if start_game == "Y" or start_game == "y":
        game_active = True
        print("Game has started!")
    elif start_game == "N" or start_game == "n":
        game_active = False
        print("Game has been cancelled. Exiting Program")
        exit()
    else:
        print("Please enter a valid command('Y', 'N' ) or press enter.")
        input("Want to play? [Y][n]") or "Y"

    while game_active:
        deck = Deck()
        deck.shuffle()
        first_hand = deck.deal_first_hand()
        dealers_hand = deck.deal_first_hand()
        player = Player("player 1", 1, first_hand)
        dealer = Player('Dealer', 2, dealers_hand)
        player.calculate_hand_str()
        dealer.calculate_hand_str()
        print("you have " + player.show_hand())
        print(player.hand_str)
        if dealer.hand_str > 21:
            print("The dealer went over 21! You win!")
            game_active = False
            begin_game()
        if player.hand_str == 21:
            print("You have Blackjack! Congrats! You win!")
            game_active = False
            begin_game()
        elif player.hand_str > 21:
            print("You went over 21! You lose!")
            game_active = False
            begin_game()
        else:
            currently_dealing = True
            while currently_dealing:
                decision = input("Do you want another card? [Y][n] ") or "Y" 
                print("You selected " + decision)
                if decision == "Y" or decision == "y":
                    hand = player.hand 
                    new_card = deck.deal_a_card()
                    hand.append(new_card)
                    player.hand = hand
                    player.calculate_hand_str()
                    print(player.show_hand())
                    print(player.hand_str)
                    if player.hand_str > 21:
                        print("You went over 21! You lose!")
                        game_active = False
                        begin_game()
                    elif player.hand_str == 21:
                        print("You got Blackjack! You win!")
                        game_active = False
                        begin_game()
                elif decision == "N" or decision == "n":
                    currently_dealing = False
                else:
                    print("Enter a valid answer")
                    continue
                
                
            print("The dealer has " + str(dealer.hand_str))        
            print("You have " + str(player.hand_str))
            if dealer.hand_str > player.hand_str:
                print("The dealer wins")
            elif dealer.hand_str == player.hand_str:
                print("It's a tie!")
            elif dealer.hand_str < player.hand_str:
                print("You win!")
        game_active = False
        begin_game()




begin_game()



