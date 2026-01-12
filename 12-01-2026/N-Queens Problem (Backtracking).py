
def nqueen(n):
    b=[-1]*n
    def ok(r,c):
        for i in range(r):
            if b[i]==c or abs(b[i]-c)==r-i:
                return False
        return True
    def solve(r):
        if r==n:
            print(b)
            return
        for c in range(n):
            if ok(r,c):
                b[r]=c
                solve(r+1)
    solve(0)

nqueen(8)
