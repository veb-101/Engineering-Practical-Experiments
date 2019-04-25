# Solutions for sorting classes
# https://stackoverflow.com/questions/4010322/sort-a-list-of-class-instances-python
#
# (1)import operator
# sorted_x = sorted(x, key=operator.attrgetter('score'))
# if you want to sort x in-place, you can also:
# x.sort(key=operator.attrgetter('score'))
#
# (2)
# class Foo(object):
#
#      def __init__(self, score):
#          self.score = score
#
#      def __lt__(self, other):
#          return self.score < other.score
#
# l = [Foo(3), Foo(1), Foo(2)]
# l.sort()

# import operator


class Edge(object):
    def __init__(self, source, dest, weight):
        self.source = source
        self.destination = dest
        self.weight = weight

    def __lt__(self, other):
        return self.weight < other.weight

    def __str__(self):
        return f"Edge {self.source, self.destination} - {self.weight}"


def findParent(vertex, parent):
    if parent[vertex] == vertex:
        return vertex
    return findParent(parent[vertex], parent)


def krushkals(edgeObj, n, E):
    # Sort input in ascending based on weights
    # edgeObj.sort(key=operator.attrgetter('weight'))
    edgeObj.sort()
    count, i, cost = 0, 0, 0
    parent = [i for i in range(n + 1)]
    output = []
    while(count != n - 1):  # so cycle is not formed
        currentEdge = edgeObj[i]
        # Check if we can add currentEdge in MST output
        sourceParent = findParent(currentEdge.source, parent)
        destinationParent = findParent(currentEdge.destination, parent)
        if sourceParent != destinationParent:
            output.append(currentEdge)
            count += 1
            parent[sourceParent] = destinationParent
        i += 1
    print("\nEdges selected:")
    for i in range(n-1):
        # print(f"Edge{output[i].source, output[i].destination}-cost:{output[i].weight}")
        print(f"{output[i]}")
        cost += output[i].weight
    print(f"Total Cost of MST= {cost}")


def Main():
    n = int(input("Enter number of vertices: "))
    E = int(input("Enter number of edges: "))
    edgeObj = []
    for i in range(E):
        s = int(input("Enter source: "))
        d = int(input("Enter sink: "))
        w = int(input("Enter weight: "))
        edgeObj.append(Edge(s, d, w))
    # for i in edgeObj:
    #     print(i)
    krushkals(edgeObj, n, E)


if __name__ == '__main__':
    Main()
# Time Complexity:  O(E log V)
