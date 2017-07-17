from collections import defaultdict


class RoutingAlgorithm:
    def __init__(self):
        self.nodes = set()

        self.edges = defaultdict(list)

        self.distances = {}

    def add_node(self, value):
        self.nodes.add(value)

    def add_edge(self, from_node, to_node, distance):
        self.edges[from_node].append(to_node)

        self.edges[to_node].append(from_node)

        self.distances[(to_node, from_node)] = distance

        self.distances[(from_node, to_node)] = distance


def dijkstra(graph, initial):
    visited = {initial: 0}

    path = {}

    nodes = set(graph.nodes)

    while nodes:
        min_node = None

        for node in nodes:

            if node in visited:

                if min_node is None:
                    min_node = node

                elif visited[node] < visited[min_node]:
                    min_node = node

        if min_node is None:
            break

        nodes.remove(min_node)

        current_weight = visited[min_node]

        for edge in graph.edges[min_node]:
            weight = current_weight + graph.distances[(min_node, edge)]

            if edge not in visited or weight < visited[edge]:
                visited[edge] = weight

                path[edge] = min_node

    return visited, path


def set_up():
    while 1:
        routers = int(raw_input("Input the total number of routers: "))

        if routers <= 2:
            flag = file_read(routers)
            if flag == 1:
                return
            else:
                continue

        else:
            print "Error must be an integer greater than or equal to 2"

            continue


def file_read(routers):
    table = open("topo.txt", 'r')

    rout = []

    for line in table:
        rout.append(map(int, line.split()))

    table.close()

    while 1:
        for name in rout:

            if name[0] < 0:
                print "Error: invalid router, cannot be negative: V%d" % name[0]

                return -1

            elif name[1] < 0:
                print "Error: invalid router, cannot be negative: V%d" % name[1]

                return -1

            elif name[0] > routers:
                print "Error: invalid router, larger provided value: V%d" % name[0]

                return -1

            elif name[1] > routers:
                print "Error: invalid router, larger provided value: V%d" % name[1]

                return -1

            elif name[2] < 0:
                print "Error: cost between routers must be a positive value %d" % name[2]

                return -1

            else:
                return 1


if __name__ == '__main__':
    set_up()


    '''
    g = RoutingAlgorithm()
    g.add_node('a')
    g.add_node('b')
    g.add_node('c')
    g.add_node('d')

    g.add_edge('a', 'b', 10)
    g.add_edge('b', 'c', 10)
    g.add_edge('a', 'c', 15)
    g.add_edge('c', 'd', 20)

    print(dijkstra(g, 'a'))
    '''
