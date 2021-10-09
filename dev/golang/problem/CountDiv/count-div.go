//Compute number of integers divisible by k in range [a..b].
//https://codility.com/programmers/lessons/5-prefix_sums/count_div/
package main

import "fmt"

func main() {
	A := 6
	B := 11
	K := 2
	result := Solution(A, B, K)
	fmt.Printf("A=%v, B=%v, K=%v\nresult=%v\n", A, B, K, result)
}

func Solution(A int, B int, K int) int {
	ret := B/K - A/K
	if A%K == 0 {
		ret++
	}
	return ret
}
