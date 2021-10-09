//Count minimal number of jumps from position X to Y.
//https://codility.com/programmers/lessons/3-time_complexity/frog_jmp/
package main

import "fmt"

func main() {
	X := 10
	Y := 85
	D := 30
	result := Solution(X, Y, D)
	fmt.Printf("X=%v, Y=%v, D=%v\nresult=%v\n", X, Y, D, result)
}

func Solution(X int, Y int, D int) int {
	if (Y-X)%D > 0 {
		return (Y-X)/D + 1
	} else {
		return (Y - X) / D
	}
}
