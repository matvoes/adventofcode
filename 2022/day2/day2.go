package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	var words []string
	var score int
	var score2 int

	gamerules := map[string]struct {
		name  string
		value int
		beats string
		loss  string
	}{
		"X": {name: "A", value: 1, beats: "C", loss: "B"},
		"Y": {name: "B", value: 2, beats: "A", loss: "C"},
		"Z": {name: "C", value: 3, beats: "B", loss: "A"},
	}

	file, _ := os.Open("day2.input")
	defer file.Close()

	scanner := bufio.NewScanner(file)

	for scanner.Scan() {
		words = strings.Split(scanner.Text(), " ")

		//Part I
		if gamerules[words[1]].name == words[0] {
			score += (gamerules[words[1]].value + 3) //draw
		} else if gamerules[words[1]].beats == words[0] {
			score += (gamerules[words[1]].value + 6) //win
		} else {
			score += gamerules[words[1]].value //loss
		}

		//Part 2
		var choice string
		var opps_choice string

		for key, unit := range gamerules {
			if unit.name == words[0] {
				opps_choice = key
			}
		}

		if words[1] == "X" {
			choice = gamerules[opps_choice].beats //our choice
		} else if words[1] == "Y" {
			choice = words[0]
			score2 += 3
		} else {
			choice = gamerules[opps_choice].loss
			score2 += 6
		}

		for _, unit := range gamerules {
			if unit.name == choice {
				score2 += unit.value
			}
		}
	}

	fmt.Printf("Total score is: %d\n", score)
	fmt.Printf("Total score for part II is: %d\n", score2)
}
