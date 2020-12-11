seats={}
for y,line in enumerate(open("input11.txt",'r').readlines()):
    for x,platz in enumerate(line):
        if platz=='L':
            seats[(x,y)]=0

def occu_seats(seats,num_too_full,look_for_seats):

    def look_around(pos,dir,max_x,max_y):
        new_pos=(pos[0]+dir[0],pos[1]+dir[1])
        return new_pos if seats.get(new_pos,-1)>=0 or pos[0]<0 or pos[0]>max_x or pos[1]<0 or pos[1]>max_y else look_around(new_pos,dir,max_x,max_y)

    max_x=max([seat[0] for seat in seats])
    max_y=max([seat[1] for seat in seats])
    '''
    for y in range(max_y):
        for x in range(max_x):
            print(['L','#','.'][seats.get((x,y),2)],end='')
        print()
    '''
    seat_n={}
    neighbours=[(-1,-1),(0,-1),(1,-1),(-1,0),(1,0),(-1,1),(0,1),(1,1)]
    for seat in seats:
        seats[seat]=0
        po_nei=[]
        for nei in neighbours:
            po_nei.append(look_around(seat,nei,max_x,max_y) if look_for_seats else (seat[0]+nei[0],seat[1]+nei[1]))
        seat_n[seat]=po_nei

    while True:
        new_seats={}
        for seat in seats:
            n_neigbours=sum(seats.get(nei,0) for nei in seat_n[seat])
            if seats[seat]==1 and n_neigbours>=num_too_full:
                new_seats[seat]=False
            elif seats[seat]==0 and n_neigbours==0:
                new_seats[seat]=True
            else:
                new_seats[seat]=seats[seat]
        if new_seats==seats:
            break
        seats=new_seats
    return sum(seats.values())

print(occu_seats(seats,4,False))
print(occu_seats(seats,5,True))