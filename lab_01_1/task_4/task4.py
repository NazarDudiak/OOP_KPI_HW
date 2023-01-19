import argparse
from itertools import chain, combinations


def powerset(list_name):
    s = list(list_name)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))


def main():
    parser = argparse.ArgumentParser(description="Lab 03")
    parser.add_argument('-W', dest="capacity", type=int)
    parser.add_argument('-w', dest="weights", nargs="+", default=[])
    parser.add_argument('-n', dest="bars_number", type=int)

    capacity = parser.parse_args().capacity
    weights = list(map(int, parser.parse_args().weights))
    bars_number = parser.parse_args().bars_number

    if bars_number == len(weights):
        max_weight = int()
        for x in powerset(weights):
            if (sum(x) > max_weight) and (sum(x) <= capacity):
                max_weight = sum(x)
            else:
                continue
        print("Max weight:", max_weight)
    else:
        print("Bars count doesn't equal entered list.")


if __name__ == "__main__":
    main()
