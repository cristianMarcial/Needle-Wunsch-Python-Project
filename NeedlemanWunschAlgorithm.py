#Scoring matrix values [[0, -2, -4, -6, -8, -10], [-2, 1, -1, -3, -5, -7], [-4, -1, 0, 0, -2, -4], [-6, -3, -2, -1, 1, -1], [-8, -5, -2, -3, -1, 2]]

#Scoring matrix
MATCH_SCORE = 1
MISMATCH_SCORE = -1
GAP_SCORE = -2

output1 = ''
output2 = ''

def S(a, b):
    return MATCH_SCORE if a == b else MISMATCH_SCORE

def generateGrid():
    grid = [[0]]

    #Initialization step
    index = 1
    for i in sequence1:
        grid[0].append(GAP_SCORE*index)
        index+=1

    index = 1
    for j in sequence2:
        grid.append([GAP_SCORE*index])
        index+=1

    #Filling the grid
    y = 0
    for j in sequence2:
        x = 0
        y+=1
        for i in sequence1:
            x+=1 #ORDER: DAIGONAL, UP, LEFT
            grid[y].append(max(grid[y-1][x-1] + S(i,j), grid[y-1][x] + GAP_SCORE, grid[y][x-1] + GAP_SCORE))
    
    return grid

#Clone 1
def backtrackingHelper(x, y):
    global output1, output2
    if x >= 0 and y >= 0:
        diag = grid[y-1][x-1] + S(sequence1[x], sequence2[y]) #revision -1
        left = grid[y][x-1] + GAP_SCORE
        up = grid[y-1][x] + GAP_SCORE

        if diag >= left and diag >= up:
            output1 = sequence1[x] + output1
            output2 = sequence2[y] + output2
            backtrackingHelper(x-1, y-1)
        else:
            if diag < left:
                output1 = sequence1[x] + output1
                output2 = '-' + output2
                backtrackingHelper(x-1, y)
            elif diag == left:
                if grid[y][x-1] > grid[y-1][x-1]: # IMP O >=
                    output1 = sequence1[x] + output1
                    output2 = '-' + output2
                    backtrackingHelper(x-1, y)
                else:
                    output1 = sequence1[x] + output1
                    output2 = sequence2[y] + output2
                    backtrackingHelper(x-1, y-1)
            elif diag < up:
                output1 = '-' + output1
                output2 = sequence2[y] + output2
                backtrackingHelper(x, y-1)
            elif diag == up:
                if grid[y-1][x] > grid[y-1][x-1]:
                    output1 = '-' + output1
                    output2 = sequence2[y] + output2
                    backtrackingHelper(x, y-1)
                else:
                    output1 = sequence1[x] + output1
                    output2 = sequence2[y] + output2
                    backtrackingHelper(x-1, y-1)

def backtracking(s1, s2):
    backtrackingHelper(s1-1, s2-1)

def printGrid(g): 
    for i in g: print(i)

def printOutput(inputText):
    global sequence1, sequence2, grid, output1, output2
    sequence1 = inputText[0]
    sequence2 = inputText[1]
    grid = generateGrid()
    backtracking(len(sequence1),len(sequence2))

    # printGrid(grid)
    # print('######')
    print(output1, output2, grid[-1][-1], '\n')

    # They must delete their content in order to not acumulate
    output1 = output2 = ''