import argparse
import logging
import unittest

from solver import Solver
from tests import test_solver, test_cards


def parse_input() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog='deck_problem_solver',

    )
    subparsers = parser.add_subparsers()

    parser_solve_problem = subparsers.add_parser('solve',
                                                 help='Size of the deck that will be used to solve the problem')
    parser_solve_problem.add_argument('-s', '--size',
                                      type=int,
                                      required=True,
                                      help='Size of the deck that will be used to solve the problem')
    parser_solve_problem.add_argument('-v', '--verbose',
                                      action='store_true',
                                      help='Adds verbosity to the solution output')
    parser_solve_problem.set_defaults(func=solve)

    parser_unit_tests = subparsers.add_parser('test-cases')
    parser_unit_tests.set_defaults(func=test_cases)

    parser_unit_tests = subparsers.add_parser('unit-tests')
    parser_unit_tests.set_defaults(func=unit_tests)

    namespace = parser.parse_args()
    return namespace


def solve(args):
    print(Solver(args.size, args.verbose).solve())


def unit_tests(args):
    text_runner = unittest.TextTestRunner(verbosity=2)
    suite_cards = unittest.TestLoader().loadTestsFromModule(test_cards)
    suite_solver = unittest.TestLoader().loadTestsFromModule(test_solver)
    text_runner.run(suite_cards)
    text_runner.run(suite_solver)


def test_cases(args):
    test_cases_list = [2, 4, 5, 10, 12, 16, 30, 52, 80, 102, 104]
    for test_case in test_cases_list:
        print_test_case(test_case)


def print_test_case(test_case: int):
    print(f'\nTesting Deck Problem with the following Deck Size: {test_case}')
    print(f'result {Solver(test_case).solve()}')


def main():
    options = parse_input()
    try:
        return options.func(options)
    except AttributeError:
        logging.exception('')


if __name__ == '__main__':
    logging.info('Running Main')
    main()
