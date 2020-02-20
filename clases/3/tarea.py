from sympy import * 

x = symbols('x')

class NewtonRaphson:
    def __init__(self, expression):
        
        self.expression = expression
        self.dx = diff(self.expression, x)
      
    def newton_raphson(self, x0, error):
        counter = 0

        while True:
            divition = self.expression.subs(x, x0)/self.dx.subs(x, x0)
            x0 = (x0 - divition).evalf()
            if(self.evaluate_error(x0) < error): 
                return { 'x': x0, 'iteration': counter}
            counter +=1

    def evaluate_error(self, x0):
        return abs(self.expression.subs(x,x0).evalf())

if __name__ == "__main__":
    error = 0.0001

    a = NewtonRaphson(4*x**3 + 21*x**3 + 10*x - 17)
    print('a')
    print(a.newton_raphson(0.5,error))
    print('a')
    print(a.newton_raphson(-8,error))

   