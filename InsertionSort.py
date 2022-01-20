## Insertion Sort Implementation
## Hezekiah Branch
## Wed Jan 19 2022
## Purpose: O(nlogn) insertion sort
## to be ran on the command line

class InsertionSort:
    def __init__(self, input):
        self.data = input

    def __str__(self):
        return "{}".format(self.data)

    def swap(self, i, j):
        temp = self.data[i]
        self.data[i] = self.data[j]
        self.data[j] = temp
        print(self.data)

    def sort(self):
        for j in range(1, len(self.data)):
            key = self.data[j]
            # Insert key into sorted sequence
            # i.e. iterate toward data[0..j-1]
            i = j - 1
            while i >= 0 and self.data[i] > key:
                self.data[i + 1] = self.data[i]
                i = i - 1
            self.data[i + 1] = key
        print(self.data)
