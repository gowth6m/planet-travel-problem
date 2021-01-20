# Question 1 - Planet Problem


def str_to_coord(line):
    """
    Takes a string, splits the string and turns it into a list that represents coordinates.
    :param line: string of coordinate
    :return: a list of floats that represents a coordinate
    """
    coordinates = []
    for i in line.split():
        i = float(i)
        if not (-10000 <= i <= 10000):  # Checks if coordinate is within given range
            raise Exception('Invalid coordinate value, not within given range')
        coordinates.append(i)
    if len(coordinates) > 3:  # Checks if there are only 3 numbers in a coordinate
        raise Exception('Invalid coordinate value, more than 3 coordinate values')
    return coordinates


def get_input():
    """
    Asks user for Zearth's coordinate, asks user for number of stations then asks for the station coordinates.
    Finally stores Zearth's coordinate in global variable ZEARTH_COORDINATE and returns 2D array of coordinates of
    teleportation stations.
    :return: a 2D array of coordinates of the teleportation stations in space
    """
    earth_coord = [0.0, 0.0, 0.0]
    all_coords = [earth_coord]
    raw_zearth_coord = input()
    zearth_coord = str_to_coord(raw_zearth_coord)
    no_of_stations = int(input())
    if 1 <= no_of_stations <= 2000:
        while no_of_stations > 0:
            raw_station_coord = input()
            all_coords.append(str_to_coord(raw_station_coord))
            no_of_stations -= 1
    else:
        raise Exception("Invalid format, number of coordinates not within given range")
    all_coords.append(zearth_coord)
    return all_coords


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


def get_weighted_graph(coords):
    """
    Format of the graph dictionary = {node_1 : {node_2: weight_1&2, node_3: weight_1&3}}
    :return: a weighted graph of stations including Earth and Zearth.
    """
    graph = {}
    for i in range(len(coords)):
        graph[i] = {}
        for j in range(len(coords)):
            if j != i:
                graph[i].update({j: get_weight(coords[i], coords[j])})
    return graph


def modified_dijkstra(graph, start, finish):
    """
    Modified version of dijkstra's algorithm that calculates the min max distance.
    :param graph: graph of the space stations
    :param start: starting node (Earth)
    :param finish: finishing node (Zearth)
    :return: max teleporting distance, total distance travelled, a list of the path taken
    """
    total_distance, infinity = 0, float('inf')
    max_distance, predecessor, tracker = {}, {}, {}
    unvisitedNodes = graph
    path = []

    for node in unvisitedNodes:
        max_distance[node] = infinity
    max_distance[start] = 0

    while len(unvisitedNodes) > 0:
        minNode = None
        for node in unvisitedNodes:
            if minNode is None:
                minNode = node
            elif max_distance[node] < max_distance[minNode]:
                minNode = node

        for childNode, weight in graph[minNode].items():
            if max(weight, max_distance[minNode]) < max_distance[childNode]:
                max_distance[childNode] = max(weight, max_distance[minNode])
                predecessor[childNode] = minNode
        tracker[minNode] = unvisitedNodes[minNode]
        unvisitedNodes.pop(minNode)

    currentNode = finish
    while currentNode != start:
        path.insert(0, currentNode)
        currentNode = predecessor[currentNode]
        total_distance += tracker.get(finish).get(currentNode)
    path.insert(0, start)
    return max_distance[finish], total_distance, path


if __name__ == '__main__':
    try:
        coordinates = get_input()
        g = get_weighted_graph(coordinates)
        earth = 0  # Earth is 0th node
        zearth = len(g) - 1  # Zearth is last node
        max_teleport_dist, total_path_dist, safest_path = modified_dijkstra(g, earth, zearth)
        print(round(max_teleport_dist, 2))  # rounding to 2 dp
        print("Total distance: ", total_path_dist)
        print("Path taken: ", safest_path)
    except KeyboardInterrupt:
        raise Exception("Program interrupted")
