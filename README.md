# AoC

My solutions to Advent of code: https://adventofcode.com/

Got no. 27 on Day 6 part A!!! https://gyazo.com/27b6c1237eaaee4f39b90571b4a7d2e7

### Helpful starter script
```sh
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
```

### Visualisation of 2023 Day 10
https://github.com/Spyabo/AoC/assets/86006893/2afb8258-587f-46ab-9e55-d0d220d2ef72
