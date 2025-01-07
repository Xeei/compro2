from math import floor

class MergeSort:
    def __init__(self, list1: list, list2: list):
        self.list1 = list1
        self.list2 = list2

    def __split(self, l: list):
        n = floor(int(len(l)/2))
        l1 = l[:n]
        l2 = l[n-1:-1]
        return l1, l2
    
    def run(self):
        l1, l2 = self.__split(self.list2)
        print(l1, l2)


l1 = [1,2,3,0,0,0]
l2 = [2,5,6]
m = MergeSort(l1, l2)

m.run()