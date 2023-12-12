## Advent of Code 2023 Day 7: Camel Cards
## @curiouskiwi 7 Dec 2023

FIVEKIND =  7
FOURKIND = 6
FULLHOUSE = 5
THREEKIND = 4
TWOPAIR = 3
PAIR = 2
HIGH = 1


def main():

    hands = []

    with open('7.txt', 'r') as f:
        allhands = f.readlines()

    for item in allhands:
        cards, bid = item.split()
        hand = {'cards': cards, 
                'bid': bid, 
                'score': score_hand(cards), 
                'values': values(cards),
                }
        hands.append(hand)
    # print(hands)


    # Part 1
    # sort hands by score then card values
    # if two hands have the same score, then the one with the higher value first card,etc.
    sorted_hands = sorted(hands, key=lambda x: (x['score'], x['values']))
    print("Part 1:", winnings(sorted_hands))
    
    # Part 2
    # adjust value accounting for J and then calculate joker_score
    for hand in hands:
        hand['values'] = values(hand['cards'], 2)
        noJ = ''.join(c for c in hand['cards'] if c != 'J')
        hand['jokerscore'] = joker_score(noJ, hand['cards'].count('J'))
    # sort hands by jokerscore then card values
    sorted_joker = sorted(hands, key=lambda x: (x['jokerscore'], x['values']))
    print("Part 2:", winnings(sorted_joker))


# determine values based on card label (to use as secondary sort)
def values(cards, part=1):
    """Calculate the value of a hand."""

    card_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    if part == 2:
        card_values['J'] = 1

    value = []
    for card in cards:
        value.append(card_values[card])
    return value


def score_hand(cards):
    """Calculate the score of a hand."""

    # Initialize dictionaries to count the occurrences of each label.
    label_count = {}

    # Split the string into individual cards.
    cards = list(cards)

    # Iterate through the cards to count labels
    for card in cards:
        label_count[card] = label_count.get(card, 0) + 1
    
    card_counts = label_count.values()

    # Determine the best hand based on the card count.
    if 5 in card_counts:
        return FIVEKIND
    if 4 in card_counts:
        return FOURKIND
    if 3 in card_counts and 2 in card_counts:
        return FULLHOUSE
    if 3 in card_counts:
        return THREEKIND
    if list(card_counts).count(2) == 2:
        return TWOPAIR
    if 2 in card_counts:
        return PAIR
    return HIGH


# takes in the cards without the Js and the number of Js
def joker_score(cards, numJ):
    """Calculate the score of a hand with jokers."""

    # if there is a 'J', it can be any other card to maximize the score
    best_so_far = score_hand(cards)
    
    if numJ == 0:
        return best_so_far
    
    if numJ == 1:
        if best_so_far == HIGH:
            return PAIR
        if best_so_far == PAIR:
            return THREEKIND
        if best_so_far == TWOPAIR:
            return FULLHOUSE
        if best_so_far == THREEKIND:
            return FOURKIND

    elif numJ == 2:
        if best_so_far == HIGH:
            return THREEKIND
        if best_so_far == PAIR:
            return FOURKIND
    
    elif numJ == 3:
        if best_so_far == HIGH:
            return FOURKIND
    
    # in every other case, you get a five of a kind
    return FIVEKIND


def winnings(hands):
    """Calculate the total winnings for a list of hands."""

    total_winnings = 0
    rank = 1
    for hand in hands:
        total_winnings += int(hand['bid']) * rank
        rank += 1
    return total_winnings


if __name__ == "__main__":
    main()
