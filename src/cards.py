from typing import Optional, List


class Card:
    # Type-hinting all parameters on classes and functions.
    def __init__(self, value: int):
        self.value = value
        self.next_card = None

    def make_bottom_card(self) -> None:
        """
        Points next card to None.
        """
        self.next_card = None


class Deck:
    def __init__(self):
        self.top_card: Optional[Card] = None
        self.bottom_card: Optional[Card] = None

    def add_card_on_top(self, card: Card) -> None:
        """
        Adds a given card to the top of the deck
        :param card: Card that will be set as the top of the deck card.
        """
        if self.is_empty():
            self.top_card = card
            self.assign_new_bottom_card(card)
        else:
            card.next_card = self.top_card
            self.top_card = card

    def assign_new_bottom_card(self, card: Card) -> None:
        """
        Used on the step of moving the top hand deck card to the bottom of hand deck
        :param card: Card that will be set as the bottom of the deck card
        """
        if self.bottom_card:
            self.bottom_card.next_card = card
        self.bottom_card = card
        card.make_bottom_card()

    def take_top_card(self) -> Card:
        """
        Grabs the top card, removes if from deck, and returns it
        :return: Top Card
        """
        top = self.top_card
        if top.next_card:
            self.top_card = top.next_card
        else:
            self.top_card = None
        return top

    def move_top_card_to_bottom(self) -> None:
        """
        Movest the card on top of the deck, to the bottom.
        """
        top_card = self.take_top_card()
        if not self.top_card:
            self.top_card = top_card
        self.assign_new_bottom_card(top_card)

    def is_sorted(self) -> bool:
        """
        Checks if the deck is sorted.
        :return: bool. True if the deck is sorted, False if not.
        """
        if self.top_card.value != 1:
            return False
        current_card = self.top_card
        while current_card.next_card:
            if current_card.value > current_card.next_card.value:
                return False
            current_card = current_card.next_card
        return True

    def is_empty(self) -> bool:
        """
        Checks if the deck is empty
        :return: bool. True if the deck is empty, False if not.
        """
        if self.top_card:
            return False
        else:
            return True

    def get_deck_cards(self) -> List:
        """
        Prints the deck card as a List.
        """
        current_card = self.top_card
        deck_list = []
        while current_card:
            deck_list.append(current_card.value)
            current_card = current_card.next_card
        return deck_list
