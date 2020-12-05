a=[[{'B':'1','R':'1','F':'0','L':'0'}[c] for c in line] for line in map(lambda s:s.strip(),open("input05.txt",'r').readlines())]
sp=sorted([int('0b'+''.join(line),2) for line in a],reverse=True)
print(sp[0],set(range(sp[-1],sp[0]))-set(sp))

