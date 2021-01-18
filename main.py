# Question 1 - Planet Problem

EARTH_COORDINATE = [0.0, 0.0, 0.0]
ZEARTH_COORDINATE = []
STATION_COORDINATES = []
ASSIGNED_COORDINATES = {}


def input_from_file(file):
    """
    Gets data from text file
    :param file: name of the text file
    :return: none
    """
    lines = open(file).read().split('\n')
    global ZEARTH_COORDINATE
    ZEARTH_COORDINATE = line_to_coord(lines[0])
    if not (1 <= int(lines[1]) <= 2000):
        raise Exception('Invalid number of stations')
    # Get coordinates of stations
    for i in range(len(lines)):
        if (i == 0) or (i == 1):
            pass
        else:
            STATION_COORDINATES.append(line_to_coord(lines[i]))


def line_to_coord(line):
    """
    Takes a string and turns it into a list that represents coordinates.
    :param line: string of coordinate
    :return: a list of floats that represents a coordinate
    """
    coords = []
    for i in line.split():
        i = float(i)
        if (i < -10000.0) or (i > 10000.0):  # Validates coordinate values
            raise Exception('Invalid coordinate value')
        coords.append(i)
    if len(coords) > 3:  # Checks if there are only 3 numbers in a coordinate
        raise Exception('Invalid coordinate value')
    return coords


def ask_for_input():
    """
    Asks user for Zearth's coordinate, asks user for number of stations then asks for the station coordinates.
    Finally stores Zearth's coordinate in global variable ZEARTH_COORDINATE and returns 2D array of coordinates of
    teleportation stations.
    :return: a 2D array of coordinates of the teleportation stations in space
    """
    correctFormat = False
    while not correctFormat:
        try:
            print("Enter coordinates of the planet Zearth:")
            raw_coordinates = input()
            x, y, z = raw_coordinates.split()
            x, y, z = float(x), float(y), float(z)
            print("Enter number of stations:")
            noOfStations = int(input())
            if (-10000 <= x <= 10000) and (-10000 <= y <= 10000) and (-10000 <= z <= 10000) and (
                    1 <= noOfStations <= 2000):
                # Storing coordinates in a 2D array & looping the 2D array while asking for coordinates from std in
                stationCoordinates = [[0 for i in range(3)] for j in range(noOfStations)]
                for coordinate in stationCoordinates:
                    raw_c = input()
                    c1, c2, c3 = raw_c.split()
                    coordinate[0], coordinate[1], coordinate[2] = float(c1), float(c2), float(c3)
                    STATION_COORDINATES.append(coordinate)
                # Checking for correct range if the station coordinates
                correctFormat = True
                for coordinate in stationCoordinates:
                    for point in coordinate:
                        if not (-10000 <= point <= 10000):
                            correctFormat = False
                            print("Error, incorrect format.")
        except ValueError:
            print("Error, incorrect format.")
    # Storing the initial coordinate of Zearth
    ZEARTH_COORDINATE.append(x), ZEARTH_COORDINATE.append(y), ZEARTH_COORDINATE.append(z)
    # return stationCoordinates


def assign_nodes_to_coordinates():
    """
    Each node is given a coordinate and assigned to global dictionary ASSIGNED_COORDINATES
    :return: null
    """
    counter = 1
    ASSIGNED_COORDINATES[0] = EARTH_COORDINATE
    for i in STATION_COORDINATES:
        ASSIGNED_COORDINATES[counter] = i
        counter += 1
    ASSIGNED_COORDINATES[counter] = ZEARTH_COORDINATE  # adding in zearth's coordinates to assigned_coordinates


def get_weighted_graph():
    """
    Format of the graph dictionary = {node_1 : {node_2: weight_1&2, node_3: weight_1&3}}
    :return: a weighted graph of stations including Earth and Zearth.
    """
    graph = {}
    for i in ASSIGNED_COORDINATES.keys():
        graph[i] = {}
        for j in ASSIGNED_COORDINATES.keys():
            if j != i:
                graph[i].update({j: get_weight(ASSIGNED_COORDINATES[i], ASSIGNED_COORDINATES[j])})
    return graph


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
    weight = (x_value + y_value + z_value) ** (1/2)
    return weight


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
    # try:
    #     ask_for_input()
    #     assign_nodes_to_coordinates()
    # except KeyboardInterrupt:
    #     pass
    filename = 'input.txt'  # Load input file
    input_from_file(filename)
    assign_nodes_to_coordinates()
    world = get_weighted_graph()
    print(world)
    print("====TEST====")
    # test_find_path(world, 0, len(world) - 1)
    answer = find_safest_path_distance(world, 0, len(world) - 1)
    print(answer)