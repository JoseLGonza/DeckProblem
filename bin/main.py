import argparse
import logging

from solver import Solver


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

    parser_unit_tests = subparsers.add_parser('unit-tests')
    parser_unit_tests.set_defaults(func=unit_tests)

    namespace = parser.parse_args()
    return namespace


def solve(args):
    return Solver(args.size, args.verbose).solve()


def test_cases():
    return 2


def unit_tests():
    return 1


def main():
    options = parse_input()
    try:
        return options.func(options)
    except AttributeError:
        logging.exception('')


if __name__ == '__main__':
    logging.info('Running Main')
    main()
