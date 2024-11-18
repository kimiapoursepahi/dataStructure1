class Array:
    def __init__(self):
        self.arr = []

    def insert(self, index, value):
        if index < 0 or index > len(self.arr):
            print("Index out of range!")
        else:
            self.arr.insert(index, value)

    def delete_by_value(self, value):
        if value in self.arr:
            index = self.arr.index(value)
            self.arr.pop(index)
            print(f"Value was deleted!")
        else:
            print("Value was not found!")

    def delete_by_index(self, index):
        if index < 0 or index >= len(self.arr):
            print("Index out of range!")
        else:   
            self.arr.pop(index)
            print(f"Element in the index deleted!") 

    def append(self, value):
        self.arr.append(value)

    def reverse(self):
        n = len(self.arr)
        for i in range(n // 2):
            self.arr[i], self.arr[n - i - 1] = self.arr[n - i - 1], self.arr[i]     
    
    def search_by_value(self, value):
        for i in range(len(self.arr)):
            if self.arr[i] == value:
               print(f"{value} is in the {i}!")
            else:
                 print(f"{value} is not in array!")

    def display(self):
        print(" ".join(map(str, self.arr)))

array = Array()
array.insert(0, 10)  
array.insert(1, 20)  
array.insert(2, 15) 
array.display()

array.delete_by_value(20)
array.display()

array.delete_by_value(30)
array.display()

array.delete_by_index(1) 
array.display() 

array.append(100)
array.display()

array.reverse()
array.display()

array.search_by_value(100)
array.display()