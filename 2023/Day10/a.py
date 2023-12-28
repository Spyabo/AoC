with open("./2023/Day10/input.txt", "r") as f:
    lines: str = f.read().splitlines()

# | is a vertical pipe connecting north and south.
# - is a horizontal pipe connecting east and west.
# L is a 90-degree bend connecting north and east.
# J is a 90-degree bend connecting north and west.
# 7 is a 90-degree bend connecting south and west.
# F is a 90-degree bend connecting south and east.


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

    while (x, y) not in past:
        distance += 1

        for i, path in enumerate(paths):
            pipe = path[2]
            cur_x, cur_y = path[0], path[1]
            direction = path[3]
            change = pipe_directions[pipe](direction)
            nx, ny = cur_x + change[0], cur_y + change[1]
            # print(direction, (nx, ny, grid[ny][nx], change), past)

            if (nx, ny) in past:
                return distance

            past[i] = (nx, ny)
            paths[i] = (nx, ny, grid[ny][nx], change)

    return distance


def main():
    grid = [list(line) for line in lines]
    x, y = find_start(grid)
    paths = find_paths(grid, x, y)
    ans = solve(grid, x, y, paths)

    print(ans)


main()
