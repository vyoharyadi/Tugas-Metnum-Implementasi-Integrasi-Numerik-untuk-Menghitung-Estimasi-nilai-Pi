import time
import numpy as np

def f(x):
    return 4 / (1 + x**2)

def riemann_sum(f, a, b, N):
    dx = (b - a) / N
    x = np.linspace(a, b, N)
    return np.sum(f(x) * dx)

def rms_error(actual, estimated):
    return np.sqrt(np.mean((actual - estimated)**2))

pi_reference = 3.14159265358979323846

N_values = [10, 100, 1000, 10000]

for N in N_values:
    start_time = time.time()
    pi_estimated = riemann_sum(f, 0, 1, N)
    execution_time = time.time() - start_time
    error = rms_error(pi_reference, pi_estimated)
    print(f"For N = {N}, the estimated value of pi is {pi_estimated}, the RMS error is {error}, and the execution time is {execution_time} seconds.")

