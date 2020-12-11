def sorted_deck():
    return Deck([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
            31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54])

class Deck:
    def __init__(self, cards):
        self.cards = cards

    def move_back(self, index):
        if index + 1 == len(self.cards):
            self.cards.insert(1, self.cards.pop())
        else:
            self.cards[index], self.cards[index + 1] = self.cards[index + 1], self.cards[index]

    def move_jokers(self):
        index_a = self.cards.index(53)
        self.move_back(index_a)

        # Do it twice for the big joker
        index_b = self.cards.index(54)
        self.move_back(index_b)

        index_b = self.cards.index(54)
        self.move_back(index_b)

    def triple_cut(self):
        indices = [self.cards.index(53), self.cards.index(54)]
        indices.sort()

        beginning = self.cards[0:indices[0]]
        middle = self.cards[indices[0]:indices[1] + 1]
        end = self.cards[indices[1] + 1:]

        self.cards = end + middle + beginning

    def update(self):
        pass

    def extract(self):
        index = self.cards[0]
        return self.cards[index - 1]

    def keystream(self, n):
        result = []
        for _ in range(n):
            self.update()
            result.append(self.extract())

        return result
