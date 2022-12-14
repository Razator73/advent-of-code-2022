import re
from pathlib import Path

with open('input/day7.txt') as f:
    data = f.read().strip().split('\n')


cd_search = r'\$ cd (.*)'
cwd = Path('/')
i = 0
folder_sizes = {}
while i < len(data):
    row = data[i]
    if cd := re.search(cd_search, row):
        if cd.group(1) == '/':
            cwd = Path('/')
        elif cd.group(1) == '..':
            cwd = cwd.parent
        else:
            cwd = cwd / cd.group(1)
    elif row == '$ ls':
        row = data[i + 1]
        while not row.startswith('$'):
            folder_sizes.setdefault(str(cwd), {'size': 0, 'folders': [], 'files': []})
            if dir_row := re.search(r'dir (.*)', row):
                folder_sizes[str(cwd)]['folders'].append(dir_row.group(1))
            elif file_row := re.search(r'(\d+)\s(.*)', row):
                folder_sizes[str(cwd)]['files'].append({'name': file_row.group(2), 'size': int(file_row.group(1))})
                folder_sizes[str(cwd)]['size'] += int(file_row.group(1))
                for parent in cwd.parents:
                    folder_sizes[str(parent)]['size'] += int(file_row.group(1))
            i += 1
            try:
                row = data[i + 1]
            except IndexError:
                break
    i += 1

# Part 1
print(sum([folder['size'] for folder in folder_sizes.values() if folder['size'] <= 100000]))

# Part 2
file_system_total = 70000000
file_system_used = folder_sizes['/']['size']
file_system_available = file_system_total - file_system_used
update_size = 30000000
space_to_free_up = update_size - file_system_available
print(min([folder['size'] for folder in folder_sizes.values() if folder['size'] > space_to_free_up]))
