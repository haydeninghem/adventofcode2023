


def process(history):
    differences = []
    
    for i in range(len(history) - 1):
        diff = int(history[i + 1])  - int(history[i])
        differences.append(diff)
        
    b = all(v == 0 for v in differences)

    
    if not b:
        process(differences)
    else:
        zzz=0

    history.append(int(differences[-1]) + int(history[-1]))
    #runner.append(history[-1])
    
    
    return history[-1]

file_path = "9_T.txt"

#runner = []

total =0
with open(file_path, 'r') as file:
    for line in file:
        s = line.strip()
        history = s.split(" ")
        #print(history)
        k = process(history)
        total += k
        #print(k)
print(total)
#for val in runner:
#    total += val
#print(total)
    
        


        
            

