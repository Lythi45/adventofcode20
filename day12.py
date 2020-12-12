hr={'N':0,'E':1,'S':2,'W':3}
ri=[(0,1),(1,0),(0,-1),(-1,0)]
wx=10
wy=1
sr=1

for ship in range(2):
    sx=0
    sy=0
    for line in open("input12.txt",'r').readlines():
        r=line[0]
        dist=int(line[1:])
        
        if ship==0:
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
        else:
            wr=0
            if r=='F':
                sx+=dist*wx
                sy+=dist*wy
            elif r=='R':
                wr=(dist//90)%4
            elif r=='L':
                wr=(-dist//90)%4
            else:
                wx+=ri[hr[r]][0]*dist
                wy+=ri[hr[r]][1]*dist
            
            while wr!=0:
                wx,wy=(wy,-wx)
                wr=(wr-1)%4

    print(abs(sx)+abs(sy))