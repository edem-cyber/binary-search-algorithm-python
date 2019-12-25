class B_search:

    def binary_s_iterative(self, array_, target):
        low = 0
        high = len(array_) - 1

        while low <= high:
            midpoint = (low + high) // 2

            if target == data[midpoint]:
                return True
            elif target > data[midpoint]:
                low = midpoint + 1
            else:
                high = midpoint - 1
        return False

    def binary_s_recursive(self, array_, target, low, high):
        if low > high:
            return False
        else:
            midpoint = (low + high)

            if target == data[midpoint]:
                return True
            elif target > data[midpoint]:
                return self.binary_s_recursive(array_, target, midpoint+1, high)
            else:
                return self.binary_s_recursive(array_, target, low, midpoint-1)


