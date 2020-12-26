package main

import "fmt"
import "time"

func main() {
	start_time:= time.Now()
	const max_turns=30000000
	nums:=make([]int,max_turns)
	start:=[...]int{0,13,1,8,6,15}
    for  i:=0;i<len(start)-1;i++ {
		nums[start[i]]=i+1
	}
	turns:=len(start)
	new_num:=0
	last_num:=start[len(start)-1]
	for turns<max_turns {
		if nums[last_num]==0 {
			new_num=0;
		} else {
			new_num=turns-nums[last_num]
		}
		nums[last_num]=turns
		turns+=1
		last_num=new_num
	}
    
    fmt.Println( new_num,time.Since(start_time))
}