//Find an result of an array such that its value occurs at more than half of indices in the array.
//https://codility.com/programmers/lessons/6-sorting/distinct/
package main

import "fmt"

func main() {
	A := []int{3, 4, 3, 2, 3, -1, 3, 3}
	// A := []int{2, 1, 1, 3, 4}
	result := Solution(A)
	fmt.Printf("A=%v\nresult=%v\n", A, result)
}

func Solution(A []int) int {
	aMap := make(map[int]int)
	half := len(A) / 2
	for i := 0; i < len(A); i++ {
		aMap[A[i]]++
		if aMap[A[i]] > half {
			return i
		}
	}
	return -1
}
