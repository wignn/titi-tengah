import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return 1 / (x + 1)

a = 0
b = 1
h = 0.05

n = int((b - a) / h)

integral = 0
x_values = np.linspace(a, b, 100)
y_values = f(x_values)

x_rectangles = []
y_rectangles = []

for i in range(n):
    x_mid = a + (i + 0.5) * h  
    integral += f(x_mid) * h
    x_rectangles.append(x_mid)
    y_rectangles.append(f(x_mid))

plt.plot(x_values, y_values, label=r'$f(x) = \frac{1}{x+1}$', color="blue")
plt.fill_between(x_values, y_values, color="lightblue", alpha=0.3)

plt.bar(x_rectangles, y_rectangles, width=h, align='center', edgecolor="black", color="orange", alpha=0.6, label="Aproksimasi Titik Tengah")

plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Aproksimasi Integral Menggunakan Metode Titik Tengah")
plt.legend()
plt.show()

print("Hasil integral adalah:", integral)