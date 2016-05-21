import random


class Sort(object):
    def __init__(self):
        pass

    def _partitionLomuto(self, array, low, high):
        """
        Lomuto partition function for quicksort. It situates the pivot in the right final position,
        with every value lower than it at the left, and every higher at the right.
        Return the pivot position for the quicksort to divide the problem cutting through the pivot.
        :param array: array to be sorted
        :param low: low parameter
        :param high: high parameter
        :return: New pivot final position
        """
        pivot = array[high]
        i = low
        for j in range(low, high):
            if array[j] <= pivot:
                array[i], array[j] = array[j], array[i]
                i += 1
        array[i], array[high] = array[high], array[i]
        return i

    def _partition(self, array, low, high):
        """
        Hoare partition function for quicksort.
        :param array:
        :param low:
        :param high:
        :return:
        """
        pivot = array[low]
        i = low - 1
        j = high + 1
        while True:
            j -= 1
            while array[j] < pivot:
                i += 1
                while array[i] > pivot:
                    if i >= j:
                        return j
                    array[i], array[j] = array[j], array[i]


    def quicksort(self, array, low=0, high=None):
        """
        Quicksort - Wikipedia algorithm.
        :param array: array to be sorted
        :return: None, in-place sorting...
        """
        if high == None:
            high = len(array) - 1
        if low < high:
            p = self._partition(array, low, high) # use _partitionLomuto instead of _partition for Lomuto's scheam
            self.quicksort(array, low, p) # put (p - 1) instead of p when using Lomuto's scheme
            self.quicksort(array, p + 1, high)

        return


if __name__ == "__main__":
    arr = [1855, 10098, 283, 1029, 934, 283, 1984, 192, 5736, 758, 371, 1855, 837, 7837, 716, 847, 987, 1098, 2045,
           4019, 8945, 10098, 9089, 8976, 18293, 7856, 190, 2378, 2379, 988, 78, 3, 897, 457, 4578, 123, 321, 4444]
    sort = Sort()
    sort.quicksort(arr)
    print arr, "\n"
