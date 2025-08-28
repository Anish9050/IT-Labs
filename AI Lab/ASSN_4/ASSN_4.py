# puzzle_a_star.py
# IDA* (Iterative Deepening A*) Search for N x N sliding puzzle
# Reads: 009_input_file.txt
# Writes: 009_output_file.txt

from typing import List, Tuple, Optional, Dict

INPUT_FILE = "009_input15puzzle_file.txt"
OUTPUT_FILE = "009_output15puzzle_file.txt"


def read_input(filename: str) -> Tuple[int, List[List[int]], List[List[int]]]:
    """Reads puzzle dimensions and states from a file."""
    try:
        with open(filename, "r") as f:
            raw_lines = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        raise FileNotFoundError(f"Error: The file '{filename}' was not found.")

    if not raw_lines:
        raise ValueError("Error: Input file is empty.")

    try:
        n = int(raw_lines[0])
    except (ValueError, IndexError):
        raise ValueError("Error: First line must be an integer N.")

    start_grid_lines = raw_lines[1:n + 1]
    goal_grid_lines = raw_lines[n + 1: (2 * n) + 1]

    if len(start_grid_lines) != n or len(goal_grid_lines) != n:
        raise ValueError(f"Error: Could not read {n} lines each for start and goal states.")

    try:
        start_state = [list(map(int, row.split())) for row in start_grid_lines]
        goal_state = [list(map(int, row.split())) for row in goal_grid_lines]
    except ValueError:
        raise ValueError("Error: Grid values must be space-separated integers.")

    return n, start_state, goal_state


def write_output(text: str, mode: str = "a") -> None:
    """Writes text to the output file and prints to the console."""
    with open(OUTPUT_FILE, mode) as f:
        f.write(text + "\n")
    print(text)


def board_to_str(state: List[List[int]]) -> str:
    """Converts a 2D board state to a string."""
    return "\n".join(" ".join(map(str, row)) for row in state)


def flatten(state: List[List[int]]) -> Tuple[int, ...]:
    """Flattens a 2D board into a tuple for hashing."""
    return tuple(val for row in state for val in row)


def find_zero(state: List[List[int]]) -> Tuple[int, int]:
    """Finds the coordinates of the blank tile (0)."""
    for r, row in enumerate(state):
        for c, val in enumerate(row):
            if val == 0:
                return r, c
    raise ValueError("Error: No blank tile (0) found.")


def get_neighbors(state: List[List[int]]) -> List[Tuple[str, List[List[int]]]]:
    """Generates valid neighbors and moves."""
    r, c = find_zero(state)
    n = len(state)
    neighbors = []

    moves = {"Up": (-1, 0), "Down": (1, 0), "Left": (0, -1), "Right": (0, 1)}
    for move_name, (dr, dc) in moves.items():
        nr, nc = r + dr, c + dc

        if 0 <= nr < n and 0 <= nc < n:
            new_state = [row[:] for row in state]
            new_state[r][c], new_state[nr][nc] = new_state[nr][nc], new_state[r][c]
            neighbors.append((move_name, new_state))

    return neighbors


def is_solvable(start: List[List[int]], goal: List[List[int]]) -> bool:
    """Checks solvability based on inversions and blank tile position."""
    n = len(start)
    start_flat = flatten(start)
    goal_map = {val: idx for idx, val in enumerate(flatten(goal))}
    start_perm = [goal_map[val] for val in start_flat]

    inversions = sum(1 for i in range(len(start_perm)) for j in range(i + 1, len(start_perm))
                     if start_perm[i] > start_perm[j] and start_perm[i] != goal_map[0] and start_perm[j] != goal_map[0])

    blank_row_from_bottom = n - find_zero(start)[0]

    if n % 2 == 1:
        return inversions % 2 == 0
    else:
        return (blank_row_from_bottom % 2 == 1 and inversions % 2 == 0) or \
               (blank_row_from_bottom % 2 == 0 and inversions % 2 == 1)


def manhattan_distance(state: List[List[int]], goal_map: Dict) -> int:
    """Calculates the Manhattan distance heuristic."""
    distance = 0
    n = len(state)
    for r in range(n):
        for c in range(n):
            val = state[r][c]
            if val != 0:
                goal_pos = goal_map[val]
                goal_r, goal_c = goal_pos // n, goal_pos % n
                distance += abs(r - goal_r) + abs(c - goal_c)
    return distance


