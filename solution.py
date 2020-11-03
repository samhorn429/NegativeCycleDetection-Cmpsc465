def negCycDetect(V, E, Src):
    dist = []
    parents = []
    startArr = [None]*V
    startArr[Src-1] = 0
    for k in range(2):
        dist.append([])
        dist[k] = startArr.copy()
    for v in range(V):
        parents.append([])
    for e in range(E):
        nums = [int(x) for x in input().split()]        
        parents[nums[1] - 1].append([nums[0], nums[2]])
    for k in range(1, V+1):
        for v in range(V):
            for u in range(len(parents[v])):
                if dist[0][parents[v][u][0] - 1] == None:
                    continue
                if dist[1][v] == None or dist[1][v] > dist[0][parents[v][u][0] - 1] + parents[v][u][1]:
                    if k == V:
                        return True
                    dist[1][v] = dist[0][parents[v][u][0] - 1] + parents[v][u][1]
        dist[0] = dist[1].copy()
    return False
            
params = [int(x) for x in input().split()]
val = negCycDetect(params[0], params[1], params[2])
print(val)
