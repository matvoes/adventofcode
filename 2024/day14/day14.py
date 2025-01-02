#Day14
import re


map_width = 101
map_length = 103


def clean_initial_pos(line):
    values = re.findall(r'-?\d+', line)
    values = [int(i) for i in values]
    pos = (values[0], values[1])
    vel = (values[2], values[3])
    return [pos, vel]


def do_move(pos, vel):

    x, y = pos[0] + vel[0], pos[1] + vel[1]

    if x < 0: x += map_width
    elif x >= map_width: x -= map_width 
    if y < 0: y += map_length
    elif y >= map_length: y -= map_length

    return (x, y)


def make_map(real_map, robot):
    real_map[robot[1]][robot[0]] += 1
    return real_map

def unmake_map(real_map, old_robot):
    real_map[old_robot[1]][old_robot[0]] -= 1
    return real_map

def sum_quadrant(pos, real_map):
    counter = 0
    for i in range(pos[2],pos[3]):
        for j in range(pos[0], pos[1]):
            counter += real_map[i][j]
            #print(real_map[i][j], i, j)
    return counter

def main():
    with open('day14.input', 'r') as f: c = f.readlines()
    #c = ["p=2,4 v=2,-3"]

    og_map = [list('0'*(map_width)) for i in range(0, map_length)]    #make empty map
    og_map = [[int(char) for char in line] for line in og_map]      #all int's
    #for l in og_map: print(l)

    robots = []
    #initialize map
    for l in c: 
        init_robot = clean_initial_pos(l)
        robots.append(init_robot)
        real_map = make_map(og_map, init_robot[0])

    #print()
    #for i in real_map:print(i)
    

    #move robots
    for i in range(100):
        for r in range(0,len(robots)):
            real_map = unmake_map(real_map, robots[r][0])
            robots[r][0] = do_move(robots[r][0], robots[r][1])
            real_map = make_map(real_map, robots[r][0])

        #print()
        #for i in real_map:print(i)

    #quadrants
    q1 = (0, map_width//2, 0, map_length//2)
    q2 = (0, map_width//2, map_length//2+1, map_length)
    q3 = (map_width//2+1, map_width, 0, map_length//2)
    q4 = (map_width//2+1, map_width, map_length//2+1, map_length)

    q1 = sum_quadrant(q1, real_map)
    q2 = sum_quadrant(q2, real_map)
    q3 = sum_quadrant(q3, real_map)
    q4 = sum_quadrant(q4, real_map)

    print(q1,q2,q3,q4)
    print(q1*q2*q3*q4)

if __name__ == '__main__': main()