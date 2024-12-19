#Day11
import re
import copy


def rules(num):
    if int(num) == 0: num = '1'                                         #rule I
    elif len(num) % 2 == 0:                                             #rule II
        middle = len(num)//2
        num = num[:middle] + ' ' + (num[middle:].lstrip('0') or '0')    #clean leading zeroes
    else: num = int(num) * 2024                                         #rule III

    return str(num)


def main():
    with open('day11.input', 'r') as f: c = f.readline()
    tokens = re.findall(r'\d+', c)
    
    blinks = 25

    for i in range(blinks):
        tmp = []
        for num in tokens: tmp.extend(rules(num).split(' '))

        tokens = copy.deepcopy(tmp)

    print(len(tokens))

if __name__ == '__main__': main()