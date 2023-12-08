file_path = "1.txt"

nums = []
total = 0
ONE = ["one", "1"]
TWO = ["two", "2"]
THREE = ["three", "3"]
FOUR = ["four", "4"]
FIVE = ["five", "5"]
SIX = ["six", "6"]
SEVEN = ["seven", "7"]
EIGHT = ["eight", "8"]
NINE = ["nine", "9"]

word_to_number = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}
def find_all_indices(main_string, substring):
    indices = []
    index = main_string.find(substring)
    while index != -1:
        indices.append(index)
        index = main_string.find(substring, index + 1)
    return indices

def first_last_numbers(s):
    x = {}
    for val in ONE:
        try:
            i = find_all_indices(s,val)
            max_val = max(i)
            min_val = min(i)
            if val.isnumeric():
                x[max_val] = val
                x[min_val] = val
            else:
                x[max_val] = word_to_number[val]
                x[min_val] = word_to_number[val]
        except:
            continue
    for val in TWO:
        try:
            i = find_all_indices(s,val)
            max_val = max(i)
            min_val = min(i)
            if val.isnumeric():
                x[max_val] = val
                x[min_val] = val
            else:
                x[max_val] = word_to_number[val]
                x[min_val] = word_to_number[val]
        except:
            continue
    for val in THREE:
        try:
            i = find_all_indices(s,val)
            max_val = max(i)
            min_val = min(i)
            if val.isnumeric():
                x[max_val] = val
                x[min_val] = val
            else:
                x[max_val] = word_to_number[val]
                x[min_val] = word_to_number[val]
        except:
            continue
    for val in FOUR:
        try:
            i = find_all_indices(s,val)
            max_val = max(i)
            min_val = min(i)
            if val.isnumeric():
                x[max_val] = val
                x[min_val] = val
            else:
                x[max_val] = word_to_number[val]
                x[min_val] = word_to_number[val]
        except:
            continue
    for val in FIVE:
        try:
            i = find_all_indices(s,val)
            max_val = max(i)
            min_val = min(i)
            if val.isnumeric():
                x[max_val] = val
                x[min_val] = val
            else:
                x[max_val] = word_to_number[val]
                x[min_val] = word_to_number[val]
        except:
            continue
    for val in SIX:
        try:
            i = find_all_indices(s,val)
            max_val = max(i)
            min_val = min(i)
            if val.isnumeric():
                x[max_val] = val
                x[min_val] = val
            else:
                x[max_val] = word_to_number[val]
                x[min_val] = word_to_number[val]
        except:
            continue
    for val in SEVEN:
        try:
            i = find_all_indices(s,val)
            max_val = max(i)
            min_val = min(i)
            if val.isnumeric():
                x[max_val] = val
                x[min_val] = val
            else:
                x[max_val] = word_to_number[val]
                x[min_val] = word_to_number[val]
        except:
            continue
    for val in EIGHT:
        try:
            i = find_all_indices(s,val)
            max_val = max(i)
            min_val = min(i)
            if val.isnumeric():
                x[max_val] = val
                x[min_val] = val
            else:
                x[max_val] = word_to_number[val]
                x[min_val] = word_to_number[val]
        except:
            continue
    for val in NINE:
        try:
            i = find_all_indices(s,val)
            max_val = max(i)
            min_val = min(i)
            if val.isnumeric():
                x[max_val] = val
                x[min_val] = val
            else:
                x[max_val] = word_to_number[val]
                x[min_val] = word_to_number[val]
        except:
            continue
    #print(x.keys())
    #print(x.values())

    res = list(sorted(x.items()))
    print(res[0][1],res[-1][1])
    return res[0][1],res[-1][1]
   



    


#print(gafds)
with open(file_path, 'r') as file:
    for line in file:
        s = line.strip()
        print(s)
        first_digit,last_digit = first_last_numbers(s)
        combined = str(first_digit) + str(last_digit)
        nums.append(combined)
        print()
for val in nums:
    total += int(val)

print(total)
        
            
        
            

