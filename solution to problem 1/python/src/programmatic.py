import itertools
from fractions import Fraction
from typing import Dict, Set
from utils import formatProbs


def get_probs_programmatically(s: Set, r: int) -> Dict:
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

    n = len(s)
    sIndexes = list(range(1, n + 1))

    #TODO: verify possible further optimization
    combinations = list(itertools.combinations(sIndexes, r))
    probs = {i: 0 for i in range(1, n + 1)}

    for combination in combinations:
        probs[min(combination)] += 1

    total = sum(probs.values())
    for sIndex, _ in probs.items():
        probs[sIndex] /= total

    #TODO: change to implace or change algorithm for vales to indexes
    FinalProbs = {}
    for key, item in probs.items():
        FinalProbs[list(s)[key-1]] = item 
        
    return FinalProbs


if __name__ == "__main__":
    s = sorted([49, 8, 48, 15, 47, 4, 16, 23, 43, 44, 42, 45, 46])
    r = 6
    probs = get_probs_programmatically(s, r)
    formatProbs(probs)
    print(probs)
