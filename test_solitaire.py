import solitaire

def test_move_jokers():
    deck = solitaire.Deck([1, 53, 3, 4, 54, 6, 7, 8])
    deck.move_jokers()
    assert deck.cards == [1, 3, 53, 4, 6, 7, 54, 8]

def test_move_jokers_respects_order():
    deck = solitaire.Deck([3, 53, 54, 8, 9])
    deck.move_jokers()
    assert deck.cards == [3, 53, 8, 54, 9]

def test_move_jokers_handles_end():
    deck = solitaire.Deck([1, 53, 2, 54])
    deck.move_jokers()
    assert deck.cards == [1, 2, 54, 53]

def test_triple_cut():
    deck = solitaire.Deck([2, 4, 6, 54, 4, 8, 7, 1, 53, 3, 9])
    deck.triple_cut()
    assert deck.cards == [3, 9, 54, 4, 8, 7, 1, 53, 2, 4, 6]

def test_count_cut():
    assert False

def test_extract():
    deck = solitaire.sorted_deck()
    assert deck.extract() == 1

def test_sample_output_one_digit():
    deck = solitaire.sorted_deck()
    assert deck.keystream(1) == [4]

def test_sample_output():
    deck = solitaire.sorted_deck()
    assert deck.keystream(9) == [4, 49, 10, 24, 8, 51, 44, 6, 33]
