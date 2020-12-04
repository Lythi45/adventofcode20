forest=open("input03.txt",'r').readlines()
width=len(forest[0].strip())
trees=0
for i in range(1,len(forest)):
    if forest[i][(i*3)%width]=='#':
        trees+=1
print(trees)

tree_mul=1
for slope in [(1,1),(1,3),(1,5),(1,7),(2,1)]:
    trees=0
    y=slope[0]
    x=slope[1]
    while y<len(forest):
        if forest[y][x%width]=='#':
            trees+=1
            print(y,x%width)
        y+=slope[0]
        x+=slope[1]
    tree_mul*=trees
    print(trees)
print(tree_mul)
