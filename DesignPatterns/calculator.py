from abc import ABC, abstractmethod


class AverageCalculator(ABC): 

    def average(self): 
        try:
            num_items = 0
            total_sum = 0
            while self.has_next():
                total_sum += self.next_item()
                num_items += 1
            if num_items == 0:
                raise RuntimeError("Can't compute the average of zero items.")
            return total_sum / num_items
        finally:
            self.dispose()

    @abstractmethod
    def has_next(self): 
        pass

    @abstractmethod
    def next_item(self): 
        pass

    def dispose(self): 
        pass

class MemoryAverageCalculator(AverageCalculator):
    def __init__(self, numarr):
        self.numarr = numarr
        self._index = 0

    def has_next(self):
        return(self._index < len(self.numarr))

    def next_item(self):
        retval = self.numarr[self._index]
        self._index += 1
        return retval

mac = MemoryAverageCalculator([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 3.9])
print(mac.average()) # Call the template method