tmp_map = {}
LOWEST_VAL = None
def process(seed,maps,tmp_map):
    for i in maps:
        #print(i)
        i_map = i.split('+')
        map_name = i_map[0]
        #print(map_name)
        seed = int(seed)       
        for j in i_map[1:]:
            #print(item)
            vals = list(map(int, j.split()))
            src = vals[1]
            dest = vals[0]
            offset = vals[2]
            if(seed >= src and seed <= src + offset):
                k = seed + (dest - src)
                seed = k
                break
    return seed

file_path = "5.txt"

clean = open(file_path).read().replace('\n', '+')
clean = clean.split('++')

seeds = clean[0].split(':')

seeds = list(map(int, seeds[1].split()))
size = len(seeds)

for i in range(0,int(size),2):
    start = seeds[i]
    end = (seeds[i] + seeds[i+1])
    #print(start,end)
    
    for j in range(start,end):
        tmp_map = {}
        res = process(j,clean[1:],tmp_map)
        #print(res)
        if LOWEST_VAL is None:
            LOWEST_VAL = res
        elif res < LOWEST_VAL:
            LOWEST_VAL = res        

        

print(LOWEST_VAL)

