#Day 10
import copy

neighbour = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

def check_neighbour(y, x, content, dir):
    tmp = None
    diff_y, diff_x = neighbour[dir]
    new_y, new_x = y+diff_y, x+diff_x

    if new_y > len(content) or new_y < 0 or new_x > len(content[y]) or new_x < 0: raise IndexError
    
    if int(content[new_y][new_x]) - int(content[y][x]) == 1: tmp = (new_y,new_x)

    return tmp

def trailhead(i,j,content):
    tmp = []
    tmp.append((i,j))     #add pos of 0 to list
    length = 0

    while length < len(tmp):
        y = tmp[length][0]
        x = tmp[length][1]

        for key in neighbour.keys():
            try: pos_num = check_neighbour(y, x, content, key)
            except IndexError: continue
        
            if pos_num != None:
                tmp.append(pos_num)

        length += 1
    return tmp


def mapping(zero, content):
    tmp_cont = []
    tmp_cont = copy.deepcopy(content)
    for i in range (len(content)):
        for j in range(len(content[i])):
             tmp_cont[i][j] = '*'
    for pos in zero:
        tmp_cont[pos[0]][pos[1]] = content[pos[0]][pos[1]]

    return tmp_cont



def main():
    with open('day10.input', 'r') as file: content = [list(i.strip('\n')) for i in file.readlines()]
    #[print(content[i]) for i in range(len(content))]

    valid_pos = []
    scores = []

    for i in range(len(content)):                           #for every line
        for j in range(len(content[i])):                    #for every val
            if content[i][j] == '0':                        #for every zero
                valid_pos.append(trailhead(i,j, content))

    for zero in valid_pos:
        tmp_cont = mapping(zero, content)

        #print('\n')
        #[print(i) for i in tmp_cont]
        counter = sum(i.count('9') for i in tmp_cont)
        scores.append(counter)

    print(sum(scores))


if __name__ == '__main__':
    main()