day=$1
mkdir -p "./2023/Day$day"
touch "./2023/Day$day/input.txt"
touch "./2023/Day$day/testinput.txt"
touch "./2023/Day$day/a.py"
touch "./2023/Day$day/b.py"

# Python code to be added
python_code="with open('./2023/Day$day/testinput.txt', 'r') as f:\n    lines: str = f.read().splitlines()"

# Write Python code to a.py and b.py
echo "$python_code" > "./2023/Day$day/a.py"
echo "$python_code" > "./2023/Day$day/b.py"
