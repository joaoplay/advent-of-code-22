import re
from curses.ascii import isdigit

def pop_n_elements(n, l):
    return [l.pop(0) for _ in range(n)]


if __name__ == '__main__':
    keep_order = True

    with open(f'data/challenge_input.txt') as f:
        lines = f.readlines()

        crates_per_stack = {}
        for line_idx, line in enumerate(lines):
            if isdigit(line[1]):
                break

            crates = re.findall(r'\s\s\s\s|[A-Z]', line)

            current_stack_pos = 1
            for crate in crates:
                if crate.strip() != "":
                    crates_per_stack.setdefault(current_stack_pos, []).append(crate)

                current_stack_pos += 1

        move_lines = lines[line_idx + 2:]

        for line in move_lines:
            move = re.findall(r'\d+', line)

            quantity = int(move[0])
            from_stack = int(move[1])
            to_stack = int(move[2])

            elements = [crates_per_stack[from_stack].pop(0) for _ in range(quantity)]
            if not keep_order:
                elements.reverse()

            crates_per_stack[to_stack] = elements + crates_per_stack[to_stack]

        sorted_dict = sorted(crates_per_stack.items())

        print("Elements at Top: ", ''.join([crate[1][0] for crate in sorted_dict]))
