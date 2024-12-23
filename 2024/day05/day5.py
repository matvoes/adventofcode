#Day 5

with open('day5.rules', 'w') as file: file.write('')    #Clean rules file
with open('day5.updates', 'w') as file: file.write('')  #Clean updates file
sum = 0
sum2 = 0

#Cleaning data and writing to seaprate rule and update files
with open('day5_input.txt', 'r') as file:

    for rules in file:
        if rules == '\n': break
        else:
            #Clean rules
            current_rule = rules.strip('\n').split('|')
            #Write rules to rules file
            with open('day5.rules', 'a') as rules_file: [rules_file.write(n + ' ') for n in current_rule]; rules_file.write('\n')

    for update in file:
        #Clean updates
        current_update = update.strip('\n').split(',')
        with open('day5.updates', 'a') as updates_file: [updates_file.write(n + ' ') for n in current_update]; updates_file.write('\n')


with open('day5.updates', 'r') as u_file:
    for update in u_file:                                               #Check every update
        current_update = update.strip('\n').split(' ')                  #Clean update
        current_update.pop(-1)
        validupdate = True                                              #Assume the update is legal
        for i in range (0, len(current_update)-1):                      #Nested loop to check every combination in the update for rules
            for n in range (1, len(current_update)-i):                  
                check = current_update[i+n] + ' ' + current_update[i]   #Swap place to see if that's a rule, if it is, the update is illegal

                with open('day5.rules', 'r') as r_file:                 
                    for rule in r_file:
                        if rule.strip(' \n') == check:                  #If the combination from update #is found in rule list
                            validupdate = False                         #Mark as invalid update
                            break                                       #Stop iteration

        if validupdate == True:
            sum += int(current_update[int(len(current_update)/2)])      #If legal sum the number in middle

#Part 2    
        else:                                                           #validupdate == False:
            while validupdate != True:
                no_error = 0
                for i in range (0, len(current_update)-1):
                    for n in range (1, len(current_update)-i):
                        check = current_update[i+n] + ' ' + current_update[i]

                        with open('day5.rules', 'r') as r_file:                 
                            for rule in r_file:
                                if rule.strip(' \n') == check:
                                    validupdate = False
                                    tmp = current_update[i+n]
                                    current_update[i+n] = current_update[i]
                                    current_update[i] = tmp
                                    no_error += 1
                                    break
                if no_error == 0:
                    validupdate = True
                    sum2 += int(current_update[int(len(current_update)/2)]) 



print('Answer 1:', sum)                                                              #Answer part 1
print('Answer 2:', sum2)

