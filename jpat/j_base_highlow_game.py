# http://acmgnyr.org/year2023/problems/index.html
# J-basehilo

import sys

DIGITS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvxyz"
TESTING = False


def main():
    input_line = input("Input Base & Tests: ") if TESTING else sys.stdin.readline()
    base, num_tests = map(int, input_line.strip().split())
    for _ in range(num_tests):
        num_digits_line = input("Input Number of Digits: ") if TESTING else sys.stdin.readline()
        num_digits = int(num_digits_line.strip())
        lower_bounds = [0] * num_digits
        upper_bounds = [base - 1] * num_digits
        current_guess = [0] * num_digits

        while True:
            for i in range(num_digits):
                current_guess[i] = (lower_bounds[i] + upper_bounds[i]) // 2

            feedback = make_guess(format_guess(current_guess))

            if feedback == "correct":
                break

            if(all(position == '=' for position in feedback)):
                print("cheater", flush=True)
                sys.stdin.readline()
                break

            update_bounds(feedback, lower_bounds, upper_bounds, current_guess)

            if check_cheating(lower_bounds, upper_bounds):
                print("cheater", flush=True)
                sys.stdin.readline()
                break


def format_guess(guess_indices):
    return ''.join(DIGITS[idx] for idx in guess_indices)


def make_guess(guess_str):
    print(guess_str, flush=True)
    if(TESTING):
        return input("Feedback: ")
    else:
        return sys.stdin.readline().strip()


def update_bounds(feedback, lower_bounds, upper_bounds, current_guess):
    for i, fb_char in enumerate(feedback):
        if fb_char == '=':
            lower_bounds[i] = upper_bounds[i] = current_guess[i]
        elif fb_char == '-':
            upper_bounds[i] = current_guess[i] - 1
        elif fb_char == '+':
            lower_bounds[i] = current_guess[i] + 1


def check_cheating(lower_bounds, upper_bounds):
    return any(low > high for low, high in zip(lower_bounds, upper_bounds))


if __name__ == "__main__":
    main()
