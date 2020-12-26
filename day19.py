from itertools import product
lines=open("input19.txt",'r').readlines()

rules={}
messages=[]
for line in lines:
    line=line.strip()
    if len(line)>0:
        if line[0].isnumeric():
            rule=line.split(':')
            rule_n=int(rule[0])
            rl=[]
            if rule[1][1]=='"':
                rules[rule_n]=rule[1][2]
            else:
                for rulepairs in rule[1].split('|'):
                    rl.append(list(map(int,rulepairs.split())))
                rules[rule_n]=rl
        else:
            messages.append(line)

def rule_set(n):
    if type(rules[n])==type('a'):
        return {rules[n]}
    rs=set()
    for ro in rules[n]:
        rs|=rule_set(ro[0]) if len(ro)==1 else set(map(lambda x:x[0]+x[1],product(rule_set(ro[0]),rule_set(ro[1]))))
    return rs

rul=rule_set(0)
print(sum([m in rul for m in messages]))

rs42=rule_set(42)
rs31=rule_set(31)

match=0
for m in messages:
    n=0
    m1=0
    m2=0
    while m[n:n+8] in rs42:
        m1+=1
        n+=8
    while m[n:n+8] in rs31:
        m2+=1
        n+=8
    if n==len(m) and m1>m2 and m2>0:
        match+=1
print(match)
