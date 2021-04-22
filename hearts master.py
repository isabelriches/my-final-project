import random
#all possibilities for what a card could be

previously_played = []
hearts_broken = False
cards = []
points = 0

class card:
 suit = {
  0: "spades",
  1: "hearts",
  2: "diamonds",
  3: "clubs",
  }
 value = {
  2: "two",
  3: "three",
  4: "four",
  5: "five",
  6: "six",
  7: "seven",
  8: "eight",
  9: "nine",
  10: "ten",
  11: "jack",
  12: "queen",
  13: "king",
  14: "ace",
  }
 #all variables set to default

 def __init__(self, suit, value):
  suit = self.suit
  value = self.value

 def equals(self, card):
  self.suit == card.suit
  self.value == card.value
  return self.suit and self.value

class deck:
 suit = {
  0: "spades",
  1: "hearts",
  2: "diamonds",
  3: "clubs",
  }
 value = {
  2: "two",
  3: "three",
  4: "four",
  5: "five",
  6: "six",
  7: "seven",
  8: "eight",
  9: "nine",
  10: "ten",
  11: "jack",
  12: "queen",
  13: "king",
  14: "ace",
  }
 
 def __init__(self):
  self.deck = []
  self.cards = self.initiate_cards()
  self.suit == card.suit
  self.value == card.value
 #creates empty lists
 
 def player_hand(self):
  random.shuffle(self.cards)
  return self.cards
 #changes up order of cards

 def initiate_cards(self):
  cards = []
  for suit in self.suit:
   for value in self.value:
    cards.append(card(suit, value))
    random.shuffle(cards)
    return cards
 #makes sure generated value is reasonable

 def grab_card(self):
  if self.cards:
   return self.cards.pop()
 #removes card

class hand:
 def __init__(self, name):
  self.cards = []
  self.name = name
  self.points = 0
  self.clubs = []
  self.diamonds = []
  self.spades = []
  self.hearts = []
  self.hand = [self.clubs, self.diamonds, self.spades, self.hearts]
 # user's hand defined by different suits

 def dealt_cards(self, card):
  hand_length = len(self.clubs) + len(self.diamonds) + len(self.spades) + len(self.hearts)
  while hand_length < 13:
   choose_suit = random.randrange(0,4)
  if choose_suit == 0:
   self.spades.append(card)
  elif choose_suit == 1:
   self.hearts.append(card)
  elif choose_suit == 2:
   self.diamonds.append(card)
  elif choose_suit == 3:
   self.clubs.append(card)
   self.hand = [self.clubs, self.diamonds, self.spades, self.hearts]
 #adds each drawn card to the designated list

 def holds(self, beginning_card):
  for card in self.cards:
   beginning_card = (card(3,2))
  if card.equals(beginning_card):
    return True
  else:
    return False
 # sets the 2 of clubs as the beginning card
  
class game:
 def __init__(self):
  self.points = 0
  self.deck = deck()
  self.primary_card = None
  self.hearts_broken = False
  self.previously_played = []
  self.first_player = 0
  self.players = self.define_players()
  self.cards = cards
  self.holds = False
  self.clubs = []
  self.diamonds = []
  self.spades = []
  self.hearts = []
  self.hand = [self.clubs, self.diamonds, self.spades, self.hearts]
 
 def define_players(self):
  players = [hand]
  for i in range(4):
   i += 1
   name = input("player name")
   players.append(hand(name))
   return players
 #asks user to name each player

 def starting_player(self):
  for i in range(len(self.players)):
   i += 1
   player = self.players[i]
   if player.holds(card(3,2)):
    return i
 #defines starting player as the one holding the 2 of clubs

 def playable_cards(self):
  if self.holds == True:
   self.clubs.remove(card(3, 2))
   previously_played.append(card(3, 2))
   playable_cards == [card(3, 2)]
  elif self.holds == False:
   if hearts_broken == True:
    playable_cards = self.hand
   elif hearts_broken == False and len(self.clubs) == 0 and len(self.diamonds) == 0 and len(self.spades) == 0:
    playable_cards = self.hand
   else:
    playable_cards = [self.clubs + self.diamonds + self.spades]
 #defines what cards in the user's hand are able to be played

 def round_play(self):
  for i in range(4):
   i += 1
   player = self.players[(self.first_player + i) % 4]
   card_played = player.play_card(self.primary_card, self.hearts_broken)
   print(player.name + " played " + str(card_played))
   if i == 0:
    self.primary_card = card_played
   if card_played.suit == 1:
    self.hearts_broken = True
    self.previously_played.append(card_played)
    sorted(self.previously_played)
    top_card = self.previously_played[0]
    trick_taker = self.players[((self.first_player + self.previously_played.index(top_card))% 4)]
    self.first_player = self.players.index(trick_taker)
    self.primary_card = None
    self.previously_played = []
 #determines who takes a particular trick based on the value of the card
 #alots points based on who took each trick 


  print(self.cards)
  print(self.points)