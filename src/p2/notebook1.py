# %%
import matplotlib.pyplot as plt
msg = "Hello, World!"
print(msg)





# %%
import matplotlib.pyplot as plt
import numpy as np

def print_colored(message):
    # Example implementation of print_colored
    print(f"\033[94m{message}\033[0m")

# Draw an example chart for a Jupyter notebook
x = np.linspace(0, 10, 100)
y = np.cos(x)
x_sin = np.linspace(0, 10, 100)
y_sin = np.sin(x_sin)

plt.figure(figsize=(8, 4))
plt.plot(x, y, label="Cosine Wave")
plt.plot(x_sin, y_sin, label="Sine Wave", linestyle='--')
plt.title("Trigonometric Functions")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()
plt.grid(True)
plt.show()

# %%
