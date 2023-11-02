# [Python] Show numerically that ∑(n≥1)(−1)(n+1)/n = ln 2.Change the order of summation in this series – for example
# by first adding p positive terms, then q negative terms, and so on – and show numerically that the
# rearrangement gives a different sum (depending on p, q)
import math
import matplotlib.pyplot as plt


def series_partial_sum_1(n: int) -> float:
    """
    Returns the partial sum of the given expression in problem 7 without grouping any terms
    :return: The value of the partial sum up to n
    """
    s = 0
    s = float(s)
    for i in range(1, n + 1):
        s += ((-1) ** (i + 1)) / i
    return s


def series_partial_sum_2(n: int, p: int, q: int) -> float:
    """
    Calculates the partial sum given in problem 7 by first adding p positive terms then q subtractions
    :return: The value of the partial sum up to n
    """
    s = 0
    s = float(s)
    p_index = 1
    q_index = 2

    while n != 0:
        for i in range(0, p):
            # p additions
            if n != 0:
                s += 1/p_index
                p_index += 2
                n -= 1

        for i in range(0, q):
            # q subtractions
            if n != 0:
                s -= 1/q_index
                q_index += 2
                n -= 1

    return s


def main():
    n_values = [5000, 10000, 20000, 50000, 100000, 200000]

    partial_sum_values_1 = []
    for i in range(0, len(n_values)):
        partial_sum_values_1.append(series_partial_sum_1(n_values[i]))

    ln2 = math.log(2)

    errors_1 = []
    for i in range(0, len(partial_sum_values_1)):
        errors_1.append(abs(partial_sum_values_1[i] - ln2))

    print("This is the graph and values for n= 5000, 10000, 20000, 50000, 100000, 200000")
    print("The blue star represents the value of ln(2)")

    # Making the first graph
    plt.figure(figsize=(8, 6))
    plt.plot(n_values, errors_1, color='#fc72b7', marker='p', linestyle='-')
    plt.xlabel('n', color='#fc72b7')
    plt.title("the partial sums were formed by adding each term as it is", color='#fc72b7')
    plt.ylabel('error compared to ln2', color='#fc72b7')
    plt.scatter(200000, 0, color='#29b8ff', marker='*')  # the error is 0 for ln2
    plt.grid(True)
    plt.show()

    for i in range(0, len(n_values)):
        print("The partial sum for n =", n_values[i], " is:", partial_sum_values_1[i])

    print("Exact value of ln(2): ", ln2, "\n")

    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    print("\nPlease input values for p and q as specified in problem 7: ")
    p = input("Please input p: ")
    q = input("Please input q: ")
    p = int(p)
    q = int(q)

    partial_sum_values_2 = []
    for i in range(0, len(n_values)):
        partial_sum_values_2.append(series_partial_sum_2(n_values[i], p, q))

    errors_2 = []
    for i in range(0, len(partial_sum_values_2)):
        errors_2.append(abs(partial_sum_values_2[i] - ln2))

    plt.figure(figsize=(8, 6))
    plt.plot(n_values, errors_2, color='#fc72b7', marker='p', linestyle='-')
    plt.xlabel(f'n, for p = {p} and q = {q}', color='#fc72b7')
    plt.title("the partial sums were formed by p additions and q subtractions each step", color='#fc72b7')
    plt.ylabel('error compared to ln2', color='#fc72b7')
    plt.scatter(200000, 0, color='#29b8ff', marker='*')  # the error is 0 for ln2
    plt.grid(True)
    plt.show()

    for i in range(0, len(n_values)):
        print("The partial sum for n =", n_values[i], " is:", partial_sum_values_2[i])

    print("Exact value of ln(2): ", ln2, "\n")


main()
