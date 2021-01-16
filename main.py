# Question 1 - Planet Problem

# Coordinate of Zearth
import math
import sys

EARTH_COORDINATE = [0.0, 0.0, 0.0]
ZEARTH_COORDINATE = []
STATION_COORDINATES = []
ASSIGNED_COORDINATES = {}


def askForInput():
    """
    Asks user for Zearth's coordinate, asks user for number of stations then asks for the station coordinates.
    Finally stores Zeath's coordinate in global variable ZEARTH_COORDINATE and returns 2D array of coordinates of
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


class Graph:
    """
    Graph class used for teleportation stations
    """
    graph_dict = {}

    def addEdge(self, node, neighbour):
        if node not in self.graph_dict:
            self.graph_dict[node] = [neighbour]
        else:
            self.graph_dict[node].append(neighbour)

    def show_edges(self):
        for node in self.graph_dict:
            for neighbour in self.graph_dict[node]:
                print("(", node, ", ", neighbour, ")")


def get_graph(num_nodes, nodes, weight_Func):
    """
    Creates a fully connected graph in dictionary form for the nodes. Each edge has a weight value determined by weight_Func
    """
    graph = {}  # Creates empty graph with the required number of nodes with no edges
    for i in range(num_nodes):
        graph[str(i)] = {}  # Each node is labeled with a number e.g: zearth = '1'

    # Adds each edge to the fully connected graph with weight values assigned
    for i, node1 in enumerate(nodes):
        for j, node2 in enumerate(nodes):
            if i != j:
                if str(j) not in graph[str(i)]:  # Assuring each weight is only calculated once
                    weight = weight_Func(node1, node2)
                    graph[str(i)][str(j)] = weight
                    graph[str(j)][str(i)] = weight
    return graph


def assignNodesToCoordinates():
    """
    Each node is given a coordinate and assigned to global dictionary ASSIGNED_COORDINATES
    :return: null
    """
    counter = 0
    for i in STATION_COORDINATES:
        ASSIGNED_COORDINATES[counter] = i
        counter += 1


def createGraphForStations():
    stations = Graph()
    # for i in ASSIGNED_COORDINATES.keys():
    #     stations.addEdge()
    return stations


def getWeight(node1, node2):
    """
    :param node1: array containing x,y,z values for first node
    :param node2: array containing x,y,z values for second node
    :return: weight of the edge between the 2 nodes
    """
    x_value = (node1[0] - node2[0]) ** 2
    y_value = (node1[1] - node2[1]) ** 2
    z_value = (node1[2] - node2[2]) ** 2
    weight = math.sqrt(x_value + y_value + z_value)
    return weight


def findSafestPathDistance():
    pathDistance = 0
    return pathDistance


def checkForInputFile():
    # print command line arguments
    args = []
    for arg in sys.argv[1:]:
        args.append(arg)
        print(args)
    if args[0] == '<':
        print("USING INPUT FILE" + args[1])


if __name__ == '__main__':
    # checkForInputFile()
    try:
        askForInput()
        assignNodesToCoordinates()
    except KeyboardInterrupt:
        pass
    createGraphForStations()
    # print(STATION_COORDINATES)
    # print(getWeight([2, 3, 2], [2, 1, 2]))
    print("Dictionary of nodes: ", ASSIGNED_COORDINATES)
    # print("Zearth Coordinate: ",ZEARTH_COORDINATE)
