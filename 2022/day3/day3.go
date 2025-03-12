package main

import (
	"bufio"
	"fmt"
	"os"
	"slices"
)

func deal_with_number(letter byte) int {
	value := int(letter)

	if letter >= 'A' && letter <= 'Z' {
		value = value - 65 + 27
	} else if letter >= 'a' && letter <= 'z' {
		value = value - 97 + 1
	}
	return value
}

func solve_common(letter1, letter2, letter3 []byte) byte {
	var tmp []byte

	uniqueMap := make(map[byte]bool)
	var uniqueSlice []byte

	for _, val := range letter1 {
		if !uniqueMap[val] {
			uniqueMap[val] = true
			uniqueSlice = append(uniqueSlice, val)
		}
	}

	for i := 0; i < len(letter2); i++ {
		if slices.Contains(uniqueSlice, letter2[i]) {
			tmp = append(tmp, letter2[i])

		}
	}

	for j := 0; j < len(letter3); j++ {
		if slices.Contains(tmp, letter3[j]) {
			return letter3[j]
		}
	}
	return 0
}

func main() {
	var main_score, main_score_2, group_three_counter int
	var line1, line2, line3 []byte

	file, err := os.Open("day3.alt2")
	if err != nil {
		fmt.Printf("Error opening file: %v\n", err)
		return
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)

	for scanner.Scan() {
		line := scanner.Bytes()
		line_length := len(line)
		var1 := line[:line_length/2]
		var2 := line[line_length/2:]

		var score int

		for i := 0; i < len(var1); i++ {
			for j := 0; j < len(var2); j++ {
				if var1[i] == var2[j] {
					score += deal_with_number(var1[i])
					break
				}
			}
			if score != 0 {
				main_score += score
				break
			}
		}
		//fmt.Printf("Sum line is: %d\n", score)

		//Part II

		if group_three_counter == 0 {
			line1 = line
			group_three_counter++
		} else if group_three_counter == 1 {
			line2 = line
			group_three_counter++
		} else {
			line3 = line
			this_group := solve_common(line1, line2, line3)
			main_score_2 += deal_with_number(this_group)
			group_three_counter = 0
		}
	}

	fmt.Printf("Total sum of errors: %d\n", main_score)
	fmt.Printf("Total sum of badges: %d\n", main_score_2)
}
