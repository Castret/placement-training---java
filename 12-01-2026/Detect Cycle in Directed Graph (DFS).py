
def cycle(g):
    v=set()
    r=set()
    def dfs(u):
        v.add(u)
        r.add(u)
        for x in g[u]:
            if x not in v:
                if dfs(x): return True
            elif x in r:
                return True
        r.remove(u)
        return False
    return any(dfs(i) for i in g if i not in v)

g={0:[1],1:[2],2:[0],3:[4],4:[]}
print(cycle(g))
