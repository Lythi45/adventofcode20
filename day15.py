num_list=[0,13,1,8,6,15]
for max_turn in [2020,30000000]:
    last_num=num_list[-1]
    turns=len(num_list)
    nums=dict(zip(num_list[:-1],range(turns-1)))
    while turns<max_turn:
        new_num=turns-nums[last_num]-1 if last_num in nums else 0
        nums[last_num]=turns-1
        last_num=new_num
        turns+=1
    print(new_num)