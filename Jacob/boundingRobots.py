'''
Jacob Stephens, ICPC
April 14, 2023
Bounding Robots Kattis https://open.kattis.com/problems/boundingrobots
'''

# repeat processes for max amnt of simulations
for i in range(100):
    inputLine = input()
    
    # case to stop program
    if inputLine == '0 0':
        break

    # parse input
    inputList = inputLine.split()
    numOrders = int(input())
    w = int(inputList[0])
    l = int(inputList[1])
    
    # positions [x, y]
    posActual = [0 , 0]
    posRobot = [0, 0]

    for _ in range(numOrders):
        order = input()
        dir = order[:1]
        distance = int(order[2:])

        # adjust positions based on order
        # right
        if dir == 'r':
            posRobot[0] += distance
            posActual[0] += distance
            
            # limit actual position to stop at right wall (x = w-1)
            if posActual[0] > (w-1):
                posActual[0] = (w-1)

        # left
        elif dir == 'l':
            posRobot[0] -= distance
            posActual[0] -= distance

            # limit actual position to stop at left wall (x = 0)
            if posActual[0] < 0:
                posActual[0] = 0

        # up
        elif dir == 'u':
            posRobot[1] += distance
            posActual[1] += distance
            
            # limit actual position to stop at top wall (y = l-1)
            if posActual[1] > (l-1): 
                posActual[1] = (l-1)

        # down
        elif dir == 'd':
            posRobot[1] -= distance
            posActual[1] -= distance
            
            # limit actual position to stop at bottom wall (y = 0)
            if posActual[1] < 0:
                posActual[1] = 0

    # print output every simulation
    print(f'Robot thinks {posRobot[0]} {posRobot[1]}')
    print(f'Actually at {posActual[0]} {posActual[1]}')
