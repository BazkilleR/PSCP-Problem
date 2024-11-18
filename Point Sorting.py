"""Point Sorting"""

def main():
    """Point Sorting"""
    results = []
    test_cases = int(input())

    for _ in range(test_cases):
        points = []
        num_points = int(input())

        for _ in range(num_points):
            coordinates = input()
            coordinates = coordinates.split()
            points.append([int(coordinates[0]) + int(coordinates[1])] + coordinates)

        points.sort(key=lambda x: (int(x[0]), -int(x[2])))

        for point in points:
            results.append(point[1] + " " + point[2])

    for result in results:
        print(result)

main()
