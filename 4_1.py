
def process_row(s):
    s = s.split('|')
    my_card = s[1]
    winner = s[0].split(':')
    return winner,my_card
    
file_path = "4.txt"
total = []
res = 0
with open(file_path, 'r') as file:
    for line in file:
        s = line.strip()
        points = 0
        winner_card,my_card = process_row(s)
        winners = list(map(int, winner_card[1].split()))
        play = list(map(int, my_card.split()))
        
        win_dict = {}
        play_dict = {}

        #print(winners)
        #print(play)
        for i in winners:
            win_dict[i] = 1
            
        for i in play:
            if i in win_dict:
                points += 1
        if points != 0:
            total.append(2 ** int(points-1))
        
            
            
print(total)
for i in total:
    res += i  
print(res)
                

            
  
            
        

        

        


        
            

