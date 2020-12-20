from itertools import combinations,product
lines=open("input20.txt",'r').readlines()
dirs=[(1,0),(0,1),(-1,0),(0,-1)]
st=[(0,0),(9,0),(9,9),(0,9)]
print(st)
n_tiles=(len(lines)+1)//12
size={9:3,144:12}[n_tiles]
tiles=[]
tile_n=[]
tile_kn={}
for n in range(n_tiles):
    print(n)
    tile_n.append(int(lines[n*12][5:9]))
    ka=[]
    for k in range(4):
        ks=''
        print(1+n*12+st[k][1]+dirs[k][1],st[k][0]+dirs[k][0])
        for i in range(10):
            ks+=lines[1+n*12+st[k][1]+dirs[k][1]*i][st[k][0]+dirs[k][0]*i]
        ka.append(ks)
    tiles.append(ka)
print(tiles)
print(n_tiles)

def match(k1,k2,fl):
    return k1==k2 if fl else k1==k2[::-1]
x=0
for c in combinations(range(n_tiles),2):
    for k in range(4):
        for ro in range(4):
            for fl in [False,True]:
                if match(tiles[c[0]][k],tiles[c[1]][(k+2+ro)%4],fl):
                    print(c,k,ro,fl)
                    tile_kn[c[0]]=tile_kn.get(c[0],[])+[(c[1],k,ro,fl)]
                    tile_kn[c[1]]=tile_kn.get(c[1],[])+[(c[0],ro,k,fl)]
                
print(x,tile_kn)
mu=1
for n in [tile_n[tn] for tn in tile_kn if len(tile_kn[tn])==2]:
    mu*=n
print(mu)

seamo='''
                  # 
#    ##    ##    ###
 #  #  #  #  #  #   
 '''.split('\n')[1:4]
 
start_tile=[tn for tn in tile_kn if len(tile_kn[tn])==2 and all(k[1] in {2,3} for k in tile_kn[tn])][0]
print(start_tile)


print(seamo)
