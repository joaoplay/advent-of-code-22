from day3.constants import ALL_ITEMS_SCORE

if __name__ == '__main__':
    with open(f'data/challenge_input.txt') as f:
        lines = f.readlines()

        result = 0
        for line in lines:
            line = line.strip()

            all_items_size = int(len(line))
            backpack1 = line[0:all_items_size//2]
            backpack2 = line[all_items_size//2:]

            common_items = list(set(backpack1) & set(backpack2))

            result += ALL_ITEMS_SCORE[common_items[0]]

    print("Result: ", result)



