#Day15
import os

wall = '#'
robot_char = '@'
hinder = 'O'
free_space = '.'

move_dir = {
    '^': (-1, 0),
    'v': (1, 0),
    '>': (0, 1),
    '<': (0, -1)
}

def find_robot(my_map):
    robotFound = False
    for y in range(len(my_map)):
        for x in range(len(my_map[y])):
            if my_map[y][x] == robot_char: robotFound = True; break
        if robotFound == True: break
    return (y, x)


def do_move(character_place, character, my_map, direction):

    while True:
        next_space, next_space_char = check_next_space(character_place, my_map, direction)#; print('next space:', next_space)

        if next_space_char == wall:
            update_status = 0
            break
        elif next_space_char == free_space:
            my_map, update_status = update_map(character_place, next_space, my_map, character)
            character_place = next_space
            break

        elif next_space_char == hinder:
            hinder_place = next_space
            hinder_place, update_status = do_move(hinder_place, hinder, my_map, direction)
            if update_status == 0:
                break

        else:
            raise AttributeError

    return character_place, update_status




def update_map(previous_place, next_place, my_map, character):
    my_map[previous_place[0]][previous_place[1]] = '.'
    my_map[next_place[0]][next_place[1]] = character
    update_status = 1

    return my_map, update_status

def check_next_space(robot, my_map, direction):
    next_space = [i+j for i,j in zip(robot, move_dir[direction])]
    next_space_char = my_map[next_space[0]][next_space[1]]
    return next_space, next_space_char

def find_all_hinders(my_map):
    all_hinders = []
    for i in range (len(my_map)):
        for j in range(len(my_map[i])):
            if my_map[i][j] == 'O':
                all_hinders.append((i, j))
    return all_hinders

def main():
    my_map = []
    move_list = []
    separator_line = False

    #interpret input
    with open('day15.input', 'r') as f:
        for line in f:
            if separator_line == True: move_list.append(line.strip())
            elif line.strip() == '': separator_line = True
            else: my_map.append(list(line.strip()))
    move_list=''.join(move_list)
    print(move_list)
    print(type(move_list))
    robot = find_robot(my_map)                          #find robot first time

    for i in move_list:
        os.system('clear')
        print(i)                                        #Print move instruction
        for j in my_map: print(j)                       #Print map
        robot, update_status = do_move(robot, robot_char, my_map, i)
        print()

    os.system('clear')
    for i in my_map: print(i)

    hinder_list = find_all_hinders(my_map)
    print(hinder_list)
    sum = 0
    for i in hinder_list:
        sum += 100*i[0]+i[1]

    print('Answer is:', sum)

if __name__ == '__main__': main()