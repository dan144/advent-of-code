package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
    "regexp"
    "strconv"
)

func main() {
	file, err := os.Open("input/12")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	s := ""
	for scanner.Scan() {
		s = scanner.Text()
        fmt.Printf("Input: %d\n", len(s))
    }

    re := regexp.MustCompile(`-?\d+`)
    nums := re.FindAllString(s, -1)
    total := 0
    t2 := []int{}

    for _, i := range nums {
        j, err := strconv.Atoi(i)
        if err != nil {
            panic(err)
        }
        total += j
        t2 = append(t2, j)
    }

	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}
	fmt.Printf("Part 1: %d\n", total)
}
