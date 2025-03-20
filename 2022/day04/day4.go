package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	var overlaps, overlaps2 int

	file, err := os.Open("day4.input")
	if err != nil {
		fmt.Printf("Error opening file: %v\n", err)
		return
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)

	for scanner.Scan() {
		areas := strings.Split(scanner.Text(), ",")
		elf1 := strings.Split(areas[0], "-")
		elf2 := strings.Split(areas[1], "-")

		start1, _ := strconv.Atoi(elf1[0])
		end1, _ := strconv.Atoi(elf1[1])
		start2, _ := strconv.Atoi(elf2[0])
		end2, _ := strconv.Atoi(elf2[1])

		if (start1 <= start2 && end1 >= end2) || (start2 <= start1 && end2 >= end1) {
			overlaps++
		}

		//Part II
		if start2 <= end1 && start1 <= end2 {
			overlaps2++
		}
	}
	fmt.Printf("Number of total overlaps: %d\n", overlaps)
	fmt.Printf("Number of partial overlaps: %d\n", overlaps2)
}
