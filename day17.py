from itertools import product
def tuple_range(start, stop):
    return product(*(range(*x) for x in zip(start, stop)))

sp={}
for y,line in enumerate(open("input17.txt",'r').readlines()):
    for x,c in enumerate(line.strip()):
        sp[x,y,0] = (c=='#')

dirs=[]
for x,y,z in tuple_range((-1,-1,-1),(2,2,2)):
    if x!=0 or y!=0 or z!=0:
        dirs.append((x,y,z))

dist=0
for i in range(6):
    dist+=1
    nsp={}
    for x,y,z in tuple_range((-1-dist,-1-dist,-1-dist),(9+dist,9+dist,2+dist)):
            nn=sum([sp.get((x+d[0],y+d[1],z+d[2]),0) for d in dirs])
            state=sp.get((x,y,z),0)
            if state: 
                nsp[(x,y,z)]=True
            if state==False and nn==3:
                nsp[(x,y,z)]=True
            if  state and (nn<2 or nn>3):
                del nsp[(x,y,z)]
    sp=nsp
print(sum(sp.values()))

sp={}
for y,line in enumerate(open("input17.txt",'r').readlines()):
    for x,c in enumerate(line.strip()):
        sp[x,y,0,0] = (c=='#')

dirs=[]
for x,y,z,w in tuple_range((-1,-1,-1,-1),(2,2,2,2)):
    if x!=0 or y!=0 or z!=0 or w!=0:
        dirs.append((x,y,z,w))
            
dist=0
for i in range(6):
    dist+=1
    nsp={}
    for x,y,z,w in tuple_range((-1-dist,-1-dist,-1-dist,-1-dist),(9+dist,9+dist,2+dist,2+dist)):
        nn=sum([sp.get((x+d[0],y+d[1],z+d[2],w+d[3]),0) for d in dirs])
        state=sp.get((x,y,z,w),0)
        if state: 
            nsp[(x,y,z,w)]=True
        if state==False and nn==3:
            nsp[(x,y,z,w)]=True
        if  state and (nn<2 or nn>3):
            del nsp[(x,y,z,w)]
    sp=nsp
print(sum(sp.values()))