import argparse
import logging


def parse_input() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog='deck_problem_solver',

    )
    subparsers = parser.add_subparsers()

    parser_solve_problem = subparsers.add_parser('solve',
                                                 type=int,
                                                 help='Size of the deck that will be used to solve the problem')
    # parser_solve_problem.add_argument('-s', '--size',
    #                                   type=int,
    #                                   required=True,
    #                                   help='Size of the deck that will be used to solve the problem')
    parser_solve_problem.add_argument('-v', '--verbose',
                                      action='store_true',
                                      help='Adds verbosity to the solution output')

    parser_test_cases = subparsers.add_parser('test-cases')
    parser_test_cases.add_argument('-v', '--verbose',
                                   action='store_true',
                                   help='Adds verbosity to the solution output')

    parser_unit_tests = subparsers.add_parser('unit-tests')
    parser_unit_tests.add_argument('-v', '--verbose', action='store_true')

    namespace = parser.parse_args()
    return namespace


def solve(args):
    if args.size <= 0:
        logging.exception('Please provide a size bigger than 0.')
        raise ValueError


def main():
    options = parse_input()
    try:
        return options.func(options)
    except AttributeError:
        logging.exception('')


if __name__ == '__main__':
    logging.info('Running Main')
    main()
