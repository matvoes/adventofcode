#Day12

direction = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

def check_direction(y, x, content, dir):
    diffy, diffx = direction[dir]
    newy, newx = y+diffy, x+diffx

    if len(content)-1 < newy or newy < 0 or len(content[y])-1 < newx or newx < 0:
        return 1
    elif content[y][x] == content[newy][newx]:
        return 0
    else: return 1


def assign_group_identifiers(array_2d):
    rows, cols = len(array_2d), len(array_2d[0])
    group_id = 1
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    group_map = [[0 for _ in range(cols)] for _ in range(rows)]
    
    def dfs(x, y, letter):
        if x < 0 or x >= rows or y < 0 or y >= cols or visited[x][y] or array_2d[x][y] != letter:
            return
        visited[x][y] = True
        group_map[x][y] = group_id
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            dfs(x + dx, y + dy, letter)
    
    for i in range(rows):
        for j in range(cols):
            if not visited[i][j]:  # New group found
                dfs(i, j, array_2d[i][j])
                group_id += 1
    
    return group_map


def main():
    with open('day12.input', 'r') as f: c = f.readlines()
    c = [list(line.strip('\n')) for line in c]
    [print(i) for i in c]

    group_map = assign_group_identifiers(c)
    print('Group map:')
    for row in group_map:
        print(row)

    group_flat = [item for row in group_map for item in row]    #Flatten after sorting in groups

    total_fence = {}
    for item in set(group_flat):                                #Create dict containing all group ID's
        total_fence[item] = 0

    for i in range(len(group_map)):                             #for every line
        for j in range(len(group_map[i])):                      #for every letter
            fence = 0
            for key in direction.keys():
                fence += check_direction(i, j, group_map, key)  #check all four directions and put fence where needed
            total_fence[group_map[i][j]] += fence               #add fence value to the group fence

    counter = 0
    for unique in total_fence:                                  #count appearance of the group id (area)
        counter += group_flat.count(unique)*total_fence[unique] #and multiply by fence length for group
    print(counter)                                              #sum all in counter
                

if __name__ == '__main__': main()