from individual import Individual

class Population():
    ''' Defines a population as a list of individuals '''

    def __init__(self, enc, csize, psize, lo_bound, up_bound):
        self.lo_bound = lo_bound
        self.up_bound = up_bound
        self.individuals = [Individual(enc, csize, lo_bound, up_bound)
                            for i in range(psize)]

    def __str__(self):
        ret = ''
        for ind in self.individuals:
            ret += str(ind) + "\n"
        return ret