import argparse
import numpy as np

LO_BOUND = 0
UP_BOUND = 0

class Individual():
    ''' Defines an individual as a set of chromosomes. '''

    def __init__(self, enc, size):
        self.chromosome = self._init_chromo(enc, size)

    def __str__(self):
        return np.array2string(self.chromosome)

    def _init_chromo(self, enc, size):
        # Discrete uniform/continuous distribution
        if enc == "BIN":
            return np.random.randint(2, size=size)
        elif enc == "INT":
            return np.random.randint(LO_BOUND, UP_BOUND, size=size)
        elif enc == "INT-PERM":
            return np.random.randint(0, size, size=size)
        elif enc == "REAL":
            return np.random.uniform(LO_BOUND, UP_BOUND, size=size)
        else:
            raise Exception('Invalid encoding.')

class Population():
    ''' Defines a population as a set of individuals '''

    def __init__(self, enc, csize, psize):
        self.individuals = [Individual(enc, csize) for i in range(psize)]

    def __str__(self):
        ret = ''
        for ind in self.individuals:
            ret += str(ind) + "\n"
        return ret

def main():
    ''' GA Project. Marcos Felipe Eipper @ 2018 | UDESC - CCT '''

    global UP_BOUND
    global LO_BOUND

    # Create argument parser
    parser = argparse.ArgumentParser(prog="ag.py")
    parser.add_argument("enc",
                         help="Encoding types. Accepted: bin, int, int-perm, real.")
    parser.add_argument("pop", type=int,
                         help="Population size.")
    parser.add_argument("chromo", type=int,
                         help="Chromosome size.")
    parser.add_argument("-l", "--lower-bounds", type=float,
                         help="Variables' lower bounds. Lower bounds are inclusive.")
    parser.add_argument("-u", "--upper-bounds", type=float,
                         help="Variables' upper bounds. Upper bounds are exclusive.")
    parser.add_argument("-v", "--verbose", action="store_true",
                         help="Enables verbosity.")
    parser.add_argument("-s", "--seed", type=int,
                         help="Runs the program with a seed.")

    # Parse arguments
    args = parser.parse_args()

    # Define bounds, if any
    LO_BOUND = args.lower_bounds
    UP_BOUND = args.upper_bounds

    # Define seed, if provided
    if args.seed:
        np.random.seed(args.seed)

    # Create population
    pop = Population(args.enc.upper(), args.chromo, args.pop)

    # Prints out verbose stuff.
    if args.verbose:
        print("Arguments: " + str(args) + "\n")
        print("Lower bound: " + str(LO_BOUND) + "\n" + "Upper bound: " + str(UP_BOUND) + "\n")
        print("Population: \n" + str(pop))

if __name__ == '__main__':
    main()
