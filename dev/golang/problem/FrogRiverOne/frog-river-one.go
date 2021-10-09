//Find the earliest time when a frog can jump to the other side of a river.
//https://codility.com/programmers/lessons/4-counting_elements/frog_river_one/
package main

import "fmt"

func main() {
	X := 5
	A := []int{1, 3, 1, 4, 2, 3, 5, 4}
	result := Solution(X, A)
	fmt.Printf("X=%v, A=%v\nresult=%v\n", X, A, result)
}

func Solution(X int, A []int) int {
	ret := -1
	aMap := make(map[int]int)
	for i, v := range A {
		if v > X {
			// don't care
			continue
		}
		aMap[v]++
		if len(aMap) == X {
			ret = i
			break
		}
	}
	return ret
}
