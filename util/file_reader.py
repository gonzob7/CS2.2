from graphs.graph import Graph


def read_graph_from_file(filename):
    """
    Read in data from the specified filename, and create and return a graph
    object corresponding to that data.

    Arguments:
    filename (string): The relative path of the file to be processed

    Returns:
    Graph: A directed or undirected Graph object containing the specified
    vertices and edges
    """

    # TODO: Use 'open' to open the file
    try:
        f = open(filename)

    # TODO: Use the first line (G or D) to determine whether graph is directed
    # and create a graph object
        first_line = next(f).strip('\n')
        if first_line == 'G':
            g = Graph(is_directed=False)
        elif first_line == 'D':
            g = Graph(is_directed=True)
        else:
            raise ValueError("Incorrect Formatting")

    # TODO: Use the second line to add the vertices to the graph
        for vertex in next(f).strip('\n').split(','):
            # print(each)
            g.add_vertex(vertex)

    # TODO: Use the 3rd+ line to add the edges to the graph
        for line in f:
            g.add_edge(line[1], line[3])

        return g

    finally:
        f.close()

if __name__ == '__main__':

    graph = read_graph_from_file('test.txt')

    print(graph)
