#Day 7
import re

def custom_eval(expression):
    tokens = re.findall(r'\d+|[+\-*/]', expression)
    tmp = int(tokens[0])
    for i in range(len(tokens)):
        if tokens[i] == '+':
            tmp += int(tokens[i+1])
        elif tokens[i] == '*':
            tmp *= int(tokens[i+1])
    return tmp



def main():
    with open('day7.input', 'r') as file:
        content = file.readlines()
    counter = 0

    for line in content:
        #print('the line is', line)
        x = line.strip('\n').split(' ')
        sum = int(x[0].strip(':')); x.pop(0)

        result ='+'.join(x)

        valid_flag = (sum == custom_eval(result))
        

        if not valid_flag:
            for i in range(len(result)):
                result_copy = str(result)       #only +'s
                if result_copy[i] == '+': 
                    result_copy = result_copy[:i] + '*' + result_copy[i+1:]     #change a + to *
                    valid_flag = (sum == custom_eval(result_copy))     #check if valid

                if not valid_flag:
                    for j in range(i+1, len(result)):
                        #print(result_copy)
                        if result_copy[j] == '+': result_copy = result_copy[:j] + '*' + result_copy[j+1:]
                        valid_flag = (sum == custom_eval(result_copy))     #check if valid
                        #print(result_copy, '=', custom_eval(result_copy))
                        if valid_flag: break
                if valid_flag: break
        if valid_flag: counter += sum

        if valid_flag: print('sum is', sum)    
        if valid_flag: print('Flag is', valid_flag)
        if valid_flag: print(result_copy, '=', custom_eval(result_copy), '\n')

    print(counter)





if __name__ == "__main__": main()