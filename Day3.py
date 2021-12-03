diagnostics = []

with open("Day3.txt") as file:
    diagnostics = file.readlines()
    file.close()

    ##Part 1##
# first = []
# second = []
# third = []
# fourth = []
# fifth = []
# sixth = []
# seventh = []
# eighth = []
# ninth = []
# tenth = []
# eleventh = []
# twelfth = []

# for log in diagnostics:
    # first.append(log[0])
    # second.append(log[1])
    # third.append(log[2])
    # fourth.append(log[3])
    # fifth.append(log[4])
    # sixth.append(log[5])
    # seventh.append(log[6])
    # eighth.append(log[7])
    # ninth.append(log[8])
    # tenth.append(log[9])
    # eleventh.append(log[10])
    # twelfth.append(log[11])

# gamma = 0
# epsilon = 0
# one = 0
# zero = 0

# for digit in first:
    # if digit == '1':
        # one += 1
    # else:
        # zero += 1

# if one > zero:
    # gamma += 2048
# else:
    # epsilon += 2048

# one = 0
# zero = 0

# for digit in second:
    # if digit == '1':
        # one += 1
    # else:
        # zero += 1

# if one > zero:
    # gamma += 1024
# else:
    # epsilon += 1024

# one = 0
# zero = 0

# for digit in third:
    # if digit == '1':
        # one += 1
    # else:
        # zero += 1

# if one > zero:
    # gamma += 512
# else:
    # epsilon += 512
    
# one = 0
# zero = 0    

# for digit in fourth:
    # if digit == '1':
        # one += 1
    # else:
        # zero += 1

# if one > zero:
    # gamma += 256
# else:
    # epsilon += 256
    
# one = 0
# zero = 0

# for digit in fifth:
    # if digit == '1':
        # one += 1
    # else:
        # zero += 1

# if one > zero:
    # gamma += 128
# else:
    # epsilon += 128
    
# one = 0
# zero = 0

# for digit in sixth:
    # if digit == '1':
        # one += 1
    # else:
        # zero += 1

# if one > zero:
    # gamma += 64
# else:
    # epsilon += 64
    
# one = 0
# zero = 0

# for digit in seventh:
    # if digit == '1':
        # one += 1
    # else:
        # zero += 1

# if one > zero:
    # gamma += 32
# else:
    # epsilon += 32
    
# one = 0
# zero = 0

# for digit in eighth:
    # if digit == '1':
        # one += 1
    # else:
        # zero += 1

# if one > zero:
    # gamma += 16
# else:
    # epsilon += 16
    
# one = 0
# zero = 0

# for digit in ninth:
    # if digit == '1':
        # one += 1
    # else:
        # zero += 1

# if one > zero:
    # gamma += 8
# else:
    # epsilon += 8
    
# one = 0
# zero = 0

# for digit in tenth:
    # if digit == '1':
        # one += 1
    # else:
        # zero += 1

# if one > zero:
    # gamma += 4
# else:
    # epsilon += 4
    
# one = 0
# zero = 0

# for digit in eleventh:
    # if digit == '1':
        # one += 1
    # else:
        # zero += 1

# if one > zero:
    # gamma += 2
# else:
    # epsilon += 2
    
# one = 0
# zero = 0

# for digit in twelfth:
    # if digit == '1':
        # one += 1
    # else:
        # zero += 1

# if one > zero:
    # gamma += 1
# else:
    # epsilon += 1
    
# print(gamma*epsilon)

    ##Part2##

def mostCommon(logs,digit):
    ones = 0
    zeros = 0
    for log in logs:
        if log[digit] == '1':
            ones += 1
        else:
            zeros += 1
    if ones < zeros:
        return '0'
    else:
        return '1'

O2list = diagnostics.copy()
CO2list = diagnostics.copy()
O2rating = 0
CO2rating = 0

i = 0

while i < 12:
    #print(i)
    if len(O2list) == 1:
        break
    most = mostCommon(O2list,i)
    j = len(O2list)-1
    while j >= 0:
        if O2list[j][i] != most:
            O2list.pop(j)
        j -= 1
    i +=1

O2rating = int(O2list[0],2)

i = 0
while i < 12:
    if len(CO2list) == 1:
        break
    most = mostCommon(CO2list,i)
    j = len(CO2list)-1
    while j >= 0:
        if CO2list[j][i] == most:
            CO2list.pop(j)
        j -= 1
    i +=1

CO2rating = int(CO2list[0],2)

print(O2rating*CO2rating)
