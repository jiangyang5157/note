//Cover "Manhattan skyline" using the minimum number of rectangles.
//https://codility.com/programmers/lessons/7-stacks_and_queues/stone_wall/
package main

import "fmt"

func main() {
	H := []int{8, 8, 5, 7, 9, 8, 7, 4, 8}
	result := Solution(H)
	fmt.Printf("H=%v\nresult=%v\n", H, result)
}

func Solution(H []int) int {
	ret := 0
	s := []int{}
	var tmp int

	for _, v := range H {
		if Length(s) == 0 || Peek(s) <= v {
			s = Push(s, v)
			continue
		}

		for Length(s) > 0 && Peek(s) > v {
			tmp, s = Pop(s)
			if Length(s) == 0 || tmp != Peek(s) {
				ret++
			}
		}

		s = Push(s, v)
	}

	for Length(s) > 0 {
		tmp, s = Pop(s)
		if Length(s) == 0 || tmp != Peek(s) {
			ret++
		}
	}
	return ret
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
