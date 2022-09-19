from fractions import Fraction
from matplotlib.pyplot as plt
import pandas as pd

def probs_formater(probs):
    for sIndex, prob in probs.items():
        print(f"{s[sIndex-1]} : {Fraction(prob)
            .limit_denominator()}")

def probs_plotter(probs):
    cols = 10
    df = pd.DataFrame(columns=list(range(1,cols+1)))
    for col in range(1,cols+1):
        probs = list(generate_numbers(cols, col).values())
        df[col] = probs


    df.applymap(lambda x: Fraction(x).limit_denominator())
    df[[4]].applymap(lambda x: Fraction(210*x).limit_denominator())
    plt.plot(df)
    plt.show()
