lines=open("input13.txt",'r').readlines()
time=int(lines[0])
b_takt=[int(x) for x in lines[1].split(',') if x!='x']
bus_arrivals=sorted(list(map(lambda x: (x-time%x,x),b_takt)),key=lambda x:x[0])
print(bus_arrivals[0][0]*bus_arrivals[0][1])

a=0
b=1
buses=[(x[0],int(x[1])) for x in enumerate(lines[1].split(',')) if x[1]!='x']
for diff,takt in  buses:
    while (a+diff)%takt!=0:
        a+=b
    b*=takt
print(a)
