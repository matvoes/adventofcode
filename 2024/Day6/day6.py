#Day 6
import re

with open('day6.mod', 'w') as file: file.write('')

with open('day6.test', 'r') as file:
    content = file.readlines()

class caret:    #^
    direction = 'up'
    value = '\^'

class r_croc:   #>
    direction = 'right'
    value = '\>'

class l_croc:   #<
    direction = 'left'
    value = '\<'

class v:        #v
    direction = 'down'
    value = 'v'

#for i in range (0,len(content)):
for line in content:
    x = re.search('\^|\>|\<|v', line)

    if x:
        line_no = content.index(line)
        char_no = x.start()
        symbol = x.group()

        if symbol == '^':
            print(caret.direction)

        print(content[line_no-1])
        print(line)
        print(line_no, char_no)

        #print(type(line_no), type(char_no))
        #print(type(content[line_no-1][char_no]))

        tmp = list(content[line_no-1])
        tmp[char_no] = symbol
        print(tmp)
        print(content[line_no-1])
        #content[line_no-1][char_no] = symbol
        tmp2 = list(content[line_no])
        tmp2[char_no] = '.'
        #print(v.direction)
    
    with open('day6.mod', 'a') as file:
        #if x: file.write(tmp)
        file.write(line)