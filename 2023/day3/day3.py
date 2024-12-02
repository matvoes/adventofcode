#day3
'''
f = open("day3sample.txt", "r")
numbers =[]
res = []
current_char = f.read(1)

while current_char:
    tmp = ""
    next_char = f.read(1)

    while(current_char.isdigit()):
        tmp += current_char
        current_char = next_char
        next_char = f.read(1)

    numbers.append(tmp)
    current_char = next_char
    
for ele in numbers:
    if ele.strip():
        res.append(ele)
        
print(res)
f.close()
'''
listofdoc =[]
f = open("day3sample.txt", "r")
for line in f:
    for char in line:
        listofdoc.append(char)
f.close()



symbols = ["*", "+", "#", "$"]
f = open("day3sample.txt", "r")
linecounter = 1

for line in f:
    for char in line:
        if char in symbols:
            try:
                if linecounter==1:
                    break #placeholder
                else:
                    print("char")
            except:
                continue
    
    linecounter += 1