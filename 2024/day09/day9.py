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


def find_period_section(input_list):
    sections = []
    start = None
    for i, char in enumerate(input_list):
        if char == '.':
            if start == None:
                start = i
        else:
            if start is not None:
                sections.append((start, i-1))
                start = None

    if start is not None:
        sections.append((start, len(input_list) -1))

    return sections


def new_layout_sorter(layout, max_value, list_no_periods):
    tokens = find_period_section(layout)
    no_max_value = list_no_periods.count(max_value)
    
    for match in tokens:
        start, end = match
        length = end-start+1

        if length >= no_max_value and start < layout.index(max_value):
            layout = ['.' if x == max_value else x for x in layout]
            for i in range(no_max_value):
                layout[start+i] = max_value
            break

    return layout



def main():
    with open('day9.input', 'r') as file: content = list(file.readline())
    layout = layout_creator(content)

    original_layout = layout_sorter(layout)
    part1_sum = 0
    for i in range(len(original_layout)):
        part1_sum += i*original_layout[i]
    print(part1_sum)

    #part II

    list_no_periods = [i for i in layout if i != '.']
    value = max(list_no_periods)

    while value > 1:
        layout = new_layout_sorter(layout, value, list_no_periods)
        value -= 1

    sum_value = 0
    sum_value = sum(i * int(num) for i, num in enumerate(layout) if num != '.')
    print(sum_value)



if __name__ == "__main__":
    main()
