import os

filename = os.path.join("day_3_part_1.txt")

with open(filename, "r") as f:
    content = f.read()


def get_max_joltage(content):

    banks = content.split('\n')
    max_joltage = 0

    def _bank_max_finder(bank, bank_index):
        try:
            battery_index = bank_index[-1] + 1
            start_index = bank_index[-1] + 1
        except:
            battery_index = 0
            start_index = 0
        battery_value = 0

        while start_index < len(bank) - (12 - len(bank_index)) + 1: 
            
            current_value = int(bank[start_index]) 
            if current_value > battery_value:
                battery_index = start_index
                battery_value = int(bank[start_index])
        
            start_index += 1

        
        bank_index += [battery_index]

        return bank_index



            
    print(banks)

    for bank in banks:
        bank_index = [] # Has to be exactly 12 long
        
        while len(bank_index) < 12:
            _bank_max_finder(bank, bank_index)
        
        print(bank_index)
        
        max_joltage += int("".join([bank[i] for i in bank_index]))
    
    return max_joltage


print(get_max_joltage(content))
        
        


