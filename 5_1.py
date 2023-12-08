file_path = "5.txt"



clean = open(file_path).read().replace('\n', '+')
clean = clean.split('++')

seeds = clean[0].split(':')

seeds = list(map(int, seeds[1].split()))

tmp_map = {}
for i in clean[1:]:
    x = i.split('+')
    map_name = x[0]
    

    
    if not tmp_map:
        maps = seeds
    else:
        maps = dict((v,k) for k,v in tmp_map.items())
        
        tmp_map = {}
        
    #print(map_name)
    #print(maps)
    
    for z,item in enumerate(maps):
        #print(item)
        for j in x[1:]:
            vals = list(map(int, j.split()))
            src = vals[1]
            dest = vals[0]
            offset = vals[2]
            #print(item,src,dest,src + offset)
            
            if(item >= src and item <= src + offset):
                k = item + (dest - src)
                tmp_map[item] = k
                break
            else:
                tmp_map[item] = item

output = list(tmp_map.values())
output.sort()
print(output[0])
            

    
        



        
            

