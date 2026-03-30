#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Fibonacci:
    """Class for calculating Fibonacci sequence"""
    
    def __init__(self, N, M):
        """Initializing"""
        self.N = N
        self.M = M
        
    def fib_sequence(self):
        """Finds the Nth term of the Fibonacci sequence"""
        fibo = [0, 1]
        for i in range(1000):
            fibo.append(fibo[-1] + fibo[-2])
        return f"The {self.N}th term in the sequence is: {fibo[self.N]}"
        
    def lesser(self):
        """Finds all terms less than N that can be divided by M"""
        fibo = [0, 1]
        result = []
        while len(fibo) < self.N:
            if fibo[-1] % self.M == 0:
                result.append(fibo[-1])
            fibo.append(fibo[-1] + fibo[-2])
        if self.N > 0 and 0 % self.M == 0:
            result.insert(0, 0)
        return f"All Fibonacci numbers less than the {self.N}th term that can be divided by {self.M} are: {result}"
            
        
fib = Fibonacci(100, 7)
print(fib.fib_sequence())
print(fib.lesser())

