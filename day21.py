aller_s=set()
ingr_s=set()
foods=[]
for line in open("input21.txt",'r').readlines():
    sp=line.split(' (contains ')
    ingr=sp[0].split(' ')
    aller=sp[1].split(', ')
    aller[-1]=aller[-1][:-2]
    print(ingr,aller)
    ingr_s|=set(ingr)
    aller_s|=set(aller)
    foods.append([set(ingr),set(aller)])
print(ingr_s,aller_s)
ingr_aller={a:ingr_s.copy() for a in aller_s}
#print(ingr_aller)
for f in foods:
    for a in f[1]:
        print('-',a,ingr_aller[a],f[0],ingr_s-f[0])
        ingr_aller[a]-=ingr_s-f[0]
        print(ingr_aller[a])
print(ingr_aller)
for i in ingr_aller.values():
    #print(i)
    ingr_s-=i
    #print(ingr_s)
print(sum(i in ingr_s for f in foods for i in f[0]))
#[print(f,i,i in ingr_s) for f in foods for i in f[0] ]
aller_list=[]
while len(ingr_aller)>0:
    l=sorted(list(zip(ingr_aller.keys(),ingr_aller.values())),key=lambda x:len(x[1]))
    for i in range(1,len(ingr_aller)):
        ingr_aller[l[i][0]]-=l[0][1]
    aller_list.append((l[0][0],list(l[0][1])[0]))
    del ingr_aller[l[0][0]]
    print(l[0],l)
    
    
print(aller_list)
print(','.join([x[1] for x in sorted(aller_list,key=lambda x:x[0])]))
