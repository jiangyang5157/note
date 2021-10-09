//Determine whether a triangle can be built from a given set of edges.
//https://codility.com/programmers/lessons/6-sorting/triangle/
package main

import (
	"fmt"
	"sort"
)

func main() {
	A := []int{10, 2, 5, 1, 8, 20}
	result := Solution(A)
	fmt.Printf("A=%v\nresult=%v\n", A, result)
}

func Solution(A []int) int {
	if len(A) < 3 {
		return 0
	}
	sort.Ints(A)
	for i := 0; i < len(A)-2; i++ {
		if A[i]+A[i+1] > A[i+2] {
			return 1
		} else {
			continue
		}
	}
	return 0
}
