file_path = "8.txt"

def traverse_graph(lr,node):
    index=0
    loc = -1
    count = 0
    while index < len(lr) and node !='ZZZ':
        if lr[index] == 'L':
            loc = 0
        else: # is R
            loc = 1
        node = graph[node][loc]
        #print(node)
        

        index +=1
        if(index == len(lr)):
            index = 0
        count +=1
    return count
        
        
        
    

def build_graph(s):
    
    node = s.split(' = ')
    key = node[0]
    
    dest = node[1]
    dest = dest[1:-1].split(', ')
    graph[key] = dest

start = 0
graph = {}
with open(file_path, 'r') as file:
    for line in file:
        s = line.strip()
        if start == 0:
            lr = s
            start = 1
        else:
            build_graph(s)
            
res = traverse_graph(lr,'AAA')            
print(res)
        
            

