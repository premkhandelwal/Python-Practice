"""  

_ _ _ _
_ _ _ _
_ _ _ _
_ _ _ _


"""



def isColumnSafe(r, c):
    while(r >= 0):
        if(arr[r][c] == 1):
            return False
        r = r - 1
    return True


def isRightDiagonalSafe(r, c):
    while(r >= 0 and c < n1):
        if(arr[r][c] == 1):
            return False
        r = r - 1
        c += 1
    return True


def isLeftDiagonalSafe(r, c):
    while(r >= 0 and c >= 0):
        if(arr[r][c] == 1):
            return False
        r = r - 1
        c = c - 1
    return True


def isSafe(r, c):
    if(isColumnSafe(r, c) and isLeftDiagonalSafe(r, c) and isRightDiagonalSafe(r, c)):
        return True
    return False


def nQueen(r, n):
    if(r >= n):
        return True
    for c in range(n):
        if(isSafe(r, c)):
            arr[r][c] = 1
            if(nQueen(r + 1, n)):
                return True

            arr[r][c] = 0


n1 = int(input("Enter the rows: "))
print("")
arr = [[0 for x in range(n1)] for y in range(n1)]

if(nQueen(0,n1)):
    for i in range(n1):
        for j in range(n1):
            print(arr[i][j], end=" ")
        print("")    