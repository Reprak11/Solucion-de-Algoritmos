// https://www.hackerrank.com/challenges/solve-me-first/problem
// Reprak11

package main

import "fmt"

func solveMeFirst(a uint32, b uint32) uint32 {
	// Hint: Type return (a+b)
	return a + b
}

func main() {
	var a, b, res uint32
	fmt.Scanf("%v\n%v", &a, &b)
	res = solveMeFirst(a, b)
	fmt.Println(res)
}
