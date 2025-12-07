import os

FILENAME =  os.path.join("day5part1.txt")

with open(FILENAME, "r") as f:
    content = f.read()

fresh_list = []
for i in content.split("\n"):
    if i == '':
        break
    else:
        fresh_list += [i]

fresh_list.sort(key= lambda x: int(x.split('-')[0]))


current_list = 0
end_previous = 0

full_count = 0
for i in fresh_list:
    current_list = i
    start_current, end_current = i.split('-')    

    # check if over lap

    if (int(start_current) > int(end_previous)):
        total_range = int(end_current) - int(start_current)  + 1
    
    else:
        total_range = int(end_current) - int(end_previous)
        if total_range < 0:
            continue

    full_count += total_range
    end_previous = end_current

print(full_count)