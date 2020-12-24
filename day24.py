dirs={'e':(1,0), 'se':(1,1), 'sw':(0,1), 'w':(-1,0), 'nw':(-1,-1), 'ne':(0,-1)}
tiles=set()
for line in map(lambda x:x.strip(),open('input24.txt','r').readlines()):
    p=0
    x,y=0,0
    while p<len(line):
        if line[p] in dirs:
            x+=dirs[line[p]][0]
            y+=dirs[line[p]][1]
            p+=1
        else:
            x+=dirs[line[p:p+2]][0]
            y+=dirs[line[p:p+2]][1]
            p+=2
    if (x,y) in tiles:
        tiles.remove((x,y))
    else:
        tiles.add((x,y))
print(len(tiles))
minx=min(map(lambda x:x[0],tiles))
maxx=max(map(lambda x:x[0],tiles))
miny=min(map(lambda x:x[1],tiles))
maxy=max(map(lambda x:x[1],tiles))

for r in range(100):
    new_tiles=set()
    for x in range(minx-r-1,maxx+r+2):
        for y in range(miny-r-1,maxy+r+2):
            n_neighbours=sum([(x+dx,y+dy) in tiles for dx,dy in dirs.values()])
            if ((x,y) in tiles and n_neighbours>0 and n_neighbours<3) or ((x,y) not in tiles and n_neighbours==2):
                new_tiles.add((x,y))
    tiles=new_tiles
print(len(tiles))


                

            


