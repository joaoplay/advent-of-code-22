def check_visibility(grid, row, col):
    """Check if a seat is visible from the given row and column."""

    # Iterate upper lines
    vis_range_up = 0
    is_visible_up = True
    for k in range(row - 1, -1, -1):
        vis_range_up += 1
        if grid[k][col] >= grid[row][col]:
            is_visible_up = False
            break

    # Iterate lower lines
    is_visible_down = True
    vis_range_down = 0
    for k in range(row + 1, len(grid)):
        vis_range_down += 1
        if grid[k][col] >= grid[row][col]:
            is_visible_down = False
            break

    # Iterate left columns
    is_visible_left = True
    vis_range_left = 0
    for k in range(col - 1, -1, -1):
        vis_range_left += 1
        if grid[row][k] >= grid[row][col]:
            is_visible_left = False
            break

    # Iterate right columns
    is_visible_right = True
    vis_range_right = 0
    for k in range(col + 1, len(grid[0])):
        vis_range_right += 1
        if grid[row][k] >= grid[row][col]:
            is_visible_right = False
            break

    return (is_visible_up, vis_range_up), (is_visible_down, vis_range_down), (is_visible_left, vis_range_left), \
           (is_visible_right, vis_range_right)


if __name__ == '__main__':
    with open(f'data/challenge.txt') as f:
        lines = f.readlines()

        grid = []

        for line in lines:
            grid.append(list([int(tree) for tree in line.strip()]))

        best_visibility_score = -1
        visible_trees = len(grid) * 2 + (len(grid[0]) - 2) * 2
        for i in range(1, len(grid) - 1):
            for j in range(1, len(grid[i]) - 1):
                vis_up, vis_down, vis_left, vis_right = check_visibility(grid, i, j)

                visible_trees += vis_up[0] or vis_down[0] or vis_left[0] or vis_right[0]

                visibility_score = vis_up[1] * vis_down[1] * vis_left[1] * vis_right[1]

                best_visibility_score = max(best_visibility_score, visibility_score)

        print("Result Part 1: ", visible_trees)
        print("Result Part 2: ", best_visibility_score)
