//Find longest sequence of zeros in binary representation of an integer.
//https://codility.com/programmers/lessons/1-iterations/binary_gap/
package main

import (
	"fmt"
	"strconv"
)

func main() {
	N := 51712
	result := Solution(N)
	fmt.Printf("N=%v\nresult=%v\n", strconv.FormatInt(int64(N), 2), result)
}

func Solution(N int) int {
	ret := 0
	count := -1
	for N > 0 {
		if N%2 == 0 {
			if count != -1 {
				count++
			}
		} else {
			if count > 0 {
				ret = MaxInt(ret, count)
			}
			count = 0
		}
		N = N >> 1
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
