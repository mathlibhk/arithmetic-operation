import random
import math
import ast
from fractions import Fraction

def qtype1():
    easy_decimal = [0.2, 0.25, 0.4, 0.5, 0.6, 0.75, 0.8, 1.25, 1.5, 1.75] #[1.2, 1.4, 1.6, 1.8]
    a = random.randint(-9, 9)
    b = random.choice(['+', '-'])
    c = random.randint(1, 9)
    d = random.choice(['\\times', '\\div'])
    if random.randint(1, 2) == 1:
        e1 = random.randint(2, 9)
        e2 = random.randint(2, 9)
        while e2 == e1:
            e2 = random.randint(2, 9)
        e = f"\\dfrac{{{e1}}}{{{e2}}}"
        e_value = e1/e2
    else:
        e = random.choice(easy_decimal)
        e_value = e
    f = random.choice(['\\times', '\\div'])
    g = random.randint(-9, 9)
    h = random.choice(['+', '-'])
    i = random.randint(1, 3)
    while i==-g:
        i = random.randint(1, 9)
    j = random.choice(['\\times', '\\div'])
    k = random.randint(1, 5)
    l = random.randint(1, 5)
    m = random.choice(['+', '-'])
    if random.randint(1, 2) == 1:
        n1 = random.randint(1, 4)
        n2 = random.randint(n1 + 1, 5)
        n = f"\\dfrac{{\\displaystyle{n1}}}{{\\displaystyle{n2}}}"
        n_value = n1/n2
    else:
        n = random.choice(easy_decimal)
        n_value = n
    
    d_value = '*' if d == '\\times' else '/'
    f_value = '*' if f == '\\times' else '/'
    j_value = '*' if j == '\\times' else '/'
        
    question = f"{a}{b}{c}{d}{e}{f}\\left({g}{h}{i}\\right){j}\\dfrac{{{k}}}{{{l}{m}{n}}}"
    
    ans_expr = f"{a}{b}{c}{d_value}{e_value}{f_value}({g}{h}{i}){j_value}({k}/({l}{m}{n_value}))"
    
    try:
        ans_value = eval(ans_expr, {"__builtins__": None}, {"Fraction": Fraction, "sqrt": math.sqrt, "abs": abs})
        ans_fraction = Fraction(ans_value).limit_denominator()
        ans_numerator = ans_fraction.numerator
        ans_denominator = ans_fraction.denominator

        if ans_denominator == 1:
            answer = ans_fraction
        else:
            answer = f"\\dfrac{{{ans_numerator}}}{{{ans_denominator}}}"

    except ZeroDivisionError:
        return question, "\mathbf{ZeroDivisionError}"
    
    return question, answer

for i in range(1050):
    question, answer = qtype1()
    if answer == "\mathbf{ZeroDivisionError}":
        continue
    print(f"\\item ${question}$\\\\")
    print(f"\\hide{{\\hideAns}}{{\\fbox{{Ans: ${answer}$}}}}")
    print()
