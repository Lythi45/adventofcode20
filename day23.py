cups='459672813'
#cups='389125467'
cups=list(map(int,cups))
lc=len(cups)

n=0
for r in range(100):
    three_cups=cups[1:4]

    cups=cups[:1]+cups[4:]
    dest=(cups[0]-2)%lc+1
    while dest in three_cups:
        dest=(dest-2)%lc+1
    po=cups.index(dest)
    cups=cups[:po+1]+three_cups+cups[po+1:]
    cups=cups[1:]+cups[:1]
    
p1=cups.index(1)
print(''.join(map(str,cups[p1+1:]+cups[:p1])))

