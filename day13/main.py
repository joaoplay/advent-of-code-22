EQUAL_TO = 0
OUT_OF_ORDER = 1
IN_ORDER = 2

HUMAN_READABLE = {
    EQUAL_TO: 'EQUAL_TO',
    OUT_OF_ORDER: 'OUT_OF_ORDER',
    IN_ORDER: 'IN ORDER',
}


def check_pairs(left, right):
    if isinstance(left, int) and isinstance(right, int):
        if left == right:
            return EQUAL_TO
        elif left > right:
            return OUT_OF_ORDER
        else:
            return IN_ORDER

    if isinstance(left, list) and isinstance(right, int):
        if len(left) == 0:
            return IN_ORDER
        right = [right]
    elif isinstance(left, int) and isinstance(right, list):
        if len(right) == 0:
            return OUT_OF_ORDER
        left = [left]

    min_len = min(len(left), len(right))

    for idx in range(min_len):
        left_item = left[idx]
        right_item = right[idx]

        if isinstance(right, list):
            result = check_pairs(left_item, right_item)

            if result != EQUAL_TO:
                return result

    if len(left) < len(right):
        return IN_ORDER
    elif len(left) > len(right):
        return OUT_OF_ORDER

    return EQUAL_TO

# FIXME: Part 2 is not already done! I need to add the two new elements and sort them according to the rules.

if __name__ == '__main__':
    with open(f'data/challenge.txt') as f:
        lines = f.readlines()

        c_index = 0
        total = 0
        for line_idx in range(0, len(lines), 3):
            c_index += 1
            l1 = eval(lines[line_idx])
            l2 = eval(lines[line_idx + 1])

            result = check_pairs(l1, l2)
            print(f"L1: {l1} and L2: {l2} are {HUMAN_READABLE[result]}")
            total += c_index if (result == IN_ORDER or result == EQUAL_TO) else 0

        print("Total: ", total)
