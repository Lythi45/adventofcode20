from itertools import combinations
nums=list(map(int,open("input09.txt",'r').readlines()))
num=0
for i in range(25,len(nums)):
    num=nums[i]
    prenums=list(map(sum,combinations(nums[i-25:i],2)))
    if num not in prenums:
        print(num)
        break
# Sucht nach einen Bereich von nums, der zusammenaddiert so groß wie num ist
# und gibt die Summe der ersten und letzten Zahl dieses Bereiches aus
ranges=combinations(range(len(nums)),2)
rangesums=map(lambda x:(sum(nums[x[0]:x[1]+1]),nums[0]+nums[x[1]]),ranges)
print([x[1] for x in rangesums if x[0]==num])


