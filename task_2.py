# Recursive functions II
# Task 2:
# Recursion with return and instructions after return (non tail-recursive)


def drill_sum(items):
    if isinstance(items,int):
        return items
    else:
        return sum(map(drill_sum, items))
     

test_data1 = [
    1,
    [1, 2],
    [1, [2, 3]],
    [1, [2, [3, 4]]],
    [1, [2, [3, [4, 5]]]],
]
test_data2 = [
    [1, [[2, 6], [3, 4]]],
    [[5, 6, [7, 8]], [2, [3, [4, 5]]]],
    [1, [2, 3]],
    [1, 2],
    1,
]
print(drill_sum(test_data1))
print(drill_sum(test_data2))