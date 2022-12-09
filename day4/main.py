if __name__ == '__main__':
    with open(f'data/challenge_input.txt') as f:
        lines = f.readlines()

        result_part_1 = 0
        result_part_2 = 0
        for line in lines:
            groups = line.strip().split(',')

            group1_range = groups[0].split('-')
            group2_range = groups[1].split('-')

            group1_min = int(group1_range[0])
            group1_max = int(group1_range[1])
            group2_min = int(group2_range[0])
            group2_max = int(group2_range[1])

            if len(set(range(group1_min, group1_max + 1)).intersection(set(range(group2_min, group2_max + 1)))) > 0:
                result_part_1 += 1

            if set(range(group1_min, group1_max + 1)).issubset(set(range(group2_min, group2_max + 1))) or set(range(group2_min, group2_max + 1)).issubset(set(range(group1_min, group1_max + 1))):
                result_part_2 += 1

    print("Result Part 1: ", result_part_1)
    print("Result Part 2: ", result_part_2)
