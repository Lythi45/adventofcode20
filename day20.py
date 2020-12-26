from itertools import combinations,product

def rotate_flip(ro,fl,s):
    yl=len(s)
    for rr in range(ro):
        r=[]
        for y in range(yl):
            rl=''
            for x in range(yl):
                rl+=s[x][yl-y-1]
            r.append(rl)
        s=r
    if fl:
        s=[s[yl-i-1] for i in range(yl)]
    return s

def ro_flip_insert(ro,fl,n,x,y,lines,image):
    size=len(image)//8
    im=[lines[i][1:9] for i in range(2+n*12,10+n*12)]
    im=rotate_flip(ro,fl,im)
    basey=y*8
    for sy in range(8):
        image[basey+sy]=image[basey+sy][:x*8]+im[sy]+image[basey+sy][x*8+8:]


lines=open("input20.txt",'r').readlines()
dirs=[(1,0),(0,1),(-1,0),(0,-1)]
st=[(0,0),(9,0),(9,9),(0,9)]
n_tiles=(len(lines)+1)//12
size={9:3,144:12}[n_tiles]
puzzle=['.'*8*size]*8*size
tiles=[]
tile_n=[]
tile_kn={}
for n in range(n_tiles):
    tile_n.append(int(lines[n*12][5:9]))
    ka=[]
    for k in range(4):
        ks=''
        for i in range(10):
            ks+=lines[1+n*12+st[k][1]+dirs[k][1]*i][st[k][0]+dirs[k][0]*i]
        ka.append(ks)
    tiles.append(ka)

def match(k1,k2,fl):
    return k1==k2 if fl else k1==k2[::-1]
x=0
tile_kn={i:{} for i in range(n_tiles)}

for c in combinations(range(n_tiles),2):
    for k in range(4):
        for ro in range(4):
            for fl in [False,True]:
                if match(tiles[c[0]][k],tiles[c[1]][ro],fl):
                    tile_kn[c[0]][k]=(c[1],ro,fl)
                    tile_kn[c[1]][ro]=(c[0],k,fl)
                    x+=1
                
mu=1
for tile in [tn for tn in tile_kn if len(tile_kn[tn])==2]:
    mu*=tile_n[tile]
print(mu)

seamo_s='''
                  # 
#    ##    ##    ###
 #  #  #  #  #  #   
 '''.split('\n')[1:4]

seamo={(x,y) for y,line in enumerate(seamo_s) for x,c in enumerate(line) if c=='#'}

right,down=tile_kn[tile].values()
rr,dr=list(tile_kn[tile].keys())
if dr!=(rr+1)%4:
    right,down=down,right
    rr,dr=dr,rr
lefttile=tile
lflip=False
for j in range(0,size):
    tile=lefttile
    flip=lflip
    for i in range(0,size):
        ro=(rr-1)%4
        ro_flip_insert(ro,flip,tile,i,j,lines,puzzle)
        if i<size-1:
            next_tile=tile_kn[tile][rr]
            tile=next_tile[0]
            flip=flip!=next_tile[2]
            rr=(next_tile[1]+2)%4
    if j<size-1:
        next_tile=tile_kn[lefttile][dr]
        lefttile=next_tile[0]
        lflip=lflip!=next_tile[2]
        dr=(next_tile[1]+2)%4
        rr=(dr-1)%4
        if rr not in tile_kn[lefttile]:
            rr=(rr+2)%4
    
for f in range(2):
    for ro in range(4):
        seamo_n=0
        for y in range(96-2):
            for x in range(96-19):
                for p in seamo:
                    if puzzle[y+p[1]][x+p[0]]!='#':
                        break
                else:
                    seamo_n+=1
        if seamo_n>0:
            print(sum([sum(1 for c in l if c=='#') for l in puzzle])-seamo_n*len(seamo))
        puzzle=rotate_flip(1,0,puzzle)
    puzzle=rotate_flip(0,1,puzzle)

    