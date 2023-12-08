
import re


def find_all_indices(main_string, substring):
    indices = []
    index = main_string.find(substring)
    while index != -1:
        indices.append(index)
        index = main_string.find(substring, index + 1)
    return indices


def generate_key(s,vals,line_num,dic):
    for num in vals:
        res = find_all_indices(s,num)
        #print('num ' + num)
        #print(res)
        for r in res:
            for j,k in enumerate(num):
                
                key = str(line_count) + '_' + str(j + r)
                #print(key)
                if key not in dic:   
                    dic[key] = num    



file_path = "3.txt"
all_nums_loc = {}
all_symb_loc = {}
line_count = 1
total = 0
nums = []
with open(file_path, 'r') as file:
    for line in file:
        special_index = []
        s = line.strip()
        line_symbols = set([char for char in s if not char.isalnum() and char != '.'])
        line_digits = [x for x in s.split('.') if  str(x).isdigit()]
        hidden_digits = set([x for x in s.split('.') if not str(x).isdigit()])
        
        
        for x in hidden_digits:
            z = re.split(r'\W+', x)
            for i in z:
                line_digits.append(i)
        
                    
        
        line_digits.sort(reverse=True)
        line_digits = sorted(line_digits, key=lambda x: int(x) if x.isdigit() else float('inf'), reverse=True)
        print(line_digits)
        
        generate_key(s,line_digits,line_count,all_nums_loc)
        generate_key(s,line_symbols,line_count,all_symb_loc)
        
        line_count += 1



#print(all_nums_loc)
for part in all_symb_loc:
    part_split = part.split('_')
    #print("Location of sysmbol: " + part)

    
    for i in range(-1,2):
        tmp = []
        for j in range(-1,2):
            
            key = str((int(part_split[0]) + i)) + '_' + str((int(part_split[1]) + j))
            #print(key)
            try:
                #print("Key Found: " + key + '\n' + all_nums_loc[key])
                tmp.append(all_nums_loc[key])          
            except:
                tmp.append('')
        
        if (tmp[0].isdigit() and tmp[1] == '' and tmp[2].isdigit()):
            nums.append(tmp[0])
            nums.append(tmp[2])       
        else:
            tmp.sort(reverse=True)
            nums.append(tmp[0])

 
                
        
#print(nums)
for num in nums:
    if num != '':
        total += int(num)

print(total)
        
        


       
            

