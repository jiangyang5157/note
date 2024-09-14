//Compute the number of intersections in a sequence of discs.
//https://codility.com/programmers/lessons/6-sorting/number_of_disc_intersections/
/*
Given array indices i, j (i < j)
If the discs are located at (0,i) and (0,j) respectively
Then the discs will intersect if j − i <= A[i] + A[j]
*/
package main

import (
	"fmt"
	"sort"
)

func main() {
	A := []int{1, 5, 2, 1, 4, 0}
	result := Solution(A)
	fmt.Printf("A=%v\nresult=%v\n", A, result)
}

func Solution(A []int) int {
	upper := make([]int, len(A))
	lower := make([]int, len(A))
	for i := 0; i < len(A); i++ {
		upper[i] = A[i] + i
		lower[i] = -(A[i] - i)
	}
	sort.Ints(upper)
	sort.Ints(lower)

	ret := 0
	i, j := 0, 1
	for ; i < len(A); i++ {
		if ret > 10000000 {
			return -1
		}
		for ; j < len(A) && upper[i] >= lower[j]; j++ {
			ret += j - i
		}
	}
	return ret
}
