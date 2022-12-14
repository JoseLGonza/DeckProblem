from src.cards import Card, Deck


def initialize_deck() -> Deck:
    """
    Initializes a Deck and adds the first Card.
    :return:
    """
    deck = Deck()
    initial_card = Card(1)
    deck.top_card = initial_card
    deck.bottom_card = initial_card
    return deck


def print_decks(hand_deck: Deck, table_deck: Deck) -> None:
    """
    Prints a given hand deck and a given table deck into console
    :param hand_deck: Hand deck to print
    :param table_deck: Table deck to print
    """
    print(f'Hand Deck: {hand_deck.get_deck_cards()} \n')
    print(f'Table Deck: {table_deck.get_deck_cards()} \n')


class Solver:
    def __init__(self, deck_size: int, verbose: bool = False):
        if deck_size <= 1:
            raise ValueError('Size must be of a value over 2')
        self.deck_size = deck_size
        self.verbose = verbose
        self.rounds = 0
        self.hand_deck = None

        self.create_hand_deck()

    def solve(self) -> int:
        """
        Main method. Retuns the number of rounds require to get sorted Deck.
        :return: int. number of rounds.
        """
        self.deck_round()
        while not self.hand_deck.is_sorted():
            self.deck_round()
        return self.rounds

    def deck_round(self) -> None:
        """
        One deck round. As described in the problem, one deck round consists on:
        1. moving first card on hand to table deck
        2. moving first card to back of hand
        3. repeat 1 and 2 until no cards are left on hand.
        4. grab table deck and repeat 3 until deck is sorted
        """
        table_deck = Deck()
        while self.hand_deck.top_card:
            table_deck.add_card_on_top(self.hand_deck.take_top_card())
            if self.hand_deck.top_card:
                self.hand_deck.move_top_card_to_bottom()
            if self.verbose:
                print_decks(self.hand_deck, table_deck)
        self.hand_deck = table_deck
        self.rounds += 1

    def create_hand_deck(self) -> None:
        """
        Creates a hand deck by initializing a deck and adding number of carts given by the user.
        """
        self.hand_deck = initialize_deck()
        for i in range(2, self.deck_size + 1):
            new_card = Card(i)
            self.hand_deck.assign_new_bottom_card(new_card)
