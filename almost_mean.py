'''AlmostMean'''
def main():
    '''_'''
    num_list = []
    id_list = []

    for _ in range(int(input())):
        text_input = input()
        input_list = text_input.split()
        num_list.append(float(input_list[1]))
        id_list.append(input_list[0])

    avg = sum(num_list) / len(num_list)
    almostmean = 0

    for i in num_list:
        if almostmean < i <= avg :
            almostmean = i
    num_index = num_list.index(almostmean)
    print(f'{id_list[num_index]}\t{almostmean}')

main()
