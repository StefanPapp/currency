"""
(C) Demo
"""

import argparse
import logging
import sys

from core import LOGGER


def _init_logging():
    console_handler = logging.StreamHandler()  # it's always on DEBUG level on Console
    console_handler.setLevel(logging.DEBUG)

    console_handler.setFormatter(logging.Formatter('%(asctime)s %(process)d '
                                                   '%(levelname)s: %(message)s'))
    LOGGER.addHandler(console_handler)
    LOGGER.setLevel(logging.DEBUG)
    LOGGER.info("SUCCESS: Logging configured and started")


def _load_settings():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--incoming', help='in currency', required=False)
    parser.add_argument('-o', '--out', help='out currency', required=False)
    parser.add_argument('-a', '--am', help='amout currency', type=float, required=False)
    args = parser.parse_args(sys.argv[1:])
    return args

def convert(source: str, dest: str, amount: float):
    # requires Python 3.10
    match source:
        case "USD":
             return amount * 0.82
        case "EUR":
             return amount * 1.18

def main():
    """
    main routine to connect to pop db and push into kafka
    """
    _init_logging()
    args = _load_settings()
    sum = convert(args.incoming, args.out, args.am)
    print(sum)

if __name__ == "__main__":
    main()
