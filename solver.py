from cards import Card, Deck


class Solver:
    def __init__(self, deck_size: int, verbose: bool = False):
        self.deck_size = deck_size
        self.verbose = verbose
        self.hand_deck = None
        self.table_deck = None

        self.create_hand_deck()

    def solve(self, deck_size: int) -> int:
        return 1

    def deck_round(self):
        return None

    def create_hand_deck(self) -> None:
        self.initialize_hand_deck()
        if self.deck_size > 1:
            for i in range(2, self.deck_size + 1):
                new_card = Card(i)
                self.hand_deck.assign_new_bottom_card(new_card)

    def initialize_hand_deck(self) -> None:
        self.hand_deck = Deck()
        initial_card = Card(1)
        self.hand_deck.top_card = initial_card
        self.hand_deck.bottom_card = initial_card


Solver = Solver(10)
Solver.hand_deck.print_deck_cards()
