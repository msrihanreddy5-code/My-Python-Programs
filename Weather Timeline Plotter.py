import matplotlib.pyplot as plt

temps = [27, 29, 31, 30, 28, 26, 25]

plt.plot(range(1, 8), temps)
plt.title("Temperature (7 Days)")
plt.xlabel("Day")
plt.ylabel("Temp (°C)")
plt.show()
