import os

filename = "day4_part1.txt"

# I will do this with a new class

class Roll:
    def __init__(self):
        self.position = None
        self.movable = None       
        self.nearby = None
    
    def get_nearby(self):
        row, col = self.position
        self.nearby = [(row-1, col-1), (row+1, col+1), (row-1, col+1), (row +1, col-1), 
                       (row, col+1), (row, col-1), (row-1, col), (row+1, col)]
        

with open(os.path.join(filename), "r") as f:
    content = f.read()


def parse_string(content):
    """ 
    parse it as a 2D array, 
    store each  
    """
    
    content_split = content.split('\n')
    num_rows = len(content_split)
    num_cols = len(content_split[0])
    
    main_array = [[False] * (num_cols+2)]

    for i in content_split:
        main_array += [[False] + [j == '@' for j in i] + [False]]
    
    main_array += [[False] * (num_cols+2)]
    return main_array, num_cols, num_rows


def parse_grid(main_array, num_cols, num_rows):
    """Checks around the 8 by 8 grid. """
    print(len(main_array), len(main_array[0]))
    # Need to think about this for a second
    movable_count = 0
    for row_index, row in enumerate(main_array):
        if (row_index == 0) | (row_index == num_rows +1):
            continue
        for object_index, object  in enumerate(row):
            if object == False:
                continue
            
            r = Roll()
            r.position = (row_index, object_index)
            r.get_nearby()
            if row_index == 10:
                print(r.nearby)
            sum_nearby = 0
            for nearby in r.nearby:
                sum_nearby += main_array[nearby[0]][nearby[1]]
            
            if sum_nearby > 3:
                r.movable = False
            else:
                r.movable = True
                main_array[r.position[0]][r.position[1]] = False

            movable_count += r.movable
    
    return movable_count, main_array
        
main_array, num_cols, num_rows = parse_string(content)

previous_moveable = -1
current_moveable = 0

while previous_moveable != current_moveable:
    previous_moveable = current_moveable
    movable_count, main_array = parse_grid(main_array, num_cols, num_rows)
    current_moveable += movable_count
print(current_moveable)
