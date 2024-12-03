#Day 1
#Part 1
file = open('day1.txt', 'r')

column1 = []; column2 = []; diff = []; count = []

for line in file: column1.append(int(line.split()[0])), column2.append(int(line.split()[1]))

column2.sort(); column1.sort()

for num in range(0,len(column1)):  diff.append(abs(column2[num] - column1[num]))

print(sum(diff))

#Part 2
for num in column1: count.append(column2.count(num)*num)

print(sum(count))