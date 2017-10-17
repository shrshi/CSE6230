import matplotlib.pyplot as plt

time = [0, 500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000]
dist = [0.000000, 0.853473, 0.545430, 0.659795, 0.707760, 0.826228, 0.842977, 0.486963, 0.835357, 0.745182, 0.647710]

plt.plot(time, dist)
plt.xlabel('Time step')
plt.ylabel('Average distance')
plt.title('Plot of average distance travelled by particles vs time')

plt.show()
