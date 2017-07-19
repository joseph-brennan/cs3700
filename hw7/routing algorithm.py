from collections import defaultdict

nodes = -1
Max_value = float("inf")


class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distances = {}

    def add_edge(self, from_node, to_node, distance):
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.distances[(from_node, to_node)] = distance
        self.distances[(to_node, from_node)] = distance


# def dijkstra(graph, initial):
#     visited = {initial: 1}
#     path = {}
#
#     nodes = set(graph.nodes)
#
#     while nodes:
#         min_node = None
#         for node in nodes:
#             if node in visited:
#                 if min_node is None:
#                     min_node = node
#                 elif visited[node] < visited[min_node]:
#                     min_node = node
#
#         if min_node is None:
#             break
#
#         nodes.remove(min_node)
#         current_weight = visited[min_node]
#
#         for edge in graph.edges[min_node]:
#             weight = current_weight + graph.distances[(min_node, edge)]
#             if edge not in visited or weight < visited[edge]:
#                 visited[edge] = weight
#                 path[edge] = min_node
#
#     return visited, path

def dijkstra(graph, start):
    N = []  # set of nodes whose least cost path definitively known
    Y = []  # set of edges currently known to be in shortest path
    D = [Max_value for i in range(nodes)]  # current value of cost of path from source to destination i
    P = [-1 for i in range(nodes)]  # predecessor node along path from source to i

    def get_min_index():
        index = -1

        min_value = Max_value

        for i in range(len(D)):
            if i not in N and D[i] < min_value:
                index = i

                min_value = D[i]

        return index

    def print_lists():
        print "N'", N
        print "Y'", Y
        print "D", D
        print "p", P

    def get_adjacent(start):
        key_list = graph.distances.keys()

        get_neighbors = []

        for key in key_list:

            if key[0] == start:
                get_neighbors.append(key[1])

        return get_neighbors

    print "initial values "

    N.append(start)

    neighbors = get_adjacent(start)

    for node in neighbors:
        P[node] = start

        D[node] = graph.distances[start, node]

    # print_lists()

    while 1:

        k = get_min_index()

        if k == -1:
            break

        N.append(k)

        Y.append((P[k], k))

        neighbors = get_adjacent(k)

        for node in neighbors:
            if node in N:
                continue
            cost = D[k] + graph.distances[k, node]

            if cost < D[node]:
                D[node] = cost

                P[node] = k
        # print_lists()
    return P, N

# def shortest_path(graph, origin, destination):
#     visited, paths = dijkstra(graph, origin)
#     full_path = deque()
#     _destination = paths[destination]
#
#     while _destination != origin:
#         full_path.appendleft(_destination)
#         _destination = paths[_destination]
#
#     full_path.appendleft(origin)
#     full_path.append(destination)
#
#     return visited[destination], list(full_path)


def check_rout(P, source, destination):
    pre = P[destination]

    if pre == source:
        return destination
    else:
        return check_rout(P, source, pre)


if __name__ == '__main__':
    graph = Graph()

    initial_node = 0
    while 1:
        nodes = 1
        nodes += input("how many nodes are there?")
        if nodes < 2:
            print "Error msut be an integer great or equal to two"
        else:
            break

    routers = open("topo.txt", 'r')

    flag = False

    while 1:
        for line in routers:

            router = line.strip().split()

            if int(router[0]) < 0:
                print "Error: invalid router, cannot be negative: V%s" % router[0]
                flag = True
                break

            elif int(router[1]) < 0:
                print "Error: invalid router, cannot be negative: V%s" % router[1]

                flag = True
                break

            elif int(router[0]) > nodes:
                print "Error: invalid router, larger provided value: V%s" % router[0]

                flag = True
                break

            elif int(router[1]) > nodes:
                print "Error: invalid router, larger provided value: V%s" % router[1]

                flag = True
                break

            elif int(router[2]) < 0:
                print "Error: cost between routers must be a positive value %s" % router[2]

                flag = True
                break

            else:
                graph.add_edge(int(router[0]), int(router[1]), int(router[2]))

        routers.close()

        if flag:
            new_file = input("enter correct cost file")

            routers = open(new_file, 'r')
        else:
            break

    P, N = dijkstra(graph, initial_node)

    source = initial_node

    f = open("testResultsClient.txt", 'w')

    for destination in N:
        if destination == source:
            pass
        else:
            print "{:15}Link".format("Destination")
            f.write("{:15}Link".format("Destination") + '\n')

            print "V{:<12} (V0, V{})".format(destination, check_rout(P, source, destination))
            f.write("V{:<12} (V0, V{})".format(destination, check_rout(P, source, destination)) + '\n')

    f.close()


