# https://open.kattis.com/problems/brickwall

from sys import stdin
import itertools


def main():
    available_bricks_str = stdin.readline().strip()
    available_bricks = [int(num) for num in available_bricks_str.split()][1:]

    top_layer_str = stdin.readline().strip()
    top_layer = [int(num) for num in top_layer_str.split()]

    top_layer_seams = set(itertools.accumulate(top_layer))
    top_layer_sum = sum(top_layer)

    victory = can_add_layer(top_layer_seams, top_layer_sum, available_bricks)
    print('YES' if victory else 'NO')


def can_add_layer(top_layer_seams, top_layer_sum, available_bricks, current_sum=0, memo=None):
    # Base
    if current_sum == top_layer_sum:
        return True

    # History
    if memo is None:
        memo = {}
    state_key = (current_sum, tuple(available_bricks))
    if state_key in memo:
        return memo[state_key]

    # Skips
    if current_sum > top_layer_sum:
        memo[state_key] = False
        return False

    if current_sum in top_layer_seams:
        memo[state_key] = False
        return False

    if sum(available_bricks) == 0:
        memo[state_key] = False
        return False

    # Try those bricks big to small
    for brick_idx in reversed(range(len(available_bricks))):
        brick_size = brick_idx + 1
        count = available_bricks[brick_idx]
        if count > 0:
            # Decrease the count for the current number and recurse
            available_bricks[brick_idx] -= 1
            victory = can_add_layer(top_layer_seams, top_layer_sum, available_bricks, current_sum + brick_size, memo)
            # We did it! Time to go home
            if victory:
                return True
            # Revert the count for backtracking
            available_bricks[brick_idx] += 1

    # Tried them all
    memo[state_key] = False
    return False


if __name__ == "__main__":
    main()
