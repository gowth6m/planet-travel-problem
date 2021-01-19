# Question 1 - Planet Problem

EARTH_COORDINATE = [0.0, 0.0, 0.0]
ZEARTH_COORDINATE = []
STATION_COORDINATES = []


def line_to_coord(line):
    """
    Takes a string and turns it into a list that represents coordinates.
    :param line: string of coordinate
    :return: a list of floats that represents a coordinate
    """
    coords = []
    for i in line.split():
        i = float(i)
        if not (-10000 <= i <= 10000):
            raise Exception('Invalid coordinate value, not within given range')
        coords.append(i)
    if len(coords) > 3:  # Checks if there are only 3 numbers in a coordinate
        raise Exception('Invalid coordinate value, more than 3 coordinate values')
    return coords


def ask_for_input():
    """
    Asks user for Zearth's coordinate, asks user for number of stations then asks for the station coordinates.
    Finally stores Zearth's coordinate in global variable ZEARTH_COORDINATE and returns 2D array of coordinates of
    teleportation stations.
    :return: a 2D array of coordinates of the teleportation stations in space
    """
    STATION_COORDINATES.append(EARTH_COORDINATE)
    raw_zearth_coord = input()
    global ZEARTH_COORDINATE
    ZEARTH_COORDINATE = line_to_coord(raw_zearth_coord)
    no_of_stations = int(input())
    if 1 <= no_of_stations <= 2000:
        while no_of_stations > 0:
            raw_station_coord = input()
            STATION_COORDINATES.append(line_to_coord(raw_station_coord))
            no_of_stations -= 1
    else:
        raise Exception("Invalid format, number of coordinates not within given range")
    STATION_COORDINATES.append(ZEARTH_COORDINATE)


def get_weight(node1, node2):
    """
    Calculates the Euclidean distance between two coordinates
    :param node1: array containing x,y,z values for first node
    :param node2: array containing x,y,z values for second node
    :return: weight of the edge between the 2 nodes
    """
    x_value = (node1[0] - node2[0]) ** 2
    y_value = (node1[1] - node2[1]) ** 2
    z_value = (node1[2] - node2[2]) ** 2
    weight = (x_value + y_value + z_value) ** (1 / 2)
    return weight


def get_weighted_graph():
    """
    Format of the graph dictionary = {node_1 : {node_2: weight_1&2, node_3: weight_1&3}}
    :return: a weighted graph of stations including Earth and Zearth.
    """
    graph = {}
    for i in range(len(STATION_COORDINATES)):
        graph[i] = {}
        for j in range(len(STATION_COORDINATES)):
            if j != i:
                graph[i].update({j: get_weight(STATION_COORDINATES[i], STATION_COORDINATES[j])})
    return graph


def find_safest_path_distance(graph, start, finish):
    max_distance = {}
    unseenNodes = graph
    infinity = float("inf")
    for node in unseenNodes:  # Initiates the minimum maximum distance for each node to be infinity
        max_distance[node] = infinity
    max_distance[start] = 0

    while unseenNodes:
        minNode = None
        for node in unseenNodes:  # Finding the minimum weighted node so far
            if minNode is None:  # Base case
                minNode = node
            elif max_distance[node] < max_distance[minNode]:
                minNode = node

        for childNode, weight in graph[minNode].items():
            if max(weight, max_distance[minNode]) < max_distance[childNode]:  # Takes maximum of weights along path
                max_distance[childNode] = max(weight, max_distance[minNode])
        unseenNodes.pop(minNode)  # Breaks loop when finished

    return max_distance[finish]


if __name__ == '__main__':
    try:
        ask_for_input()
        world = get_weighted_graph()
        # Earth = 0th node, Zearth = Last node
        shortest_distance = find_safest_path_distance(world, 0, len(world) - 1)
        print(shortest_distance)
    except KeyboardInterrupt:
        raise Exception("Program interrupted")
