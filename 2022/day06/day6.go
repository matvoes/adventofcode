package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	messageMarker := 14 //Edit this for part II

	file, err := os.Open("day6.input")
	if err != nil {
		fmt.Printf("Error opening file: %v\n", err)
		return
	}
	defer file.Close()

	scanner := bufio.NewReader(file)

	myVars := make(map[int]rune)

	//Is it needed??
	for i := 1; i < 4; i++ { // initialize empty variables
		myVars[i] = 32
	}

	counter := 1 //to always assign index 1-x

	//Initialize first x chars
	for counter <= messageMarker {
		ch, _, err := scanner.ReadRune()
		if err != nil {
			break
		}

		myVars[counter] = ch //change value of next index
		counter++
	}

	counter = 1
	mainCounter := messageMarker

	for {
		ch, _, err := scanner.ReadRune()
		if err != nil {
			break
		}

		var res bool

		//Check if different
		for i := 1; i < messageMarker; i++ { //check the first x-1 against the others
			for index := range myVars {
				if res {
					break
				} else if index != i { //font check against itself
					res = myVars[i] == myVars[index]
				}
			}

		}

		if !res {
			for index := range myVars {
				fmt.Print(string(myVars[index]), " ")
			}
			fmt.Println(mainCounter)
			break
		}

		myVars[counter] = ch //change value of next index
		mainCounter++

		if counter == messageMarker { //to always assign index 1-x
			counter = 1
		} else {
			counter++
		}
	}
}
