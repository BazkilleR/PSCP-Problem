'''Amefuri Plus'''

def tak_dai_mai(h: int, log: str):
    '''gada gadi gada O'''
    wet_lv = 8
    log = log.lower()

    for current in log:
        if current == 'h':
            return 'Lost'

        is_morning = 6 <= h < 18

        if current == 'c':
            wet_lv -= 0.5 if is_morning else 0.25
        elif current == 'n':
            wet_lv -= 1.0 if is_morning else 0.50
        elif current == 'w':
            wet_lv -= 1.5 if is_morning else 0.75
        elif current == 'r':
            wet_lv += 2
        elif current == 's':
            wet_lv += 3

        wet_lv = min(wet_lv, 16)

        if wet_lv <= 0:
            return 'Dry'

        h = (h + 1) % 24

    return f'Still Wet (Wet Level: {wet_lv:.2f})'

print(tak_dai_mai(int(input()), input()))
