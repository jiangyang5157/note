//Divide an array into the maximum number of same-sized blocks, each of which should contain an index P such that A[P - 1] < A[P] > A[P + 1].
//https://codility.com/programmers/lessons/10-prime_and_composite_numbers/peaks/
package main

import (
	"fmt"
	"math"
	"sort"
)

func main() {
	// A := []int{1, 2, 3, 4, 3, 4, 1, 2, 3, 4, 6, 2, 2}
	// A := []int{1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1}
	// A := []int{1, 2, 3, 4, 3, 4, 1, 2, 3, 4, 6, 2}
	A := []int{1, 3, 2, 4, 3, 4, 1, 2, 3, 4, 6, 2}
	// A := []int{1, 1, 1, 2, 1, 1}
	// A := []int{1, 3, 2, 1}
	result := Solution(A)
	fmt.Printf("A=%v\nresult=%v\n", A, result)
}

func Solution(A []int) int {
	// holds factors, worst-case space complexity is O(sqrt(N)*2)
	factors := []int{}
	// holds increased peaks' index, worst-case space complexity is O(N/2-1)
	peaks := []int{}

	sqrtN := int(math.Sqrt(float64(len(A))))
	maxPeakDis := len(A)
	for i := 1; i < len(A)-1; i++ {
		// add factors
		if i <= sqrtN {
			if len(A)%i == 0 {
				j := len(A) / i
				if j == i {
					factors = append(factors, i)
				} else {
					factors = append(factors, i)
					factors = append(factors, j)
				}
			}
		}
		// add peaks
		if A[i] > A[i-1] && A[i] > A[i+1] {
			if len(peaks) == 0 {
				maxPeakDis = MaxInt(i, len(A)-1-i)
			} else {
				maxPeakDis = MinInt(maxPeakDis, MaxInt(i-peaks[len(peaks)-1]-1, len(A)-1-i))
			}
			peaks = append(peaks, i)
		}
	}
	if len(peaks) == 0 {
		return 0
	}

	sort.Ints(factors)
	minK := maxPeakDis/2 + 1
	for i := 0; i < len(factors); i++ {
		if factors[i] < minK {
			continue
		}

		// verify if each group contains at least one peak
		ok := true
		currGroup := 0
		for _, peak := range peaks {
			landing := peak / factors[i]
			if landing > currGroup {
				ok = false
				break
			}
			if landing == currGroup {
				currGroup++
			} // else, the peak land on prev group
		}

		if ok {
			groups := len(A) / factors[i]
			if currGroup == groups {
				// return as the smallest i has the bigest groups value
				return groups
			}
		}
	}

	return 0
}

func MinInt(a, b int) int {
	if a < b {
		return a
	} else {
		return b
	}
}

func MaxInt(a, b int) int {
	if a > b {
		return a
	} else {
		return b
	}
}
