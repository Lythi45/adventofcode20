adapters=sorted(list(map(int,open("input10.txt",'r').readlines())))

adapters=[0]+adapters+[adapters[-1]+3]

diffs=list(map(lambda x:x[1]-x[0],zip(adapters[:-1],adapters[1:])))

print(sum([x == 1 for x in diffs]*sum(x==3 for x in diffs)))

jo=''.join(map(str,diffs))
parts=jo.split('3')

poss=1
for p in parts:
    poss*={'':1,'1':1,'11':2,'111':4,'1111':7}[p]
print(poss)