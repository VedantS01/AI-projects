from utils import *
def db_dfs_1(S, depthBound):
    count = 0
    open = [(S, None, 0)]
    closed = []
    while len(open) != 0:
        nodePair = open[0]
        N, _, depth = nodePair
        if(GoalTest(N)):
            return count, ReconstructPath2(nodePair, closed)
        else:
            closed.insert(0, nodePair)
            if(depth < depthBound):
                neighbors = MoveGen(N)
                newNodes = RemoveSeen(neighbors, open, closed)
                newPairs = list(zip(newNodes, [N]*len(newNodes), [depth+1]*len(newNodes)))
                open = newPairs + open[1:]
                count += len(newPairs)
            else:
                open = open[1:]
    return count, []

def dfid1(S):
    count = -1
    path = []
    depthBound = 0
    while(True):
        previousCount = count
        count, path = db_dfs_1(S, depthBound)
        depthBound += 1
        if(len(path) != 0 or previousCount == count):
            break
    return path