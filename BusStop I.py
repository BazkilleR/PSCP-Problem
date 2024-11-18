"""BusStop I"""

def main():
    """BusStop I"""
    max_bus_stops = int(input())
    num_stops = int(input())
    stop_data = []
    bus_stops = []
    bus = []

    for _ in range(num_stops):
        stop_info = input().split()
        stop_data.append(stop_info)

    stop_data.sort(key=lambda x: int(x[0]))

    for stop in stop_data:
        bus_stops.append(stop[0])

    k = 0
    successful_buses = 0

    for stop in stop_data:
        for j in stop[1:]:
            if j in bus_stops[k:] and len(bus) < max_bus_stops:
                bus.append(j)

        k += 1

        for bus_stop in bus[:]:
            if bus_stop == bus_stops[k]:
                bus.remove(bus_stop)
                successful_buses += 1

    print(successful_buses)

main()
