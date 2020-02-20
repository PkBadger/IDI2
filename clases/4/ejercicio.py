import sympy

x, y, z = sympy.symbols('x y z')

X = sympy.MatrixSymbol('X', 2,1)

#F = sympy.Matrix([f1,f2])
#F.jacobian([x,y])

class NewtonRaphsonMult:
    def __init__(self, expressions, variables):     
        self.expressions = expressions
        expression_matrix = sympy.Matrix(expressions)
        self.jacobian = expression_matrix.jacobian(variables)
        self.jacobian_inv = self.jacobian.inv()
        self.mult = self.jacobian_inv * expression_matrix
      
    def newton_raphson_mult(self, initial_values, variables, matrix_symbol, error):
        initial_values = sympy.Matrix(initial_values)

        for _ in range(15):
            mapped_values = self.map_values(initial_values, variables)
            x_subs = X.subs(mapped_values)
            for i in range(len(initial_values)):
                value = initial_values[i]
                value = value - self.

            print(initial_values)

    def map_values(self, initial_values, variables):
        mapped = {}
        for i in range(len(initial_values)):
            mapped[variables[i]] = initial_values[i]

        return mapped

    def evaluate_error(self, x0):
        return abs(self.expressions.subs(x,x0).evalf())

if __name__ == "__main__":
    #fx = (-4*y*x**2 - 2*y**2 - x + 4*y)/(8*x*y + 1)
    #gx = (x**2 - y - 4*x*y**2 + 1)/(8*x*y + 1)
    #newton_raphson_mult(1,1, fx, gx)

    #newton_raphson_mult(2, 0.5, fx, gx)
    fx = x**2 + y - 1
    gx = x - 2*y**2
    first = NewtonRaphsonMult([fx,gx], [x,y])
    print(first.mult)
    #print(first.jacobian_inv)
    #first.newton_raphson_mult([2,0.5],['x', 'y'],X, 3)

