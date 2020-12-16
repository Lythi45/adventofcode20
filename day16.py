from functools import reduce 
lines=list(map(lambda x:x.strip(),open("input16.txt",'r').readlines()))
yt=lines.index('your ticket:')
nt=lines.index('nearby tickets:')
rules=[]

def between_or(x,ran):
    return (x>=ran[0][0] and x<=ran[0][1]) or (x>=ran[1][0] and x<=ran[1][1]) 

for i in range(0,yt-1):
    rules.append(list(map(lambda x:tuple(map(int,x.split('-'))),lines[i].split(':')[1].split('or'))))

yticket=list(map(int,lines[yt+1].split(',')))

ntickets=list(map(lambda x:list(map(int,x.split(','))),lines[nt+1:]))

su=0
valid_tickets=[]
for n in ntickets:
    tsu=0
    for v in n:
        tsu+=0 if any(map(lambda x:between_or(v,x),rules))  else v
    if tsu==0:
        valid_tickets.append(n)
    su+=tsu
print(su)

tnt=list(map(list, zip(*valid_tickets)))  #transpose
#print('tnt',valid_tickets, tnt)
ticks=[0]
matches=[[all(map(lambda v:between_or(v,r),t))for r in rules] for t in tnt]
print(matches)
def search(ru,po,mat,rl):
    for rul in range(ru,rl):
        for pos in po:
            if matches[pos][rul]:
                se=search(rul+1,po-set({pos}),mat+[(rul,pos)],rl)
                if len(se)==rl:
                    return se
        ticks[0]+=1
        if ticks[0]%100000==0:
            print(ticks[0],mat)
        #print(rul,len(po),mat)
    return mat
 
mapping=search(0,set(range(len(rules))),[],len(rules))
print(mapping)

mu=1
for i in mapping[:6]:
    print(i)
    mu*=yticket[i[1]]
print(mu)

    

