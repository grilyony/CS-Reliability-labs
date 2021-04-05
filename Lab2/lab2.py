from itertools import product, compress
from math import prod


def calc_P_Sys(N: int, source: str, probs: list):
    with open(source, 'r') as data:
        table = data.readlines()[1:]
        table = [list(map(lambda x: int(x), elem.rstrip("\n").split(", "))) for elem in table]

    if len(table) - 2 != N:
        print("Wrong input data!")
    else:
        if all([True if 0 <= p <= 1 else False for p in probs]):
            vertices = [i for i in range(len(table[0])) if table[0][i] == 1]
            sts = [int('1' + '0' * (elem - 1) + '1' + '0' * ((len(table) - 1) - elem), 2) for elem in vertices]
            vital = []
            while len(vertices) != 0:
                next_vertices = []
                next_sts = []
                start = 0
                for vt, i in enumerate(vertices):
                    next_vertices += [j for j in range(len(table[i])) if table[i][j] == 1 and bin(sts[vt])[2:][j] == '0']
                    next_sts += [sts[vt] + int("0" * elem + "1" + "0" * ((len(table) - 1) - elem), 2)
                                   for elem in next_vertices[start:]]
                    start = len(next_vertices)
                sts = next_sts
                vertices = next_vertices
                vital += [sts[i] for i in range(len(vertices)) if vertices[i] == len(table) - 1]
                sts = [state for state in sts if state not in vital]
                vertices = [ix for ix in vertices if ix != len(table) - 1]

            vital = [int(bin(elem)[2:][1: -1], 2) for elem in vital]
            P_sys = 0
            work_states = []
            for path in vital:
                all_states = product(range(2), repeat=len(table) - 2)
                for state in all_states:
                    mask = int("".join(list(map(lambda x: str(x), state))), 2)
                    if path & mask == path:
                        work_states.append(mask)
            work_states = list(set(work_states))

            elems = [f'E{i}' for i in range(1, len(table) - 1)]
            print("\nAll possible paths from start to end:")
            for path in vital:
                bin_mask = list(map(lambda x: int(x), list(bin(path)[2:])))
                possible_path = compress(elems, bin_mask)
                print(" -> ".join(possible_path))
            title_str = "| " + " | ".join([f'E{i}' for i in range(1, len(table) - 1)] + [""]) + "P".center(14) + "|"
            print("\nAll working states and their probabilities:")
            print(title_str)
            for state in work_states:
                binary = bin(state)[2:]
                binary_state = list(binary.rjust(len(table) - 2, '0'))
                element_probs = [p if binary_state[i] == '1' else 1 - p for i, p in enumerate(probs)]
                state_prob = prod(element_probs)
                print('-' * len(title_str))
                print("| " + "  | ".join(binary_state + [""]) + f"{state_prob:e}".center(14) + "|")
                P_sys += state_prob
            print(f"Number of all working states: {len(work_states)}")
            return P_sys
        else:
            print("Incorrect probabilities!")


if __name__ == "__main__":
    N = input("Input number of elements: ")
    while not N.isnumeric():
        N = input("Incorrect value, try again:")
    N = int(N)

    while True:
        ps = input("Input probabilities: ").strip()
        try:
            ps = list(map(lambda x: float(x), ps.split(" ")))
            if len(ps) == N:
                break
            else:
                print("Incorrect number of probabilities!")
        except ValueError:
            print("Incorrect input")
    P_sys = calc_P_Sys(N, 'data.txt', ps)
    print(f"Total system reliability: {P_sys}")
