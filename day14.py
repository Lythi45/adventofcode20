memory={}
for line in open("input14.txt",'r').readlines():
    if line[:4]=="mask":
        mask=line[7:7+36]
        or_mask=int(mask.replace('X','0'),2)
        and_mask=int(mask.replace('X','1'),2)
    else:
        addr=int(line.split(']')[0][4:])
        value=int(line.split('=')[1])
        memory[addr]=(value & and_mask)| or_mask
print(sum(memory.values()))

memory={}
for line in open("input14.txt",'r').readlines():
    if line[:4]=="mask":
        mask=line[7:7+36]
        or_mask=int(mask.replace('X','0'),2)
        and_mask=int(mask.replace('0','1').replace('X','0'),2)
        flip_list=[]
        for n_bit,bit in enumerate(mask):
            if bit=='X':
                flip_list.append(35-n_bit)
    else:
        base_addr=(int(line.split(']')[0][4:]) & and_mask)| or_mask
        value=int(line.split('=')[1])
        for i in range(2**len(flip_list)):
            addr=base_addr
            for j in range(len(flip_list)):
                addr+= 2**flip_list[j] if i & 2**j >0 else 0
            memory[addr]=value
print(sum(memory.values()))




