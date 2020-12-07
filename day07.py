parents={}
children={}

def count_parents(bag):
    if bag in parents:
        pbags=[]+parents[bag]
        for b in parents[bag]: 
            pbags+=count_parents(b)
        return pbags
    else:
        return []

def count_children(bag):
    return bag[1]+bag[1]*sum(map(count_children,children[bag[0]])) if bag[1]>0 else 0

for line in open("input07.txt",'r').readlines():
    contain=line.split('contain')
    parent=' '.join(contain[0].split()[0:2])
    childss=contain[1].split(',')
    childs=map(lambda s:(' '.join(s.split()[1:3]),int(s.split()[0].replace('no','0'))),childss)
    childs=list(childs)
    for child in childs:
        parents[child[0]]=parents.get(child[0],[])+[parent]
    children[parent]=childs


print(len(set(count_parents('shiny gold'))))
print(count_children(('shiny gold',1))-1)