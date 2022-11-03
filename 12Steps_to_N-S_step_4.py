import numpy  # loading our favorite library
import sympy

from matplotlib import pyplot  # and the useful plotting library
from sympy import init_printing
init_printing(use_latex=True)
from sympy.utilities.lambdify import lambdify
#% matplotlib inline


'''
u = numpy.ones(nx)  # a numpy array with nx elements all equal to 1.
u[int(.5 / dx):int(1 / dx + 1)] = 2  # setting u = 2 between 0.5 and 1 as per our I.C.s

un = numpy.ones(nx)  # our placeholder array, un, to advance the solution in time

for n in range(nt):  # iterate through time
    un = u.copy()  ##copy the existing values of u into un
    for i in range(1, nx - 1):
        u[i] = un[i] + nu * dt / dx ** 2 * (un[i + 1] - 2 * un[i] + un[i - 1])
    pyplot.plot(numpy.linspace(0, 2, nx), u)
#pyplot.plot(numpy.linspace(0, 2, nx), u)
pyplot.show()

'''
x, nu, t = sympy.symbols('x nu t')
phi = (sympy.exp(-(x - 4*t)**2 / (4 * nu * (t + 1))) + sympy.exp(-(x - 4 * t - 2 * sympy.pi)**2 / (4 * nu * (t + 1))))

phiprime = phi.diff(x)
u = -2 * nu * (phiprime / phi) + 4
ufunc = lambdify((t, x, nu), u)

nx = 101
dx = 2 * numpy.pi / (nx - 1)
nt = 100  # the number of timesteps we want to calculate
nu = 0.07  # the value of viscosity
#sigma = .2  # sigma is a parameter, we'll learn more about it later
dt = dx * nu

x = numpy.linspace(0, 2 * numpy.pi, nx)
un = numpy.empty(nx)
t=0
u = numpy.asarray([ufunc(t, x0, nu) for x0 in x])
print(u)

pyplot.figure(figsize=(11, 7), dpi=100)
pyplot.plot(x, u, marker='o', lw=2)
pyplot.xlim([0, 2 * numpy.pi])
pyplot.ylim([0, 10]);
pyplot.show()