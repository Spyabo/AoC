txt = open("/home/spy/AoC2022/Day7/testinput.txt", "r")
commands = txt.read().strip().split("\n")

from collections import deque, defaultdict
from functools import lru_cache

def parse_filesystem(commands):
	lines = deque(commands)
	fs    = defaultdict(list)
	path  = ()

	while lines:
		_, command, *args = lines.popleft().split()

		if command == 'ls':
			while lines and not lines[0].startswith('$'):
				size = lines.popleft().split()[0]
				if size != 'dir':
					fs[path].append(int(size))
		else:
			if args[0] == '..':
				path = path[:-1]
			else:
				new_path = path + (args[0],)
				fs[path].append(new_path)
				path = new_path

	return fs

@lru_cache(maxsize=None)
def directory_size(path):
	size = 0

	for subdir_or_size in fs[path]:
		if isinstance(subdir_or_size, int):
			size += subdir_or_size
		else:
			size += directory_size(subdir_or_size)

	return size


fs = parse_filesystem(commands)

small_dir_total  = 0

for path in fs:
	size = directory_size(path)

	if size <= 100000:
		small_dir_total += size
  
print(small_dir_total)
