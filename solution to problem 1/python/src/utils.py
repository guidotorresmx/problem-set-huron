from fractions import Fraction

def format_to_fractional(probs):
    return {k: Fraction(v).limit_denominator() for k, v in probs.items()}

def print_probs(probs):
    for key, prob in probs.items():
        if type(prob) is Fraction:
            print(f"    {key} = {prob}")
        else: 
            print(f"    {key} = {prob:.2f}")
