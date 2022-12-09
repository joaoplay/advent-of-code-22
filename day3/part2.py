from day3.constants import ALL_ITEMS_SCORE

if __name__ == '__main__':
    with open(f'data/challenge_input.txt') as f:
        lines = f.readlines()

        result = 0
        lines = [line.strip() for line in lines]
        for start_idx in range(0, len(lines), 3):
            group = lines[start_idx: start_idx + 3]

            common_items = None
            for elem in group:
                if common_items is None:
                    common_items = set(elem)
                else:
                    common_items = common_items & set(elem)

            result += ALL_ITEMS_SCORE[list(common_items)[0]]

    print("Result: ", result)



