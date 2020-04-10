"""
*.*.*.*.*.*
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
*.*.*.*.*.*


# Example 
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.
"""
class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.inner_list = []
        
    def push(self, x):
        self.inner_list += [x]

    def pop(self):
        self.inner_list = self.inner_list[:-1]
        
    def top(self):
        return self.inner_list[-1]

    def getMin(self):
        return min(self.inner_list)


# Faster implementation
class MinStack2:
    def __init__(self):
        self.stack = []

    def push(self, x):
        if self.stack:
            self.stack.append((x, min(x, self.stack[-1][1])))
        else:
            self.stack.append((x, x))

    def pop(self):
        if not self.stack:
            return None
        pop = self.stack[-1][0]
        self.stack = self.stack[:-1]

    def top(self):
        if not self.stack:
            return None
        return self.stack[-1][0]

    def getMin(self):
        if not self.stack:
            return None
        return self.stack[-1][1]

        
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


if __name__ == "__main__":
    
    obj = MinStack()

    print 'initialize MinStack ...'
    print 'push -2 to MinStack ... ', obj.push(-2)
    print 'push 0 to MinStack ... ', obj.push(0)
    print 'push -3 to MinStack ... ', obj.push(-3)
    print 'getMin of MinStack :: ', obj.getMin()
    print 'pop MinStack ... ', obj.pop()
    print 'top of MinStack :: ', obj.top()
    print 'getMin of MinStack :: ', obj.getMin()
	
