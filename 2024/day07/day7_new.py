#Day 7 new approach
from itertools import product


def generate_combinations(length):
    symbols = ['+', '*', '|']                                                        #all symbols possible
    combinations = [''.join(comb) for comb in product(symbols, repeat=length)]
    return combinations


def custom_eval(numbers, symbols):
    tmp = int(numbers[0])
    for i in range(len(symbols)):
        if symbols[i] == '+':
            tmp += int(numbers[i+1])
        elif symbols[i] == '*':
            tmp *= int(numbers[i+1])
        elif symbols[i] == '|':
            tmp = int(str(tmp) + numbers[i+1])
    return tmp


def main():
    with open('day7.input', 'r') as file:
        content = file.readlines()
    counter = 0                                                        #counter for answer    

    for line in content:
        x = line.strip('\n').split(' ')                                 #list of numbers
        sum = int(x[0].strip(':')); x.pop(0)                            #filter out sum and remove from problem list
        length_line = len(x)-1                                          #how many places for symbols

        combinations = generate_combinations(length_line)               #generate array for all possible combinations

        valid_sum = False
        for i in combinations:                                          #do for every set of valid combinations            
            calculated_sum = custom_eval(x, i)                          #try next set of operators
            valid_sum = (sum == calculated_sum)                         #set valid flag
            if valid_sum == False: continue                             #if not valid sum
            else:
                print('Calc', calculated_sum, 'Sum', sum)
                print(i)
                counter += sum                                          #increase counter if valid
                break

    print(counter)

if __name__ == "__main__": main()