//Find the minimal average of any slice containing at least two elements.
//https://codility.com/programmers/lessons/5-prefix_sums/min_avg_two_slice/
/*
Let:
  len(s) = length of a slice s,
  sum(s) = sum of the all elements of the slice s
  ave(s) = average of the slice s
Then:
  Every slice s having len(s) > 3 contains a sub-slice s’ such that ave(s) >= ave(s’).
Proof:
  Suppose,
    That s is a slice having len(s) > 3 and does NOT contain a sub-slice s’ such that ave(s) >= ave(s’).
    Since, len(s) > 3, s can be divided into sub-slices t and u.
    Then,
      ave(t) = sum(t) / len(t)
      ave(u) = sum(u) / len(u)
      ave(s) = sum(s) / len(s)
             = [sum(t) + sum(u)] / [len(t) + len(u)]
             = [len(t) * ave(t) + len(u) * ave(u)] / [len(t) + len(u)]
    If ave(u) >= ave(t) then let s’ be t,
      ave(s) = [len(t) * ave(t) + len(u) * ave(u)] / [len(t) + len(u)]
      ave(s) >= [[len(t) + len(u)] * ave(t)] / [len(t) + len(u)]
      ave(s) >= ave(t)
      ave(s) >= ave(s’)
    Otherwise, if ave(t) >= ave(u) then let s’ be u,
      ave(s) = [len(t) * ave(t) + len(u) * ave(u)] / [len(t) + len(u)]
      ave(s) >= [[len(t) + len(u)] * ave(u)] / [len(t) + len(u)]
      ave(s) >= ave(u)
      ave(s) >= ave(s’)
    Therefore, we can alwasy find a sub-slice s’ such that ave(s) >= ave(s’).
  So,
    This leads a contradiction of
      "That s is a slice having len(s) > 3 and does NOT contain a sub-slice s’ such that ave(s) >= ave(s’)."
    and completes the proof.
*/
package main

import (
	"fmt"
	"math"
)

func main() {
	A := []int{4, 2, 2, 5, 1, 5, 8}
	result := Solution(A)
	fmt.Printf("A=%v\nresult=%v\n", A, result)
}

func Solution(A []int) int {
	if len(A) < 2 {
		return 0
	}

	ret := 0
	minAve := math.MaxFloat32
	for i := 0; i < len(A); i++ {
		if i < len(A)-1 {
			ave := float64(A[i]+A[i+1]) / 2
			if ave < minAve {
				minAve = ave
				ret = i
			}
		}
		if i < len(A)-2 {
			ave := float64(A[i]+A[i+1]+A[i+2]) / 3
			if ave < minAve {
				minAve = ave
				ret = i
			}
		}
	}

	return ret
}
