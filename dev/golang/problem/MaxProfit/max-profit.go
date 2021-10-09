//Given a log of stock prices compute the maximum possible earning.
//https://codility.com/programmers/lessons/9-maximum_slice_problem/max_profit/
package main

import "fmt"

func main() {
	A := []int{23171, 21011, 21123, 21366, 21013, 21367}
	result := Solution(A)
	fmt.Printf("A=%v\nresult=%v\n", A, result)
}

func Solution(A []int) int {
	currProfit, maxProfit := 0, 0
	for i := 1; i < len(A); i++ {
		currProfit = MaxInt(0, currProfit+A[i]-A[i-1])
		maxProfit = MaxInt(maxProfit, currProfit)
	}
	return maxProfit
}

func MaxInt(a, b int) int {
	if a > b {
		return a
	} else {
		return b
	}
}
