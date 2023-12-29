import matplotlib.pyplot as plt
import matplotlib.patches as patches

file = "input"

with open(f"./2023/Day10/{file}.txt", "r") as f:
    lines: str = f.read().splitlines()


# Your provided code with slight modifications for visualization
def find_start(grid):
    for i, line in enumerate(grid):
        if "S" in line:
            return line.index("S"), i


def find_paths(grid, x, y):
    paths = []
    #  N, E, S, W
    directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]

    for i, direction in enumerate(directions):
        nx, ny = x + direction[0], y + direction[1]

        if nx < 0 or nx >= len(grid[0]) or ny < 0 or ny >= len(grid):
            continue

        if i == 0 and grid[ny][nx] in ["|", "7", "F"]:
            paths.append((nx, ny, grid[ny][nx], directions[i]))
        if i == 1 and grid[ny][nx] in ["-", "J", "7"]:
            paths.append((nx, ny, grid[ny][nx], directions[i]))
        if i == 2 and grid[ny][nx] in ["|", "L", "J"]:
            paths.append((nx, ny, grid[ny][nx], directions[i]))
        if i == 3 and grid[ny][nx] in ["-", "L", "F"]:
            paths.append((nx, ny, grid[ny][nx], directions[i]))

    return paths


def solve(grid, x, y, paths):
    past = [None for _ in range(len(paths))]
    distance = 1
    pipe_directions = {
        "|": lambda d: d,
        "-": lambda d: d,
        "L": lambda d: (1, 0) if d == (0, 1) else (0, -1),
        "J": lambda d: (-1, 0) if d == (0, 1) else (0, -1),
        "7": lambda d: (-1, 0) if d == (0, -1) else (0, 1),
        "F": lambda d: (1, 0) if d == (0, -1) else (0, 1),
    }

    # Visualization data
    path_data = []

    while (x, y) not in past:
        distance += 1

        for i, path in enumerate(paths):
            pipe = path[2]
            cur_x, cur_y = path[0], path[1]
            direction = path[3]
            change = pipe_directions[pipe](direction)
            nx, ny = cur_x + change[0], cur_y + change[1]

            if (nx, ny) in past:
                path_data.append((cur_x, cur_y, nx, ny))
                return distance, path_data

            past[i] = (nx, ny)
            paths[i] = (nx, ny, grid[ny][nx], change)
            path_data.append((cur_x, cur_y, nx, ny))

    return distance, path_data


def visualize_grid_and_save(grid, path_data, filename, start_pos):
    # Increase the figure size for better visibility of arrows
    scale_factor = 1.5  # Adjust this factor based on your needs
    fig_width = scale_factor * len(grid[0])
    fig_height = scale_factor * len(grid)

    fig, ax = plt.subplots(figsize=(fig_width, fig_height))
    ax.set_xlim(-0.5, len(grid[0]) - 0.5)
    ax.set_ylim(-0.5, len(grid) - 0.5)
    ax.set_aspect("equal", adjustable="box")

    # Set the background of each square to dark slate grey and add borders
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            square = patches.Rectangle(
                (x - 0.5, y - 0.5),
                1,
                1,
                facecolor="darkslategrey",
                edgecolor="grey",
                linewidth=0.5,
            )
            ax.add_patch(square)

    # Highlight the start position in green
    start_rect = patches.Rectangle(
        (start_pos[0] - 0.5, start_pos[1] - 0.5), 1, 1, facecolor="green"
    )
    ax.add_patch(start_rect)

    # Draw the path
    for i, (start_x, start_y, end_x, end_y) in enumerate(path_data):
        color = "lime" if i % 2 else "aqua"
        # Draw arrows for all but the last segment
        ax.add_patch(
            patches.FancyArrow(
                start_x,
                start_y,
                end_x - start_x,
                end_y - start_y,
                length_includes_head=True,
                head_width=0.1 * scale_factor,
                head_length=0.1 * scale_factor,
                color=color,
            )
        )

    # Highlight the end position in red (last position in the path)
    if path_data:
        end_x, end_y = path_data[-1][2], path_data[-1][3]
        end_rect = patches.Rectangle((end_x - 0.5, end_y - 0.5), 1, 1, facecolor="red")
        ax.add_patch(end_rect)

    # Annotate the grid with symbols
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            ax.text(
                x, y, grid[y][x], ha="center", va="center", color="white", fontsize=38
            )

    plt.gca().invert_yaxis()
    plt.savefig(filename)
    plt.close()


grid = [list(line) for line in lines]
x, y = find_start(grid)
paths = find_paths(grid, x, y)
distance, path_data = solve(grid, x, y, paths)

# Save the visualization as an image
image_path = f"./2023/visuals/day10_{file}.png"
print(f"Saving image to {image_path}")
visualize_grid_and_save(grid, path_data, image_path, (x, y))
print("Done!")