def ida_star_search(current_state: List[List[int]], goal_state: List[List[int]],
                   goal_map: Dict, path: List[str], g_cost: int, threshold: int) -> Tuple[int, bool]:
    """
    Recursive depth-first search with f-cost threshold.
    Returns: (minimum_threshold_exceeded, solution_found)
    """
    # Calculate f-cost = g-cost + heuristic
    h_cost = manhattan_distance(current_state, goal_map)
    f_cost = g_cost + h_cost

    # If f-cost exceeds threshold, return the exceeded value for next iteration
    if f_cost > threshold:
        return f_cost, False

    # Goal test
    if current_state == goal_state:
        return threshold, True

    min_threshold = float('inf')

    # Explore all possible moves
    for move, neighbor_state in get_neighbors(current_state):
        # Add move to path
        path.append(move)

        # Recursive call with increased g-cost
        result_threshold, found = ida_star_search(neighbor_state, goal_state, goal_map,
                                                 path, g_cost + 1, threshold)

        # If solution found, propagate success
        if found:
            return result_threshold, True

        # Track minimum threshold for next iteration
        if result_threshold < min_threshold:
            min_threshold = result_threshold

        # Remove move from path (backtrack)
        path.pop()

    return min_threshold, False


def ida_star_solve(start: List[List[int]], goal: List[List[int]]) -> Optional[List[str]]:
    """Solves the puzzle using IDA* (Iterative Deepening A*) algorithm."""
    if start == goal:
        write_output("Start state is already the goal state.")
        return []

    if not is_solvable(start, goal):
        write_output("❌ This puzzle configuration is UNSOLVABLE.")
        return None

    # Create goal mapping for heuristic calculation
    goal_map = {val: idx for idx, val in enumerate(flatten(goal))}

    # Initialize threshold with heuristic of start state
    threshold = manhattan_distance(start, goal_map)

    # Iterative deepening loop
    while True:
        path = []
        result_threshold, found = ida_star_search(start, goal, goal_map, path, 0, threshold)

        if found:
            return path

        # If no improvement possible, no solution exists
        if result_threshold == float('inf'):
            return None

        # Increase threshold for next iteration
        threshold = result_threshold


def main():
    """Main function to run the puzzle solver."""
    open(OUTPUT_FILE, "w").close()

    try:
        n, start, goal = read_input(INPUT_FILE)
    except (ValueError, FileNotFoundError) as e:
        write_output(str(e))
        return

    write_output("Input read successfully.")
    write_output(f"Start state:\n{board_to_str(start)}\n")
    write_output(f"Goal state:\n{board_to_str(goal)}\n")

    solution = ida_star_solve(start, goal)

    if solution is None:
        write_output("\nNo solution exists. Exiting.")
        return

    write_output("\n===== Solution Found =====")
    write_output(f"Solution depth: {len(solution)}")
    write_output("\n===== Final Path (Step-by-step) =====")

    current_state = start
    write_output(f"Step 0 (Start):\n{board_to_str(current_state)}")
    for i, move in enumerate(solution, 1):
        current_state = [row[:] for row in current_state]
        zero_r, zero_c = find_zero(current_state)

        if move == "Up":
            current_state[zero_r][zero_c], current_state[zero_r-1][zero_c] = current_state[zero_r-1][zero_c], current_state[zero_r][zero_c]
        elif move == "Down":
            current_state[zero_r][zero_c], current_state[zero_r+1][zero_c] = current_state[zero_r+1][zero_c], current_state[zero_r][zero_c]
        elif move == "Left":
            current_state[zero_r][zero_c], current_state[zero_r][zero_c-1] = current_state[zero_r][zero_c-1], current_state[zero_r][zero_c]
        elif move == "Right":
            current_state[zero_r][zero_c], current_state[zero_r][zero_c+1] = current_state[zero_r][zero_c+1], current_state[zero_r][zero_c]

        write_output(f"\nStep {i}: Move {move}\n{board_to_str(current_state)}")

    write_output("\nMoves sequence:")
    write_output(" -> ".join(solution) if solution else "(no moves needed)")


if __name__ == "__main__":
    main()