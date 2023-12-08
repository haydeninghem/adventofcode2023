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
            time = list(map(int, time[1].split()))
        else:
            distance = s.split(':')
            distance = list(map(int, distance[1].split()))
        

t_d_dict = dict(zip(time, distance))
print(t_d_dict)

total = 1
for i in range(len(time)):
    p = get_count(time[i],distance[i])
    total *= p
print(total)


    

        

    
    




            

