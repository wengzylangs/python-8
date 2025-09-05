"""
TASK: Create a Calculator class.

Requirements:
1. The class should allow basic operations: add, subtract, multiply, divide.
2. Each operation should be a separate method.
3. Handle division by zero gracefully.
4. Allow both integers and floats.

Example Usage:
    calc = Calculator()
    print(calc.add(5, 3))        # 8
    print(calc.divide(10, 0))    # "Error: Division by zero"
"""
class Calculator: # class variable
	
	def add(self,a,b):
		return a + b


	def sub(self, a,b):
		return a - b
	
	def mul(self, a , b):
		return a * b


	def divide(self, a, b):
		return a / b

calc = Calculator()
print(calc.add(5,3))
print(calc.divide(10,0)) 
