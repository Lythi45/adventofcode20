seats={}
for y,line in enumerate(open("input11.txt",'r').readlines()):
    for x,platz in enumerate(line):
        if platz=='L':
            seats[(x,y)]=False

neighbours=[(-1,-1),(0,-1),(1,-1),(-1,0),(1,0),(-1,1),(0,1),(1,1)]

while True:
    '''
    print(sum(seats.values()))
    for y in range(10):
        for x in range(10):
            print(['L','#','.'][seats.get((x,y),2)],end='')
        print()
    '''
    new_seats={}
    for seat in seats:
        n_neigbours=sum([seats.get((seat[0]+neighbour[0],seat[1]+neighbour[1]),False) for neighbour in neighbours])
        if seats[seat] and n_neigbours>=4:
            new_seats[seat]=False
        elif not seats[seat] and n_neigbours==0:
            new_seats[seat]=True
        else:
            new_seats[seat]=seats[seat]
    if new_seats==seats:
        break
    seats=new_seats

print(sum(seats.values()))

max_x=max([seat[0] for seat in seats])
max_y=max([seat[1] for seat in seats])
for seat in seats:
    seats[seat]=False

while True:
    new_seats={}
    for seat in seats:
        n_neigbours=0
        for nei in neighbours:
            occu=2 
            sx=seat[0]+nei[0]
            sy=seat[1]+nei[1]
            while occu==2 and sx>=0 and sx<=max_x and sy>=0 and sy<=max_y:
                occu=seats.get((sx,sy),2)
                sx+=nei[0]
                sy+=nei[1]
            if occu==1:
                n_neigbours+=1
        if seats[seat] and n_neigbours>=5:
            new_seats[seat]=False
        elif not seats[seat] and n_neigbours==0:
            new_seats[seat]=True
        else:
            new_seats[seat]=seats[seat]
    if new_seats==seats:
        break
    seats=new_seats

print(sum(seats.values()))
