# https://open.kattis.com/problems/nodup
# No Duplicates: Output is "yes" if no word is repeated,
# and "no" if one or more words repeat.

# split input line into tokens them map to a list
input_line = input().strip()
words = list(input_line.split())

if len(words) == len(set(words)):
    print('yes')
else:
    print('no')
