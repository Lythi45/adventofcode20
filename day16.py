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

matches=[(pr,[p for p,t in enumerate(tnt) if all(map(lambda v:between_or(v,r),t))]) for pr,r in enumerate(rules)]
matches.sort(key=lambda x:len(x[1]))

for i in range(1,len(rules)-1):
    for j in range(i,len(rules)):
        matches[j][1].remove(matches[i-1][1][0])

mu=1
for i in range(len(rules)):
    if matches[i][0]<6:
        mu*=yticket[matches[i][1][0]]
print(mu)

    

