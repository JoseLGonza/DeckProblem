import unittest

import solver
from solver import Solver


class TestSolver(unittest.TestCase):
    def setUp(self) -> None:
        self.solver = Solver(4)

    def test_initialize_deck(self):
        deck = solver.initialize_deck()
        self.assertTrue(deck.top_card.value == 1)
        self.assertTrue(deck.bottom_card.value == 1)

    def test_create_hand_deck(self):
        self.assertEqual(self.solver.hand_deck.top_card.value, 1)
        self.assertEqual(self.solver.hand_deck.bottom_card.value, 4)

    def test_solve_fails_with_negative_number(self):
        with self.assertRaises(ValueError):
            Solver(-1).solve()
            Solver(0).solve()
            Solver(1).solve()

    def test_solve_gives_right_answer(self):
        self.assertEqual(Solver(2).solve(), 2)
        self.assertEqual(Solver(3).solve(), 3)
        self.assertEqual(Solver(4).solve(), 2)
        self.assertEqual(Solver(10).solve(), 6)
        self.assertEqual(Solver(16).solve(), 4)
        self.assertEqual(Solver(32).solve(), 12)
        self.assertEqual(Solver(52).solve(), 510)
        self.assertEqual(Solver(54).solve(), 1680)
        self.assertEqual(Solver(80).solve(), 210)
        self.assertEqual(Solver(104).solve(), 1722)
        self.assertEqual(Solver(156).solve(), 5040)


if __name__ == '__main__':
    unittest.main(verbosity=2)
