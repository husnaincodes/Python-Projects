import matplotlib.pyplot as plt
import numpy as np

X = np.linspace(0.1, 5, 100)  # Good X
U1 = 2  
U2 = 4  


Y1 = U1 / X
Y2 = U2 / X

plt.figure(figsize=(7,5))
plt.plot(X, Y1, label='Indifference Curve U=2', color='blue')
plt.plot(X, Y2, label='Indifference Curve U=4', color='green')
plt.scatter([2, 1], [1, 2], color='red')  
plt.text(2, 1, '(2,1)', fontsize=10, color='red')
plt.text(1, 2, '(1,2)', fontsize=10, color='red')

plt.title("Indifference Curves")
plt.xlabel("Good X (Burgers)")
plt.ylabel("Good Y (Pizza)")
plt.grid(True)
plt.legend()
plt.show()
