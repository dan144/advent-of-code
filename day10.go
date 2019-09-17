package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
    "strconv"
)

func main() {
	file, err := os.Open("input/10")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	s := ""
	for scanner.Scan() {
		s = scanner.Text()
        fmt.Printf("Input: %s\n", s)
    }

    for i := 0; i < 50; i++ {
        in_ord := 0
        new_s := ""
        c := ""
		for pos, chr := range s {
            in_ord += 1
            if pos + 1 == len(s) {
                c = string(chr)
                break
            }
            if s[pos] != s[pos + 1] {
                new_s += strconv.Itoa(in_ord) + string(chr)
                in_ord = 0
            }
		}
        s = new_s + strconv.Itoa(in_ord) + c
	    fmt.Printf("After %d: %d\n", i + 1, len(s))
        if i == 39 {
	        fmt.Printf("Part 1: %d\n", len(s))
        }

	}

	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}
	fmt.Printf("Part 2: %d\n", len(s))
}
