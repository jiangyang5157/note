//Rotate an array to the right by a given number of steps.
//https://codility.com/programmers/lessons/2-arrays/cyclic_rotation/
package main

import "fmt"

func main() {
	A := []int{3, 8, 9, 7, 6}
	K := 3
	result := Solution(A, K)
	fmt.Printf("A=%v, K=%v\nresult=%v\n", A, K, result)
}

func Solution(A []int, K int) []int {
	if len(A) > 1 {
		for K > 0 {
			var x int
			//pop
			x, A = A[len(A)-1], A[:len(A)-1]
			//push back
			A = append([]int{x}, A...)
			K--
		}
	}
	return A
}
