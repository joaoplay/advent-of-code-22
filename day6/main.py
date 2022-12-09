
def find_maker(com_seq, marker_length):
    result = None
    for i in range(len(com_seq)):
        start_idx = i
        end_idx = i + marker_length

        sub_str = input_seq[start_idx:end_idx]

        x = list(set(sub_str))
        y = list(sub_str)

        if len(x) == len(y):
            result = end_idx
            break

    return result


if __name__ == '__main__':
    with open(f'data/challenge_input.txt') as f:
        input_seq = f.readline().strip()

        part1_marker_len = 4
        part2_marker_len = 14

        print("Part 1: ", find_maker(input_seq, part1_marker_len))
        print("Part 2: ", find_maker(input_seq, part2_marker_len))



