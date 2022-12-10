from collections import deque

import numpy as np

OPERATION_ADDX = 'addx'
OPERATION_NOOP = 'noop'

OPERATIONS_CYCLE = {
    'addx': 2,
    'noop': 1,
}

SCREEN_HEIGHT = 6
SCREEN_WIDTH = 40


def parse_operations(input_lines):
    operations = []
    for line in input_lines:
        instructions = line.strip().split(' ')

        operation = instructions[0]
        value = int(instructions[1]) if len(instructions) > 1 else None

        operations.append((operation, value))

    return operations


with open(f'data/challenge.txt') as f:
    lines = f.readlines()

    cycles_to_log = [20, 60, 100, 140, 180, 220, 260]

    operations_list = parse_operations(lines)

    operations_queue = deque(operations_list)
    current_operation = operations_queue.popleft()
    current_operation_status = [current_operation, OPERATIONS_CYCLE[current_operation[0]]]

    current_row_pixels = ['.' for _ in range(SCREEN_WIDTH)]
    current_row = 0
    previous_row = 0

    signal_strength_sum = 0
    sprite_pos = 1
    for cycle in range(cycles_to_log[-1]):
        previous_row = current_row
        current_row = int(cycle / SCREEN_WIDTH)

        if current_row != previous_row:
            print(''.join(current_row_pixels))
            current_row_pixels = ['.' for _ in range(SCREEN_WIDTH)]

        current_column_pos = cycle % SCREEN_WIDTH

        if (sprite_pos - 1) <= current_column_pos <= (sprite_pos + 1):
            current_row_pixels[current_column_pos] = '@'

        if (cycle + 1) in cycles_to_log:
            signal_strength = sprite_pos * (cycle + 1)
            signal_strength_sum += signal_strength

        current_operation_status[1] -= 1

        if current_operation_status[1] == 0 and current_operation_status[0][0] == OPERATION_ADDX:
            sprite_pos += current_operation_status[0][1]

        if current_operation_status[1] == 0:
            if len(operations_queue) == 0:
                print(''.join(current_row_pixels))
                break

            current_operation = operations_queue.popleft()
            current_operation_status = [current_operation, OPERATIONS_CYCLE[current_operation[0]]]

    print(f'Cycle {cycle + 1}: {sprite_pos} | Signal strength: {signal_strength} | Sum: {signal_strength_sum}')