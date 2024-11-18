"""BookWorm"""

def main():
    """BookWorm"""
    num_cases = int(input())
    results = []

    for _ in range(num_cases):
        total_time = float(input())
        num_books = int(input())
        book_times = []

        time_spent = 0
        books_read = 0

        for _ in range(num_books):
            book_times.append(float(input()))

        book_times.sort()

        for time in book_times:
            if time_spent + time <= total_time:
                time_spent += time
                books_read += 1

        results.append(books_read)

    for result in results:
        print(result)

main()
