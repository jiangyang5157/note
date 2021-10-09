//Find the minimal nucleotide from a range of sequence DNA.
//https://codility.com/programmers/lessons/5-prefix_sums/genomic_range_query/
package main

import "fmt"

func main() {
	S := "CAGCCTA"
	P := []int{2, 5, 0}
	Q := []int{4, 5, 6}
	result := Solution(S, P, Q)
	fmt.Printf("S=%v, P=%v, Q=%v\nresult=%v\n", S, P, Q, result)
}

func Solution(S string, P []int, Q []int) []int {
	ret := make([]int, len(P))
	A := make([]int, len(S)+1)
	C := make([]int, len(S)+1)
	G := make([]int, len(S)+1)
	for i := 0; i < len(S); i++ {
		switch S[i] {
		case 'A':
			A[i+1] = A[i] + 1
			C[i+1] = C[i]
			G[i+1] = G[i]
		case 'C':
			A[i+1] = A[i]
			C[i+1] = C[i] + 1
			G[i+1] = G[i]
		case 'G':
			A[i+1] = A[i]
			C[i+1] = C[i]
			G[i+1] = G[i] + 1
		default:
			A[i+1] = A[i]
			C[i+1] = C[i]
			G[i+1] = G[i]
		}
	}

	for i := 0; i < len(P); i++ {
		if A[Q[i]+1]-A[P[i]] > 0 {
			ret[i] = 1
		} else if C[Q[i]+1]-C[P[i]] > 0 {
			ret[i] = 2
		} else if G[Q[i]+1]-G[P[i]] > 0 {
			ret[i] = 3
		} else {
			ret[i] = 4
		}
	}

	return ret
}
