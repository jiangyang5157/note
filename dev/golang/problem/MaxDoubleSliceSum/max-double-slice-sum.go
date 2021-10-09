//Find the maximal sum of any double slice.
//https://codility.com/programmers/lessons/9-maximum_slice_problem/max_double_slice_sum/
package main

import (
	"fmt"
	"math"
)

func main() {
	// A := []int{3, 2, 6, -1, 4, 5, -1, 2}
	A := []int{6, 1, 5, 6, 4, 2, 9, 4}
	result := Solution(A)
	fmt.Printf("A=%v\nresult=%v\n", A, result)
}

/*
  A triplet (X, Y, Z), such that 0 <= X < Y < Z < N, is called a double slice.
  leftMaxSum holds the max passible sum from a continuous left part of the double slice.
  The index of leftMaxSum indicates the split position (Y), such that 1 <= Y <= N-2.
  The max double slice sum occur as the max value of leftMaxSum[i] + rightMaxSum[i] locked.
*/
func Solution(A []int) int {
	if len(A) <= 3 {
		return 0
	}
	leftMaxSum := make([]int, len(A))
	rightMaxSum := make([]int, len(A))

	for i := 1; i <= len(A)-2; i++ {
		if i > 1 {
			leftMaxSum[i] = MaxInt(0, leftMaxSum[i-1]+A[i-1])
		}
		if i < len(A)-2 {
			rightMaxSum[len(A)-i-2] = MaxInt(0, rightMaxSum[len(A)-i-1]+A[len(A)-i-1])
		}
	}

	ret := math.MinInt32
	for i := 1; i <= len(A)-2; i++ {
		ret = MaxInt(ret, leftMaxSum[i]+rightMaxSum[i])
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
