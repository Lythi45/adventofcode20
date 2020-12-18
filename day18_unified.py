calc={'+':lambda a,b:a+b,'*':lambda a,b:a*b}
prec=[[['+','*']],[['+'],['*']]]


def isn(n):
    return type(n)==type(1)

cc=[0]
def parse(line,i):
    c1=True
    while c1:
        c1=False
        for pr in prec[i]:
            c2=True
            while c2:
                c2=False
                p=0
                while line[p]!=')':
                    c3=False
                    if line[p]=='(':
                        line=line[:p]+parse(line[p+1:],i)
                        p=0
                        c3=True
                    if line[p+1] in pr and isn(line[p]) and isn(line[p+2]):
                        line=line[:p]+[calc[line[p+1]](line[p],line[p+2])]+line[p+3:]
                        c3=True
                    if p>0 and p<=len(line)-2 and line[p-1]=='(' and line[p+1]==')':
                        line=line[:p-1]+[line[p]]+line[p+2:]
                        c3=True
                    if c3==True:
                        c2=True
                        c1=True
                    if not c3:
                        p+=1
    return line[0:1]+line[2:]
    
su=[0,0]
lines=open("input18b.txt",'r').readlines()
lines=[line.strip().replace('(','( ').replace(')',' )').split() for line in lines]
lines=[['(']+[int(x) if x.isnumeric() else x for x in line]+[')'] for line in lines]
print([sum([parse(line[1:],i)[0] for line in lines]) for i in range(2)])