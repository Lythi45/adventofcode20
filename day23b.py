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
    cup1=cupl[current]
    cup2=cupl[cup1]
    cup3=cupl[cup2]
    cupl[current]=cupl[cup3]

    dest=(current-1)%lc
    while dest in {cup1,cup2,cup3}:
        dest=(dest-1)%lc

    cupl[dest],cupl[cup3]=cup1,cupl[dest]
    current=cupl[current]
  
n=cupl[0]
n2=cupl[n]
print((n+1)*(n2+1))