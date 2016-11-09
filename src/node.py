import collections

class Node(object):

    def __init__(self, id):
        self.id = id

    def get_id(self):
        return self.id

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __hash__(self):
        return hash(self.id)
