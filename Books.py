'''books'''
import math

def read_book(books_count, pages_per_book, x, y):
    '''Calculate the total number of days needed to read all books.'''

    if not books_count:
        return 0

    day_count = 0
    i = 0
    while_count = 0
    for loop_idx in range(1, books_count + 1):
        current_page = 0

        if while_count == 1:
            day_count += (books_count - loop_idx) + 1
            break

        while_count = 0
        while current_page < pages_per_book:
            pages_today = math.ceil(((x + i) / (y + i)) * pages_per_book)
            # print(f'pages_today :  ({x} + {i}) / ({x} + {i}) = {pages_today}')
            current_page += pages_today
            day_count += 1
            i += 1
            while_count += 1

            if current_page >= pages_per_book:
                break

        # print('------------')

    return day_count

print(read_book(int(input()), int(input()), int(input()), int(input())))
