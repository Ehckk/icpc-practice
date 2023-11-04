num_seq = input()
seq = list(map(int, input().split()))
seq.append("")  # Adding an empty string to denote the end of the sequence


def solution(sequence):
    i = 1
    curr = sequence[0]
    val = 0
    while i < len(sequence) - 1:
        if sequence[i] == curr:
            curr *= 2
            i += 1
        elif sequence[i] == val:
            val *= 2
            i += 1
        elif i + 1 < len(sequence) and sequence[i] == sequence[i + 1]:
            val += sequence[i] + sequence[i + 1]
            if val == curr:
                curr *= 2
                i += 2
                val = 0
            elif val > curr:
                curr = val
                val = 0
                i += 1
            else:
                i += 2
        else:
            if val == 0:
                val = sequence[i]
            i += 1
    if val == curr:
        curr *= 2
    return curr


print(solution(seq))
