#Day 6 new appraoch
import os
import time

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
        return (guard[0], guard[1], turn_right[guard[2]], 0)
    else:
        return (new_y, new_x, guard[2])



def write_map(guard_pos, map):
    map[guard_pos[0]][guard_pos[1]] = guard_pos[2]
    return map


def check_obstacle(guard_pos, map):
    diff_y, diff_x = move[turn_right[guard_pos[2]]]
    new_y, new_x = diff_y+guard_pos[0], diff_x+guard_pos[1]
    tmp_y, tmp_x = move[guard_pos[2]]

    if map[new_y][new_x] == turn_right[guard_pos[2]]: #or map[new_y][new_x] == turn_right[turn_right[guard_pos[2]]]:
        map[guard_pos[0]+tmp_y][guard_pos[1]+tmp_x] = 'O'
        for line in map:
            print(''.join(line))
        #print(new_y, new_x)
        print(guard_pos[0]+tmp_y, guard_pos[1]+tmp_x)
        return 1
    
    elif map[new_y][new_x] in turn_right and (map[new_y+diff_y][new_x+diff_x] == '#' or map[new_y+diff_y][new_x+diff_x] == turn_right[guard_pos[2]]):
        map[guard_pos[0]+tmp_y][guard_pos[1]+tmp_x] = 'O'
        for line in map:
            print(''.join(line))
        #print(new_y, new_x)
        print(guard_pos[0]+tmp_y, guard_pos[1]+tmp_x)
        return 1

    else: return 0

def main():

    content = []
    pos = ()
    counter = 0
    obstacle_counter = 0
    
    with open('day6.test', 'r') as file:
        for line in file:
            l = line.strip('\n')
            content.append(list(l))
            for n in range(0, len(line)):
                if line[n] in move:
                    pos = (content.index(list(l)), n, line[n])
    guard = pos

    while True:
        try:
            obstacle_counter += check_obstacle(guard, content)
 
            guard = do_move(guard=guard, map=content)
        except IndexError:
            break
        content = write_map(guard, content)

        #os.system('clear')
        
        #for line in content:
        #    print(''.join(line))

        #print(check_obstacle(guard, content))

        #print(obstacle_counter)
        
        #time.sleep(2.0)   

    for i in content:
        for j in i:
            if j in move:
                counter += 1
    
    print('Part 1:', counter)
    print('Possible places for obstacles:', obstacle_counter)
    
    

if __name__ == "__main__":
    main()