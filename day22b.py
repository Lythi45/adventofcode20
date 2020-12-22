lines=list(map(lambda x:x.strip(),open("input22.txt",'r').readlines()))
cards=[]
half=(len(lines)+1)//2
for i in range(2):
    cards.append(list(map(int,lines[1+i*half:i*half+half-1])))

def state(cards):
    return (tuple(cards[0]),tuple(cards[1]))

#winner_d={}
def game(cards):
    state_s=set()
    while cards[0]!=[] and cards[1]!=[] and state(cards) not in state_s:
        state_s.add(state(cards))
        if all([len(card)>card[0] for card in cards] ):
            winner,x=game([cards[0][1:cards[0][0]+1],cards[1][1:cards[1][0]+1]])
        else:
            winner=0 if cards[0][0]>cards[1][0] else 1
        if winner==0:
            cards[0]+=[cards[0].pop(0),cards[1].pop(0)]
        else:
            cards[1]+=[cards[1].pop(0),cards[0].pop(0)]
    if state(cards) in state_s:
        winner=0
    else:
        winner=0 if cards[0]!=[] else 1
    return(winner,cards)

winner,cards=game(cards)

print(sum([v*(len(cards[winner])-i) for i,v in enumerate(cards[winner])]))