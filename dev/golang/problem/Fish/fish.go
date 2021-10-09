//N voracious fish are moving along a river. Calculate how many fish are alive.
//https://codility.com/programmers/lessons/7-stacks_and_queues/fish/
package main

import "fmt"

func main() {
	A := []int{4, 3, 2, 1, 5}
	B := []int{0, 1, 0, 0, 0}
	result := Solution(A, B)
	fmt.Printf("A=%v, B=%v\nresult=%v\n", A, B, result)
}

func Solution(A []int, B []int) int {
	downs := []int{}
	upNum := 0

	for i := 0; i < len(B); i++ {
		if B[i] == 1 {
			down := A[i]
			// cache the downstream fish size
			downs = Push(downs, down)
		} else {
			up := A[i]

			if Length(downs) == 0 {
				// no downstream fish in front of me
				upNum++
			} else {
				// has downstream fish in front of me, and I am going to eat anything smaller
				for Length(downs) != 0 && up > Peek(downs) {
					_, downs = Pop(downs)
				}
				if Length(downs) == 0 {
					// no bigger downstream fish in front of me
					upNum++
				} // else be eaten by the bigger downstream fish
			}
		}
	}

	return Length(downs) + upNum
}

func Length(s []int) int {
	return len(s)
}

func Peek(s []int) int {
	return s[len(s)-1]
}

func Pop(s []int) (int, []int) {
	return s[len(s)-1], s[:len(s)-1]
}

func Push(s []int, x ...int) []int {
	return append(s, x...)
}
