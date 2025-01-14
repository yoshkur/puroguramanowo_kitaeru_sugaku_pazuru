# This code calculates the total resistance in parallel and series configurations.
from fractions import Fraction
from itertools import combinations

# Calculate the Cartesian product of arrays


def calculate_product(array):
    result = array[0]
    for index in range(1, len(array)):
        result = [x + y for x in result for y in array[index]]
    return [list(item) for item in result]

# Calculate the resistance in parallel


def calculate_parallel(array):
    return Fraction(1, sum(Fraction(1, value) for value in array))


memo = {1: [[1]]}


def calculate(n):
    if n in memo:
        return memo[n]

    # Series
    result = [value + 1 for value in calculate(n - 1)]

    # Parallel
    for i in range(2, n + 1):
        # Setting the number of segments for parallel
        cut = {}
        for combination in combinations(range(1, n), i - 1):
            position = 0
            resistance_segments = []
            for j in range(len(combination)):
                resistance_segments.append(combination[j] - position)
                position = combination[j]
            resistance_segments.append(n - position)
            cut[tuple(sorted(resistance_segments))] = 1

        # Recursively set resistances at the cut positions
        keys = [list(cut_key) for cut_key in cut.keys()]
        for key in keys:
            product_values = calculate_product([calculate(segment) for segment in key])
            for product_value in product_values:
                for value in product_value:
                    result.append(calculate_parallel(value))

    memo[n] = result
    return result


golden_ratio = 1.61800339887
minimum_value = float('inf')
for value in calculate(10):
    if abs(golden_ratio - value) < abs(golden_ratio - minimum_value):
        minimum_value = value

print(f"{minimum_value:.10f}")
print(minimum_value)
