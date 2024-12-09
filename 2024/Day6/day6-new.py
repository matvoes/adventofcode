#Day 6 new appraoch

move = {
    '^': (-1, 0),
    '>': (0, 1),
    'v': (1, 0),
    '<': (0, -1)
}

turn_right = {
    '^': '>',
    '>': 'v',
    'v': '<',
    '<': '^'
}


def do_move(guard:tuple, map):
    diff_y, diff_x = move[guard[2]]
    new_y, new_x = (guard[0]+diff_y, guard[1]+diff_x)

    if new_y > len(map) or new_x > len(map[0]) or new_y < 0 or new_x < 0:
        raise IndexError

    if map[new_y][new_x] == '#':
        return (guard[0], guard[1], turn_right[guard[2]])
    else:
        return (new_y, new_x, guard[2])



def write_map(guard_pos, map):
    map[guard_pos[0]][guard_pos[1]] = guard_pos[2]
    return map



def main():

    content = []
    pos = ()
    counter = 0

    with open('day6.input', 'r') as file:
        for line in file:
            l = line.strip('\n')
            content.append(list(l))
            for n in range(0, len(line)):
                if line[n] in move:
                    pos = (content.index(list(l)), n, line[n])
    guard = pos

    while True:
        try:
            guard = do_move(guard=guard, map=content)
        except IndexError:
            break
        content = write_map(guard, content)

        for line in content:
            print(''.join(line))

    for i in content:
        for j in i:
            if j in move:
                counter += 1
    
    print(counter)
    

if __name__ == "__main__":
    main()