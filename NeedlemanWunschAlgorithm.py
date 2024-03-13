
MATCH_SCORE = 1
MISMATCH_SCORE = -1
GAP_SCORE = -2

grid = []

def S(a, b):
    return MATCH_SCORE if a == b else MISMATCH_SCORE

def generateGrid(s1, s2):
    #Initialization step
    firstRow = [0]

    index = 1
    for i in s1:
        firstRow.append(GAP_SCORE*index)
        index+=1
    grid.append(firstRow)

    index = 1
    for j in s2:
        grid.append([GAP_SCORE*index])
        index+=1

    #Filling the grid
    
    index = 1
    for j in s2:
        for i in s1:
            grid[index].append(max(5,7))

def printOutput(inputText):
    s1 = inputText[0]
    s2 = inputText[1]
    score = 0

    generateGrid(s1,s2)

    print(grid)