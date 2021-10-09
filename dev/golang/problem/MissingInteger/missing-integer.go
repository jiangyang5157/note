//Find the minimal positive integer not occurring in a given sequence.
//https://codility.com/programmers/lessons/4-counting_elements/missing_integer/
package main

import "fmt"

func main() {
	// A := []int{1, 3, 6, 4, 1, 2}
	A := []int{1}
	result := Solution(A)
	fmt.Printf("A=%v\nresult=%v\n", A, result)
}

func Solution(A []int) int {
	aMap := make(map[int]int)
	max := 0
	for _, v := range A {
		aMap[v]++
		max = MaxInt(max, v)
	}

	ret := max + 1
	for i := 1; i < max; i++ {
		if aMap[i] == 0 {
			ret = i
			break
		}
	}

	return ret
}

func MaxInt(a, b int) int {
	if a > b {
		return a
	} else {
		return b
	}
}
