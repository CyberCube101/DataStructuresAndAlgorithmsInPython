class ArrayStack:
    def __init__(self):
        self.data = []

    def __len__(self):
        print(len(self.data))

    def is_empty(self):
        return len(self.data) == 0

    def push(self, e):
        self.data.append(e)

    def top(self):
        if self.is_empty():
            print('Stack is empty')
        else:
            return self.data[-1]

    def pop(self):
        if not self.is_empty():
            return self.data.pop()


s = ArrayStack()
s.push(5)
s.push(6)
s.push(7)
s.__len__()
print(s.top())


#### Stacks are ideal for reversing data since the values 1, 2, 3pushed onto a stack will come out 3,2,1

def reverse_file(filename):
    s1 = ArrayStack()
    original = open(filename)
    for line in original:
        s1.push(line.rstrip('\n'))  # strip newlines when pushing and will re-insert when reading out
    original.close()

    # now for the output

    output = open(filename, 'w')  # reopening file overwrites original
    while not s1.is_empty():
        output.write(s1.pop() + '\n')  # re-insert lines
    output.close()
