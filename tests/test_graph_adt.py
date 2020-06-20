import unittest
from graphs.graph import Graph
from util.file_reader import read_graph_from_file


class TestGraph(unittest.TestCase):

    def test_create_directed_graph(self):
        """Create a graph."""
        graph = Graph(is_directed=True)
        vertex_a = graph.add_vertex('A')
        vertex_b = graph.add_vertex('B')
        vertex_c = graph.add_vertex('C')
        graph.add_edge('A','B')
        graph.add_edge('A','C')
        graph.add_edge('B','C')

        self.assertEqual(len(graph.get_vertices()), 3)

        self.assertEqual(len(vertex_a.get_neighbors()), 2)
        self.assertEqual(len(vertex_b.get_neighbors()), 1)
        self.assertEqual(len(vertex_c.get_neighbors()), 0)

    def test_create_undirected_graph(self):
        """Create a graph."""
        graph = Graph(is_directed=False)
        vertex_a = graph.add_vertex('A')
        vertex_b = graph.add_vertex('B')
        vertex_c = graph.add_vertex('C')
        graph.add_edge('A','B')
        graph.add_edge('A','C')
        graph.add_edge('B','C')

        self.assertEqual(len(graph.get_vertices()), 3)

        self.assertEqual(len(vertex_a.get_neighbors()), 2)
        self.assertEqual(len(vertex_b.get_neighbors()), 2)
        self.assertEqual(len(vertex_c.get_neighbors()), 2)

class TestReadGraphFromFile(unittest.TestCase):
    def test_read_directed_graph_from_file(self):
        filename = 'test_files/graph_small_directed.txt'
        graph = read_graph_from_file(filename)

        self.assertEqual(len(graph.get_vertices()), 4)

        vertex1 = graph.get_vertex('1')
        vertex2 = graph.get_vertex('2')
        vertex3 = graph.get_vertex('3')
        vertex4 = graph.get_vertex('4')

        self.assertEqual(len(vertex1.get_neighbors()), 1)
        self.assertEqual(len(vertex2.get_neighbors()), 1)
        self.assertEqual(len(vertex3.get_neighbors()), 1)
        self.assertEqual(len(vertex4.get_neighbors()), 0)

    def test_read_undirected_graph_from_file(self):
        filename = 'test_files/graph_small_undirected.txt'
        graph = read_graph_from_file(filename)

        self.assertEqual(len(graph.get_vertices()), 4)

        vertex1 = graph.get_vertex('1')
        vertex2 = graph.get_vertex('2')
        vertex3 = graph.get_vertex('3')
        vertex4 = graph.get_vertex('4')

        self.assertEqual(len(vertex1.get_neighbors()), 1)
        self.assertEqual(len(vertex2.get_neighbors()), 2)
        self.assertEqual(len(vertex3.get_neighbors()), 1)
        self.assertEqual(len(vertex4.get_neighbors()), 2)

    def test_improper_graph_type(self):
        filename = 'test_files/improper_graph_type.txt'

        with self.assertRaises(ValueError) as error:
            graph = read_graph_from_file(filename)

    def test_find_shortest_path(self):
        filename = 'test_files/graph_medium_undirected.txt'
        graph = read_graph_from_file(filename)

        path_from_A_to_F = graph.find_shortest_path('A', 'F')

        self.assertEqual(len(path_from_A_to_F), 4)

    def test_get_all_vertices_n_away(self):
        filename = 'test_files/graph_medium_undirected.txt'
        graph = read_graph_from_file(filename)

        vertices_1_away = graph.find_vertices_n_away('A', 1)
        self.assertEqual(sorted(vertices_1_away), ['B','C'])

        vertices_2_away = graph.find_vertices_n_away('A', 2)
        self.assertEqual(sorted(vertices_2_away), ['D','E'])

        vertices_3_away = graph.find_vertices_n_away('A', 3)
        self.assertEqual(vertices_3_away, ['F'])


    def test_not_bipartite(self):
        """Test that a cycle on 3 vertices is NOT bipartite."""
        graph = Graph(is_directed=False)
        graph.add_vertex('A')
        graph.add_vertex('B')
        graph.add_vertex('C')
        graph.add_edge('A','B')
        graph.add_edge('A','C')
        graph.add_edge('B','C')

        self.assertFalse(graph.is_bipartite())


    # @weight(3)
    def test_is_bipartite_cycle(self):
        """Test that a cycle on 4 vertices is bipartite."""
        graph = Graph(is_directed=False)
        graph.add_vertex('A')
        graph.add_vertex('B')
        graph.add_vertex('C')
        graph.add_vertex('D')
        graph.add_edge('A','B')
        graph.add_edge('B','C')
        graph.add_edge('C','D')
        graph.add_edge('A','D')

        self.assertTrue(graph.is_bipartite())


    # @weight(3)
    def test_is_bipartite_tree(self):
        """Test that a tree on 4 vertices is bipartite."""
        graph = Graph(is_directed=False)
        vertex_a = graph.add_vertex('A')
        vertex_b = graph.add_vertex('B')
        vertex_c = graph.add_vertex('C')
        vertex_d = graph.add_vertex('D')
        graph.add_edge('A','B')
        graph.add_edge('A','C')
        graph.add_edge('A','D')

        self.assertTrue(graph.is_bipartite())


    def test_get_connected_components(self):
        """Get connected components of a graph."""
        graph = Graph(is_directed=False)
        vertex_a = graph.add_vertex('A')
        vertex_b = graph.add_vertex('B')
        vertex_c = graph.add_vertex('C')
        vertex_d = graph.add_vertex('D')
        vertex_d = graph.add_vertex('E')
        vertex_d = graph.add_vertex('F')
        graph.add_edge('A','B')
        graph.add_edge('A','C')
        graph.add_edge('B','C')
        graph.add_edge('D', 'E')

        expected_components = [
            ['A', 'B', 'C'],
            ['D', 'E'],
            ['F']
        ]
        # sort each component for ease of comparison
        actual_components = graph.get_connected_components()
        actual_components = [sorted(comp) for comp in actual_components]

        self.assertCountEqual(expected_components, actual_components)

    def test_find_path_dfs(self):
        graph = Graph(is_directed=True)
        graph.add_vertex('A')
        graph.add_vertex('B')
        graph.add_vertex('C')
        graph.add_edge('A','B')
        graph.add_edge('B','C')
        graph.add_edge('C','A')

        path = graph.find_path_dfs_iter('A', 'C')
        self.assertEqual(path, ['A', 'B', 'C'])

    def test_contains_cycle(self):
        graph = Graph(is_directed=True)
        graph.add_vertex('A')
        graph.add_vertex('B')
        graph.add_vertex('C')
        graph.add_edge('A','B')
        graph.add_edge('B','C')
        graph.add_edge('C','A')

if __name__ == '__main__':
    unittest.main()
