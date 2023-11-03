import argparse
import difflib
import os
import subprocess
import sys

# Example usage
# python submit.py --test-dir=../../icpc_gnyr_2023/B-apivotalquestion/secret --solution=a_pivotal_question.py --timeout=3

# Define command-line argument parser
parser = argparse.ArgumentParser(description="ICPC Competition Test Enviroment")
parser.add_argument("--solution", type=str, required=True, help="Path to the solution script.")
parser.add_argument("--test-dir", type=str, required=True, help="Directory with test cases.")
parser.add_argument("--timeout", type=int, default=2, help="Timeout for each test case in seconds.")
parser.add_argument("--detailed", action="store_true", help="Provide detailed output.")
args = parser.parse_args()

# Retrieve test files
input_files = sorted([f for f in os.listdir(args.test_dir) if f.endswith('.in')])
expected_output_files = [f.replace('.in', '.ans') for f in input_files]

# Define the icons
icons = {'pass': "✅", 'fail': "❌", 'timeout': "⏳"}

# Define the grid and row size for the output
row_size = 10
total_tests = len(input_files)
grid = [' ' * 2] * total_tests  # Initialize the grid with empty slots

# Function to print the grid
def print_grid(grid):
    for i in range(0, total_tests, row_size):
        print(' '.join(grid[i:i+row_size]))
    sys.stdout.flush()  # Flush to ensure the output is displayed immediately

# Function to update the grid with an icon
def update_grid(grid, index, icon):
    grid[index] = icon
    print("\033[H", end='')  # Move cursor to the top of the console
    print_grid(grid)

# Clear the console and print the initial grid
os.system('cls' if os.name == 'nt' else 'clear')
print_grid(grid)

# Run the tests
for index, (test_file, expected_output_file) in enumerate(zip(input_files, expected_output_files)):
    test_file_path = os.path.join(args.test_dir, test_file)
    expected_output_path = os.path.join(args.test_dir, expected_output_file)

    # Run the solution script
    try:
        proc = subprocess.run(
            ["python", args.solution],
            stdin=open(test_file_path, 'r'),
            capture_output=True,
            text=True,
            timeout=args.timeout
        )
        actual_output = proc.stdout
        result_key = 'pass' if actual_output.strip() == open(expected_output_path, 'r').read().strip() else 'fail'
    except subprocess.TimeoutExpired:
        result_key = 'timeout'

    # Update the grid with the result icon
    update_grid(grid, index, icons[result_key])

# After testing, if detailed flag is set, print detailed results
if args.detailed:
    print("\nDetailed Results:")
    for index, test_file in enumerate(input_files):
        expected_output_path = os.path.join(args.test_dir, test_file.replace('.in', '.ans'))
        with open(expected_output_path, 'r') as f:
            expected_output = f.read().strip()
        actual_output = proc.stdout.strip()
        if grid[index].strip() != icons['pass']:
            diff = difflib.unified_diff(
                expected_output.splitlines(keepends=True),
                actual_output.splitlines(keepends=True),
                fromfile="expected",
                tofile="actual",
            )
            print(f"Test '{test_file}':")
            print('\n'.join(diff))
            print()
