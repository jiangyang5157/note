//Determine whether a given string of parentheses is properly nested.
//https://codility.com/programmers/lessons/7-stacks_and_queues/brackets/
package main

import "fmt"

func main() {
	S := "{[()()]}"
	// S := "([)()]"
	result := Solution(S)
	fmt.Printf("S=%v\nresult=%v\n", S, result)
}

func Solution(S string) int {
	if len(S)%2 != 0 {
		return 0
	}

	s := []byte{}
	for i := 0; i < len(S); i++ {
		switch S[i] {
		case ')':
			s = process(s, '(')
		case ']':
			s = process(s, '[')
		case '}':
			s = process(s, '{')
		default:
			s = Push(s, S[i])
		}
	}

	if len(s) == 0 {
		return 1
	}
	return 0
}

func process(s []byte, b byte) []byte {
	if Length(s) != 0 && Peek(s) == b {
		_, s = Pop(s)
	}
	return s
}

func Length(s []byte) int {
	return len(s)
}

func Peek(s []byte) byte {
	return s[len(s)-1]
}

func Pop(s []byte) (byte, []byte) {
	return s[len(s)-1], s[:len(s)-1]
}

func Push(s []byte, x ...byte) []byte {
	return append(s, x...)
}
