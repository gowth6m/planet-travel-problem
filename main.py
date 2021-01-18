# Question 1 - Planet Problem

# Coordinate of Zearth
import math
import fileinput

EARTH_COORDINATE = [0.0, 0.0, 0.0]
ZEARTH_COORDINATE = []
STATION_COORDINATES = []
ASSIGNED_COORDINATES = {0: EARTH_COORDINATE}


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
    for i in STATION_COORDINATES:
        ASSIGNED_COORDINATES[counter] = i
        counter += 1
    ASSIGNED_COORDINATES[counter] = ZEARTH_COORDINATE  # adding in zearth's coordinates to assigned_coordinates


def get_weighted_graph():
    """
    Format of the graph dictionary = { node_1 : [[node_2, weight_1&2],[node_3, weight_1&3]] }
    :return: a weighted graph of stations including Earth and Zearth.
    """
    graph = {}
    final_node = len(ASSIGNED_COORDINATES)  # Zearth's node
    for i in ASSIGNED_COORDINATES.keys():
        if i == 0:
            graph[0] = [0, ASSIGNED_COORDINATES[0]]  # setting 0th node as earth's coordinate
        if i == final_node:
            graph[final_node] = [final_node, ASSIGNED_COORDINATES[final_node]]

        graph[i] = []
        for j in ASSIGNED_COORDINATES.keys():
            if j != i:
                graph[i].append([j, get_weight(ASSIGNED_COORDINATES[i], ASSIGNED_COORDINATES[j])])
    # print(graph)
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
    weight = math.sqrt(x_value + y_value + z_value)
    return weight


def find_safest_path_distance():
    pathDistance = 0
    return pathDistance


# def checkForInputFile():
#     # print command line arguments
#     args = []
#     for arg in sys.argv[1:]:
#         args.append(arg)
#         print(args)
#     if args[0] == '<':
#         print("USING INPUT FILE" + args[1])


if __name__ == '__main__':
    try:
        ask_for_input()
        assign_nodes_to_coordinates()
    except KeyboardInterrupt:
        pass
    print(get_weighted_graph())
    # print(STATION_COORDINATES)
    # print(getWeight([2, 3.5, 2], [2, 12, 213]))
    print("Dictionary of nodes: ", ASSIGNED_COORDINATES)
    # print("Zearth Coordinate: ",ZEARTH_COORDINATE)
