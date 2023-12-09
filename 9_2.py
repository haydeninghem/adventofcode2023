


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

    history.insert( 0, int(history[0]) - int(differences[0]) )
    #print(history)
    
    
    return history[0]

file_path = "9.txt"

runner = []

total =0
with open(file_path, 'r') as file:
    for line in file:
        s = line.strip()
        history = s.split(" ")
        #print(history)
        k = process(history)
        
        runner.append(k)

for val in runner:
    total += val
print(total)
    
        


        
            

