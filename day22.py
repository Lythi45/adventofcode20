lines=list(map(lambda x:x.strip(),open("input22.txt",'r').readlines()))
cards=[]
half=(len(lines)+1)//2
for i in range(2):
    print(lines[2+i*half:i*half+half])
    cards.append(list(map(int,lines[1+i*half:i*half+half-1])))
while cards[0]!=[] and cards[1]!=[]:
    if cards[0][0]>cards[1][0]:
        cards[0]+=[cards[0].pop(0),cards[1].pop(0)]
    else:
        cards[1]+=[cards[1].pop(0),cards[0].pop(0)]
    print(cards)
winner=0 if cards[0]!=[] else 1

print(sum([v*(len(cards[winner])-i) for i,v in enumerate(cards[winner])]))

print(cards)
