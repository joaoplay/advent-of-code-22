from string import ascii_lowercase

import networkx as nx

CHAR_MAP = dict((ch, idx) for idx, ch in enumerate(ascii_lowercase))


def connect_nodes_if_needed(node1, node2, node1_pos, node2_pos, edges_list):
    node1_idx = CHAR_MAP[node1]
    node2_idx = CHAR_MAP[node2]

    distance = node1_idx - node2_idx

    if node1_idx > node2_idx:
        edges_list += [(node1_pos, node2_pos)]
    elif node1_idx < node2_idx:
        edges_list += [(node2_pos, node1_pos)]

    if distance == 0:
        edges_list.append((node1_pos, node2_pos))
        edges_list.append((node2_pos, node1_pos))
    elif distance == -1:
        edges_list.append((node1_pos, node2_pos))
    elif distance == 1:
        edges_list.append((node2_pos, node1_pos))


def find_character_in_multiple_lines(lines, character, stop_at_first=True):
    char_pos = []
    for line_idx in range(len(lines)):
        line = lines[line_idx]
        try:
            char_col = line.index(character)
            char_pos += [(line_idx, char_col)]
        except ValueError:
            continue
        else:
            if stop_at_first:
                break

    return char_pos if len(char_pos) > 1 else char_pos[0]


def replace_character_in_multiple_lines(lines, character, new_character):
    char_pos = find_character_in_multiple_lines(lines, character)
    if char_pos is not None:
        line_idx, char_col = char_pos
        lines[line_idx] = lines[line_idx].replace(character, new_character)


if __name__ == '__main__':
    with open(f'data/challenge.txt') as f:

        lines = [line.strip() for line in f.readlines()]

        # FIXME: This is quite inefficient. We are iterating over the input multiple times.
        # Find the start and end positions
        start_node_pos = find_character_in_multiple_lines(lines, 'S')
        end_node_pos = find_character_in_multiple_lines(lines, 'E')
        # Replace the start and end positions with a and z, respectively
        replace_character_in_multiple_lines(lines, 'S', 'a')
        replace_character_in_multiple_lines(lines, 'E', 'z')

        start_node = None
        end_node = None

        graph = nx.DiGraph()

        edges = []
        previous_row = None
        for current_row_idx in range(len(lines)):
            current_row = lines[current_row_idx]

            # Connect elements in the same row
            previous_char = current_row[0]
            for current_char_idx in range(1, len(current_row)):
                current_char = current_row[current_char_idx]
                previous_char_pos = (current_row_idx, current_char_idx - 1)
                current_char_pos = (current_row_idx, current_char_idx)
                connect_nodes_if_needed(previous_char, current_char, previous_char_pos, current_char_pos, edges)
                previous_char = current_char

            # Connect elements of the current row to the previous row
            if previous_row is not None:
                for previous_char_idx in range(len(previous_row)):
                    previous_char = previous_row[previous_char_idx]
                    current_char = current_row[previous_char_idx]
                    previous_char_pos = (current_row_idx - 1, previous_char_idx)
                    current_char_pos = (current_row_idx, previous_char_idx)
                    connect_nodes_if_needed(previous_char, current_char, previous_char_pos, current_char_pos, edges)

            previous_row = current_row

        graph.add_edges_from(edges)

        all_possible_start_nodes = find_character_in_multiple_lines(lines, 'a', stop_at_first=False)

        print("Result Part 1: ", nx.astar_path_length(graph, start_node_pos, end_node_pos))
        print("Result Part 2: ",
              min(nx.astar_path_length(graph, start_node, end_node_pos) for start_node in all_possible_start_nodes))
