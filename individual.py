import numpy as np

class Individual():
    ''' Defines an individual as a chromosome. '''

    def __init__(self, enc, size, lo_bound, up_bound):
        self.lo_bound = lo_bound
        self.up_bound = up_bound
        self.chromosome = self._init_chromo(enc, size)

    def __str__(self):
        return np.array2string(self.chromosome)

    def _init_chromo(self, enc, size):
        # Discrete uniform/continuous distribution
        if enc == "BIN":
            return np.random.randint(2, size=size)
        elif enc == "INT":
            return np.random.randint(self.lo_bound, self.up_bound, size=size)
        elif enc == "INT-PERM":
            return np.random.permutation(size)
        elif enc == "REAL":
            return np.random.uniform(self.lo_bound, self.up_bound, size=size)