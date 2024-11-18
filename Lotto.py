'''Lotto'''

def confirm_don_dak():
    '''why are you readind this message?'''

    # Assign all prize
    winner = input()
    last_2 = input()
    first_3_1, first_3_2 = input(), input()
    last_3_1, last_3_2 = input(), input()

    # User infomation
    lottery = input()
    total_prize = 0

    # Calculate near winner prize
    if winner == "999999":
        winner_plus = "000000"
        winner_minus = "999998"
    elif winner == "000000":
        winner_plus = "000001"
        winner_minus = "999999"
    else:
        winner_plus = str(int(winner) + 1).zfill(6)
        winner_minus = str(int(winner) - 1).zfill(6)

    if lottery == winner:
        total_prize += 6000000
    if lottery in (winner_minus, winner_plus):
        total_prize += 100000
    if lottery[-2:] == last_2:
        total_prize += 2000
    if lottery[:3] == first_3_1:
        total_prize += 4000
    if lottery[:3] == first_3_2:
        total_prize += 4000
    if lottery[-3:] == last_3_1:
        total_prize += 4000
    if lottery[-3:] == last_3_2:
        total_prize += 4000

    return total_prize

print(confirm_don_dak())
