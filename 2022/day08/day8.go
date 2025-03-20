package main

import (
	"bufio"
	"fmt"
	"os"
	"slices"
)

func main() {

	file, err := os.Open("day8.test")
	if err != nil {
		fmt.Printf("Error opening file: %v\n", err)
		return
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)

	verticalTrees := make(map[int][]int)
	result := make(map[int][]int)
	var indexCounter int

	for scanner.Scan() {
		var correctSlice []int
		var reversedSlice []int

		line := scanner.Text()        //take input line
		correctSlice = strToInt(line) //parse chars to ints

		addToVertical(correctSlice, verticalTrees)

		reversedSlice = append(reversedSlice, correctSlice...) //deepcopy line
		slices.Reverse(reversedSlice)                          //reverse line

		correctSlice = checkTreeline(correctSlice)   //find visible trees
		reversedSlice = checkTreeline(reversedSlice) //find visible trees

		correctSlice = combineTreelines(correctSlice, reversedSlice) //combine the lists of visible trees

		result[indexCounter] = correctSlice
		indexCounter++

	}

	for index := range verticalTrees {
		correctVertical := verticalTrees[index]
		var reversedVertical []int
		reversedVertical = append(reversedVertical, correctVertical...)
		slices.Reverse(reversedVertical)

		correctVertical = checkTreeline(correctVertical)
		reversedVertical = checkTreeline(reversedVertical)

		correctVertical = combineTreelines(correctVertical, reversedVertical)

		combineHorVeritcal(index, correctVertical, result)
	}

	//Print solution
	var notZeroCounter int
	for _, v := range result { // count visible trees
		for _, v2 := range v {
			if v2 != 0 {
				notZeroCounter += 1
			}
		}
	}
	fmt.Printf("Visible trees: %d\n", notZeroCounter)

	for i, v := range result {
		fmt.Println(i, v)
	}
}

//Functions

func strToInt(str string) []int {
	var ints []int

	for _, s := range str {
		num := s - '0'                //rune to correct int value, given its a number 0-9
		ints = append(ints, int(num)) //runt to int
	}
	return ints
}

func checkTreeline(trees []int) []int {
	max := -1
	for index := range trees {
		if trees[index] > max { //if taller than all the prev
			max = trees[index] //this is now the tallest tree in this dir
			trees[index] = 1   // set value as 1 for visible in this dir
		} else {
			trees[index] = 0 //else not visible in this dir
		}
	}
	return trees
}

func combineTreelines(trees, treesRev []int) []int {
	slices.Reverse(treesRev) //get both slies "same way"

	for index := range trees {
		trees[index] = trees[index] + treesRev[index] //combine values, visible in a dir if > 0
	}
	return trees
}

func addToVertical(trees []int, verticalTrees map[int][]int) {
	for index, value := range trees {
		verticalTrees[index] = append(verticalTrees[index], value) //make map of "vertical lines"
	}
}

func combineHorVeritcal(realIndex int, vertical []int, result map[int][]int) {
	for index, value := range result {
		value[realIndex] += vertical[index] //per result line add the corresponding vertical value
	}
}
