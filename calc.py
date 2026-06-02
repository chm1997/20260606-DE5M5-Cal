class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    
    def get_sum(self):
        return self.num1 + self.num2
    
    def get_sub(self):
        return self.num1 - self.num2
    
    def get_mult(self):
        return self.num1 * self.num2
    
    def get_div(self):
        return self.num1 / self.num2