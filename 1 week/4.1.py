import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
x1 = [0, 0.145833333, 0.28125, 0.432291667, 0.567708333, 0.697916667, 0.838541667, 0.958333333, 1.098958333, 1.234375, 1.364583333, 1.489583333]
x2 = [0, 0.151041667, 0.307291667, 0.447916667, 0.583333333, 0.713541667, 0.84375, 0.973958333, 1.109375, 1.244791667, 1.375, 1.505208333]
x3 = [0, 0.1875, 0.302083333, 0.447916667, 0.588541667, 0.713541667, 0.854166667, 0.984375, 1.119791667, 1.25, 1.375, 1.510416667]
x4= [0, 0.15625, 0.302083333, 0.442708333, 0.583333333, 0.71875, 0.848958333, 0.984375, 1.114583333, 1.25, 1.380208333, 1.515625]
x = [0 , 0.138995278, 0.278103744, 0.416929239, 0.555867922, 0.694127476, 0.832952971, 0.971891655, 1.110886932, 1.250165181, 1.389160459, 1.528155736]
y = [0, 245.6, 491.4, 736.7, 982.2, 1226.5, 1471.8, 1717.3, 1962.9, 2209, 2454.6, 2700.2]

plt.figure(figsize=(10,5), dpi=400)
plt.plot(x1,y, color='red', label='y(x₁)', linewidth=1, marker='.', linestyle='--', markersize=5, markeredgecolor='red')
plt.plot(x2, y, color='green', label='y(x₂)', linewidth=1, marker='.', linestyle='--', markersize=5, markeredgecolor='green')
plt.plot(x3, y, color='blue', label='y(x₃)', linewidth=1, marker='.', linestyle='--', markersize=5, markeredgecolor='blue')
plt.plot(x4, y, color='palevioletred', label='y(x₄)', linewidth=1, marker='.', linestyle='--', markersize=5, markeredgecolor='palevioletred')
plt.plot(x, y, color='black', label='y(x) – линейная аппроксимация', linewidth=1.5, marker='.', markersize=5, markeredgecolor='black')

plt.title('Зависимость массы от удлинения проволоки m(Δl)', fontdict={'fontname': 'sans-serif', 'fontsize': 20})
plt.xlabel('Δl, см')
plt.ylabel('m, г')
plt.xticks([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1.1, 1.2, 1.3, 1.4, 1.5])
plt.yticks([0, 245.6, 491.4, 736.7, 982.2, 1226.5, 1471.8, 1717.3, 1962.9, 2209, 2454.6, 2700.2])
plt.grid()
plt.legend()
plt.show()