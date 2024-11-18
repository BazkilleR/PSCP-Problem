'''blackjack'''
def count_aces(card_list):
    ''' Count the number of Aces in card list '''
    ace_count = 0
    for card in card_list:
        if card == 'A':
            ace_count += 1
    return ace_count

def calculate_best_score(card_list, card_values, possible_ace_values):
    ''' Calculate the best score given the card list and possible ace values '''
    non_ace_total = 0
    for card in card_list:
        if card != 'A':
            non_ace_total += card_values[card]

    possible_scores = []
    for ace_value in possible_ace_values:
        possible_scores.append(non_ace_total + ace_value)

    best_score = 0
    for score in possible_scores:
        if score <= 21:
            best_score = max(best_score, score)

    if not best_score:
        best_score = min(possible_scores)

    return best_score

def main():
    ''' Main function '''
    length_of_cards = int(input())

    if length_of_cards < 2 or length_of_cards > 3:
        return

    card_values = {
        '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
        '7': 7, '8': 8, '9': 9, '10': 10,
        'J': 10, 'Q': 10, 'K': 10
    }

    card_list = []

    for _ in range(length_of_cards):
        card = input().strip()
        if card in card_values or card == 'A':
            card_list.append(card)

    total_aces = count_aces(card_list)

    if not total_aces:
        total_score = 0
        for card in card_list:
            total_score += card_values[card]
        print(total_score)
    else:
        possible_ace_values = []
        for i in range(total_aces + 1):
            possible_ace_values.append(total_aces + 10 * i)

        total_score = calculate_best_score(card_list, card_values, possible_ace_values)
        print(total_score)

main()
