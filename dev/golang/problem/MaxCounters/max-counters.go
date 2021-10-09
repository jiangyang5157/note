//Calculate the values of counters after applying all alternating operations: increase counter by 1; set value of all counters to current maximum.
//https://codility.com/programmers/lessons/4-counting_elements/max_counters/
package main

import "fmt"

func main() {
	N := 5
	A := []int{3, 4, 4, 6, 1, 4, 4}
	// A := []int{6, 1, 6, 6, 6, 6, 1}
	result := Solution(N, A)
	fmt.Printf("N=%v, A=%v\nresult=%v\n", N, A, result)
}

func Solution(N int, A []int) []int {
	ret := make([]int, N)
	max := 0
	lastMax := 0
	for _, v := range A {
		if v >= 1 && v <= N {
			ret[v-1] = MaxInt(ret[v-1], lastMax) + 1
			max = MaxInt(max, ret[v-1])
		} else if v == N+1 {
			lastMax = max
		}
	}

	for i := 0; i < N; i++ {
		ret[i] = MaxInt(ret[i], lastMax)
	}

	return ret
}

func MaxInt(a, b int) int {
	if a > b {
		return a
	} else {
		return b
	}
}
