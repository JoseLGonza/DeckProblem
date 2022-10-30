import unittest

from cards import Card, Deck


class TestCard(unittest.TestCase):
    def setUp(self) -> None:
        self.card1 = Card(1)
        self.card2 = Card(2)

    def test_make_bottom_card(self):
        self.card1.next_card = self.card2
        self.card1.make_bottom_card()
        self.assertIsNone(self.card1.next_card)


class TestDeck(unittest.TestCase):
    def setUp(self) -> None:
        self.card1 = Card(1)
        self.card2 = Card(2)
        self.card3 = Card(3)
        self.deck1 = Deck()
        self.deck2 = Deck()

    def test_add_card_on_top(self):
        self.deck1.add_card_on_top(self.card1)
        self.assertEqual(self.deck1.top_card, self.card1)
        self.assertEqual(self.deck1.bottom_card, self.card1)

    def test_assign_new_bottom_card(self):
        self.deck2.assign_new_bottom_card(self.card2)
        self.assertEqual(self.deck2.bottom_card, self.card2)

    def test_take_top_card(self):
        self.deck1.add_card_on_top(self.card1)
        top_card = self.deck1.take_top_card()
        self.assertEqual(top_card, self.card1)

    def test_move_top_card_to_bottom(self):
        self.deck1.add_card_on_top(self.card1)
        self.assertTrue(self.deck1.top_card == self.card1)

        self.deck1.top_card.next_card = self.card2
        self.deck1.move_top_card_to_bottom()
        self.assertEqual(self.deck1.bottom_card, self.card1)

    def test_is_sorted(self):
        self.deck1.add_card_on_top(self.card1)
        self.deck1.add_card_on_top(self.card2)
        self.deck1.add_card_on_top(self.card3)
        self.assertFalse(self.deck1.is_sorted())

        self.deck2.add_card_on_top(self.card1)
        self.deck2.assign_new_bottom_card(self.card2)
        self.deck2.assign_new_bottom_card(self.card3)
        self.assertTrue(self.deck2.is_sorted())

    def test_is_empty(self):
        self.assertTrue(self.deck1.is_empty())

        self.deck2.add_card_on_top(self.card1)
        self.assertFalse(self.deck2.is_empty())

    def test_get_deck_cards(self):
        self.deck1.add_card_on_top(self.card1)
        self.deck1.add_card_on_top(self.card2)
        self.deck1.add_card_on_top(self.card3)

        expected_deck_cards = [3, 2, 1]
        self.assertEqual(self.deck1.get_deck_cards(), expected_deck_cards)


if __name__ == '__main__':
    unittest.main(verbosity=2)
