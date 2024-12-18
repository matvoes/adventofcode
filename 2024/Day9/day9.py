#Day 9

def layout_creator(disk_map):
    layout = []
    id=0
    for i in range(0, len(disk_map), 2):
        for n in range(int(disk_map[i])):
            layout.append(id)
        try:
            for k in range(int(disk_map[i+1])):
                layout.append('.')
        except: break
        id+=1
    return(layout)


def layout_sorter(original_layout):
    sorted = []
    original_layout = list(original_layout)
    first = 0
    last = len(original_layout)-1
    while first <= last:
        if type(original_layout[first]) == int:
            sorted.append(int(original_layout[first]))
            first += 1
        elif original_layout[first] == '.' and original_layout[last] != '.':
            sorted.append(int(original_layout[last]))
            first += 1
            last -= 1
        else:
            last -= 1
            continue
    return sorted


def main():
    with open('day9.input', 'r') as file: content = list(file.readline())
    layout = layout_creator(content)

    original_layout = layout_sorter(layout)
    sum = 0
    for i in range(len(original_layout)):
        sum += i*original_layout[i]
    print(sum)

if __name__ == "__main__":
    main()
