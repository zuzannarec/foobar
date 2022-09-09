import numpy as np
from fractions import Fraction

def solution(m):
    terminalStates = normalize_matrix_and_get_terminal_states(m)
    v = np.zeros(len(m))
    v[0] = 1
    I = np.identity(len(m))
    X = I - m
    inversed = np.linalg.inv(X)
    w = np.dot(v, inversed)
    result = [Fraction(w[idx]).limit_denominator() for idx in range(len(w)) if idx in terminalStates]
    return reduction_fraction(result)

def reduction_fraction(A):    
    denoms = []
    for fraction in A:
        denoms.append(fraction.denominator)
    reduced_fractions = []
    for fraction in A:
        reduced_fractions.append(fraction.numerator * np.lcm.reduce(denoms) / fraction.denominator)
    reduced_fractions.append(np.lcm.reduce(denoms))
    return reduced_fractions

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

def normalize_matrix_and_get_terminal_states(m):
    terminalStates = []
    for row in range(len(m)):
        states = []
        rowSum = 0
        for col in range(len(m[row])):
            if m[row][col] != 0:
                states.append(Point(row, col))
                rowSum += m[row][col]
        if rowSum == 0:
            terminalStates.append(row)
            continue
        for state in states:
            m[state.x][state.y] = (m[state.x][state.y])/(rowSum * 1.0)
    return terminalStates

res1 = solution([[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0,0], [0, 0, 0, 0, 0]])
res2 = solution([[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]])

print(res1, " [7, 6, 8, 21]")
print(res2, " [0, 3, 2, 9, 14]")
