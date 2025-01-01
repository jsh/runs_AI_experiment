import random
from collections import Counter
from itertools import permutations
from sympy.functions.combinatorial.numbers import stirling
import sys
import time


def generate_floats(n: int) -> list[float]:
    """Returns a list of n random floats"""
    return [random.uniform(0, 1) for _ in range(n)]


def round_floats(floats: list[float]) -> list[float]:
    """Returns a list of floats rounded to two decimal places each"""
    return [round(f, 2) for f in floats]


def is_first_smallest(floats: list[float]) -> bool:
    """Returns True if the first float is the smallest, False otherwise"""
    return floats[0] == min(floats)


def split_into_sublists(lst: list[float]) -> list[list[float]]:
    sublists: list[list[float]] = []
    current_sublist = []

    for num in lst:
        if not current_sublist or num > current_sublist[0]:
            current_sublist.append(num)
        else:
            sublists.append(current_sublist)
            current_sublist = [num]

    if current_sublist:
        sublists.append(current_sublist)

    return sublists


def count_sublists(sublists: list[list[float]]) -> int:
    """Returns the number of sublists in a list of sublists"""
    return len(sublists)


def count_runs(flist: list[float]) -> int:
    """Returns the number of runs in a list of floats"""
    return count_sublists(split_into_sublists(flist))


def collect_runs_count(n: int) -> Counter[int]:
    """Generates r lists of n floats and returns the number of times each run count appears"""
    lst = generate_floats(n)
    c = Counter(count_runs(permutation) for permutation in permutations(lst))
    return dict(sorted(c.items()))


def stirling_numbers_first_kind(n: int) -> list[int]:
    """Returns a list of Stirling numbers of the first kind for 1 to n"""
    return [stirling(n, k, kind=1, signed=False) for k in range(n + 1)]


def weighted_average(counter: Counter) -> float:
    """Returns the weighted average of all keys in a counter"""
    total = sum(k * v for k, v in counter.items())
    return total / counter.total()


def list_length() -> int:
    """Returns the first command-line argument as an int, or 10 if conversion fails."""
    try:
        return int(sys.argv[1])
    except (IndexError, ValueError):
        return 10


# Add this at the end of the main function to calculate and print the elapsed time
def main():
    start_time = time.time()
    max = list_length()
    for n in range(1, max + 1):
        counts = list(collect_runs_count(n).values())
        stirlings = stirling_numbers_first_kind(n)[1:]
        print(f"n: {n}, time: {time.time() - start_time}, equal: {counts == stirlings}")


if __name__ == "__main__":
    main()
