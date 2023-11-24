wordsList = list(input().split())
wordsSet = set(wordsList)

if len(wordsSet) == len(wordsList):
    print('yes')
else:
    print('no')