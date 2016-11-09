import collections

class Graph:

    '''representing the graph using adjacency list
    a dict of sets representing nodes and neighbors
    and a dict of lists representing transactions'''
    def __init__(self):
        self.adjacency_list = {}
        self.transactions = {}

    def add_friends(self, node1, node2):
        if node1 in self.adjacency_list:
            self.adjacency_list[node1].add(node2)
        else:
            self.adjacency_list[node1] = set([node2])

        if node2 in self.adjacency_list:
            self.adjacency_list[node2].add(node1)
        else:
            self.adjacency_list[node2] = set([node1])

    def add_transaction(self, nodes, transaction):
        if nodes not in self.transactions:
            self.transactions[nodes] = [transaction]
        else:
            self.transactions[nodes].append(transaction)

    '''other functionality seen in venmo.'''
    def find_common_transactions(self, node1, node2):
        return self.transactions[(node1, node2)] + self.transactions[(node2, node1)]

    def find_outgoing(self, node):
        outgoing=[]
        for key in self.adjacency_list.keys():
            if key[0] == node:
                outgoing = outgoing + self.adjacency_list[key]
        return outgoing

    def find_incoming(self, node):
        incoming=[]
        for key in self.adjacency_list.keys():
             if key[1] == node:
                 incoming = incoming + self.adjacency_list[key]
        return incoming

    '''iterative bfs implementation using a list as a queue
    returns None if current level > level or not found
    returns level if found'''
    def breadth_first_search(self, start, end, level):
        level_dict = {start: {"level":0}}
        queue = [start]
        while queue:
            current = queue.pop(0)
            if current == end:
                return level_dict[current]["level"]
            for node in self.adjacency_list[current]:
                if node not in level_dict and level_dict[current]["level"] < level:
                    level_dict[node] = {"level":level_dict[current]["level"]+1}
                    queue.append(node)
        return None
