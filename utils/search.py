

class Search(object):
    def __init__(self):
        pass

    def binary(self, array, value):
        """
        Binary Search - My Algorithm
        """
        index = len(array)/2
        if value == array[index]:
            return index
        elif len(array) == 1:
            return "Value is not in Array"
        else:
            if value > array[index]:
                aux = self.binary(array[index:], value)
                if type(aux) == int:
                    return index + aux
                else:
                    return aux
            elif value < array[index]:
                return self.binary(array[:index], value)

    def otherBinary(self, array, value):
        """
        Binary Search - Wikipedia Algorithm
        """
        low = 0
        high = len(array)-1
        while True:
            if low > high:
                return "Value is not in Array"
            m = (high + low)/2
            if array[m] < value:
                low = m + 1
            elif array[m] > value:
                high = m - 1
            elif array[m] == value:
                return m


if __name__ == "__main__":
    arr = [7, 19, 45, 76, 99, 102, 104, 146, 179, 199, 201, 572, 631, 678, 698, 809, 891, 910, 1042, 1052, 1105, 1205,
           1298, 1390, 1399, 1401, 1455, 1477, 1591, 1891, 2091, 2405, 2489, 2765, 3091, 3791, 5901, 6001, 6098, 6973,
           7601, 8091, 8234, 8345, 8787, 8976, 9032, 9123, 9234, 9392, 9444, 9595, 9679, 9689, 9776, 9898, 9901, 9999]
    # arr = range(1000)
    value = 8234
    search = Search()

    if type(search.binary(arr, value)) == int:
        print arr[search.binary(arr, value)]
    else:
        print search.binary(arr, value)

    if type(search.otherBinary(arr, value)) == int:
        print arr[search.otherBinary(arr, value)]
    else:
        print search.otherBinary(arr, value)
