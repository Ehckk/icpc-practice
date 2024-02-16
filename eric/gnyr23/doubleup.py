import sys

sys.setrecursionlimit(pow(10, 6))


def solve():
    def merge(seq, i):
        new_seq = []
        for j in range(len(seq)):
            if j == i:
                continue
            if j == i + 1:
                new_seq.append(seq[j] * 2)
                continue
            new_seq.append(seq[j])
        return new_seq

    def remove(seq, i):
        new_seq = []
        for j in range(len(seq)):
            if j == i:
                continue
            new_seq.append(seq[j])
        return new_seq

    results = {}  # DP

    def double_up(seq):
        seq_str = " ".join(map(str, seq))
        if results.get(seq_str, None):
            return results[seq_str]
        print(seq_str)

        if len(seq) == 1:
            return seq[0]  # Sequence is 1 number -> max

        max_value = max(seq)  # max value is highest possible power of 2

        for i in range(len(seq)):
            if i == len(seq) - 1:  # avoid array out of bounds
                continue
            if seq[i] == seq[i + 1]:  # two equal, adjacent terms
                new_seq = merge(seq, i)
                result = double_up(new_seq)
                if result < max_value:
                    continue
                max_value = result

        for i in range(len(seq)):  # removing any term -> a case
            new_seq = remove(seq, i)
            result = double_up(new_seq)
            if result < max_value:
                continue
            max_value = result

        results[seq_str] = max_value
        return max_value

    _ = input()
    sequence = list(map(int, input().strip().split()))
    solution = double_up(sequence)
    # print(results)
    return solution


print(solve())
