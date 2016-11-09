class Edge(object):

    #each edge has transaction info
    def __init__(self, time, amount, message):
        self.time = time
        self.amount = amount
        self.message = message

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
