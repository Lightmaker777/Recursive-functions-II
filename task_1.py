# Recursive functions II
# Task 1:
# A recursive function named sum_series that takes a single argument as an integer and returns the sum of the positive integers of n+(n-2)+(n-4)... (until n-x =< 0).

def sum_series(n):

    if n <= 0:
        return 0
    else:
        return n + sum_series(n-2)


# Test cases:
print(sum_series(7))
print(sum_series(8))
print(sum_series(15))
