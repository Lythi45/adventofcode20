n=0
n2=0
for line in open('input02.txt','r').readlines():
    parts=line.split()
    char=parts[1][0]
    nc=parts[2].count(char)
    min,max=map(int,parts[0].split('-'))
    if nc>=min and nc<=max:
        n+=1
    if (parts[2][min-1]==char)+(parts[2][max-1]==char)==1:
        n2+=1
print(n,n2)
    