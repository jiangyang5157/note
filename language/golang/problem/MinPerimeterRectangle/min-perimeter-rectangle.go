//Find the minimal perimeter of any rectangle whose area equals N.
//https://codility.com/programmers/lessons/10-prime_and_composite_numbers/min_perimeter_rectangle/
package main

import (
	"fmt"
	"math"
)

func main() {
	N := 30
	result := Solution(N)
	fmt.Printf("N=%v\nresult=%v\n", N, result)
}

func Solution(N int) int {
	for i := int(math.Sqrt(float64(N))); i > 0; i-- {
		if N%i == 0 {
			return 2 * (i + N/i)
		}
	}
	return 0
}
