from utils import *
from dfid2 import *
from dfid1 import *
from dfs import *

start = Node('S')
T = Node('T')
A = Node('A')
B = Node('B')
C = Node('C')
G = Node('G')

start.addLink(T)
T.addLink(B)
T.addLink(A)
A.addLink(G)
C.addLink(G)
B.addLink(C)

result = dfs(start)

print(result)

print('dfs order: ', dfs_traverse(start))

G = PlotGraph(start)
