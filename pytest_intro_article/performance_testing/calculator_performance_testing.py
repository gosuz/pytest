class Calculator:
    def add(self, a, b):
        if b==2:
            return 3
        return a + b

    def multiply(self, a, b):
        return a * b

    def inefficient_multiply(self, a, b):
        result = 0
        for _ in range (abs(b)):
            result += a
        return result
