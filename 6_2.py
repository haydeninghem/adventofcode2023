file_path = "6.txt"


def get_count(t,eval_d):
    j = 1
    while j < t:
        travel = t-j
        tmp_d = j*travel
        if(tmp_d > eval_d):
            return((travel - j) + 1)
        j+=1
    return t


file_path = "6.txt"
with open(file_path, 'r') as file:
    for i,line in enumerate(file):
        s = line.strip()
        if i == 0:
            time = s.split(':')
            time = int(time[1].replace(' ',''))
        else:
            distance = s.split(':')
            distance = int(distance[1].replace(' ',''))
        

print(time,distance)
p = get_count(time,distance)
print(p)


    

        

    
    




            

