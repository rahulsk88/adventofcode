import os

FILE_PATH = os.path.join("code.txt")

with open(FILE_PATH, "r") as f:
    lines = f.read()

lines = lines.split("\n")

def santa_parser(codes, start = 50):
    """Solve"""
    zero_count = 0
    current_value = start
    for code in codes:
        if code:
            direction = code[0]
            number = code[1:]
            if direction == "L":
                for _ in range(int(number)):
                    current_value -= 1
                    if current_value == 0:
                        zero_count += 1
                    if current_value == -1:
                        current_value = 99
            else: 
                for _ in range(int(number)):
                    current_value += 1
                    if current_value == 100:
                        zero_count += 1
                    if current_value == 101:
                        current_value = 1
    
    return zero_count


print(santa_parser(lines))
