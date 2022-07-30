from utils import *

def dfs(S):
    open = [(S, None)]
    closed = []
    safety_count = 1000
    while len(open) != 0:
        safety_count -= 1
        nodePair = open[0]
        N, _ = nodePair
        print('attempting goal test for ', N)
        if(GoalTest(N)):
            return ReconstructPath(nodePair, closed)
        else:
            closed.insert(0, nodePair)
            neighbors = MoveGen(N)
            newNodes = RemoveSeen(neighbors, open, closed)
            newPairs = list(zip(newNodes, [N]*len(newNodes)))
            print('open was ', open, ' adding ', newPairs)
            open = newPairs + open[1:]
            print('now open is ', open)
        if(safety_count <= 0):
            print('safety exceeded: closed {} nodes'.format(len(closed)))
            break
    return []
