#!/usr/bin/env python3

from itertools import permutations
from sys import argv


def input_check(args_received):
    if len(args_received) not in [2, 7]:
        print(
            "Usage: wordle-permuter.py <green_letters> [<pos1_yellow> <pos2_yellow> ... <pos5_yellow>]\n",
            "NOTE: ensure all possible letters are menitoned in either the green and/or yellow sections",
        )
        return False
    if len(args_received) == 7 and len(args_received[1]) != 5:
        print("Error: provide known letters in their positions ('_'-padded)")
        return False

    return True


def parse_inputs(args_received):
    green_letters = argv[1]
    yellow_letters = argv[2:7] if len(argv) == 7 else [""] * 5
    # no need to flatten "_" entries

    all_letters = set("".join(yellow_letters) + green_letters)
    all_letters.remove("_")

    return "".join(all_letters), green_letters, yellow_letters


def allowed_permutations(all_letters, green_letters, yellow_letters):
    if len(all_letters) != 5:
        all_letters += "_" * (5 - len(all_letters))

    # options = ["".join(p) for p in set(permutations(all_letters)) if p[0] not in yellow_letters[0] and p[1] == green_letters[1]...]
    options = []
    for p in set(permutations(all_letters)):
        keep_possibility = True
        for pos in range(5):
            if (green_letters[pos] != "_" and p[pos] != green_letters[pos]) or (
                p[pos] != "_" and p[pos] in yellow_letters[pos]
            ):
                keep_possibility = False
                break

        if keep_possibility:
            options.append("".join(p))

    return options


if __name__ == "__main__":
    # argv = ["script_name _RE__ R _ IA _ _".split(" ")]
    if not input_check(argv):
        exit(1)

    all, greens, yellows = parse_inputs(argv)

    print(allowed_permutations(all, greens, yellows))
