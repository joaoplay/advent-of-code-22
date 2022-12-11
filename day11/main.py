from itertools import islice
from math import lcm


def parse_monkey_input(monkey_lines):
    monkey_obj = {
        'name': monkey_lines[0].strip(),
        'items': [int(item) for item in monkey_lines[1][16:].split(', ')],
        'operation': monkey_lines[2][11:].split(' = ')[1].strip(),
        'divisible_by': int(monkey_lines[3][19:].strip()),
        'true_operation': monkey_lines[4][25:].strip(),
        'false_operation': monkey_lines[5][26:].strip()
    }

    return monkey_obj


PART_1 = 0
PART_2 = 1

CURRENT_PART = PART_2

TOTAL_ROUNDS = 20 if CURRENT_PART == PART_1 else 10000

if __name__ == '__main__':
    monkeys = {}
    with open(f'data/challenge.txt') as f:
        while True:
            next_n_lines = list(islice(f, 7))
            if not next_n_lines:
                break

            next_n_lines = [line.strip() for line in next_n_lines]
            monkey = parse_monkey_input(next_n_lines)

            monkeys[monkey['name'].split(' ')[1][:-1]] = monkey

    least_common_multiple = lcm(*[monkey['divisible_by'] for monkey in monkeys.values()])

    inspected_items_count = {monkey_id: 0 for monkey_id in monkeys.keys()}
    for _ in range(TOTAL_ROUNDS):
        for monkey_id, monkey_info in monkeys.items():
            total_elements_removed = 0
            for item in monkey_info['items']:
                inspected_items_count[monkey_id] += 1

                old = item
                if CURRENT_PART == PART_1:
                    new = int(eval(monkey_info['operation']) / 3.0)
                else:
                    new = int(eval(monkey_info['operation']) % least_common_multiple)

                new_monkey = monkey_info['true_operation'] if new % monkey_info['divisible_by'] == 0 else monkey_info[
                    'false_operation']

                total_elements_removed += 1

                # Send it to the new monkey
                monkeys[new_monkey]['items'].append(new)

            monkey_info['items'] = monkey_info['items'][total_elements_removed:]

    top_2 = sorted(inspected_items_count.items(), key=lambda x: x[1], reverse=True)[:2]
    print(f"Result Part {PART_2 + 1}: {top_2[0][1] * top_2[1][1]}")
