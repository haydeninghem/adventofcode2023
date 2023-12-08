import re
import numpy as np
 
total_power = []
total = 0
game_list = []
RED_CNT = 12
GREEN_CNT = 13
BLUE_CNT = 14

rules = {
    'red':0,
    'green':0,
    'blue':0
}

file_path = "2.txt"   
with open(file_path, 'r') as file:
    for line in file:
        
        largest = {
                'red':1,
                'green':1,
                'blue':1
        }
        line = line.strip()
        game_id = line.split(':')
        raw_turn_data = game_id[1]
        
        game_id = re.sub('\D', '' ,game_id[0])
        game_list.append(game_id)
        turn_data = raw_turn_data.split(';')
        print(line)
        for turn in turn_data:
            cubes = turn.split(',')
            for i in cubes:
                vals = i.split(' ')
                num   =   vals[1] 
                color =   vals[2]
                if int(largest[color]) < int(num):
                    largest[color] = num
        power = int(largest['red']) * int(largest['blue']) * int(largest['green'])
        total_power.append(power)

for powers in total_power:
    total += powers

print(total)
        
        
        
                
                
            




            
        
            

