package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

func main() {

	file, err := os.Open("day5.input")
	if err != nil {
		fmt.Printf("Error opening file: %v\n", err)
		return
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)

	crates := make(map[int][]string) //map for holding crates

	//Deal with crates initially
	for scanner.Scan() {
		line := scanner.Bytes()

		if len(line) == 0 {
			break
		}
		for i := 1; i < len(line); i += 4 {
			if line[i] > 65 {
				crates[i/4+1] = append(crates[i/4+1], string(line[i])) //add crates to correct index in map
			}
		}
	}
	for _, chars := range crates {
		reverseSlice(chars) //reverse order so bottom crate is at beginning of slice
	}
	crates_copy := deepCopyMap(crates)

	//Move crates
	for scanner.Scan() { //for each move instruction
		lineSlice := strings.Split(scanner.Text(), " ")
		move, _ := strconv.Atoi(lineSlice[1])
		from, _ := strconv.Atoi(lineSlice[3])
		to, _ := strconv.Atoi(lineSlice[5])

		for i := 0; i < move; i++ {
			crates[to] = append(crates[to], crates[from][len(crates[from])-1]) //move a crate from last of a stack to other stack
			crates[from] = crates[from][:len(crates[from])-1]                  //remove moved crates from last pos
		}

		//Part II move crates

		for i := move; i > 0; i-- {
			crates_copy[to] = append(crates_copy[to], crates_copy[from][len(crates_copy[from])-i])
		}
		crates_copy[from] = crates_copy[from][:len(crates_copy[from])-move]
	}

	//Sort and print last crates in correct order
	keys := make([]int, 0, len(crates))

	for index := range crates {
		keys = append(keys, index)
	}
	sort.Ints(keys)

	fmt.Print("Solution part 1 is: ")
	for _, index := range keys {
		fmt.Print(crates[index][len(crates[index])-1], " ")
	}

	keys_part2 := make([]int, 0, len(crates_copy))

	fmt.Print("\nSolution part 2: ")

	for index := range crates_copy {
		keys_part2 = append(keys_part2, index)
	}
	sort.Ints(keys_part2)

	for _, index := range keys_part2 {
		fmt.Print(crates_copy[index][len(crates_copy[index])-1], " ")
	}

	fmt.Println()

}

func reverseSlice(s []string) {
	for i, j := 0, len(s)-1; i < j; i, j = i+1, j-1 {
		s[i], s[j] = s[j], s[i]
	}
}

func deepCopyMap(original map[int][]string) map[int][]string {
	new_copy := make(map[int][]string, len(original))
	for key, value := range original {
		new_copy[key] = make([]string, len(value))
		copy(new_copy[key], value)
	}
	return new_copy
}
