expenses=sorted(map(int,open('input01.txt','r').readlines()))
a=0
e=len(expenses)-1
while (expenses[a]+expenses[e])!=2020:
    if expenses[a]+expenses[e]<2020:
        a+=1
    else:
        e-=1
print(expenses[a]*expenses[e])

a=0
while True:
    b=a+1
    c=len(expenses)-1
    summe=2020-expenses[a]
    while b<c and (expenses[b]+expenses[c])!=summe:
        if expenses[b]+expenses[c]<summe:
            b+=1
        else:
            c-=1
    if b<c:
        print(expenses[a]*expenses[b]*expenses[c])
        break
    else:
        a+=1

from itertools import combinations
from functools import reduce
from operator import mul

for i in [2,3]:
    print(reduce(mul,next(filter(lambda x:sum(x)==2020,combinations(map(int,open('input01.txt','r').readlines()),i))),1))

