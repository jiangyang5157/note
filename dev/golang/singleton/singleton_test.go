package singleton

import (
	"fmt"
	"testing"
)

func Test_(t *testing.T) {
	Instance()["a"] = "C"
	Instance()["a"] = "A"
	Instance()["b"] = "B"
	fmt.Println("Instance=", Instance())
}
