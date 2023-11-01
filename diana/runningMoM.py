import sys
from collections import defaultdict

def parse(input):
    flights = defaultdict(list)
    lines = input.splitlines()

    numflights = int(lines[0])

    for flight in range(numflights):
        origin, destination = lines[flight+1].split(" ")

        if not origin in flights:
            flights[origin] = []
        flights[origin].append(destination)

    cities = []
    for city in lines[numflights+1:]:
        cities.append(city)

    return flights, cities

def has_cycle(flights, origin, visited, recursion_stack):
    visited.add(origin)
    recursion_stack.add(origin)

    for destination in flights[origin]:
        if destination not in visited:
            if has_cycle(flights, destination, visited, recursion_stack):
                return True
        elif destination in recursion_stack:
            return True

    recursion_stack.remove(origin)
    return False

input_str = "".join(sys.stdin.readlines())
flights, cities = parse(input_str)

for city in cities:
    visited = set()
    recursion_stack = set()
    if has_cycle(flights, city, visited, recursion_stack):
        print(city, "safe")
    else:
        print(city, "trapped")