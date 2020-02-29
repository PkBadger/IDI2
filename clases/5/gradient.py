import numpy
from sympy import symbols, diff, sin, cos, exp

x, y = symbols('x y')

class Mult_gradient:
	def __init__(self, fx, variables, alpha=0.02):
		self.alpha = alpha
		self.function = fx
		self.derivarives = [diff(fx, variable) for variable in variables]
		self.variables = variables

	def gradient(self, initial_values, error, is_ascent=False):
		initial_values = numpy.matrix(initial_values).T
		counter = 0
		multiplier = 1 if is_ascent else -1 

		while True:
			derivative = self.calculate_derivative(initial_values)
			initial_values = initial_values + multiplier * self.alpha * derivative.T
			counter += 1
			
			if numpy.min(numpy.abs(derivative)) < error:
				return {'iterations': counter, 'values': numpy.asarray(initial_values.T) }
    
	def calculate_derivative(self, initial_values):
		derivatives = []

		for index in range(len(self.derivarives)):
			derivative = self.derivarives[index]

			derivative_a = derivative.subs(zip(self.variables, numpy.asarray(initial_values.T)[0]))
			derivatives.append(derivative_a.evalf())

		return numpy.matrix(derivatives)

	def eval(self, values):
		return self.function.subs({x: values[0][0], y: values[0][1]}).evalf()

if __name__ == "__main__":

	error = 0.001
	#1:
	fx1 = x**4 - 3*x**3 + 2

	ejercicio1 = Mult_gradient(fx1, [x])
	print(ejercicio1.derivarives)

	print(ejercicio1.gradient([1], error))

	#2:
	fx2 = x**2 - 24*x + y**2 - 10*y

	ejercicio2 = Mult_gradient(fx2, [x,y])
	print(ejercicio2.derivarives)

	print(ejercicio2.gradient([1,1], error))

	#3:
	fx3 = sin((1/2)*x**2 - (1/4)*y**2 + 3)*cos(2*x - 1 - exp(y))

	ejercicio3 = Mult_gradient(fx3, [x,y])
	print(ejercicio3.derivarives)

	#minimum
	result = ejercicio3.gradient([1,1], error)

	print(result)

	print(ejercicio3.eval(result.get('values')))

	#maximum

	result = ejercicio3.gradient([1,1], error, True)

	print(result)

	print(ejercicio3.eval(result.get('values')))


	