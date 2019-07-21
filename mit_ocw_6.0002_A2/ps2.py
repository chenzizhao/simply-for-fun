# 6.0002 Problem Set 5
# Graph optimization
# Name:
# Collaborators:
# Time:

#
# Finding shortest paths through MIT buildings
#
import unittest
from graph import Digraph, Node, WeightedEdge

#
# Problem 2: Building up the Campus Map
#
# Problem 2a: Designing your graph
#
# What do the graph's nodes represent in this problem? What
# do the graph's edges represent? Where are the distances
# represented?
#
# Answer:
# Node: building; Edge: road; Distances: distance between the building. 


# Problem 2b: Implementing load_map
def load_map(map_filename):
    """
    Parses the map file and constructs a directed graph

    Parameters:
        map_filename : name of the map file

    Assumes:
        Each entry in the map file consists of the following four positive
        integers, separated by a blank space:
            From To TotalDistance DistanceOutdoors
        e.g.
            32 76 54 23
        This entry would become an edge from 32 to 76.

    Returns:
        a Digraph representing the map
    """
    print("Loading map from file...")
    g = Digraph()
    with open(map_filename) as f:
        for line in f:
            # parse the line
            src, dest, total_dist, outdoor_dist = line.split()
            # create nodes
            nsrc = Node(src)
            ndest = Node(dest)
            # add nodes if not already in the map
            if not g.has_node(nsrc): 
                g.add_node(nsrc)
            if not g.has_node(ndest):
                g.add_node(ndest)
            # add edge to the map
            g.add_edge(WeightedEdge(nsrc, ndest, int(total_dist), int(outdoor_dist)))
    return g

# Problem 2c: Testing load_map
# Include the lines used to test load_map below, but comment them out: 

# g = load_map("test_load_map.txt")
# print(str(g))

#
# Problem 3: Finding the Shorest Path using Optimized Search Method
#
# Problem 3a: Objective function
#
# What is the objective function for this problem? What are the constraints?
#
# Answer: Objective: minimize total distance travelled; Constraints: not exceeds max distance outdoors, nodes exist, edge exist
#

# Problem 3b: Implement get_best_path
def get_best_path(digraph, start, end, path, max_dist_outdoors, best_dist,
                  best_path):
    """
    Finds the shortest path between buildings subject to constraints.

    Parameters:
        digraph: const Digraph instance
            The graph on which to carry out the search
        start: string
            Building number at which to start
        end: const string
            Building number at which to end
        path: list composed of [[list of strings], int, int] !! Global vriables !!
            Represents the current path of nodes being traversed. Contains
            a list of node names, total distance traveled, and total
            distance outdoors.
        max_dist_outdoors: const int
            Maximum distance spent outdoors on a path
        best_dist: int
            The smallest distance between the original start and end node
            for the initial problem that you are trying to solve
        best_path: list of strings
            The shortest path found so far between the original start
            and end node.

    Returns:
        A tuple with the shortest-path from start to end, represented by
        a list of building numbers (in strings), [n_1, n_2, ..., n_k],
        where there exists an edge from n_i to n_(i+1) in digraph,
        for all 1 <= i < k and the distance of that path.

        If there exists no path that satisfies max_total_dist and
        max_dist_outdoors constraints, then return None.

    Recursive helper function
    """
    # for simplicity
    g = digraph

    # check if start and end are valid
    startn = Node(start)
    endn = Node(end)
    if not (g.has_node(startn) and g.has_node(endn)):
        raise ValueError
    
    # DEBUG:
    # print(f'start = {start}, end = {end}, path = {path}, max_dist_outdoors = {max_dist_outdoors}, best_dist = {best_dist}, best_path = {best_path}')

    # update path, which keeps track of current path, total_dist and outdoor_dist in a list
    if path[0] != []:
        prevEdge = g.get_edge(path[0][-1], start)
        path[1] += prevEdge.get_total_distance()
        path[2] += prevEdge.get_outdoor_distance()
        path[0] += [start]
    else: # it is the first recursion, where there is not previous node nor distance travelled
        path[0] = [start]
    
    # DEBUG:
    # print(f'current path = {path}')
    
    # base case
    if path[2] > max_dist_outdoors:
        # DEBUG
        # print("Exceeding max_dist_outdoors already!")
        return [None, float('inf')]
    if start == end:
        # DEBUG: 
        # print(f'find a path! path = {path[0:2]}')
        return path[0: 2]

    # recursive case
    startn = g.get_node(start)
    for edge in g.get_edges_for_node(startn):
        childn = edge.get_destination()
        child = childn.get_name()
        while path[0][-1] != start: # make sure the last item of current path is "start"
            path[0].pop()
        if child not in path[0]:    # avoid loops
            if best_path == None or path[1] < best_dist:    #the new path may be a best path
                # solve the problem recursively: find the best path from child to end
                # TODO: explain why "path.copy()" works but "path" does not? 
                newPath = get_best_path(g, child, end, path.copy(), max_dist_outdoors, best_dist, best_path)
                if newPath[0] != None and newPath[1] < best_dist:   #final check if the return is indeed a better path than the current best_path
                    # TODO: explain why "path.copy()" works but "path" does not? 
                    # ANS: maybe due to the fact that asssignment only redirects the reference while copying actually memorizes the values
                    best_path = newPath[0].copy()
                    best_dist = newPath[1]
    # after iterating over all childs, return best path and best_dist (might have been updated, might have not)
    # TODO: consider return a tuple instead of a list -- this may solve the previous reference problem
    return [best_path, best_dist]

