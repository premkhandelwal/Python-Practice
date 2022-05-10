def isColSafe(r, c):
    while(r >= 0):
        if(arr[r][c] == 1):
            return False
        r = r - 1
    return True


def isLeftDiagSafe(r, c):
    while(r >= 0 and c >= 0):
        if(arr[r][c] == 1):
            return False
        r = r-1
        c = c-1
    return True


def isRightDiagSafe(r, c):
    while(r >= 0 and c < n1):
        if(arr[r][c] == 1):
            return False
        r = r - 1
        c = c + 1
    return True


def isSafe(r, c):
    if(isColSafe(r, c) and isLeftDiagSafe(r, c) and isRightDiagSafe(r, c)):
        return True
    return False


def nQueen(r, n):
    if(r >= n):
        return True
    for col in range(n):
        if(isSafe(r, col)):
            arr[r][col] = 1
            if(nQueen(r + 1, n)):
                return True
            arr[r][col] = 0


n1 = 4
arr = [[0 for x in range(n1)] for y in range(n1)]
nQueen(0, n1)
print(arr)
