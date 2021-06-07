"""
(C) Demo
"""

import logging

def convert(source: str, dest: str, amount: float):
    # requires Python 3.10
    match source:
        case "USD":
             return amount * 0.82
        case "EUR":
             return amount * 1.18
    # return 1

def main():
    """
    main routine to connect to pop db and push into kafka
    """
    while True:
        # ysb
        vals = input().split(" ")
        print (convert(vals[0], vals[1], float(vals[2])))


if __name__ == "__main__":
    main()
