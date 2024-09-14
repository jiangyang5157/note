//Maximize A[P] * A[Q] * A[R] for any triplet (P, Q, R).
//https://codility.com/programmers/lessons/6-sorting/max_product_of_three/
package main

import "fmt"
import "sort"

func main() {
	A := []int{-3, 1, 2, -2, 5, 6}
	result := Solution(A)
	fmt.Printf("A=%v\nresult=%v\n", A, result)
}

func Solution(A []int) int {
	if len(A) == 3 {
		return A[0] * A[1] * A[2]
	}
	sort.Ints(A)
	return MaxInt(A[len(A)-1]*A[len(A)-2]*A[len(A)-3], A[len(A)-1]*A[0]*A[1])
}

func MaxInt(a, b int) int {
	if a > b {
		return a
	} else {
		return b
	}
}
