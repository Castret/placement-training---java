
def solve(b):
    for i in range(9):
        for j in range(9):
            if b[i][j]==0:
                for k in range(1,10):
                    if k not in b[i] and k not in [b[x][j] for x in range(9)] and k not in [b[x][y] for x in range(i//3*3,i//3*3+3) for y in range(j//3*3,j//3*3+3)]:
                        b[i][j]=k
                        if solve(b): return True
                        b[i][j]=0
                return False
    return True
