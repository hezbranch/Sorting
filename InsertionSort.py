## Insertion Sort Implementation
## Hezekiah Branch
## Wed Jan 19 2022
## Purpose: O(n^2) insertion sort
## to be ran on the command line

# Import time module
# Follows PEP-8 Style
import time

class InsertionSort:
    
    # Object initialization
    def __init__(self, input):
        self.data = input
        self.duration = None
        
    # Custom define print function
    def __str__(self):
        return "{}".format(self.data)
        
    # In-place swap operation
    def swap(self, i, j):
        temp = self.data[i]
        self.data[i] = self.data[j]
        self.data[j] = temp
        print(self.data)

    # Insertion Sort implementation
    def sort(self):
        # Begin timing sort runtime
        start = time.time()
        for j in range(1, len(self.data)):
            key = self.data[j]
            # Insert key into sorted sequence
            # i.e. iterate toward data[0..j-1]
            i = j - 1
            while i >= 0 and self.data[i] > key:
                self.data[i + 1] = self.data[i]
                i = i - 1
            self.data[i + 1] = key
        # Finish timing
        end = time.time()
        self.duration = end - start
        # Display output to user
        print(self.data)
        
    # Provide runtime of Insertion Sort
    def time_it(self):
        # If time available already generated
        if self.duration:
            print(format(self.duration, '.9f'), "seconds")
            print("Access duration value using .duration")
        else:
            # Generate time data
            self.sort()
            print(format(self.duration, '.9f'), "seconds")
            print("Access duration value using .duration")

