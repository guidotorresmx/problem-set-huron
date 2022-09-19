import itertools
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
    sIndexes = list(range(1, n + 1))

    #optimizable by mixing following 4 lines into a single iterative function
    #instead of list of combinations but less readable
    combinations = list(itertools.combinations(sIndexes, r))
    probs = {i: 0 for i in s}
    for combination in combinations:
        probs[s[min(combination)-1]] += 1

    total = sum(probs.values())
    for sIndex, _ in probs.items():
        probs[sIndex] /= total

    return probs


if __name__ == "__main__":
    s = sorted([49, 8, 48, 15, 47, 4, 16, 23, 43, 44, 42, 45, 46])
    r = 6
    probs = get_probs_analytically(s, r)
    print("Probabilities in fractional form:")
    print_probs(format_to_fractional(probs))
    print("Probabilities in decimal form:")
    print_probs(probs)
