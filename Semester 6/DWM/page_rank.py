import string

LETTERS = string.ascii_uppercase

graph = [
        [0, 0, 1, 1, 1, 0, 0],
        [0, 1, 0, 1, 1, 0, 1],
        [0, 1, 1, 0, 0, 1, 0],
        [1, 0, 0, 1, 1, 1, 0],
        [1, 0, 1, 0, 0, 1, 0],
        [1, 1, 0, 0, 1, 0, 1],
        [1, 1, 1, 0, 1, 0, 0],
]


class Node:
    def __init__(self, name):
        self.name = name
        self.inbound = []
        self.outbound = []

    def add_inbound(self, node):
        self.inbound.append(node)

    def add_outbound(self, node):
        self.outbound.append(node)

    def __repr__(self):
        return f"Node {self.name}: Inbound: {self.inbound} ; Outbound: {self.outbound}"


def page_rank(nodes, limit=20, d=0.85):
    ranks = {}
    for node in nodes:
        ranks[node.name] = 1

    outbounds = {}
    for node in nodes:
        outbounds[node.name] = len(node.outbound)

    last_iteration_ranks = ranks.copy()

    i = 0
    while True:
        print(f"======= Iteration {i + 1} =======")
        for j, node in enumerate(nodes):
            ranks[node.name] = round((1 - d) / num_nodes + d * sum(
                [ranks[ib] / outbounds[ib] for ib in node.inbound]
            ), 5)

        ranks = dict(
            sorted(ranks.items(), key=lambda item: item[1], reverse=True))

        if ranks == last_iteration_ranks:
            print("Page ranks converged.")
            print(ranks)
            break
        else:
            last_iteration_ranks = ranks.copy()

        print(ranks)
        i += 1


def main():
    num_nodes = len(graph)

    names = list(LETTERS[:num_nodes])

    nodes = [Node(name) for name in names]

    for ri, row in enumerate(graph):
        for ci, col in enumerate(row):
            if col == 1:
                nodes[ci].add_inbound(names[ri])
                nodes[ri].add_outbound(names[ci])

    print("======= Nodes =======")
    for node in nodes:
        print(node)

    page_rank(nodes)


if __name__ == "__main__":
    num_nodes = len(graph)
    main()
