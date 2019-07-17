# In this file, tested several versions of DFS, each adding one feature to the previous one.
# The goal is to complete 6.0002 A2 Problem 3 & 4
import unittest
from graph import Digraph, Node, WeightedEdge

def dfs1(digraph, start, end, currentPath):
    """
    digraph: the graph
    start: string name of the start node
    end: string name of the end node; should be constant
    currentPath: list of node from initial start to currentNode

    return: the last edge; should also print all possible paths along the way
    """
    if start == end:
        return currentPath
    else: 
        startn = None
        for node in digraph.nodes:
            if node.name == start:
                startn = node
                break
        # assume can always find start
        for edge in digraph.get_edges_for_node(startn):
            child = edge.get_destination().get_name()
            newPath = currentPath.copy() + [child]
            dfs1(digraph, child, end, newPath)
            return newPath


class TestGraph(unittest.TestCase):

    def setUp(self):
        self.g = Digraph()
        self.na = Node('a')
        self.nb = Node('b')
        self.nc = Node('c')
        self.g.add_node(self.na)
        self.g.add_node(self.nb)
        self.g.add_node(self.nc)
        self.e1 = WeightedEdge(self.na, self.nb, 15, 10)
        self.e2 = WeightedEdge(self.na, self.nc, 14, 6)
        self.e3 = WeightedEdge(self.nb, self.nc, 3, 1)
        self.g.add_edge(self.e1)
        self.g.add_edge(self.e2)
        self.g.add_edge(self.e3)
    
    def test_dfs1(self):
        g = self.g
        start = 'a'
        end = 'c'
        latest_path = ['a', 'c']
        self.assertEqual(dfs1(g, start, end, [str(start)]), latest_path)

if __name__=="__main__":
    unittest.main()