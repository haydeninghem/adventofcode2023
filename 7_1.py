def custom_sort(hand):
    card_order = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2}
    return [card_order[card] for card in hand]


def sorta(arr):
    sorted_hands = sorted(arr, key=custom_sort)
    total = my['total']
    #print(sorted_hands)
    for j in sorted_hands:
        my['i'] = my['i'] + 1
        #print(j,my['i'],bid[j])
        i = my['i']
        #print(int( (bid[j] * i)))
        my['total'] = my['total'] + int(bid[j]) * int(my['i'])
        
        
    




def rnk(hand,rn):
    highest_card = 1
    hand_eval = {}
    
    bid[hand] = rn
    for card in hand:
        
        card_amt = hand_eval.get(card, 0) + 1
        hand_eval[card] = card_amt
        

    # 5 values = high card
    # 4 VALUES = pair
    # 3 VALUES = 2 PAIR
    # 3 VALUES = 3 of a kind
    # 2 VALUES = full house
    # 2 VALUES = four of kind
    # 1 VALUES = five of a kind

    card_len = len(hand_eval.values())
    

    #print(hand)
    local_rank = 0
    hand[0] + '_'
    if card_len == 5:
        _HC.append(hand)
        return 'high card'
    if card_len == 4:
        _1P.append(hand)
        return '1 pair'
    
    if card_len == 3:
        if 3 in hand_eval.values():
            _3OAK.append(hand)
            return 'three of a kind'
        else:
            _2P.append(hand)
            return 'two pair'
    
    if card_len == 2:
        if 4 in hand_eval.values():
            _4OAK.append(hand)
            return 'four of a kind'
        else:
            _FH.append(hand)
            return 'full house'
    
    if card_len == 1:
        _5OAK.append(hand)
        return 'five of a kind'
    

file_path = "7.txt"

bid = {}

_5OAK = []
_4OAK = []
_FH = []
_3OAK = []
_2P = []
_1P = []
_HC =[]

my = {
    'total':0,
    'i':0
    }

def main():

    
    with open(file_path, 'r') as file:
        for line in file:
            s = line.strip()
            vals = s.split(' ')
            hand = vals[0]
            rn = vals[1]
            #print()
            res = rnk(hand,rn)
            #print(res)

    

 
    sorta(_HC)
    sorta(_1P)
    sorta(_2P)
    sorta(_3OAK)
    sorta(_FH)
    sorta(_4OAK)
    sorta(_5OAK)
    print(my['total'])

main()









            

