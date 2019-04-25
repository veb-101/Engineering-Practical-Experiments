# credits: https://www.geeksforgeeks.org/python-program-for-dijkstras-shortest-path-algorithm-greedy-algo-7/
'''
Algorithm
1) Create a set sptSet (shortest path tree set) that keeps track of vertices
included in shortest path tree, i.e., whose minimum distance from source is calculated and finalized.
Initially, this set is empty.

2) Assign a distance value to all vertices in the input graph.
Initialize all distance values as INFINITE.
Assign distance value as 0 for the source vertex so that it is picked first.

3) While sptSet doesn’t include all vertices
….a) Pick a vertex u which is not there in sptSet and has minimum distance value.
….b) Include u to sptSet.
….c) Update distance value of all adjacent vertices of u. To update the distance values,
    iterate through all adjacent vertices. For every adjacent vertex v,
    if sum of distance value of u (from source) and weight of edge u-v, is less than
    the distance value of v, then update the distance value of v.
'''

import sys


class Graph():

    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]

    def printSolution(self, dist):
        print("Vertex Distance from Source")
        for node in range(self.V):
            print(f"Distance from  vertex {self.src} to vertex {node}: {dist[node]}")

    def minDistance(self, dist, sptSet):
        minimum = sys.maxsize
        for v in range(self.V):
            if dist[v] < minimum and sptSet[v] == False:
                # print(f"dist[{v}] = {dist[v]}")
                minimum = dist[v]
                min_index = v

        return min_index

    def dijkstra(self, src):
        self.src = src

        dist = [sys.maxsize] * self.V
        dist[src] = 0

        sptSet = [False] * self.V

        for _ in range(self.V):
            u = self.minDistance(dist, sptSet)
            # print(f"start: {u}")

            sptSet[u] = True

            for v in range(self.V):
                if self.graph[u][v] > 0 and sptSet[v] == False and \
                        dist[v] > dist[u] + self.graph[u][v]:
                    # print(f"u, v: {u,v}")
                    dist[v] = dist[u] + self.graph[u][v]
            # print(f"Dist: {dist}")

        self.printSolution(dist)


# Driver program
if __name__ == '__main__':
    g = Graph(9)
    g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
               [4, 0, 8, 0, 0, 0, 0, 11, 0],
               [0, 8, 0, 7, 0, 4, 0, 0, 2],
               [0, 0, 7, 0, 9, 14, 0, 0, 0],
               [0, 0, 0, 9, 0, 10, 0, 0, 0],
               [0, 0, 4, 14, 10, 0, 2, 0, 0],
               [0, 0, 0, 0, 0, 2, 0, 1, 6],
               [8, 11, 0, 0, 0, 0, 1, 0, 7],
               [0, 0, 2, 0, 0, 0, 6, 7, 0]
               ]

    g.dijkstra(5)
# Time Complexity: O(vertices^2)
