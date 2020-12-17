sp={}
for y,line in enumerate(open("input17.txt",'r').readlines()):
    for x,c in enumerate(line.strip()):
        sp[x,y,0] = (c=='#')

dirs=[]
for z in range(-1,2):
    for y in range(-1,2):
        for x in range(-1,2):
            if x!=0 or y!=0 or z!=0:
                dirs.append((x,y,z))
            else:
                print(x,y,z)
print(dirs,len(dirs))
dist=0
for i in range(6):
    dist+=1
    nsp={}
    for z in range(-1-dist,2+dist):
        for y in range(-1-dist,9+dist):
            for x in range(-1-dist,9+dist):
                nn=sum([sp.get((x+d[0],y+d[1],z+d[2]),0) for d in dirs])
                state=sp.get((x,y,z),0)
                #print(state,x,y,z)
                if state: 
                    nsp[(x,y,z)]=True
                if state==False and nn==3:
                    nsp[(x,y,z)]=True
                if  state and (nn<2 or nn>3):
                    #print(state)
                    del nsp[(x,y,z)]
    sp=nsp
    #print(sp)
print(sum(sp.values()))

sp={}
for y,line in enumerate(open("input17.txt",'r').readlines()):
    for x,c in enumerate(line.strip()):
        sp[x,y,0,0] = (c=='#')

dirs=[]
for w in range(-1,2):
    for z in range(-1,2):
        for y in range(-1,2):
            for x in range(-1,2):
                if x!=0 or y!=0 or z!=0 or w!=0:
                    dirs.append((x,y,z,w))
            
            
print(dirs,len(dirs))
dist=0
for i in range(6):
    dist+=1
    nsp={}
    for w in range(-1-dist,2+dist):
        for z in range(-1-dist,2+dist):
            for y in range(-1-dist,9+dist):
                for x in range(-1-dist,9+dist):
                    nn=sum([sp.get((x+d[0],y+d[1],z+d[2],w+d[3]),0) for d in dirs])
                    state=sp.get((x,y,z,w),0)
                    #print(state,x,y,z)
                    if state: 
                        nsp[(x,y,z,w)]=True
                    if state==False and nn==3:
                        nsp[(x,y,z,w)]=True
                    if  state and (nn<2 or nn>3):
                        #print(state)
                        del nsp[(x,y,z,w)]
    sp=nsp
    #print(sp)
print(sum(sp.values()))






