import itertools
from math import comb as nCr
from typing import Dict, Set
from utils import format_to_fractional, print_probs

def get_probs_analytically(s: Set, r: int) -> Dict:
    '''
    Recives a set (s) of numbers and a sampling number (r), from which, the
    function returns the probability of of picking each element as the minimum
    of each set
        params:
            s: set of integers
            r: number of sampled elements
        return:
            probs: dict of probabilities of minimum of subsets
    e.g.:
        params:
            s = {49, 8, 48, 15, 47, 4, 16, 23, 43, 44, 42, 45, 46}.
            r = 6
        returns:
            probs = {
                4: .41,
                8: .22,
                15 .16,
        }
    '''

    if not s:
        raise ValueError("please specify a set")
    if not r:
        raise ValueError("please specify a sampling number")

    s = sorted(s)
    n = len(s)

    probs = {}
    denominator = nCr(n,r)
    for i, val in enumerate(s):
        numerator = nCr(n-i-1,r-1)
        probs[val] = numerator/denominator

    return probs


def main():
    s = sorted([49, 8, 48, 15, 47, 4, 16, 23, 43, 44, 42, 45, 46])
    r = 6
    probs = get_probs_analytically(s, r)
    print("Probabilities in fractional form:")
    print_probs(format_to_fractional(probs))
    print("Probabilities in decimal form:")
    print_probs(probs)

if __name__ == "__main__":
    main()
