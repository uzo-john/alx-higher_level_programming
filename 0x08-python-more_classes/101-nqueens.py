#!/usr/bin/python3
"""
the N queens puzzle is the challenge of placing N non-attacking queens
this program will solves the queens problem
"""
from sys import argv

if __name__ == "__main__":
    a = []
    if len(argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    if argv[1].isdigit() is False:
        print("N must be a number")
        exit(1)
    N = int(argv[1])
    if N < 4:
        print("N must be at least 4")
        exit(1)

    # initialize the answer list
    for i in range(N):
        a.append([i, None])

    def already_exists(y):
        """check whether the queen exist already in y value"""
        for x in range(N):
            if y == a[x][1]:
                return True
        return False

    def reject(x, y):
        """To check whether the solution is rejected or not"""
        if (already_exists(y)):
            return False
        i = 0
        while(i < x):
            if abs(a[i][1] - y) == abs(i - x):
                return False
            i += 1
        return True

    def clear_a(x):
        """answers from the point of failure on"""
        for i in range(x, n):
            a[i][1] = None

    def nqueens(x):
        """recursive backtracking function to find the solution"""
        for y in range(N):
            clear_a(x)
            if reject(x, y):
                a[x][1] = y
                if (x == N - 1):  # accepts the solution
                    print(a)
                else:
                    nqueens(x + 1)  # moves on to next x value to continue

    # start the recursive process at x = 0
    nqueens(0)
