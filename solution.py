
def solvepart1():
    #format data
    data = fileRead("input.txt")
    springsRows = []
    recordsRows = []
    for row in data:
        splitRow = row.split(" ")
        springsRows.append([*splitRow[0]])
        recordsRows.append([int(i) for i in splitRow[1].strip().split(",")])
    
    #find valid arrangements
    sum = 0
    for i in range(len(springsRows)):
        sum = sum + checkAllArrangements(springsRows[i], [], recordsRows[i], 0)
    print(sum)

#recursively checks all possible arrangements for a row of springs and returns the number which are valid
def checkAllArrangements(incompleteSprings,possibleSprings, record, depth):
    if (depth >= len(incompleteSprings)):
        if checkIfRowValid(possibleSprings, record):
            return 1
        else:
            return 0
    elif (incompleteSprings[depth] != "?"):
        return checkAllArrangements(incompleteSprings, possibleSprings + [incompleteSprings[depth]], record, depth+1)
    else:
        val = checkAllArrangements(incompleteSprings, possibleSprings + ["."], record, depth+1)
        val = val + checkAllArrangements(incompleteSprings, possibleSprings + ["#"], record, depth+1)
        return val

#takes in a row and a record and checks if they match
def checkIfRowValid(springs, record):
    newRecord = []
    lastRecordSpring = False
    for i in range(len(springs)):
        if (not lastRecordSpring) and (springs[i] == "#"):
            newRecord.append(1)
            lastRecordSpring = True
        elif (lastRecordSpring) and (springs[i] == "#"):
            newRecord[-1] = newRecord[-1] + 1
            lastRecordSpring = True
        elif springs[i] == ".":
            lastRecordSpring = False
    return newRecord == record

def fileRead(name):
    data = []
    f = open(name, "r")
    for line in f:
        data.append(line);
    return data

solvepart1()