# Question 1 - Planet Problem

# Coordinate of Zearth
import sys

ZEARTH_COORDINATE = []


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
            if (-10000 <= x <= 10000) and (-10000 <= y <= 10000) and (-10000 <= z <= 10000) and (1 <= noOfStations <= 2000):
                # Storing coordinates in a 2D array & looping the 2D array while asking for coordinates from std in
                stationCoordinates = [[0 for i in range(3)] for j in range(noOfStations)]
                for coordinate in stationCoordinates:
                    raw_c = input()
                    c1, c2, c3 = raw_c.split()
                    coordinate[0], coordinate[1], coordinate[2] = float(c1), float(c2), float(c3)
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
    return stationCoordinates


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
        print("USING INPUT FILE"+args[1])


if __name__ == '__main__':
    # checkForInputFile()
    print(askForInput())
    print("Zearth Coordinate: ",ZEARTH_COORDINATE)
