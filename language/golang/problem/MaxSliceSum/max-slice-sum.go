//Find a maximum sum of a compact subsequence of array elements.
//https://codility.com/programmers/lessons/9-maximum_slice_problem/
package main

import "fmt"

func main() {
	A := []int{3, 2, -6, 4, 0}
	result := Solution(A)
	fmt.Printf("A=%v\nresult=%v\n", A, result)
}

func Solution(A []int) int {
	ret := A[0]
	curr := ret
	for i := 1; i < len(A); i++ {
		curr = MaxInt(curr+A[i], A[i])
		ret = MaxInt(ret, curr)
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
