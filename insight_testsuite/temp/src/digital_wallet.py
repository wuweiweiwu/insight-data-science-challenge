import sys

import graph
import node
import edge

class DigitalWallet:

    def __init__(self, batch_file, stream_file, outputs):
        self.clear_outputs(outputs)
        self.graph = graph.Graph()
        self.process_batch(batch_file)
        self.process_stream(stream_file, outputs[0], outputs[1], outputs[2])

    def clear_outputs(self, outputs):
        for output in outputs:
            open(output,'w').close()

    def tokenize(self, line):
        line = line.replace('\n', '')
        return line.split(', ')

    def write_to_file(self, filename, string):
        f = open(filename,'a')
        f.write(string+'\n')
        f.close()

    def is_friend_trusted(self, src, des, level = None):
        if level == None:
            level = 4
        if self.graph.breadth_first_search(src, des, level) == None:
            return False
        else:
            return True

    def process_batch(self, batch_file):
        with open(batch_file) as f:
            next(f)
            for line in f:
                tokens = self.tokenize(line)
                (time, src_id, des_id, amount, message) = tuple(tokens)
                src_node = node.Node(src_id)
                des_node = node.Node(des_id)
                transaction = edge.Edge(time, amount, message)
                self.graph.add_friends(src_node, des_node)
                self.graph.add_transaction((src_node, des_node), transaction)

    def process_stream(self, stream_file, output_1, output_2, output_3):
        with open(stream_file) as f:
            next(f)
            for line in f:
                tokens = self.tokenize(line)
                (time, src_id, des_id, amount, message) = tuple(tokens)
                src_node = node.Node(src_id)
                des_node = node.Node(des_id)
                transaction = edge.Edge(time, amount, message)

                is_level_1 = self.is_friend_trusted(src_node, des_node, level=1)
                is_level_2 = is_level_1 if is_level_1 else self.is_friend_trusted(src_node, des_node, level=2)
                is_level_4 = is_level_2 if is_level_2 else self.is_friend_trusted(src_node, des_node, level=4)

                if is_level_1:
                    self.write_to_file(output_1,"trusted")
                else:
                    self.write_to_file(output_1,"unverified")

                if is_level_2:
                    self.write_to_file(output_2,"trusted")
                else:
                    self.write_to_file(output_2,"unverified")

                if is_level_4:
                    self.write_to_file(output_3,"trusted")
                else:
                    self.write_to_file(output_3,"unverified")

                self.graph.add_friends(src_node, des_node)
                self.graph.add_transaction((src_node, des_node), transaction)

if __name__ == '__main__':
    if len(sys.argv) == 6:
        DigitalWallet(sys.argv[1],sys.argv[2],sys.argv[3:6])
    else:
        print("Invalid number of arguments")
