'''6.5
Implement a function that reverses a list of elements by pushing them onto a stack and then writes back in reverse order
'''


class StackArray:
    def __init__(self):
        self.data = []

    def push(self, e):
        self.data.append(e)

    def pop(self):
        return self.data.pop()


def reverse(alist):
    S = StackArray()
    for i in range(len(alist)):
        S.push(alist[i])
    for j in range(len(alist)):
        alist[j] = S.pop()
    print(alist)


mylist = [3, 6, 9, 12, 15]
reverse(mylist)
