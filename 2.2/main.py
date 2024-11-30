import numpy as np
import matplotlib.pyplot as plt

p = 0.2

k_values = np.arange(0, 10)
probabilities = (1 - p) ** k_values * p

E_X = 1 / p
D_X = (1 - p) / (p ** 2)
std_X = np.sqrt(D_X)

plt.plot(k_values, probabilities, marker='o', linestyle='-', color='b')

# Add values on each marker with no trailing zeros
for k, prob in zip(k_values, probabilities):
    plt.text(k, prob, f'{prob:.5g}', ha='left', va='bottom', fontsize=14)

plt.tick_params(axis='x', labelsize=14)
plt.tick_params(axis='y', labelsize=14)
plt.grid(True)
plt.show()

