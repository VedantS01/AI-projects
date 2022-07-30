class Node:
    def __init__(self, label):
        self.data = label
        self.neighbors = []
        
    def movegen(self):
        return self.neighbors
    
    def addLink(self, childNode):
        self.neighbors.append(childNode)
        
    def __repr__(self):
        return str(self.data)
        
def MoveGen(N):
    return N.movegen()


def GoalTest(N):
    '''
    N is a node in the graph
    N.data is node label
    N.neighbors is a list of links to neighbors
    '''
    return N.data == 'G'

def ReconstructPath(nodePair, closed):
    print('start with closed = ', closed, ' node pair = ', nodePair)
    def SkipTo(parent, nodePairs):
        if(parent.data == list(nodePairs[0])[0].data):
            return nodePairs
        else:
            return SkipTo(parent, nodePairs[1:])
        
    node, parent = nodePair
    path = [node]
    while(parent != None):
        path.insert(0, parent)
        print('inserted ', parent)
        closed = SkipTo(parent, closed)
        _, parent = closed[0]
        
    return path

def ReconstructPath2(nodePair, closed):
    def SkipTo(parent, parent_depth, nodePairs):
        if(parent.data == list(nodePairs[0])[0].data and parent_depth == list(nodePairs[0])[2]):
            return nodePairs
        else:
            return SkipTo(parent, parent_depth, nodePairs[1:])
        
    node, parent, curr_depth = nodePair
    path = [node]
    while(parent != None):
        path.insert(0, parent)
        closed = SkipTo(parent, curr_depth-1, closed)
        _, parent, _ = closed[0]
        curr_depth -= 1
        
    return path

def OccursIn(node, list_):
    for nodePair in list_:
        node_ = list(nodePair)[0]
        if(node.data == node_.data):
            return True
    return False

def RemoveSeen(nodeList, open, closed):
    if(len(nodeList) == 0):
        ret = []
        return ret
    else:
        node = nodeList[0]
        if(OccursIn(node, open) or OccursIn(node, closed)):
            ret = RemoveSeen(nodeList[1:], open, closed)
            return ret
        else:
            ret = [node]
            ret.extend(RemoveSeen(nodeList[1:], open, closed))
            return ret
        
def dfs_traverse(S):
    open = [(S, None)]
    closed = []
    safety_count = 100000
    while len(open) != 0:
        safety_count -= 1
        nodePair = open[0]
        N, _ = nodePair
        closed.insert(0, nodePair)
        neighbors = MoveGen(N)
        newNodes = RemoveSeen(neighbors, open, closed)
        newPairs = list(zip(newNodes, [N]*len(newNodes)))
        open = newPairs + open[1:]
        if(safety_count <= 0):
            print('safety exceeded: closed {} nodes'.format(len(closed)))
            break
    return [node for node, _ in reversed(closed)]        

def PlotGraph(S):
    import networkx as nx
    import matplotlib.pyplot as plt
    # create a list of all nodes
    
    nodes = dfs_traverse(S)
    
    G = nx.DiGraph()
    G.add_nodes_from([N.data for N in nodes])
    for node in nodes:
        for neighbor in node.neighbors:
            G.add_edge(node.data, neighbor.data)
            
    nx.draw(G, with_labels=True)
    plt.show()
    return G
