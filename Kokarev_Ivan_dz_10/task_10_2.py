from abc import ABC, abstractmethod

class Clothes(ABC):
    @abstractmethod
    def expense(self):
        pass

class Suit(Clothes):
    def __init__(self, H):
        self.H = H

    @property
    def expense(self):
        return 2 * self.H + 0.3

class Coat(Clothes):
    def __init__(self, V):
        self.V = V

    @property
    def expense(self):
        return self.V / 6.5 + 0.5

coat = Coat(50)
coat_2 = Coat(170)
suit = Suit(60)
suit_2 = Suit(150)

print(coat.expense + coat_2.expense + suit.expense + suit_2.expense)