"""Runner"""

def main():
    """Runner"""
    distance = float(input())
    num_runners = int(input())
    speed_list = []
    times = []
    runner_times = []

    for _ in range(num_runners):
        runner_data = input().split()
        speed_list.append(str((distance - int(runner_data[1]))
                              / int(runner_data[0])) + " " + runner_data[0])

    for speed in speed_list:
        times.append(str(speed).split())

    for i, row in enumerate(times):
        for j, value in enumerate(row):
            times[i][j] = float(value)

    for row in times:
        runner_times.append(row[0])

    if runner_times.count(min(runner_times)) <= 1:
        print(runner_times.index(min(runner_times)) + 1)
    else:
        print(runner_times.index(min(runner_times)) + 2)

main()
