to_morse = {
    "A": "._",
    "B": "_...",
    "C": "_._.",
    "D": "_..",
    "E": ".",
    "F": ".._.",
    "G": "__.",
    "H": "....",
    "I": "..",
    "J": ".___",
    "K": "_._",
    "L": "._..",
    "M": "__",
    "N": "_.",
    "O": "___",
    "P": ".__.",
    "Q": "__._",
    "R": "._.",
    "S": "...",
    "T": "_",
    "U": ".._",
    "V": "..._",
    "W": ".__",
    "X": "_.._",
    "Y": "_.__",
    "Z": "__..",
    "0": "_____",
    "1": ".____",
    "2": "..___",
    "3": "...__",
    "4": "...._",
    "5": ".....",
    "6": "_....",
    "7": "__...",
    "8": "___..",
    "9": "____."
}
fmt_chars = {" ", ".", "?", "!", ",", "'", "\""}


def is_palindrome(s):
    i = 0
    j = len(s) - 1
    while i < j:
        if not s[i] == s[j]:
            return False
        i += 1
        j -= 1
    return True


def judge(submission, answer, testcase):
    s_values = submission.strip().split()
    a_values = answer.strip().split()
    s_count = int(s_values[0])
    a_count = int(a_values[0])
    if a_count == 0:
        return s_count == a_count
    full_str = testcase.strip() + s_values[1]
    full_morse_str = "".join([to_morse[ch] for ch in full_str if ch not in fmt_chars])
    return s_count <= a_count and is_palindrome(full_morse_str)
