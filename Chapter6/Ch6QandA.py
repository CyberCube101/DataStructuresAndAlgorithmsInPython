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


def reverse(a_list):
    S = StackArray()
    for i in range(len(a_list)):
        S.push(a_list[i])
    for j in range(len(a_list)):
        a_list[j] = S.pop()
    print(a_list)


my_list = [3, 6, 9, 12, 15]
reverse(my_list)
