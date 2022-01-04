import numpy as np
import matplotlib.pyplot as plt

## Movements verticals and horizontals
N = 1000

def f(x):
  return x**2;

c = 2

x = np.linspace(-5, 5, num=N)

y = f(x)
# y = f(x) + c
# y = f(x) - c
# y = f(x - c)
# y = f(x + c)


fig, ax = plt.subplots()
ax.plot(x,y)
ax.grid()
ax.axhline(y=0, color='r')
ax.axvline(x=0, color='r')
plt.show()


## Lengthening and compressions
N = 1000

def f(x):
  return np.sin(x);

c = 2

x = np.linspace(-15,15, num=N)

y = f(x)
# y = c*f(x)
# y = (1/c)*f(x)
# y = f(c*x)
# y = f((1/c)*x)


fig, ax = plt.subplots()
ax.plot(x,y)
ax.grid()
ax.axhline(y=0, color='r')
ax.axvline(x=0, color='r')
plt.show()

N = 1000

## Reflexions
def f(x):
  return x**3;

x = np.linspace(-10,10, num=N)

y = f(x)
# y = -f(x)
# y = f(-x)


fig, ax = plt.subplots()
ax.plot(x,y)
ax.grid()
ax.axhline(y=0, color='r')
ax.axvline(x=0, color='r')
plt.show()
