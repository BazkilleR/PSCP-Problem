'''ping'''
import re

def summary():
    '''Summarize ping data'''
    input()
    input()
    website = input()

    # Extract the server address from input
    if '[' in website:
        server = re.search(r'\[(.*?)\]', website).group(1)
    else:
        server = website[8: website.find('with') - 1]

    received = 0
    total_time = 0
    min_time = float('inf')
    max_time = float('-inf')

    # Collect ping times
    for _ in range(4):
        response = input()

        if 'Reply from' in response:
            received += 1
            time_idx = response.rfind('time')
            ms_idx = response.rfind('ms')
            time_str = response[time_idx + 5:ms_idx]

            time = 0 if response[time_idx + 4:ms_idx] == '<1' else int(time_str)
            total_time += time

            if time < min_time:
                min_time = time
            if time > max_time:
                max_time = time

    # Calculate statistics
    lost = 4 - received
    avg_time = total_time // received if received > 0 else 0

    # Output results
    print(f'Ping statistics for {server}:')
    print(f'    Packets: Sent = 4, Received = {received}, Lost = {lost} ({lost/4:.0%} loss),')

    if received > 0:
        print('Approximate round trip times in milli-seconds:')
        print(f'    Minimum = {min_time}ms, Maximum = {max_time}ms, Average = {avg_time}ms')

summary()
