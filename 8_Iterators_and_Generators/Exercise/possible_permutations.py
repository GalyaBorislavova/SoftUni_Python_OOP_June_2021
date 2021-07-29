# from itertools import permutations
#
#
# def possible_permutations(sequence):
#     perms = permutations(sequence)
#     for p in perms:
#         yield list(p)

def generate_all_permutations(sequence):
    if len(sequence) == 0 or len(sequence) == 1:
        return [sequence]

    current = []

    for ind, el in enumerate(sequence):
        first = el

        rest_elements = sequence[:ind] + sequence[ind + 1:]
        for p in generate_all_permutations(rest_elements):
            current.append([first] + p)

    return current


def possible_permutations(sequence):
    perms = generate_all_permutations(sequence)
    for p in perms:
        yield p


[print(n) for n in possible_permutations([1, 2, 3, 4])]