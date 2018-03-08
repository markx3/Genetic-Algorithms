import argparse
import numpy as np
from population import Population
from time import sleep

def main(args):
    ''' GA Project. Marcos Felipe Eipper @ 2018 | UDESC - CCT '''
    # Checks encoding param.
    enc = args.enc.upper()
    if (enc  != "INT"      and
        enc  != "REAL"     and
        enc  != "INT-PERM" and
        enc  != "BIN"        ):
        raise Exception('Invalid encoding.')

    # Define seed, if provided
    if args.seed:
        np.random.seed(args.seed)

    # Create population
    pop = Population(args.enc.upper(), args.chromo, args.pop,
                     args.lower_bounds, args.upper_bounds)

    # Prints out verbose fun stuff.
    if args.verbose:
        print("+====================================+")
        print("+===========  Welcome to  ===========+")
        print("+=========== Verbose Mode ===========+")
        print("+====================================+\n")
        sleep(0.25)
        print("==> Arguments: " + str(args) + "\n")
        print("==> Population: \n" + str(pop) + "<==")


def parse_args():
    # Create argument parser
    parser = argparse.ArgumentParser(prog="ag.py")
    parser.add_argument("enc",
                         help=
                         "Encoding types. Accepted: bin, int, int-perm, real.")
    parser.add_argument("pop", type=int,
                         help="Population size.")
    parser.add_argument("chromo", type=int,
                         help="Chromosome size.")
    parser.add_argument("-l", "--lower-bounds", type=float,
                         help=
                         "Variables lower bounds. Lower bounds are inclusive.")
    parser.add_argument("-u", "--upper-bounds", type=float,
                         help=
                         "Variables upper bounds. Upper bounds are exclusive.")
    parser.add_argument("-v", "--verbose", action="store_true",
                         help="Enables verbosity.")
    parser.add_argument("-s", "--seed", type=int,
                         help="Runs the program with a seed.")

    # Parse arguments
    return parser.parse_args()

if __name__ == '__main__':
    args = parse_args()
    main(args)
