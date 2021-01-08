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
	file, err := os.Open("input14")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	s := ""
	seconds := 2503
	var speeds [][]int
	var points []int
	var dist []int

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

		speeds = append(speeds, []int{speed, time, rest})
		points = append(points, 0)
		dist = append(dist, 0)
	}

	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}

	for sec := 0; sec <= seconds; sec++ {
		for i, r := range speeds {
			m_sec := math.Mod(float64(sec), float64(r[1]+r[2]))
			if int(m_sec) < r[1] {
				dist[i] += r[0]
			}
		}
		max := 0
		var winners []int
		for i, _ := range speeds {
			if dist[i] == dist[max] {
				winners = append(winners, i)
			} else if dist[i] > dist[max] {
				winners = []int{i}
				max = i
			}
		}
		for _, m := range winners {
			points[m] += 1
		}
	}

	d_max := 0
	p_max := 0
	for i, _ := range speeds {
		if dist[i] > d_max {
			d_max = dist[i]
		}
		if points[i] > p_max {
			p_max = points[i]
		}
	}

	fmt.Printf("Part 1: %d\n", int(d_max))
	fmt.Printf("Part 2: %d\n", int(p_max))
}
