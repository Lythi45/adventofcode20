hr={'N':0,'E':1,'S':2,'W':3}
ri=[(0,1),(1,0),(0,-1),(-1,0)]
sx=0
sy=0
sr=1
for line in open("input12.txt",'r').readlines():
    r=line[0]
    dist=int(line[1:])
    if r=='F':
        sx+=ri[sr][0]*dist
        sy+=ri[sr][1]*dist
    elif r=='R':
        sr=(sr+(dist//90))%4
    elif r=='L':
        sr=(sr-(dist//90))%4
    else:
        sx+=ri[hr[r]][0]*dist
        sy+=ri[hr[r]][1]*dist
print(abs(sx)+abs(sy))

hr={'N':0,'E':1,'S':2,'W':3}
ri=[(0,1),(1,0),(0,-1),(-1,0)]
sx=0
sy=0
wx=10
wy=1
sr=1
for line in open("input12.txt",'r').readlines():
    r=line[0]
    dist=int(line[1:])
    
    osr=sr
    if r=='F':
        sx+=dist*wx
        sy+=dist*wy
    elif r=='R':
        sr=(sr+(dist//90))%4
    elif r=='L':
        sr=(sr-(dist//90))%4
    else:
        wx+=ri[hr[r]][0]*dist
        wy+=ri[hr[r]][1]*dist
    
    while osr!=sr:
        wx,wy=(wy,-wx)
        osr=(osr+1)%4

print(abs(sx)+abs(sy))
