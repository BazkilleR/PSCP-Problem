"""distribute"""

def distribute_funds():
    """Distribute funds among recipients"""
    total_money = int(input())
    num_recipients = int(input())

    if num_recipients > total_money:
        print(-1)
    elif total_money - num_recipients < 8:
        print(0)
    else:
        if total_money / num_recipients > 8:
            print(num_recipients - 1)
        else:
            remaining_money = total_money - num_recipients
            max_extra_distributions = remaining_money // 7

            if remaining_money % 7 == 3 and num_recipients - max_extra_distributions == 1:
                max_extra_distributions -= 1

            print(max_extra_distributions)

distribute_funds()
