lines=open("input08.txt",'r').readlines()

def run():
    visit=set()
    pc=0
    acc=0
    while pc not in visit and pc<len(lines) and pc>=0:
        visit.add(pc)
        parts=lines[pc].split()
        comm=parts[0]
        arg=int(parts[1])
        if comm=='jmp':
            pc+=arg
        else:
            if comm=='acc':
                acc+=arg
            pc+=1
    return (pc in visit,acc)

print(run()[1])
print(run()[1])

for ln in range(len(lines)):
    line=lines[ln]
    if lines[:3]=='nop':
        lines[ln]='jmp'+lines[ln][3:]
    elif line[:3]=='jmp':
        lines[ln]='nop'+lines[ln][3:]
    result=run()
    print(ln,result)
    if not result[0]:
        print(result[1])
        break
    lines[ln]=line
print(run()[1])
