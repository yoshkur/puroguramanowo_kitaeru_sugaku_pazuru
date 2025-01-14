# P.23
if __name__ == '__main__':
    card_state_dict = {i: False for i in range(100)}

    for hito in range(1, 100):
        for junban in range(hito, len(card_state_dict), hito + 1):
            card_state_dict[junban] = not card_state_dict[junban]

    for key, value in card_state_dict.items():
        if not value:
            print(key + 1)
