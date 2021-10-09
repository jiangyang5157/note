//Find the missing element in a given permutation.
//https://codility.com/programmers/lessons/3-time_complexity/perm_missing_elem/
package main

import "fmt"

func main() {
	A := []int{2, 3, 1, 5}
	result := Solution(A)
	fmt.Printf("A=%v\nresult=%v\n", A, result)
}

func Solution(A []int) int {
	n := len(A) + 1
	sum := n * (n + 1) / 2
	tmp := 0
	for _, v := range A {
		tmp += v
	}
	return sum - tmp
}
