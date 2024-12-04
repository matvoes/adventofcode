#Day 3

'''
Cleaned input with:
mul\(\d*\,\d*\)
in regex
'''
sum = 0

with open('day3_clean.txt', 'r') as file:
    for line in file: nums = line.strip('mul()\n').split(','); sum += int(nums[0])*int(nums[1])
print(sum)

#Part 2
'''
Cleaned input with:
do\(\)|don\'t\(\)|mul\(\d*\,\d*\)
in regex
'''

with open('day3_part2_clean.txt', 'r') as file:
    do = True
    sum2=0
    for line in file:
        if "don\'t" in line:
            do = False
        elif "do" in line:
            do = True
        else:
            if do == True: validnums = line.strip('mul()\n').split(','); sum2 += int(validnums[0])*int(validnums[1])
print(sum2)