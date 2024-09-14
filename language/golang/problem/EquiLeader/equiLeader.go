//Find the index S such that the leaders of the sequences A[0], A[1], ..., A[S] and A[S + 1], A[S + 2], ..., A[N - 1] are the same.
//https://codility.com/programmers/lessons/8-leader/equi_leader/
package main

import "fmt"

func main() {
	A := []int{4, 3, 4, 4, 4, 2}
	// A := []int{0, 0, 0, 0, 0, 0, 0, 0, 0, 0}
	result := Solution(A)
	fmt.Printf("A=%v\nresult=%v\n", A, result)
}

func Solution(A []int) int {
	aMap := make(map[int]int)
	leaderIndex := -1
	for i := 0; i < len(A); i++ {
		aMap[A[i]]++
		if leaderIndex == -1 && aMap[A[i]] > len(A)/2 {
			leaderIndex = i // leader of A exist
		}
	}
	if leaderIndex == -1 {
		return 0
	}

	ret := 0
	leaderCount := 0
	leaderCountRemain := aMap[A[leaderIndex]]
	for i := 0; i < len(A)-1; i++ {
		if A[i] == A[leaderIndex] {
			leaderCount++
			leaderCountRemain--
		}
		len1 := i + 1         // length of first part
		len2 := len(A) - len1 // length of second part
		if leaderCount > len1/2 && leaderCountRemain > len2/2 {
			ret++
		}
	}

	return ret
}
