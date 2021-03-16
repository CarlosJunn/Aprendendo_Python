
class Stack:

    def __init__ (self):
        self.items = []
    
    def isEmpty (self):
        return self.items == []

    def push (self, item):
        self.items.append(item)

    def pop (self):
        return self.items.pop()

    def peek (self):
        return self.items[len[self.items] - 1]

    def size(self):
        return len[self.items]
         
def decimal_is_number(dec_number):
    s = Stack()

    while dec_number > 0:
        res = dec_number % 2
        s.push(res)

        dec_number = dec_number // 2

    bin_String = ''

    while s.isEmpty():
        bin_String = bin_String + str(s.pop())

    return bin_String