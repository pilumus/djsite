from random import shuffle

class Card:
    suits = ["Hearts",
             "Clubs",
             "Diamonds",
             "Spades"]

    values = [None, None, "2", "3", "4", "5", "6", "7", "8", "9", "10",
              'Jack', 'Queen', 'King', 'Ace']

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
        # print(value, suit)

    def __lt__(self, c2):
        if self.value < c2.value:
            return True
        if self.value == c2.value:
            if self.suit < c2.suit:
                return True
            else:
                return False
        return False

    def __gt__(self, c2):
        if self.value > c2.value:
            return True
        if self.value == c2.value:
            if self.suit > c2.suit:
                return True
            else:
                return False
        return False

    def __repr__(self):
        # print(self.value, self.suit)
        # print(self.values[self.value], self.suits[self.suit])
        value = self.values[self.value] + " of " + self.suits[self.suit]
        return value

# cards = []
# for i in range(2, 15):
#     for j in range(4):
#         c = Card(i,j)
#         cards.append(c)
#         print(c.suits[c.suit], c.values[c.value])

# print(cards)

# print(Card(2,0))

class Deck:
    def __init__(self):
        self.cards = []
        for i in range(2,15):
            for j in range(4):
                c = Card(i, j)
                self.cards.append(c)
                # print(c)
        shuffle(self.cards)


    def rm_card(self):
        if len (self.cards) == 0:
            print ("Deck is empty")
            return
        return self.cards.pop()

class Player:
    def __init__(self, name):
        self.wins = 0
        self.card = None
        self.name = name

class Game:
    def __init__(self):
        name1 = input('First player name: ')
        name2 = input('Second player name: ')
        self.deck = Deck()
        self.p1 = Player(name1)
        self.p2 = Player(name2)

    def wins(self, winner):
        w = "{} get cards".format(winner)
        print(w)
        print("Score:{}:{} {}:{}".format(self.p1.name, self.p1.wins, self.p2.name, self.p2.wins))
        print("Deck left: {}".format(len(self.deck.cards)))

    def draw(self, p1n, p1c, p2n, p2c):
        d = "{} puts {} and {} puts {}".format(p1n, p1c, p2n, p2c)
        print(d)

    def play_game(self):
        cards = self.deck.cards
        # print(cards)
        print("Lets play!")
        while len(cards) >= 2:
            m = "Press X to quit. Press any key to start."
            response = input(m)
            if response == "X":
                break
            p1c = self.deck.rm_card()
            p2c = self.deck.rm_card()
            p1n = self.p1.name
            p2n = self.p2.name
            self.draw(p1n, p1c, p2n, p2c)
            if p1c > p2c:
                self.p1.wins +=1
                self.wins(self.p1.name)
            else:
                self.p2.wins +=1
                self.wins(self.p2.name)

    def winner(self, p1, p2):
        if p1.wins > p2.wins:
            return p1.name
        if p1.wins < p2.wins:
            return p2.name
        return "Draw!"

game = Game()
game.play_game()

