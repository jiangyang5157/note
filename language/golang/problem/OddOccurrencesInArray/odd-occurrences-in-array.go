//Find value that occurs in odd number of elements.
//https://codility.com/programmers/lessons/2-arrays/odd_occurrences_in_array/
package main

import "fmt"

func main() {
	A := []int{9, 3, 9, 3, 9, 7, 9}
	result := Solution(A)
	fmt.Printf("A=%v\nresult=%v\n", A, result)
}

func Solution(A []int) int {
	aMap := make(map[int]int)
	for _, v := range A {
		aMap[v]++
		if aMap[v] > 1 {
			delete(aMap, v)
		}
	}
	for k, _ := range aMap {
		return k
	}
	return 0
}
