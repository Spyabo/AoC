day=$(printf "%02d" "$1")
year=${2:-$(date +'%Y')}
cookie=

mkdir -p "./$year/Day$day"
touch "./$year/Day$day/input.txt"
touch "./$year/Day$day/testinput.txt"
touch "./$year/Day$day/a.py"
touch "./$year/Day$day/b.py"

# Download input
curl -s -H "Cookie: session=$cookie" "https://adventofcode.com/$year/day/${day#0}/input" > "./$year/Day$day/input.txt"

# Python code to be added
python_code="with open('./$year/Day$day/testinput.txt', 'r') as f:\n    lines: str = f.read().splitlines()"

# Write Python code to a.py and b.py
echo "$python_code" > "./$year/Day$day/a.py"
echo "$python_code" > "./$year/Day$day/b.py"
