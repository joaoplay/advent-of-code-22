from itertools import pairwise

import numpy as np

MOVE_UP = 'U'
MOVE_DOWN = 'D'
MOVE_LEFT = 'L'
MOVE_RIGHT = 'R'

MOVES_MAP = {
    MOVE_UP: (1, 0),
    MOVE_DOWN: (-1, 0),
    MOVE_LEFT: (0, -1),
    MOVE_RIGHT: (0, 1),
}


if __name__ == '__main__':
    with open(f'data/challenge.txt') as f:
        lines = f.readlines()

        knots = [[0, 0] for _ in range(10)]

        result_part_1 = set()
        result_part_2 = set()

        for line in lines:
            move_direction = line[0]
            move_steps = int(line[2:])

            for _ in range(move_steps):
                move = MOVES_MAP[move_direction]

                knots[0][0] += move[0]
                knots[0][1] += move[1]

                for cur_knot, prev_knot in pairwise(range(len(knots))):
                    move_x = knots[cur_knot][0] - knots[prev_knot][0]
                    move_y = knots[cur_knot][1] - knots[prev_knot][1]

                    vec = np.array([move_x, move_y])

                    if np.linalg.norm(vec, np.inf) > 1:
                        clipped_vec = vec.clip(-1, 1)
                        knots[prev_knot][0] += clipped_vec[0]
                        knots[prev_knot][1] += clipped_vec[1]

                result_part_1.add(tuple(knots[1]))
                result_part_2.add(tuple(knots[-1]))

    print("Result part 1: ", len(result_part_1))
    print("Result part 2: ", len(result_part_2))









