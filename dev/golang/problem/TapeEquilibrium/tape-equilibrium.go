//Minimize the value |(A[0] + ... + A[P-1]) - (A[P] + ... + A[N-1])|.
//https://codility.com/programmers/lessons/3-time_complexity/tape_equilibrium/
package main

import (
	"fmt"
	"math"
)

func main() {
	// A := []int{3, 1, 2, 4, 3}
	// A := []int{-1000, 1000}
	A := []int{-10, -20, -30, -40, 100}
	result := Solution(A)
	fmt.Printf("A=%v\nresult=%v\n", A, result)
}

func Solution(A []int) int {
	sum1 := 0
	sum2 := 0
	minimal := math.MaxInt32

	for _, v := range A {
		sum2 += v
	}

	for i, v := range A {
		sum1 += v
		sum2 -= v
		if i == len(A)-1 {
			continue
		}
		minimal = MinInt(minimal, Abs(sum2-sum1))
	}

	return minimal
}

func MinInt(a, b int) int {
	if a < b {
		return a
	} else {
		return b
	}
}

func Abs(a int) int {
	if a < 0 {
		return -a
	} else {
		return a
	}
}
