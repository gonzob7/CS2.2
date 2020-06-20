
from collections import deque

class Vertex(object):
    """
    Defines a single vertex and its neighbors.
    """

    def __init__(self, vertex_id):
        """
        Initialize a vertex and its neighbors dictionary.
        Parameters:
        vertex_id (string): A unique identifier to identify this vertex.
        """
        self.__id = vertex_id
        self.__neighbors_dict = {} # id -> object

    def add_neighbor(self, vertex_obj):
        """
        Add a neighbor by storing it in the neighbors dictionary.
        Parameters:
        vertex_obj (Vertex): An instance of Vertex to be stored as a neighbor.
        """
        self.__neighbors_dict[vertex_obj.__id] = vertex_obj

    def __str__(self):
        """Output the list of neighbors of this vertex."""
        neighbor_ids = list(self.__neighbors_dict.keys())
        return f'{self.__id} adjacent to {neighbor_ids}'

    def __repr__(self):
        """Output the list of neighbors of this vertex."""
        return self.__str__()

    def get_neighbors(self):
        """Return the neighbors of this vertex."""
        return list(self.__neighbors_dict.values())

    def get_id(self):
        """Return the id of this vertex."""
        return self.__id


class Graph:
    """ Graph Class
    Represents a directed or undirected graph.
    """
    def __init__(self, is_directed=True):
        """
        Initialize a graph object with an empty vertex dictionary.
        Parameters:
        is_directed (boolean): Whether the graph is directed (edges go in only one direction).
        """
        self.__vertex_dict = {} # id -> object
        self.__is_directed = is_directed

    def add_vertex(self, vertex_id):
        """
        Add a new vertex object to the graph with the given key and return the vertex.
        Parameters:
        vertex_id (string): The unique identifier for the new vertex.
        Returns:
        Vertex: The new vertex object.
        """
        vt = Vertex(vertex_id)
        self.__vertex_dict[vertex_id] = vt
        return vt



    def get_vertex(self, vertex_id):
        """Return the vertex if it exists."""
        if vertex_id not in self.__vertex_dict:
            return None

        vertex_obj = self.__vertex_dict[vertex_id]
        return vertex_obj

    def add_edge(self, vertex_id1, vertex_id2):
        """
        Add an edge from vertex with id `vertex_id1` to vertex with id `vertex_id2`.
        Parameters:
        vertex_id1 (string): The unique identifier of the first vertex.
        vertex_id2 (string): The unique identifier of the second vertex.
        """

        self.__vertex_dict[vertex_id1].add_neighbor(self.__vertex_dict[vertex_id2])

        if not self.__is_directed:
            self.__vertex_dict[vertex_id2].add_neighbor(self.__vertex_dict[vertex_id1])


    def get_vertices(self):
        """
        Return all vertices in the graph.
        Returns:
        List<Vertex>: The vertex objects contained in the graph.
        """
        return list(self.__vertex_dict.values())

    def get_vertex(self, vertex_id):
        """Return the vertex with given id."""
        return self.__vertex_dict[vertex_id]

    def contains_id(self, vertex_id):
        return vertex_id in self.__vertex_dict

    def __str__(self):
        """Return a string representation of the graph."""
        return f'Graph with vertices: {self.get_vertices()}'

    def __repr__(self):
        """Return a string representation of the graph."""
        return self.__str__()

    def bfs_traversal(self, start_id):
        """
        Traverse the graph using breadth-first search.
        """
        if not self.contains_id(start_id):
            raise KeyError("One or both vertices are not in the graph!")

        # Keep a set to denote which vertices we've seen before
        seen = set()
        seen.add(start_id)

        # Keep a queue so that we visit vertices in the appropriate order
        queue = deque()
        queue.append(self.get_vertex(start_id))

        while queue:
            current_vertex_obj = queue.popleft()
            current_vertex_id = current_vertex_obj.get_id()

            # Process current node
            print('Processing vertex {}'.format(current_vertex_id))

            # Add its neighbors to the queue
            for neighbor in current_vertex_obj.get_neighbors():
                if neighbor.get_id() not in seen:
                    seen.add(neighbor.get_id())
                    queue.append(neighbor)

        return # everything has been processed

    def find_shortest_path(self, start_id, target_id):
        """
        Find and return the shortest path from start_id to target_id.
        Parameters:
        start_id (string): The id of the start vertex.
        target_id (string): The id of the target (end) vertex.
        Returns:
        list<string>: A list of all vertex ids in the shortest path, from start to end.
        """
        if not self.contains_id(start_id) or not self.contains_id(target_id):
            raise KeyError("One or both vertices are not in the graph!")

        # vertex keys we've seen before and their paths from the start vertex
        vertex_id_to_path = {
            start_id: [start_id] # only one thing in the path
        }

        # queue of vertices to visit next
        queue = deque()
        queue.append(self.get_vertex(start_id))

        # while queue is not empty
        while queue:
            current_vertex_obj = queue.popleft() # vertex obj to visit next
            current_vertex_id = current_vertex_obj.get_id()

            # found target, can stop the loop early
            if current_vertex_id == target_id:
                break

            neighbors = current_vertex_obj.get_neighbors()
            for neighbor in neighbors:
                if neighbor.get_id() not in vertex_id_to_path:
                    current_path = vertex_id_to_path[current_vertex_id]
                    # extend the path by 1 vertex
                    next_path = current_path + [neighbor.get_id()]
                    vertex_id_to_path[neighbor.get_id()] = next_path
                    queue.append(neighbor)
                    # print(vertex_id_to_path)

        if target_id not in vertex_id_to_path: # path not found
            return None

        return vertex_id_to_path[target_id]

    def find_vertices_n_away(self, start_id, target_distance):
        """
        Find and return all vertices n distance away.
        Arguments:
        start_id (string): The id of the start vertex.
        target_distance (integer): The distance from the start vertex we are looking for
        Returns:
        list<string>: All vertex ids that are `target_distance` away from the start vertex
        """
        if not self.contains_id(start_id):
            raise KeyError("One or both vertices are not in the graph!")

        vertex_distance_to_path = {
            start_id: 0 # only one thing in the path
        }

        target_vertices = []
        #have a set of visited vertices
        visited = set()
        visited.add(start_id)
        #deque to store vertex and distance
        queue = deque()
        queue.append(self.get_vertex(start_id))

        found_a_target_distance = False

        while queue:
            current_vertex_obj = queue.pop() # vertex obj to visit next
            current_vertex_id = current_vertex_obj.get_id()

            if vertex_distance_to_path[current_vertex_id] == target_distance-1:
                found_a_target_distance = True
            neighbors = current_vertex_obj.get_neighbors()

            for neighbor in neighbors:
                if neighbor.get_id() not in visited:
                    if neighbor.get_id() not in vertex_distance_to_path:
                        vertex_distance_to_path[neighbor.get_id()] = vertex_distance_to_path[current_vertex_id]
                    vertex_distance_to_path[neighbor.get_id()] += 1
                    if vertex_distance_to_path[neighbor.get_id()] == target_distance:
                        target_vertices.append(neighbor.get_id())
                    if found_a_target_distance == False:
                        visited.add(neighbor.get_id())
                        queue.append(neighbor)

        return target_vertices


    def is_bipartite(self):

        """
        Return True if the graph is bipartite, and False otherwise.
        """

        #where to start the bfs
        start_id = list(self.__vertex_dict.keys())[0]

        # Keep a set to denote which vertices we've seen before
        seen = set()
        seen.add(start_id)

        # Keep a queue so that we visit vertices in the appropriate order
        queue = deque()
        queue.append(start_id)

        colors = {
            start_id: 0
        }

        current_color = 0

        while queue:
            current_vertex_id = queue.pop()
            current_vertex_obj = self.get_vertex(current_vertex_id)
            current_color = colors[current_vertex_id]
            seen.add(current_vertex_id)

            neighbors = current_vertex_obj.get_neighbors()

            for neighbor in neighbors:
                neighbor_id = neighbor.get_id()

                if neighbor_id in colors:
                    if colors[neighbor_id] == current_color: #not bipartite
                        return False
                else:
                    colors[neighbor_id] = (current_color + 1) % 2 # will always be 0 or 1, so set to oppposite
                    queue.append(neighbor_id)


        return True #the graph is bipartite


    def get_connected_components(self):
        """
        Return a list of all connected components, with each connected component
        represented as a list of vertex ids.
        """

        all_vertex_ids = list(self.__vertex_dict.keys())

        components = list()

        while all_vertex_ids:
            start_vertex_id = list(all_vertex_ids).pop()
            start_vertex_obj = self.get_vertex(start_vertex_id)
            all_vertex_ids.remove(start_vertex_id)

            # Keep a set to denote which vertices we've seen before
            seen = set()
            seen.add(start_vertex_id)

            # Keep a queue so that we visit vertices in the appropriate order
            queue = deque()
            queue.append(start_vertex_id)
            #bfs on each
            while queue:
                current_vertex_id = queue.pop()
                current_vertex_obj = self.get_vertex(current_vertex_id)

                neighbors = current_vertex_obj.get_neighbors()

                for neighbor in neighbors:
                    neighbor_id = neighbor.get_id()

                    if neighbor_id in all_vertex_ids:
                        all_vertex_ids.remove(neighbor_id)

                    if neighbor_id not in seen:
                        queue.append(neighbor_id)
                        seen.add(neighbor_id)

            components.append(seen)

        return(components)



    def find_path_dfs_iter(self, start_id, target_id):
        """
        Use DFS with a stack to find a path from start_id to target_id.
        """
        if not self.contains_id(start_id):
            raise KeyError("One or both vertices are not in the graph!")

        # vertex keys we've seen before and their paths from the start vertex
        vertex_id_to_path = {
            start_id: [start_id] # only one thing in the path
        }

        # Keep a set to denote which vertices we've seen before
        seen = set()
        seen.add(start_id)

        # Keep a stack so that we visit vertices in the appropriate order
        stack = deque()
        stack.append(self.get_vertex(start_id))

        while stack:
            current_vertex_obj = stack.pop()
            current_vertex_id = current_vertex_obj.get_id()

            # found target, can stop the loop early
            if current_vertex_id == target_id:
                break

            # Add its neighbors to the stack
            for neighbor in current_vertex_obj.get_neighbors():
                if neighbor.get_id() not in vertex_id_to_path:
                    current_path = vertex_id_to_path[current_vertex_id]
                    # extend the path by 1 vertex
                    next_path = current_path + [neighbor.get_id()]
                    vertex_id_to_path[neighbor.get_id()] = next_path
                    stack.append(neighbor)

        if target_id not in vertex_id_to_path: # path not found
            return None

        return vertex_id_to_path[target_id] #path found, return
