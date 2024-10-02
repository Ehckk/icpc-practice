def main():
    s = input()

    currentColor = s[0]
    sign = 1 if currentColor == 'B' else -1
    count = 0

    # Condense letters into numbers where R = (-) and B = (+)
    # For instance 'RRRBBRB' becomes [-3, 2, -1, 1]
    blocks = []
    for color in s:

        if color != currentColor:
            blocks.append(count * sign)
            currentColor = 'B' if currentColor == 'R' else 'R'
            sign *= -1
            count = 0
        
        count += 1

    blocks.append(count * sign)

    # initialize variables
    ## max value and indeces
    maxDiff = 0
    maxIndeces = (-1, -1)

    ## sum
    runningSum = 0

    ## detect sign change
    prevSign = getSign(blocks[0])

    ## pointers
    left_ans = len(s)+1
    right_ans = len(s)

    # iterate backwards through blocks
    for i in range(len(blocks)-1, -1, -1):

        prevSign = getSign(runningSum)
        
        # move left pointer and add to sum
        left_ans = left_ans - abs(blocks[i])
        runningSum += blocks[i]

        # if running sum sign flipped or is 0, move pointers 
        # and reset sum
        if (getSign(runningSum) != prevSign):
            runningSum = blocks[i]
            right_ans = left_ans + abs(blocks[i]) - 1

        # update max value and pointers 
        if abs(runningSum) >= abs(maxDiff):
            maxDiff = runningSum
            maxIndeces = (left_ans, right_ans) 

    # return result
    print(maxIndeces[0], maxIndeces[1]) 

# helper function to get sign of running sum
def getSign(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0

main()
