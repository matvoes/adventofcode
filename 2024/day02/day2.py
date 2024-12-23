#Day 2

with open('rejects.txt', 'w') as file: file.write('')

with open('day2_input.txt', 'r') as file:
    
    valid_lines = 0

    for line in file:
        line = [int(n) for n in line.split()]
        islinevalid = True
        delta = line[0]-line[1]

        if 0 < delta: # synkende
            for i in range(0, len(line)-1):
                if 0 < (line[i]-line[i+1]) <= 3: # synkende
                    continue
                else:
                    islinevalid = False
                    break
        elif delta < 0: #stigende
            for i in range(0, len(line)-1):
                if 0 > (line[i]-line[i+1]) >= -3:
                    continue
                else:
                    islinevalid = False
                    break
        else:
            islinevalid = False

        valid_lines += islinevalid

        if islinevalid == False:
            with open('rejects.txt', 'a') as file:
                line_string = [str(n) for n in line]
                #print(line_string)
                [file.write(n + ' ') for n in line_string]
                file.write('\n')

print('Valid lines:', valid_lines)  

#Part 2
valid_lines2 = 0

with open('rejects.txt', 'r') as file:
    for report in file:

        line = [int(n) for n in report.split()]
        line2 = [int(n) for n in report.split()]

        islinevalid = True
        altered = False

        for n in range(0, len(line)):

            line2 = [int(n) for n in report.split()]
            if altered == False:
                line2.pop(n)
            delta = line2[0]-line2[1]

            if 0 < delta: # synkende
                
                if altered==False:
                    for i in range(0, len(line2)-1):
                        if 0 < (line2[i]-line2[i+1]) <= 3: # synkende
                            islinevalid = True
                            continue
                        else:
                            islinevalid = False
                            print(line)
                            break

                if islinevalid==True:
                    break

            elif delta < 0: #stigende
                    #line2 = [int(n) for n in report.split()]
                    #line2.pop(n)
                    #print(line2)

                if altered==False:
                    for i in range(0, len(line2)-1):
                        if 0 > (line2[i]-line2[i+1]) >= -3:
                            islinevalid = True
                            continue
                        else:
                            islinevalid = False
                            print(line)
                            break
                    if islinevalid==True:
                        break

            else:
                islinevalid = False

        valid_lines2 += islinevalid

    print('Valid lines:', valid_lines2+valid_lines)