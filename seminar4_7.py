import math
import matplotlib.pyplot as plt

def series_partial_sum(n):
    s = 0
    s = float(s)
    for i in range(1, n + 1):
        s += ((-1) ** (i + 1)) / i
    print(s)
    return s


def main():
    n_values = [5000, 10000, 20000, 50000, 100000, 200000]

    partial_sum_values = []
    for i in range(0, len(n_values)):
        partial_sum_values.append(series_partial_sum(n_values[i]))

    ln2 = math.log(2)

    errors = []
    for i in range(0 , len(partial_sum_values)):
        errors.append(abs(partial_sum_values[i] - ln2))

    plt.figure(figsize=(5, 10))
    plt.plot(n_values, errors, color='#fc72b7', marker='p', linestyle='-')
    plt.xlabel('n')
    plt.ylabel('error to ln2')
    plt.scatter(max(n_values), [0], color='#29b8ff', marker='o') # the error is 0 for ln2
    plt.grid(True)
    plt.show()

    for i in range(0, len(n_values)):
        print("The partial sum for n =", n_values[i], " is:", partial_sum_values[i])

    print('Exact value of ln(2): ', ln2)

main()

