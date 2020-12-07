for fu in [lambda s1,s2:s1.union(s2),lambda s1,s2:s1.intersection(s2)]:
    ng=True
    ans=set()
    su=0
    for answers in map(lambda s:s.strip(),open("input06.txt",'r').readlines()):
        if answers=='':
            su+=len(ans)

            ans=set()
            ng=True
        else:
            if ng:
                ans=set(list(answers))
                ng=False
            else:
                ans=fu(ans,set(list(answers)))
    print(su+len(ans))

#one liner
from functools import reduce 

print([sum(map(len,[reduce(lambda x,y:fu(x,y),block) for block in map(lambda s:map(set,s.split('\n')),open("input06.txt",'r').read().split('\n\n'))])) for fu in [lambda s1,s2:s1.union(s2),lambda s1,s2:s1.intersection(s2)]])

