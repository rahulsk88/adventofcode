import os

file_name = os.path.join("day_2_part1.txt")

with open(file_name, "r") as f:
    content = f.read()

content = content.split(',')


def getall_ids(content):
    content_list = []
    for i in content:
        if "-" in i:
            split = i.split("-")
            for j in range(int(split[0]), int(split[1])+1):
                content_list += [str(j).strip("\n")]
        else:
            content_list += [i.strip("\n")]
    
    return content_list

all_ids = getall_ids(content)



def get_false_numbers(ids):
    """ 
    Given some list of ids. The logic is to check whether the digits are palindrome. 
    """

    def _getmultiples(id):
        """returns multiples"""
        ith_length = len(id)
        multiples = []
        for j in range(1, ith_length // 2 + 1): # When the range is to small
            if j == 0:
                continue
            if ith_length % j == 0:
                multiples += [j]
        
        return multiples
    
    def _checkrepeat(id, multiple):
        chunks = [id[i:i+multiple] for i in range(0, len(id), multiple)]
        check_chunks = all(x == chunks[0] for x in chunks)
        return check_chunks    

        
    false_ids = 0 
    for i in ids:
        multiples = _getmultiples(i)
        for k in multiples:
            if _checkrepeat(i, k):
                false_ids += int(i)
                break
                
        
    return false_ids

false_ids = get_false_numbers(all_ids)

print(false_ids)

