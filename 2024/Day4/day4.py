#Day 4

with open('day4.padding', 'w') as file: file.write('')

with open('day4_input.txt', 'r') as file:
    for line in file:
        line = '*' + line.strip('\n') + '*\n'
        length = len(line)
        with open('day4.padding', 'a') as padding:
            padding.write(line)

with open('day4.padding', 'r') as file: content = file.readlines()

content.insert(0, '*'*(int(len(content[2]))-1) + '\n')
content.append('*'*(int(len(content[2]))-1))

with open('day4.padding', 'w') as file: file.writelines(content)

counter = 0

pattern = [-length-1, -length, -length+1, -1, 1, length-1, length, length+1]

array = []
with open('day4.padding', 'r') as file:
    padded_content = file.readlines()

    for i in range (0, len(padded_content)):
        for n in range (0, len(padded_content[i])):
            array.append(padded_content[i][n])
    for m in range(0, len(array)):
        if array[m] == 'X':
            for h in range(0,8):
                if (array[m-pattern[h]] == 'M' and array[(m-pattern[h])-pattern[h]] == 'A' and array[((m-pattern[h])-pattern[h])-pattern[h]] == 'S'):
                    counter += 1

print(counter)  #Answer part I

#Part II
ans = 0
pattern.pop(1); pattern.pop(2); pattern.pop(2); pattern.pop(3)  #New pattern
print(pattern)
for t in range(0, len(array)):
    a_counter = 0
    if array[t] == 'A':
        for h in range(0,4):
            if array[t-pattern[h]] == 'M' and array[t+pattern[h]] == 'S': a_counter += 1;  
        if a_counter == 2:
            ans += 1
            print('XMAS')

print(ans)    #Answer part II