import ctypes


class DynamicArray:
    # similiar to a list
    def __init__(self):
        self._n = 0  # count elements
        self._capacity = 1  # default array capacity
        self._A = self._make_array(self._capacity)  # low level array

    def __len__(self):
        return self._n

    def __getitem__(self, k):
        # return element at position k
        if not 0 <= k < self._n:
            raise IndexError('invalid index')
        return self._A[k]

    def append(self, obj):
        if self._n == self._capacity:  # not enough room
            self._resize(2 * self._capacity)  # double the size
        self._A[self._n] = obj
        self._n += 1

    def _resize(self, c):
        B = self._make_array(c)  # new bigger array
        for k in range(self._n):
            B[k] = self._A[k]
        self._A = B  # use the bigger array
        self._capacity = c

    def _make_array(self, c):
        return c * ctypes.py_object()
