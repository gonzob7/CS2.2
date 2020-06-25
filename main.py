from graphs.graph import Graph
from graphs.weighted_graph import WeightedGraph
from util.file_reader import read_graph_from_file
# from graphs.weighted_graph import WeightedGraph


# Driver code
if __name__ == '__main__':

    # Create the graph

    graph = WeightedGraph(is_directed=True)

    # Add some vertices
    graph.add_vertex('A')
    graph.add_vertex('B')
    graph.add_vertex('C')
    graph.add_vertex('D')

    # Add connections
    graph.add_edge('A', 'B', 3)
    graph.add_edge('A', 'D', 7)
    graph.add_edge('B', 'A', 8)
    graph.add_edge('B', 'C', 2)
    graph.add_edge('C', 'A', 5)
    graph.add_edge('C', 'D', 1)
    graph.add_edge('D', 'A', 2)

    # Or, read a graph in from a file
    # graph = read_graph_from_file('test_files/graph_small_directed.txt')

    # Output the vertices & edges
    # Print vertices
    # print(f'The vertices are: {graph.get_vertices()} \n')

    # Print edges
    # print('The edges are:')
    # for vertex_obj in graph.get_vertices():
    #     for neighbor_obj in vertex_obj.get_neighbors():
    #         print(f'({vertex_obj.get_id()} , {neighbor_obj.get_id()})')

    # # Search the graph
    # print('Performing BFS traversal...')
    # graph.bfs_traversal('A')
    #
    # # Find shortest path
    # print('Finding shortest path from vertex A to vertex E...')
    # shortest_path = graph.find_shortest_path('A', 'E')
    # print(shortest_path)
    #
    # # Find all vertices N distance away
    # print('Finding all vertices distance 2 away...')
    # vertices_2_away = graph.find_vertices_n_away('A', 2)
    # print(vertices_2_away)
    # print(graph.is_bipartite)

    print(graph.floyd_warshall())
