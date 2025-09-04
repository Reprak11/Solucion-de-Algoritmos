// https://www.hackerrank.com/challenges/time-conversion/problem
// Reprak11

package main

import (
	"bufio"
	"fmt"
	"io"
	"os"
	"strconv"
	"strings"
)

/*
 * Complete the 'timeConversion' function below.
 *
 * The function is expected to return a STRING.
 * The function accepts STRING s as parameter.
 */

func timeConversion(s string) string {
	hour := s[:2]
	amPM := string(rune(s[len(s)-2]))
	result := hour

	if hour == "12" {
		if amPM == "A" {
			result = "00"
		} else {
			result = "12"
		}
	} else if amPM == "P" {
		i, _ := strconv.Atoi(result)
		result = strconv.Itoa(i + 12)
	}

	return result + s[2:len(s)-2]

}

func main() {
	reader := bufio.NewReaderSize(os.Stdin, 16*1024*1024)

	s := readLine(reader)

	result := timeConversion(s)

	fmt.Println(result) // directly print
}

func readLine(reader *bufio.Reader) string {
	str, _, err := reader.ReadLine()
	if err == io.EOF {
		return ""
	}

	return strings.TrimRight(string(str), "\r\n")
}

func checkError(err error) {
	if err != nil {
		panic(err)
	}
}
