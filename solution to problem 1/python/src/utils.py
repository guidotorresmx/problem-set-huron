from fractions import Fraction

def fractional_formater(probs):
    probs = {k: Fraction(v).limit_denominator() for k, v in probs.items()}