def perform_shuffle(deck):
    shuffled_deck = []
    for item in range(len(deck)):
        if item % 2 == 0:
            shuffled_deck.append(deck[item//2])
        else:
            shuffled_deck.append(deck[len(deck)//2:][item//2])
    return shuffled_deck

def shuffle_count(n):

    # Faro shuffle challenge is designed for even n, if uneven value given force even by simulating discarding last card from shuffle
    if n % 2 == 1:
        n -= 1

    deck = [card for card in range(1, n + 1)]
    original_deck = deck.copy()
    shuffle_count = 1
    deck = perform_shuffle(deck)
    while deck != original_deck:
        deck = perform_shuffle(deck)
        shuffle_count += 1
    return shuffle_count

assert shuffle_count(2) == 1
assert shuffle_count(8) == 3
assert shuffle_count(14) == 12
assert shuffle_count(38) == 36
assert shuffle_count(52) == 8
assert shuffle_count(70) == 22
