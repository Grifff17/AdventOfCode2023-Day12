from cgitb import small
import time
from functools import cache

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
        val = checkAllArrangements(springsRows[i], [], recordsRows[i], 0)
        sum = sum + val
        # print("val: ", val)
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

def solvepart2():
    #format data
    data = fileRead("input.txt")
    smallSpringsRows = []
    smallRecordsRows = []
    for row in data:
        splitRow = row.split(" ")
        smallSpringsRows.append( splitRow[0] )
        smallRecordsRows.append( tuple(splitRow[1].strip().split(",")) )

    #multiply data by 5
    springsRows = []
    recordsRows = []
    for i in range(len(smallSpringsRows)):
        springsRows.append( "?".join([smallSpringsRows[i]] * 5) + ".")
        recordsRows.append( tuple(smallRecordsRows[i] * 5) )
    
    #find valid arrangements
    sum = 0
    for i in range(len(springsRows)):
        val = checkAllArrangmentsCaching(springsRows[i],recordsRows[i], 0)
        sum = sum + val 
    print(sum)

#uses caching to recursively check all possible springs efficently
#uses strings instead of arrays so caching can happen
@cache
def checkAllArrangmentsCaching(currentSpring, currentRecord, springRowLen):
    if currentSpring == "":
        if len(currentRecord) == 0 and springRowLen == 0:
            return 1
        else:
            return 0

    paths = []
    if currentSpring[0] == "?":
        paths = ["#","."]
    else:
        paths = currentSpring[0]
    
    sum = 0
    for path in paths:
        if path == "#":
            sum = sum + checkAllArrangmentsCaching(currentSpring[1:], currentRecord, springRowLen + 1)
        else:
            if springRowLen > 0:
                if len(currentRecord) > 0 and springRowLen == int(currentRecord[0]):
                    sum = sum + checkAllArrangmentsCaching(currentSpring[1:], currentRecord[1:], 0)
            else:
                sum = sum + checkAllArrangmentsCaching(currentSpring[1:], currentRecord, 0)
    return sum

def fileRead(name):
    data = []
    f = open(name, "r")
    for line in f:
        data.append(line);
    return data

start = time.time()
solvepart2()
print(time.time()-start)