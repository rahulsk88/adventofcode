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

        while start_index < len(bank) - (12 - len(bank_index)) + 1:  # What if you are at the last. 
                                                              # Then it should automatically stop
            if int(bank[start_index]) > int(bank[battery_index]):
                battery_index = start_index
        
            start_index += 1

        
        bank_index += [battery_index]

        return bank_index



            
    
    for bank in banks:
        bank_index = [] # Has to be exactly 12 long
        
        while len(bank_index) < 12:
            _bank_max_finder(bank, bank_index)


        # battery_index = 0
        # while battery_index < len(bank)-1:
        #     if int(bank[battery_index]) > int(bank[high_index]):
        #         high_index = battery_index
            
        #     battery_index += 1

        # battery_index = high_index + 1
        # second_high_index = high_index + 1
        
        # while battery_index <= len(bank)-1:
        #     if int(bank[battery_index]) > int(bank[second_high_index]):
        #         second_high_index = battery_index
        #     battery_index += 1

        # print(high_index, second_high_index)
        # assert high_index < second_high_index
       
        # string_joltage =  bank[high_index] + bank[second_high_index]
        # max_joltage += int(string_joltage)

    return max_joltage

print(get_max_joltage(content))
        
        


