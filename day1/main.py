

if __name__ == '__main__':
    with open(f'data/challenge_input.txt') as f:
        lines = f.readlines()

        max_per_elf = []
        current_values = []
        for line in lines:
            line = line.strip()
            if line == '':
                max_per_elf.append(sum(current_values))
                current_values = []
            else:
                current_values.append(int(line))

    # Consider the values for the last elf
    max_per_elf.append(sum(current_values))

    top_elf = sorted(max_per_elf, reverse=True)

    print("Result: ", sum(top_elf[0:3]))
