cups='459672813'
cups=list(map(int,cups))
lc=1000000
cupl=[i+1 for i in range(lc)]

for i,c in enumerate(cups):
    cupl[c-1]=cups[(i+1)%len(cups)]-1
cupl[cups[-1]-1]=len(cups)
current=cups[0]-1
cupl[lc-1]=current

three_cups=[0,0,0]
for r in range(10000000):
    next=current
    for i in range(3):
        next=cupl[next]
        three_cups[i]=next
    cupl[current]=cupl[next]

    dest=(current-1)%lc
    while dest in three_cups:
        dest=(dest-1)%lc

    cupl[dest],cupl[three_cups[2]]=three_cups[0],cupl[dest]
    current=cupl[current]
  
n=cupl[0]
n2=cupl[n]
print((n+1)*(n2+1))