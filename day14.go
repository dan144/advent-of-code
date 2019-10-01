package main

import (
	"bufio"
	"fmt"
	"log"
    "math"
	"os"
    "regexp"
    "strconv"
)

func main() {
	file, err := os.Open("input/14")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	s := ""
    seconds := 2503
    max := float64(0)
	for scanner.Scan() {
		s = scanner.Text()
        re := regexp.MustCompile(`\d+`)
        nums := re.FindAllString(s, -1)

        speed, err := strconv.Atoi(nums[0])
        time, err := strconv.Atoi(nums[1])
        rest, err := strconv.Atoi(nums[2])
        if err != nil {
            panic(err)
        }

        fulls := seconds / (time + rest)
        last := math.Mod(float64(seconds), float64(time + rest))
        dist := (float64(fulls * time) + math.Min(float64(time), last)) * float64(speed)
        if dist > max {
            max = dist;
        }
    }

	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}
	fmt.Printf("Part 1: %d\n", int(max))
}
