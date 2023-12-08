import re
def process_row(s):
    s = s.split('|')
    my_card = s[1]
    winner = s[0].split(':')
    return winner,my_card
    
file_path = "4.txt"
total = []
res = 0
card_results = {}
card_count = []
with open(file_path, 'r') as file:
    for line in file:
        s = line.strip()
        points = 0
        winner_card,my_card = process_row(s)
        winners = list(map(int, winner_card[1].split()))
        play = list(map(int, my_card.split()))
        
        game_num = int(re.sub('\D', '' ,winner_card[0])) - 1

        
        
        win_dict = {}
        play_dict = {}
        
        #print(winners)
        #print(play)
        for i in winners:
            win_dict[i] = 1           
        for i in play:
            if i in win_dict:
                points += 1
        card_results[game_num] = points
        card_count.append(1)

#print(card_results.keys())
for i,count in enumerate(card_count):
    wins = card_results[i]
    #print(i,wins)  
    for x in range(card_count[i]):
        for j in range(wins):
            card_count[i+(j+1)] += 1
    #print(card_count)
    #print()

k = 0
for z in card_count:
    k += z
print(k)

        

        
            

            
  
            
        

        

        


        
            

