#Scoring matrix values [[0, -2, -4, -6, -8, -10], [-2, 1, -1, -3, -5, -7], [-4, -1, 0, 0, -2, -4], [-6, -3, -2, -1, 1, -1], [-8, -5, -2, -3, -1, 2]]
MATCH_SCORE = 1
MISMATCH_SCORE = -1
GAP_SCORE = -2

def S(a, b):
    return MATCH_SCORE if a == b else MISMATCH_SCORE

def path(a, b, c):
    #recursive
    pass

def generateGrid(s1, s2):
    grid = [[0]]

    #Initialization step
    index = 1
    for i in s1:
        grid[0].append(GAP_SCORE*index)
        index+=1

    index = 1
    for j in s2:
        grid.append([GAP_SCORE*index])
        index+=1

    #Filling the grid
    y = 0
    for j in s2:
        x = 0
        y+=1
        for i in s1:
            x+=1
            grid[y].append(max(grid[y-1][x-1] + S(i,j), grid[y-1][x] + GAP_SCORE, grid[y][x-1] + GAP_SCORE))
    
    return grid

def printGrid(g):
    for i in g:
        print(i)

def printOutput(inputText):
    s1 = inputText[0]
    s2 = inputText[1]
    grid = generateGrid(s1,s2)
    score = grid[-1][-1]

    #
    printGrid(grid)
    print('######')

    #print(s2)