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
to_char = {}  # for converting from morse back to chars
for key, value in to_morse.items():
    to_char[value] = key
fmt_chars = {" ", ".", "?", "!", ",", "'", "\""}


def is_end_palindrome(s, i):
    j = len(s) - 1
    while i < j:
        if not s[i] == s[j]:
            return False
        i += 1
        j -= 1
    return True


def morse_code_palindrome():
    in_str = input().strip()
    morse_chars = []
    for ch in in_str:
        if ch in fmt_chars:  # Get rid of the special chars
            continue
        morse_chars.append(to_morse[ch])

    morse = "".join(morse_chars)  # convert string to morse code
    i = 0
    while not is_end_palindrome(morse, i):  # check for end-inclusive LPS in morse code string
        i += 1

    if i == 0:  # Input string is already palindromic
        return 0

    # Get the reverse of the chars not in the LPS from the end
    chars = []
    while i > 0:
        i -= 1
        chars.append(morse[i])
    needed = "".join(chars)

    min_found = float("inf")
    found_chars = None
    visited = set()

    def find_chars(current_chars):
        current_morse = "".join(current_chars)

        # print(current_morse)
        if current_morse in visited:  # DP
            return False
        visited.add(current_morse)  # store this tested combination

        if len(current_morse) == len(needed):  # We have mapped the characters needed
            return True

        if len(current_chars) == min_found:  # We already found a shorter combination
            return False

        # no morse code char is greater than 5 chars, no need to check morse than that each iter
        check_len = min(5, len(needed) - len(current_morse))
        while check_len > 0:
            sub_str = needed[len(current_morse):(len(current_morse) + check_len)]
            if to_char.get(sub_str, None):  # substring is a valid morse code char
                # print(morse_needed, current_morse, sub_str)
                current_chars.append(sub_str)  # use the morse char
                is_valid = find_chars(current_chars)  # recurse
                if is_valid:  # valid combination
                    return True
                current_chars.pop()  # invalid combination
            check_len -= 1  # check the next_longest substr
        return False

    needed_count = min(5, len(needed))
    for i in range(needed_count):
        morse_char = needed[:(needed_count - i)]
        if not to_char.get(morse_char, None):
            continue
        current = [morse_char]
        result = find_chars(current)
        if not result:
            continue
        if not len(current) < min_found:
            continue
        found_chars = current
        min_found = len(current)

    # morse_added = "".join(found)
    # print(is_end_palindrome(morse + morse_added, 0))

    chars_to_add = "".join(map(lambda x: to_char[x], found_chars))
    solution = [str(len(found_chars)), chars_to_add]
    return " ".join(solution)


print(morse_code_palindrome())
