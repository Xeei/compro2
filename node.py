class Node:
    def __init__(self, name):
        self.name = name
        self.ref = None
        print(f'Node {self.name} had Created.')

    def __del__(self):
        print(f'Node {self.name} destroy!!')


node1 = Node('A')
node2 = Node('B')
node3 = Node('C')
node4 = Node('D')

node1.ref = node2
node2.ref = node1


del node1 #? this wont delete if both node1 and node2 to are ref


print('End of program')