# Problem 3c: Implement directed_dfs
def directed_dfs(digraph, start, end, max_total_dist, max_dist_outdoors):
    """
    Finds the shortest path from start to end using a directed depth-first
    search. The total distance traveled on the path must not
    exceed max_total_dist, and the distance spent outdoors on this path must
    not exceed max_dist_outdoors.

    Parameters:
        digraph: Digraph instance
            The graph on which to carry out the search
        start: string
            Building number at which to start
        end: string
            Building number at which to end
        max_total_dist: int
            Maximum total distance on a path
        max_dist_outdoors: int
            Maximum distance spent outdoors on a path

    Returns:
        The shortest-path from start to end, represented by
        a list of building numbers (in strings), [n_1, n_2, ..., n_k],
        where there exists an edge from n_i to n_(i+1) in digraph,
        for all 1 <= i < k

        If there exists no path that satisfies max_total_dist and
        max_dist_outdoors constraints, then raises a ValueError.

    Wrapper function
    """
    # Sanity check: maybe extra
    if start == end:
        return [start]
    # set up the recurison
    path = get_best_path(digraph, start, end, [[], 0, 0], max_dist_outdoors, float('inf'), None)
    if path[1] <= max_total_dist:
        # valid path found
        return path[0]
    # valid path not found: path[1] == inf or path[1] > mac_total_dist
    raise ValueError

# ================================================================
# Begin tests -- you do not need to modify anything below this line
# ================================================================

class Ps2Test(unittest.TestCase):
    LARGE_DIST = 99999

    def setUp(self):
        self.graph = load_map("mit_map.txt")

    def test_load_map_basic(self):
        self.assertTrue(isinstance(self.graph, Digraph))
        self.assertEqual(len(self.graph.nodes), 37)
        all_edges = []
        for _, edges in self.graph.edges.items():
            all_edges += edges  # edges must be dict of node -> list of edges
        all_edges = set(all_edges)
        self.assertEqual(len(all_edges), 129)

    def _print_path_description(self, start, end, total_dist, outdoor_dist):
        constraint = ""
        if outdoor_dist != Ps2Test.LARGE_DIST:
            constraint = "without walking more than {}m outdoors".format(
                outdoor_dist)
        if total_dist != Ps2Test.LARGE_DIST:
            if constraint:
                constraint += ' or {}m total'.format(total_dist)
            else:
                constraint = "without walking more than {}m total".format(
                    total_dist)

        print("------------------------")
        print("Shortest path from Building {} to {} {}".format(
            start, end, constraint))

    def _test_path(self,
                   expectedPath,
                   total_dist=LARGE_DIST,
                   outdoor_dist=LARGE_DIST):
        start, end = expectedPath[0], expectedPath[-1]
        self._print_path_description(start, end, total_dist, outdoor_dist)
        dfsPath = directed_dfs(self.graph, start, end, total_dist, outdoor_dist)
        print("Expected: ", expectedPath)
        print("DFS: ", dfsPath)
        self.assertEqual(expectedPath, dfsPath)

    def _test_impossible_path(self,
                              start,
                              end,
                              total_dist=LARGE_DIST,
                              outdoor_dist=LARGE_DIST):
        self._print_path_description(start, end, total_dist, outdoor_dist)
        with self.assertRaises(ValueError):
            directed_dfs(self.graph, start, end, total_dist, outdoor_dist)

    def test_path_one_step(self):
        self._test_path(expectedPath=['32', '56'])

    def test_path_no_outdoors(self):
        self._test_path(
            expectedPath=['32', '36', '26', '16', '56'], outdoor_dist=0)

    def test_path_multi_step(self):
        self._test_path(expectedPath=['2', '3', '7', '9'])

    def test_path_multi_step_no_outdoors(self):
        self._test_path(
            expectedPath=['2', '4', '10', '13', '9'], outdoor_dist=0)

    def test_path_multi_step2(self):
        self._test_path(expectedPath=['1', '4', '12', '32'])

    def test_path_multi_step_no_outdoors2(self):
        self._test_path(
            expectedPath=['1', '3', '10', '4', '12', '24', '34', '36', '32'],
            outdoor_dist=0)

    def test_impossible_path1(self):
        self._test_impossible_path('8', '50', outdoor_dist=0)

    def test_impossible_path2(self):
        self._test_impossible_path('10', '32', total_dist=100)


if __name__ == "__main__":
    unittest.main()
