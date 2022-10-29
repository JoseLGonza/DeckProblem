from cards import Card, Deck


def initialize_deck() -> Deck:
    deck = Deck()
    initial_card = Card(1)
    deck.top_card = initial_card
    deck.bottom_card = initial_card
    return deck


class Solver:
    def __init__(self, deck_size: int, verbose: bool = False):
        self.deck_size = deck_size
        self.verbose = verbose
        self.rounds = 0
        self.hand_deck = None

        self.create_hand_deck()

    def solve(self) -> int:
        self.deck_round()
        while not self.hand_deck.is_sorted():
            self.deck_round()
        return self.rounds

    def deck_round(self):
        table_deck = Deck()
        while self.hand_deck.top_card:
            table_deck.add_card_on_top(self.hand_deck.take_top_card())
            if self.hand_deck.top_card:
                self.hand_deck.move_top_card_to_bottom()
        self.hand_deck = table_deck
        self.rounds += 1
        if self.verbose:
            table_deck.print_deck_cards()

    def create_hand_deck(self) -> None:
        self.hand_deck = initialize_deck()
        if self.deck_size > 1:
            for i in range(2, self.deck_size + 1):
                new_card = Card(i)
                self.hand_deck.assign_new_bottom_card(new_card)

