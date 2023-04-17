import sys


def parse_input(airports: list):  # -> dict, list

    n_trips = int(airports[0][0])
    check_safe = [i for arr in airports[n_trips + 1:] for i in arr]

    flight_graph = {}

    for dep, des in airports[1:n_trips + 1]:
        if dep not in flight_graph:
            flight_graph[dep] = [des]
        else:
            flight_graph[dep].append(des)

    return flight_graph, check_safe


def find_safe_cities(from_parse: list) -> str:
    graph, cities_to_check = parse_input(from_parse)
    visit = set()
    visited = set()  # remember visited nodes

    def dfs(city: str):
        if city in visit:
            # safe.add(city)
            return True

        if city in visited:
            return

        visit.add(city)
        visited.add(city)

        for destination in graph.get(city, []):
            if dfs(destination):
                return True
            # if destination in safe:
            #     safe.add(destination)
            #     return True

        visit.remove(city)

    res = []

    for location in cities_to_check:
        # visited.clear()
        if dfs(location):
            # if location in safe:
            res.append(location + ' safe')
        else:
            res.append(location + ' trapped')

    return '\n'.join(res)


flights = []

for flight in sys.stdin:
    flights.append(flight.split())

print(find_safe_cities(flights))
