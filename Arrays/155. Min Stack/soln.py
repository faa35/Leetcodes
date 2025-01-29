class MinStack:    
#class MinStack(object):    is the old version way

    def __init__(self):
        self.stack = []
        self.min_valueStack = []


    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        # for stack
        self.stack.append(val)

        #for min_valueStack
        if len(self.min_valueStack) != 0:
            min_value = self.min_valueStack[-1]

            if min_value > val:
                min_value = val
                self.min_valueStack.append(min_value)
            else:
                self.min_valueStack.append(min_value)
        else:
            self.min_valueStack.append(val)


    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()
        self.min_valueStack.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

        
    def getMin(self):
        """
        :rtype: int
        """

        return self.min_valueStack[-1]
    

# Example Execution Flow
myStack = MinStack()  # Output: null (constructor returns nothing)
#MinStack myStack = new MinStack(); is the old version way
myStack.push(-2)      # Output: null (method returns None)
myStack.push(0)       # Output: null
myStack.push(-3)      # Output: null
print(myStack.getMin())  # Output: -3
myStack.pop()         # Output: null
print(myStack.top())     # Output: 0
print(myStack.getMin())  # Output: -2