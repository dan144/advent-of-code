package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
)

func main() {
	file, err := os.Open("input/8")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	total := 0
	value := 0
	ignore := 0
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		s := scanner.Text()
		total += len(s)
		value += len(s)
		ignore = 0
		for pos, chr := range s {
			if ignore > 0 {
				ignore -= 1
				continue
			}
			if pos == 0 || pos == len(s)-1 {
				value -= 1
				continue
			}
			if chr == '\\' {
				next := s[pos+1]
				if next == 'x' {
					ignore = 3
				} else if next == '"' || next == '\\' {
					ignore = 1
				}
				value -= ignore
			}
		}
	}

	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}
	fmt.Printf("Total: %d\n", total)
	fmt.Printf("Value: %d\n", value)
	fmt.Printf("Answer: %d\n", total-value)
}
