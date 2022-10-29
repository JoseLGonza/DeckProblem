from typing import Optional


class Card:
    # Type-hinting all parameters on classes and functions.
    def __init__(self, value: int):
        self.value = value
        self.next_card = None

    def make_bottom_card(self) -> None:
        self.next_card = None


class Deck:
    def __init__(self):
        self.top_card: Optional[Card] = None
        self.bottom_card: Optional[Card] = None
        self.deck_size = 0

    def add_card_on_top(self, card: Card) -> None:
        if self.is_empty():
            self.top_card = card
            self.assign_new_bottom_card(card)
        else:
            card.next_card = self.top_card
            self.top_card = card

    def assign_new_bottom_card(self, card: Card) -> None:
        if self.bottom_card:
            self.bottom_card.next_card = card
        self.bottom_card = card
        card.make_bottom_card()

    def take_top_card(self) -> Card:
        top = self.top_card
        if top.next_card:
            self.top_card = top.next_card
        else:
            self.top_card = None
        return top

    def move_top_card_to_bottom(self) -> None:
        top_card = self.take_top_card()
        if not self.top_card:
            self.top_card = top_card
        self.assign_new_bottom_card(top_card)

    def is_sorted(self) -> bool:
        if self.top_card.value != 1:
            return False
        current_card = self.top_card
        while current_card.next_card:
            if current_card.value > current_card.next_card.value:
                return False
            current_card = current_card.next_card
        return True

    def is_empty(self) -> bool:
        if self.top_card:
            return False
        else:
            return True

    def print_deck_cards(self):
        current_card = self.top_card
        deck_list = []
        while current_card:
            deck_list.append(current_card.value)
            current_card = current_card.next_card
        print(deck_list)