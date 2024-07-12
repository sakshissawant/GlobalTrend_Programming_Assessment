class MaxHeap:
    List = []

    def insert(number):
        MaxHeap.List.append(number)
        
    def delete(number):
        MaxHeap.List.remove(number)
        
    def get_max():
        Max = 0
        for i in MaxHeap.List:
            if i>Max:
                Max = i
        return Max
