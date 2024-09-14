//Find the maximum number of flags that can be set on mountain peaks.
//https://codility.com/programmers/lessons/10-prime_and_composite_numbers/flags/
package main

import (
	"fmt"
	"math"
)

func main() {
	A := []int{1, 5, 3, 4, 3, 4, 1, 2, 3, 4, 6, 2}
	result := Solution(A)
	fmt.Printf("A=%v\nresult=%v\n", A, result)
}

func Solution(A []int) int {
	if len(A) <= 2 {
		return 0
	}

	peaks := []int{}
	for i := 1; i < len(A)-1; i++ {
		if A[i] > A[i-1] && A[i] > A[i+1] {
			peaks = append(peaks, i)
		}
	}

	if len(peaks) <= 2 {
		return len(peaks)
	}

	maxFlags := int(math.Sqrt(float64(peaks[len(peaks)-1]-peaks[0]))) + 1
	for flags := maxFlags; flags > 2; flags-- {
		count := 1
		currPeak := peaks[0]
		for i := 1; i < len(peaks); i++ {
			if peaks[i]-currPeak >= flags {
				currPeak = peaks[i]
				count++
			}
		}
		if count == flags {
			return flags
		}
	}
	return 2
}
