""" represents a poisson distribution """


class Poisson:
    """ poisson distribution """

    def __init__(self, data=None, lambtha=1.):
        """ poisson distribution """
        if data is None:
            if lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
            self.lambtha = float(lambtha)
        else:
            if type(data) is not list:
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            self.lambtha = float(sum(data) / len(data))

    def pmf(self, k):
        """ PMF Calculate number of successes and k at number events """
        if k < 0:
            return 0
        k = int(k)
        return(pow(self.lambtha, k) *
               pow(2.7182818284590452353602874713527, -1 * self.lambtha) /
               factorial(k))

    def cdf(self, k):
        """ CDF Calculate number of successes and k at number events """
        if k < 0:
            return 0
        k = int(k)
        return sum([self.pmf(n) for n in range(k+1)])


def factorial(n):
    """ Calculate factorial of n """
    fact = 1
    for x in range(1, n + 1):
        fact = x * fact
    return fact
