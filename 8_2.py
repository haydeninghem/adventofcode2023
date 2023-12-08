import math
file_path = "8.txt"

def lcm_of_list(numbers):
    if not numbers:
        return None  # Return None for an empty list, as LCM is undefined

    result = numbers[0]
    for num in numbers[1:]:
        result = result * num // math.gcd(result, num)

    return result

def traverse_graph(lr,node):
    index=0
    loc = -1
    count = 0
    while index < len(lr):
        if lr[index] == 'L':
            loc = 0
        else: # is R
            loc = 1
            
        node = graph[node][loc]
        
        if node[2] == 'Z':
            index = 9000

        #print(node,loc,node[2])
        

        index +=1
        if(index == len(lr)):
            index = 0
        count +=1
        
    return count

def traverse_alphagraph(lr):
    index=0
    loc = -1
    count = 1
    gr = alpha_graph['A']
    my_list = []
    for node in gr:
        #print(node)
        my_list.append(traverse_graph(lr,node))
    return my_list
            




        
        
    

def build_graph(s):
    
    node = s.split(' = ')
    key = node[0]
    
    dest = node[1]
    dest = dest[1:-1].split(', ')
    #print(key,dest)
    graph[key] = dest
  
        
    if key[2] in alpha_graph:
        alpha_graph[key[2]].append(key)
    else:
        alpha_graph[key[2]] = list()
        alpha_graph[key[2]].append(key)

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y']    
start = 0
graph = {}
alpha_graph = {}
with open(file_path, 'r') as file:
    for line in file:
        s = line.strip()
        if start == 0:
            lr = s
            start = 1
        else:
            build_graph(s)

print(alpha_graph)
res = traverse_alphagraph(lr)
print(lcm_of_list(res))
#res = traverse_graph(lr,'11A')            
print(res)
        
            

