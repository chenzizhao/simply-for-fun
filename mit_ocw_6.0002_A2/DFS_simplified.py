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

    return: the last edge
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
        newPath = None
        shortest = currentPath.copy()
        for edge in digraph.get_edges_for_node(startn):
            child = edge.get_destination().get_name()
            newPath = currentPath.copy() + [child]
            newPath = dfs1(digraph, child, end, newPath)
            if newPath != None:
                shortest = newPath
        return shortest

def dfs2(digraph, start, end, currentPath):
    """
    added feature: avoid loops
    """
    if start == end:
        return currentPath
    else:
        startn = None
        for node in digraph.nodes:
            if node.name == start:
                startn = node
                break
        newPath = None
        for edge in digraph.get_edges_for_node(startn):
            child = edge.get_destination().get_name()
            if child not in currentPath and newPath == None:
                newPath = currentPath + [child]
                dfs2(digraph, child, end, newPath)
        return newPath


class TestGraph(unittest.TestCase):

    def setUp(self):
        self.g = Digraph()
        self.na = Node('a')
        self.nb = Node('b')
        self.nc = Node('c')
        self.nd = Node('d')
        self.g.add_node(self.na)
        self.g.add_node(self.nb)
        self.g.add_node(self.nc)
        self.g.add_node(self.nd)
        self.e1 = WeightedEdge(self.na, self.nb, 15, 10)
        self.e2 = WeightedEdge(self.na, self.nc, 14, 6)
        self.e3 = WeightedEdge(self.nb, self.nc, 3, 1)
        self.e4 = WeightedEdge(self.nc, self.na, 4, 1)
        self.e5 = WeightedEdge(self.na, self.nd, 4, 2)
        self.g.add_edge(self.e1)
        self.g.add_edge(self.e2)
        self.g.add_edge(self.e3)
        self.g.add_edge(self.e4)
        self.g.add_edge(self.e5)
    
    def test_dfs1(self):
        g = self.g
        start = 'a'
        end = 'c'
        latest_path = ['a', 'c']
        self.assertEqual(dfs1(g, start, end, [str(start)]), latest_path)

    def test_dfs2(self):
        g = self.g
        start = 'a'
        end = 'd'
        latest_path = ['a', 'd']
        self.assertEqual(dfs2(g, start, end, [str(start)]), latest_path)        

if __name__=="__main__":
    g = Digraph()
    na = Node('a')
    g.add_node(na)
    nb = Node('b')
    g.add_node(nb)
    e1 = WeightedEdge(na, nb, 10, 11)
    g.add_edge(e1)
    na2 = Node('a')
    print(g.has_node(na2))
    print([node.get_destination().get_name() for node in g.get_edges_for_node(na)])
    print([node.get_destination().get_name() for node in g.get_edges_for_node(na2)])
    # unittest.main()