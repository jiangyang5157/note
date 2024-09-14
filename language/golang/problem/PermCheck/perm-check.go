//Check whether array A is a permutation.
//https://codility.com/programmers/lessons/4-counting_elements/perm_check/
package main

import "fmt"

func main() {
	A := []int{4, 1, 3, 2}
	// A := []int{4, 1, 3}
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

	if len(aMap) == max && len(A) == max {
		return 1
	} else {
		return 0
	}
}

func MaxInt(a, b int) int {
	if a > b {
		return a
	} else {
		return b
	}
}
