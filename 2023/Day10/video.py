import matplotlib.pyplot as plt
import matplotlib.patches as patches
import multiprocessing

file = "testinput"

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


def visualize_grid_and_save(grid, path_data, filename, start_pos, step):
    scale_factor = 1.5
    fig_width = scale_factor * len(grid[0])
    fig_height = scale_factor * len(grid)

    fig, ax = plt.subplots(figsize=(fig_width, fig_height))
    ax.set_xlim(-0.5, len(grid[0]) - 0.5)
    ax.set_ylim(-0.5, len(grid) - 0.5)
    ax.set_aspect("equal", adjustable="box")

    # Draw background squares
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

    # Draw the path up to the current step
    for i, (start_x, start_y, end_x, end_y) in enumerate(path_data[: step + 1]):
        color = "lime" if i % 2 else "aqua"
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
    end_x, end_y = path_data[step][2], path_data[step][3]
    end_rect = patches.Rectangle((end_x - 0.5, end_y - 0.5), 1, 1, facecolor="red")
    ax.add_patch(end_rect)

    # Annotate the grid with symbols
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            ax.text(
                x, y, grid[y][x], ha="center", va="center", color="white", fontsize=38
            )

    plt.gca().invert_yaxis()
    filename_step = f"2023/frames/day10/{filename}/step_{step}.png"
    plt.savefig(filename_step)
    plt.close()


def worker(grid, path_data, file, start_pos, step):
    visualize_grid_and_save(grid, path_data, file, start_pos, step)


def create_frames(grid, path_data, file, start_pos, batch_size=10):
    total_steps = len(path_data)
    for batch_start in range(0, total_steps, batch_size):
        batch_end = min(batch_start + batch_size, total_steps)
        batch_tasks = [
            (grid, path_data, file, start_pos, step)
            for step in range(batch_start, batch_end)
        ]

        # Create a pool of worker processes for each batch
        with multiprocessing.Pool() as pool:
            pool.starmap(worker, batch_tasks)


# Main script execution
grid = [list(line) for line in lines]
x, y = find_start(grid)
paths = find_paths(grid, x, y)
distance, path_data = solve(grid, x, y, paths)

import time

start_time = time.time()
print(f"Saving images to ./2023/frames/day10/{file}")
create_frames(grid, path_data, file, (x, y))
end_time = time.time()
print(f"Done! Time taken: {end_time - start_time} seconds")
