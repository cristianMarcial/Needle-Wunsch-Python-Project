MATCH_SCORE = 1
MISMATCH_SCORE = -1
GAP_SCORE = -2

output1 = ''
output2 = ''

def S(a, b):
    return MATCH_SCORE if a == b else MISMATCH_SCORE

def generateGrid():
    grid = [[0]]

    # Initialization step
    index = 1
    for i in sequence1:
        grid[0].append(GAP_SCORE*index)
        index+=1

    index = 1
    for j in sequence2:
        grid.append([GAP_SCORE*index])
        index+=1

    # Filling the grid
    y = 0
    for j in sequence2:
        x = 0
        y+=1
        for i in sequence1:
            x+=1
            grid[y].append(max(grid[y-1][x-1] + S(i,j), grid[y-1][x] + GAP_SCORE, grid[y][x-1] + GAP_SCORE))
    
    return grid

def backtrackingHelper(x, y):
    global output1, output2
    if x >= 0 and y >= 0:
        diag = grid[y][x] + S(sequence1[x], sequence2[y])
        up = grid[y+1][x] + GAP_SCORE
        left = grid[y][x+1] + GAP_SCORE

        if diag > up and diag > left:
            output1 = sequence1[x] + output1
            output2 = sequence2[y] + output2
            backtrackingHelper(x-1, y-1)
        else:
            if diag < up:
                output1 = sequence1[x] + output1
                output2 = '-' + output2
                backtrackingHelper(x-1, y)
            elif diag == up:
                if grid[y][x-1] > grid[y-1][x-1]:
                    output1 = sequence1[x] + output1
                    output2 = '-' + output2
                    backtrackingHelper(x-1, y)
                else:
                    output1 = sequence1[x] + output1
                    output2 = sequence2[y] + output2
                    backtrackingHelper(x-1, y-1)
            elif diag < left:
                output1 = '-' + output1
                output2 = sequence2[y] + output2
                backtrackingHelper(x, y-1)
            elif diag == left:
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

def printOutput(inputText):
    global sequence1, sequence2, grid, output1, output2
    sequence1 = inputText[0]
    sequence2 = inputText[1]
    grid = generateGrid()
    backtracking(len(sequence1), len(sequence2))
    print(output1, output2, grid[-1][-1])
    output1 = output2 = ''