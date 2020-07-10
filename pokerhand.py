"""
A famous casino is suddenly faced with a sharp decline of their revenues. They decide to offer Texas hold'em also online. Can you help them by writing an algorithm that can rank poker hands?

Task
Create a poker hand that has a method to compare itself to another poker hand:

compare_with(self, other_hand)
A poker hand has a constructor that accepts a string containing 5 cards:

PokerHand("KS 2H 5C JD TD")
The characteristics of the string of cards are:

Each card consists of two characters, where
The first character is the value of the card: 2, 3, 4, 5, 6, 7, 8, 9, T(en), J(ack), Q(ueen), K(ing), A(ce)
The second character represents the suit: S(pades), H(earts), D(iamonds), C(lubs)
A space is used as card separator between cards
The result of your poker hand compare can be one of these 3 options:

[ "Win", "Tie", "Loss" ]
Notes
Apply the Texas Hold'em rules for ranking the cards.
Low aces are NOT valid in this kata.
There is no ranking for the suits.
If you finished this kata, you might want to continue with Sortable Poker Hands
"""

class PokerHand(object):

    RESULT = ["Loss", "Tie", "Win"]

    def __init__(self, hand):
        self.hand = hand.split()
        self.nums = sorted([int(c[0].translate(str.maketrans({
            'A': '14', 'T': '10', 'J': '11', 'Q': '12', 'K': '13'
        }))) - 1 for c in self.hand])
        self.suits = [c[1] for c in self.hand]

        unique_nums = set(self.nums)
        unique_suits = set(self.suits)

        score = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        if len(unique_suits) == 1:
            score[4] = 1  # flush
        if len(unique_nums) == 5:
            if self.nums[0] + 4 == self.nums[4] or self.nums in [
                [1,2,3,4,13],[1,2,3,12,13],[1,2,11,12,13],[1,10,11,12,13]
            ]:
                score[5] = 1  # straight
            else:
                score[9] = 1  # no pair
        if len(unique_nums) == 4:
            score[8] = 1  # one pair
        if len(unique_nums) == 3:
            if 3 in [self.nums.count(i) for i in tuple(unique_nums)]:
                score[6] = 1  # three card
            else:
                score[7] = 1  # two pair
        if len(unique_nums) == 2:
            if self.nums.count(tuple(unique_nums)[1]) == 2 | 3:
                score[3] = 1  # full house
            else:
                score[2] = 1  # four card
        if score[4:5 + 1] == [1, 1]:
            if self.nums[0] == 9:
                score[0] = 1  # royal flush
            else:
                score[1] = 1  # straight flush

        self.score = score.index(1)


    def compare_with(self, other):
        if self.score < other.score:
            return('Win')
        elif self.score > other.score:
            return("Loss")
        # same score below
        elif self.score == 0:
            return("Tie")
        elif self.score == 1 | 5 | 9:
            if self.nums[4] > other.nums[4]:
                return('Win')
            if self.nums[4] < other.nums[4]:
                return('Loss')
            if self.nums[4] == other.nums[4]:
                return('Tie')
        else:
            return('Tie')

# Dealing with 'Tie' incomplete...


class PokerHand_answer(object):
    CARD = "23456789TJQKA"
    RESULT = ["Loss", "Tie", "Win"]

    def __init__(self, hand):
        values = ''.join(sorted(hand[::3], key=self.CARD.index))
        suits = set(hand[1::3])
        is_straight = values in self.CARD
        is_flush = len(suits) == 1
        self.score = (2 * sum(values.count(card) for card in values)
                      + 13 * is_straight + 15 * is_flush,
                      [self.CARD.index(card) for card in values[::-1]])

    def compare_with(self, other):
        return self.RESULT[(self.score > other.score) - (self.score < other.score) + 1]

hand = "2H 3H 4H 5H 6H"
print(PokerHand_answer(hand).score)
others = (38, [0, 3, 2, 1, 0])
print(PokerHand_answer(hand).score > others)
