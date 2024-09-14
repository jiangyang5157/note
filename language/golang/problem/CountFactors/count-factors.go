//Count factors of given number n.
//https://codility.com/programmers/lessons/10-prime_and_composite_numbers/count_factors/
package main

import (
	"fmt"
	"math"
)

func main() {
	N := 24
	result := Solution(N)
	fmt.Printf("N=%v\nresult=%v\n", N, result)
}

func Solution(N int) int {
	ret := 0
	for i := int(math.Sqrt(float64(N))); i > 0; i-- {
		if N%i == 0 {
			if N/i == i {
				ret += 1
			} else {
				ret += 2
			}
		}
	}
	return ret
}
