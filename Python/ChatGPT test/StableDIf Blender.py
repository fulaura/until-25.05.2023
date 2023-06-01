import numpy as np

# Set the parameters
D = 0.1   # diffusion coefficient
dt = 0.01  # time step
dx = 0.1  # spatial step
L = 1.0  # length of the domain
T = 1.0  # simulation time

# Create the grid
x = np.arange(0, L+dx, dx)  # spatial grid
t = np.arange(0, T+dt, dt)  # time grid

# Initialize the solution array
u = np.zeros((len(t), len(x)))  # solution array

# Set the initial condition
u[0, :] = np.sin(np.pi*x/L)

# Implement stable diffusion using an explicit scheme
for n in range(0, len(t)-1):
    u[n+1, 1:-1] = u[n, 1:-1] + D*dt/(dx**2) * (u[n, 2:] - 2*u[n, 1:-1] + u[n, :-2])

# Plot the solution
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

X, T = np.meshgrid(x, t)

ax.plot_surface(X, T, u)

plt.show()
