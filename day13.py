lines=open("input13.txt",'r').readlines()
time=int(lines[0])
buses=[(x[0],int(x[1])) for x in enumerate(lines[1].split(',')) if x[1]!='x']
bus_arrivals=sorted(list(map(lambda x: (x[1]-time%x[1],x[1]),buses)),key=lambda x:x[0])
print(bus_arrivals[0][0]*bus_arrivals[0][1])

a=0
b=1
for diff,takt in buses:
    while (a+diff)%takt!=0:
        a+=b
    b*=takt
print(a)

#oneliner
print((lambda a:lambda v:a(a,v))(lambda s,x:x if len(x[2])==0 else s(s,(x[0]+x[1],x[1],x[2])) if (x[0]+x[2][0][0])%x[2][0][1]!=0 else s(s,(x[0],x[1]*x[2][0][1],x[2][1:])))((0,1,[(x[0],int(x[1])) for x in enumerate(open("input13.txt",'r').readlines()[1].split(',')) if x[1]!='x']))[0])
