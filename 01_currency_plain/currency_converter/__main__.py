"""
(C) Demo
"""

import argparse
import sys


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
    sample
    """
    args = _load_settings()
    sum = convert(args.incoming, args.out, args.am)
    print(sum)

if __name__ == "__main__":
    main()
