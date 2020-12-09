from itertools import combinations
nums=list(map(int,open("input09.txt",'r').readlines()))
num=0
for i in range(25,len(nums)):
    num=nums[i]
    prenums=list(map(sum,combinations(nums[i-25:i],2)))
    if num not in prenums:
        print(num)
        break
ranges=combinations(range(len(nums)),2)
rangesums=map(lambda x:(sum(nums[x[0]:x[1]+1]),x[0],x[1]),ranges)
sums={}
for x in rangesums:
        sums[x[0]]=(x[1],x[2])
minmax=sums[num]
print(nums[minmax[0]]+nums[minmax[1]])



